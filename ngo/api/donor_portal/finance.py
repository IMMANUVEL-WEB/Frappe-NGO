import frappe
from frappe import _
from frappe.utils import flt, getdate, formatdate
from collections import defaultdict
from ngo.api.donor_portal.auth import get_current_donor

@frappe.whitelist()
def get_spend_breakdown(grant=None, from_date=None, to_date=None):
	"""
	Returns detailed categorization:
	Goods purchased vs Cash assistance vs Services/salaries vs Admin vs Remaining balance.
	"""
	donor = get_current_donor(allow_admin_preview=True)

	grant_filters = {"donor_name": donor, "status": "Active"}
	if grant:
		grant_filters["name"] = grant
	grants = frappe.get_all("Donor Grant", filters=grant_filters, fields=["name", "linked_project", "total_amount"])

	projects = list(set([g.linked_project for g in grants if g.linked_project]))
	total_committed = sum(flt(g.total_amount) for g in grants)

	if not projects:
		return {
			"goods": 0.0,
			"cash_assistance": 0.0,
			"services_salaries": 0.0,
			"admin": 0.0,
			"remaining_balance": total_committed
		}

	# Category breakdown from GL Entry
	conditions = ["gle.project IN %(projects)s", "acc.root_type = 'Expense'", "gle.is_cancelled = 0", "gle.debit > 0"]
	params = {"projects": tuple(projects)}
	if from_date:
		conditions.append("gle.posting_date >= %(from_date)s")
		params["from_date"] = from_date
	if to_date:
		conditions.append("gle.posting_date <= %(to_date)s")
		params["to_date"] = to_date

	query_where = " AND ".join(conditions)
	entries = frappe.db.sql(f"""
		SELECT gle.account, SUM(gle.debit - gle.credit) as amount
		FROM `tabGL Entry` gle
		JOIN `tabAccount` acc ON acc.name = gle.account
		WHERE {query_where}
		GROUP BY gle.account
	""", params, as_dict=True)

	category_map = {}
	if frappe.db.table_exists("Spend Category Mapping"):
		mappings = frappe.get_all("Spend Category Mapping", fields=["account", "category"])
		for m in mappings:
			category_map[m.account] = m.category

	goods = 0.0
	cash_assistance = 0.0
	services = 0.0
	admin = 0.0

	for e in entries:
		amt = flt(e.amount)
		acc_name = e.account or ""
		cat = category_map.get(acc_name)
		if cat:
			if cat == "Goods" or cat == "CapEx":
				goods += amt
			elif cat == "Cash Assistance":
				cash_assistance += amt
			elif cat == "Services" or cat == "OpEx":
				services += amt
			else:
				admin += amt
		else:
			acc_lower = acc_name.lower()
			if "capital" in acc_lower or "material" in acc_lower or "goods" in acc_lower or "stock" in acc_lower:
				goods += amt
			elif "cash" in acc_lower or "relief" in acc_lower or "aid" in acc_lower:
				cash_assistance += amt
			elif "salary" in acc_lower or "service" in acc_lower or "fee" in acc_lower or "program" in acc_lower:
				services += amt
			else:
				admin += amt

	total_spent = goods + cash_assistance + services + admin
	remaining = max(total_committed - total_spent, 0.0)

	return {
		"goods": round(goods, 2),
		"cash_assistance": round(cash_assistance, 2),
		"services_salaries": round(services, 2),
		"admin": round(admin, 2),
		"total_spent": round(total_spent, 2),
		"remaining_balance": round(remaining, 2)
	}

@frappe.whitelist()
def get_transactions(grant=None, from_date=None, to_date=None, category=None, page=1, page_size=20):
	"""
	Paginated GL transactions for donor projects with party confidentiality check.
	"""
	donor = get_current_donor(allow_admin_preview=True)
	page = int(page or 1)
	page_size = int(page_size or 20)
	offset = (page - 1) * page_size

	grant_filters = {"donor_name": donor, "status": "Active"}
	if grant:
		grant_filters["name"] = grant
	grants = frappe.get_all("Donor Grant", filters=grant_filters, fields=["name", "linked_project"])
	projects = list(set([g.linked_project for g in grants if g.linked_project]))

	if not projects:
		return {"transactions": [], "total_count": 0, "page": page, "page_size": page_size}

	conditions = ["gle.project IN %(projects)s", "acc.root_type = 'Expense'", "gle.is_cancelled = 0", "gle.debit > 0"]
	params = {"projects": tuple(projects), "limit": page_size, "offset": offset}
	if from_date:
		conditions.append("gle.posting_date >= %(from_date)s")
		params["from_date"] = from_date
	if to_date:
		conditions.append("gle.posting_date <= %(to_date)s")
		params["to_date"] = to_date

	query_where = " AND ".join(conditions)

	# Check vendor visibility setting
	show_vendor = False
	try:
		show_vendor = bool(frappe.db.get_single_value("NGO Settings", "donor_portal_show_vendor_names"))
	except Exception:
		pass

	# Count total
	count_res = frappe.db.sql(f"""
		SELECT COUNT(*) as total
		FROM `tabGL Entry` gle
		JOIN `tabAccount` acc ON acc.name = gle.account
		WHERE {query_where}
	""", params, as_dict=True)
	total_count = count_res[0].total if count_res else 0

	# Fetch rows
	rows = frappe.db.sql(f"""
		SELECT
			gle.name, gle.posting_date, gle.account, gle.debit, gle.credit,
			gle.voucher_type, gle.voucher_no, gle.party, gle.remarks, gle.project
		FROM `tabGL Entry` gle
		JOIN `tabAccount` acc ON acc.name = gle.account
		WHERE {query_where}
		ORDER BY gle.posting_date DESC, gle.creation DESC
		LIMIT %(limit)s OFFSET %(offset)s
	""", params, as_dict=True)

	transactions = []
	for r in rows:
		party_display = "Authorized Vendor / Partner"
		if show_vendor and r.party:
			party_display = r.party

		cat_label = "OpEx"
		acc_lower = (r.account or "").lower()
		if "capital" in acc_lower or "capex" in acc_lower:
			cat_label = "CapEx"
		elif "admin" in acc_lower:
			cat_label = "Admin"

		transactions.append({
			"name": r.name,
			"date": r.posting_date,
			"account": r.account,
			"category": cat_label,
			"amount": flt(r.debit),
			"currency": "INR",
			"voucher_type": r.voucher_type,
			"voucher_no": r.voucher_no,
			"party": party_display,
			"remarks": r.remarks or "",
			"project": r.project
		})

	return {
		"transactions": transactions,
		"total_count": total_count,
		"page": page,
		"page_size": page_size
	}
