import frappe
from frappe import _
from frappe.utils import flt, getdate, formatdate
from collections import defaultdict
from ngo.api.donor_portal.auth import get_current_donor

@frappe.whitelist()
def get_grants():
	"""
	Returns list of active/submitted grants for the current authenticated donor.
	"""
	donor = get_current_donor(allow_admin_preview=True)
	
	grants = frappe.get_all(
		"Donor Grant",
		filters={"donor_name": donor, "status": ["in", ["Active", "Closed"]]},
		fields=[
			"name", "grant_id", "grant_title", "currency", "linked_project", 
			"valid_from", "valid_to", "status", "cost_center", "funding_type", 
			"total_amount", "compliance_tag", "donor_notes"
		],
		order_by="creation desc"
	)

	# Calculate spent and received per grant
	result = []
	for g in grants:
		proj = g.linked_project
		cc = g.cost_center

		# Calculate spent from GL Entry
		spent = 0.0
		conditions = []
		params = {}
		if proj:
			conditions.append("gle.project = %(proj)s")
			params["proj"] = proj
		if cc:
			conditions.append("gle.cost_center = %(cc)s")
			params["cc"] = cc

		if conditions:
			gle = frappe.db.sql(f"""
				SELECT SUM(gle.debit - gle.credit) as total_spent
				FROM `tabGL Entry` gle
				JOIN `tabAccount` acc ON acc.name = gle.account
				WHERE ({" OR ".join(conditions)})
				  AND acc.root_type = 'Expense'
				  AND gle.is_cancelled = 0
			""", params, as_dict=True)
			if gle and gle[0].total_spent:
				spent = max(flt(gle[0].total_spent), 0.0)

		# Received funds from Payment Entry
		received = 0.0
		pe = frappe.db.sql("""
			SELECT SUM(received_amount) as total_received
			FROM `tabPayment Entry`
			WHERE party_type = 'Supplier' AND party = %(donor)s 
			  AND payment_type = 'Receive' AND docstatus = 1
		""", {"donor": donor}, as_dict=True)
		if pe and pe[0].total_received:
			# For single grant, received is total or proportionate
			received = flt(pe[0].total_received)

		total_amt = flt(g.total_amount)
		balance = max(total_amt - spent, 0.0)
		utilization = round((spent / total_amt * 100), 1) if total_amt > 0 else 0

		result.append({
			"name": g.name,
			"grant_id": g.grant_id or g.name,
			"grant_title": g.grant_title,
			"linked_project": g.linked_project,
			"currency": g.currency or "INR",
			"valid_from": g.valid_from,
			"valid_to": g.valid_to,
			"total_amount": total_amt,
			"received": received,
			"spent": spent,
			"balance": balance,
			"utilization_percent": utilization,
			"status": g.status,
			"compliance_tag": g.compliance_tag or "General",
			"funding_type": g.funding_type or "General"
		})

	return result

@frappe.whitelist()
def get_grant_detail(grant):
	"""
	Returns deep details for a specific grant, with budget vs actual and variance.
	"""
	donor = get_current_donor(allow_admin_preview=True)

	if not frappe.db.exists("Donor Grant", grant):
		frappe.throw(_("Grant {0} not found.").format(grant), frappe.DoesNotExistError)

	g = frappe.get_doc("Donor Grant", grant)
	if g.donor_name != donor:
		frappe.throw(_("Access denied: You are not authorized to view this grant."), frappe.PermissionError)

	proj = g.linked_project
	cc = g.cost_center

	# 1. Budget vs Actual comparison
	budget_vs_actual = []
	if proj:
		# Fetch the 3 separate Budget records for CapEx, OpEx, Admin
		budgets = frappe.get_all(
			"Budget",
			filters={"project": proj, "docstatus": 1},
			fields=["name", "account", "budget_amount"]
		)
		for b in budgets:
			b_acc = b.account
			b_amt = flt(b.budget_amount)
			# Find actual GL spend on this account
			actual_row = frappe.db.sql("""
				SELECT SUM(debit - credit) as actual
				FROM `tabGL Entry`
				WHERE project = %(proj)s AND account = %(acc)s AND is_cancelled = 0
			""", {"proj": proj, "acc": b_acc}, as_dict=True)
			actual_spent = flt(actual_row[0].actual) if actual_row and actual_row[0].actual else 0.0
			variance = b_amt - actual_spent
			var_pct = round((actual_spent / b_amt * 100), 1) if b_amt > 0 else 0

			category = "OpEx"
			if "capital" in b_acc.lower() or "capex" in b_acc.lower():
				category = "CapEx"
			elif "admin" in b_acc.lower():
				category = "Admin"

			budget_vs_actual.append({
				"account": b_acc,
				"category": category,
				"budget_amount": b_amt,
				"actual_spent": actual_spent,
				"variance": variance,
				"utilization_percent": var_pct
			})

	# 2. Fund Flow Timeline
	timeline = [
		{"stage": "Grant Committed", "date": g.valid_from, "amount": flt(g.total_amount), "status": "Completed"},
		{"stage": "Funds Received", "date": g.valid_from, "amount": flt(g.total_amount), "status": "Completed"},
		{"stage": "Allocated to Project", "date": g.valid_from, "amount": flt(g.total_amount), "status": "In Progress"},
		{"stage": "Utilized & Disbursed", "date": None, "amount": sum(x["actual_spent"] for x in budget_vs_actual), "status": "Active"}
	]

	return {
		"grant": {
			"name": g.name,
			"grant_id": g.grant_id or g.name,
			"grant_title": g.grant_title,
			"currency": g.currency or "INR",
			"linked_project": g.linked_project,
			"valid_from": g.valid_from,
			"valid_to": g.valid_to,
			"total_amount": flt(g.total_amount),
			"status": g.status,
			"compliance_tag": g.compliance_tag,
			"funding_type": g.funding_type,
			"cost_center": g.cost_center,
			"donor_notes": g.donor_notes
		},
		"budget_vs_actual": budget_vs_actual,
		"timeline": timeline
	}
