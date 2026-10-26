import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields


def execute():
	# 1. Reload doctypes
	try:
		frappe.reload_doc("ngo", "doctype", "donor_portal_user")
		frappe.reload_doc("ngo", "doctype", "spend_category_mapping")
		frappe.reload_doc("beneficiary_management", "doctype", "ngo_settings")
	except Exception as e:
		frappe.log_error(f"Error reloading doctypes: {e}")

	# 2. Add custom fields
	custom_fields = {
		"File": [
			{
				"fieldname": "custom_shared_with_donor",
				"label": "Shared with Donor",
				"fieldtype": "Check",
				"default": "0",
				"insert_after": "attached_to_name",
			}
		],
		"Project Proposal": [
			{
				"fieldname": "donor_rejection_reason",
				"label": "Donor Rejection Reason",
				"fieldtype": "Small Text",
				"insert_after": "approval_notes",
				"read_only": 1,
			}
		],
	}
	create_custom_fields(custom_fields, update=True)

	# 3. Add index on GL Entry
	try:
		columns = [col[0] for col in frappe.db.sql("DESC `tabGL Entry`")]
		grant_col = None
		if "custom_donor_grant" in columns:
			grant_col = "custom_donor_grant"
		elif "donor_grant" in columns:
			grant_col = "donor_grant"

		if grant_col:
			indices = [idx[2] for idx in frappe.db.sql("SHOW INDEX FROM `tabGL Entry`")]
			if "idx_gl_donor_grant" not in indices:
				frappe.db.sql(
					f"CREATE INDEX idx_gl_donor_grant ON `tabGL Entry` ({grant_col}, voucher_type, posting_date)"
				)
				frappe.db.commit()
	except Exception as e:
		frappe.log_error(f"Error adding index on GL Entry: {e}")

	# 4. Initialize NGO Settings defaults
	try:
		ngo_settings = frappe.get_single("NGO Settings")
		updated = False
		if not getattr(ngo_settings, "donor_portal_role", None):
			ngo_settings.donor_portal_role = "Donor Liaison"
			updated = True
		if getattr(ngo_settings, "donor_portal_show_procurement", None) is None:
			ngo_settings.donor_portal_show_procurement = 1
			updated = True
		if updated:
			ngo_settings.save(ignore_permissions=True)
			frappe.db.commit()
	except Exception as e:
		frappe.log_error(f"Error setting NGO Settings: {e}")
