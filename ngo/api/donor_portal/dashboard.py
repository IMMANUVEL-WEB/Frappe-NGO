from collections import defaultdict
from datetime import datetime

import frappe
from frappe import _
from frappe.utils import add_days, flt, formatdate, getdate, today

from ngo.api.donor_portal.auth import get_current_donor


@frappe.whitelist()
def get_dashboard():
	"""
	Returns dashboard aggregates matching the reference UI:
	- KPI cards: Total Given, Total Spend, Balance Available, Active Grants, Total Purchase Amount
	- Charts: Given vs Spent vs Variance by Month (Lakh), Spend by Category (CapEx/OpEx/Admin), Spend by Project
	- Decision Card: Project Proposals awaiting donor decision
	"""
	donor = get_current_donor(allow_admin_preview=True)

	# 1. Active Grants for current donor
	grants = frappe.get_all(
		"Donor Grant",
		filters={"donor_name": donor, "status": "Active"},
		fields=[
			"name",
			"grant_id",
			"grant_title",
			"total_amount",
			"linked_project",
			"cost_center",
			"valid_from",
			"valid_to",
			"currency",
		],
	)

	active_grants_count = len(grants)
	project_ids = list(set([g.linked_project for g in grants if g.linked_project]))
	cost_centers = list(set([g.cost_center for g in grants if g.cost_center]))

	# Also find projects where Project-custom_donor is this donor
	donor_projects = frappe.get_all(
		"Project", filters={"custom_donor": donor}, fields=["name", "project_name", "cost_center"]
	)
	for dp in donor_projects:
		if dp.name not in project_ids:
			project_ids.append(dp.name)
		if getattr(dp, "cost_center", None) and dp.cost_center not in cost_centers:
			cost_centers.append(dp.cost_center)

	# Check grants expiring within 90 days
	today_date = getdate(today())
	in_90_days = add_days(today_date, 90)
	expiring_soon_count = sum(
		1 for g in grants if g.valid_to and today_date <= getdate(g.valid_to) <= in_90_days
	)

	# Total Committed Amount across grants
	total_committed = sum(flt(g.total_amount) for g in grants)

	# 2. Total Given (Incoming Payment Entries from Donor)
	payment_filters = {"party_type": "Supplier", "party": donor, "payment_type": "Receive", "docstatus": 1}
	payments = frappe.get_all(
		"Payment Entry",
		filters=payment_filters,
		fields=["name", "received_amount", "paid_amount", "posting_date"],
	)
	total_given = sum(flt(p.received_amount or p.paid_amount) for p in payments)

	# 3. Total Spent (GL Entries on Donor Projects / Cost Centers)
	spent_conditions = []
	spent_params = {}
	if project_ids:
		spent_conditions.append("gle.project IN %(projects)s")
		spent_params["projects"] = tuple(project_ids)
	if cost_centers:
		spent_conditions.append("gle.cost_center IN %(cost_centers)s")
		spent_params["cost_centers"] = tuple(cost_centers)

	gl_entries = []
	if spent_conditions:
		query_where = " OR ".join(spent_conditions)
		gl_entries = frappe.db.sql(
			f"""
			SELECT
				gle.name, gle.posting_date, gle.account, gle.debit, gle.credit,
				gle.project, gle.cost_center, gle.voucher_type, gle.voucher_no
			FROM `tabGL Entry` gle
			JOIN `tabAccount` acc ON acc.name = gle.account
			WHERE ({query_where})
			  AND acc.root_type = 'Expense'
			  AND gle.is_cancelled = 0
			  AND gle.debit > 0
			ORDER BY gle.posting_date ASC
		""",
			spent_params,
			as_dict=True,
		)

	total_spent = sum(flt(entry.debit) - flt(entry.credit) for entry in gl_entries)
	if total_spent < 0:
		total_spent = 0.0

	# 4. Total Purchases / Procurement
	total_purchases = 0.0
	if project_ids or cost_centers:
		p_where = []
		p_params = {}
		if project_ids:
			p_where.append("project IN %(projects)s")
			p_params["projects"] = tuple(project_ids)
		if cost_centers:
			p_where.append("cost_center IN %(cost_centers)s")
			p_params["cost_centers"] = tuple(cost_centers)

		purchases = frappe.db.sql(
			f"""
			SELECT SUM(grand_total) as total
			FROM `tabPurchase Invoice`
			WHERE ({" OR ".join(p_where)}) AND docstatus = 1
		""",
			p_params,
			as_dict=True,
		)
		if purchases and purchases[0].total:
			total_purchases = flt(purchases[0].total)

	# 5. Balances
	balance_available = max(total_given - total_spent, 0.0)
	committed_balance = max(total_committed - total_spent, 0.0)
	percent_given_of_committed = round((total_given / total_committed * 100), 1) if total_committed > 0 else 0
	percent_spent_of_given = round((total_spent / total_given * 100), 1) if total_given > 0 else 0

	# 6. Monthly Series: Given vs Spent vs Variance (Last 7 Months)
	monthly_given = defaultdict(float)
	for p in payments:
		if p.posting_date:
			m_key = formatdate(p.posting_date, "MMM yyyy")
			monthly_given[m_key] += flt(p.received_amount or p.paid_amount)

	monthly_spent = defaultdict(float)
	for g in gl_entries:
		if g.posting_date:
			m_key = formatdate(g.posting_date, "MMM yyyy")
			monthly_spent[m_key] += flt(g.debit)

	# Default last 7 months if sparse
	month_order = []
	now = datetime.now()
	for i in range(6, -1, -1):
		m = (now.month - i - 1) % 12 + 1
		y = now.year if (now.month - i) > 0 else now.year - 1
		dt = datetime(y, m, 1)
		month_order.append(dt.strftime("%b %Y"))

	monthly_series = []
	for m_key in month_order:
		given_val = round(monthly_given.get(m_key, 0.0) / 100000.0, 2)  # In Lakhs
		spent_val = round(monthly_spent.get(m_key, 0.0) / 100000.0, 2)  # In Lakhs
		var_val = round(given_val - spent_val, 2)
		monthly_series.append(
			{
				"month": m_key.split(" ")[0],
				"month_year": m_key,
				"given": given_val,
				"spent": spent_val,
				"variance": var_val,
			}
		)

	# 7. Spend by Category: CapEx, OpEx, Admin
	capex_spent = 0.0
	opex_spent = 0.0
	admin_spent = 0.0

	# Fetch custom mappings if configured
	category_map = {}
	if frappe.db.table_exists("Spend Category Mapping"):
		mappings = frappe.get_all("Spend Category Mapping", fields=["account", "category"])
		for m in mappings:
			category_map[m.account] = m.category

	for g in gl_entries:
		acc_name = g.account or ""
		cat = category_map.get(acc_name)
		amt = flt(g.debit)
		if cat:
			if cat in ["CapEx", "Goods"]:
				capex_spent += amt
			elif cat in ["OpEx", "Cash Assistance", "Services"]:
				opex_spent += amt
			else:
				admin_spent += amt
		else:
			# Differentiate by account title keywords
			acc_lower = acc_name.lower()
			if "capital" in acc_lower or "capex" in acc_lower or "asset" in acc_lower:
				capex_spent += amt
			elif "admin" in acc_lower or "office" in acc_lower or "rent" in acc_lower:
				admin_spent += amt
			else:
				opex_spent += amt

	cat_total = capex_spent + opex_spent + admin_spent or 1.0
	spend_by_category = {
		"capex": {
			"amount": round(capex_spent / 100000.0, 2),  # in Lakh
			"raw_amount": round(capex_spent, 2),
			"percent": round(capex_spent / cat_total * 100, 1),
		},
		"opex": {
			"amount": round(opex_spent / 100000.0, 2),  # in Lakh
			"raw_amount": round(opex_spent, 2),
			"percent": round(opex_spent / cat_total * 100, 1),
		},
		"admin": {
			"amount": round(admin_spent / 100000.0, 2),  # in Lakh
			"raw_amount": round(admin_spent, 2),
			"percent": round(admin_spent / cat_total * 100, 1),
		},
	}

	# 8. Spend by Project
	spend_by_project = []
	project_spent_map = defaultdict(float)
	for g in gl_entries:
		if g.project:
			project_spent_map[g.project] += flt(g.debit)

	# Fetch project names/details
	if project_ids:
		projects_meta = frappe.get_all(
			"Project", filters={"name": ["in", project_ids]}, fields=["name", "project_name", "custom_sector"]
		)
		meta_dict = {p.name: p for p in projects_meta}
		for pid in project_ids:
			pm = meta_dict.get(pid)
			p_name = pm.project_name if pm else pid
			p_amt = project_spent_map.get(pid, 0.0)
			spend_by_project.append(
				{
					"project_id": pid,
					"project_name": p_name,
					"sector": getattr(pm, "custom_sector", "") or "General",
					"amount_lakh": round(p_amt / 100000.0, 2),
					"amount_raw": round(p_amt, 2),
					"percent": round(p_amt / (total_spent or 1.0) * 100, 1),
				}
			)
	spend_by_project.sort(key=lambda x: x["amount_raw"], reverse=True)

	# 9. Project proposals awaiting decision
	proposals = frappe.get_all(
		"Project Proposal",
		filters={"donor_profile": donor, "docstatus": ["in", [0, 1]]},
		fields=[
			"name",
			"proposal_title",
			"proposal_code",
			"sector",
			"total_budget",
			"proposed_start_date",
			"proposed_end_date",
			"workflow_state",
		],
		order_by="creation desc",
	)

	pending_proposals = []
	for prop in proposals:
		state = prop.workflow_state or ""
		if state in ["Donor Approval Pending", "Under Review", "Draft", "Internal Review", "Pending"]:
			items = frappe.get_all(
				"Budget Item", filters={"parent": prop.name}, fields=["category", "amount"]
			)
			c_capex = sum(flt(i.amount) for i in items if i.category == "CapEx")
			c_opex = sum(flt(i.amount) for i in items if i.category == "OpEx")
			c_admin = sum(flt(i.amount) for i in items if i.category == "Admin")

			months = 12
			if prop.proposed_start_date and prop.proposed_end_date:
				d1 = getdate(prop.proposed_start_date)
				d2 = getdate(prop.proposed_end_date)
				months = max(round((d2 - d1).days / 30), 1)

			pending_proposals.append(
				{
					"name": prop.name,
					"title": prop.proposal_title or prop.name,
					"code": prop.proposal_code or prop.name,
					"sector": prop.sector or "Community Development",
					"total_budget_lakh": round(flt(prop.total_budget) / 100000.0, 2),
					"duration_months": months,
					"capex_lakh": round(c_capex / 100000.0, 2),
					"opex_lakh": round(c_opex / 100000.0, 2),
					"admin_lakh": round(c_admin / 100000.0, 2),
					"state": state,
				}
			)

	# 10. Beneficiaries reached count
	beneficiaries_reached = 0
	if project_ids:
		b_count = frappe.db.sql(
			"""
			SELECT COUNT(DISTINCT beneficiary) as total
			FROM `tabBeneficiary Service`
			WHERE project IN %(projects)s AND docstatus = 1
		""",
			{"projects": tuple(project_ids)},
			as_dict=True,
		)
		if b_count and b_count[0].total:
			beneficiaries_reached = b_count[0].total

	return {
		"donor": donor,
		"currency": "INR",
		"kpis": {
			"total_given": total_given,
			"total_committed": total_committed,
			"percent_given_committed": percent_given_of_committed,
			"total_spent": total_spent,
			"percent_spent_given": percent_spent_of_given,
			"balance_available": balance_available,
			"committed_balance": committed_balance,
			"active_grants_count": active_grants_count,
			"expiring_soon_count": expiring_soon_count,
			"total_purchase_amount": total_purchases,
			"beneficiaries_reached": beneficiaries_reached,
		},
		"charts": {
			"monthly_series": monthly_series,
			"spend_by_category": spend_by_category,
			"spend_by_project": spend_by_project,
		},
		"pending_proposals": pending_proposals,
	}
