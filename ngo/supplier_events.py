import frappe

def create_supplier_cost_center(doc, method=None):
	company = doc.get("company") or frappe.defaults.get_user_default("Company")
	if not company:
		companies = frappe.get_all("Company", limit=1, pluck="name")
		company = companies[0] if companies else None

	if not company:
		return

	parent_cc = None
	if doc.supplier_type == "Donor":
		donor_ccs = frappe.get_all(
			"Cost Center",
			filters={"company": company, "cost_center_name": ["like", "%Donor%"], "is_group": 1},
			pluck="name",
			limit=1
		)
		if donor_ccs:
			parent_cc = donor_ccs[0]

	if not parent_cc:
		root_ccs = frappe.get_all(
			"Cost Center",
			filters={"company": company, "is_group": 1},
			pluck="name",
			limit=1
		)
		if root_ccs:
			parent_cc = root_ccs[0]

	if parent_cc and not frappe.db.exists("Cost Center", {"cost_center_name": doc.supplier_name, "company": company}):
		cc = frappe.get_doc({
			"doctype": "Cost Center",
			"cost_center_name": doc.supplier_name,
			"parent_cost_center": parent_cc,
			"company": company,
			"is_group": 0
		})
		cc.insert(ignore_permissions=True)
		frappe.db.set_value("Supplier", doc.name, "custom_cost_center", cc.name, update_modified=False)
		doc.custom_cost_center = cc.name
