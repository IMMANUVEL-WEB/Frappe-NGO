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
			frappe.db.add_index("GL Entry", [grant_col, "voucher_type", "posting_date"], "idx_gl_donor_grant")
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
		if getattr(ngo_settings, "footer_enabled", None) is None or ngo_settings.footer_enabled == 0:
			ngo_settings.footer_enabled = 1
			updated = True
		if not getattr(ngo_settings, "footer_organization_name", None):
			ngo_settings.footer_organization_name = "Non Governmentl Organization"
			updated = True
		if not getattr(ngo_settings, "footer_tagline", None):
			ngo_settings.footer_tagline = "Non Governmentl Organization Platform"
			updated = True
		if not getattr(ngo_settings, "footer_copyright_text", None):
			ngo_settings.footer_copyright_text = "© 2026 Non Governmentl Organization. All rights reserved."
			updated = True
		if not getattr(ngo_settings, "footer_powered_by", None):
			ngo_settings.footer_powered_by = "Non Governmentl Organization Platform"
			updated = True
		if (
			getattr(ngo_settings, "footer_show_quick_links", None) is None
			or ngo_settings.footer_show_quick_links == 0
		):
			ngo_settings.footer_show_quick_links = 1
			updated = True
		if (
			getattr(ngo_settings, "footer_show_social_links", None) is None
			or ngo_settings.footer_show_social_links == 0
		):
			ngo_settings.footer_show_social_links = 1
			updated = True
		if (
			getattr(ngo_settings, "footer_show_contact_info", None) is None
			or ngo_settings.footer_show_contact_info == 0
		):
			ngo_settings.footer_show_contact_info = 1
			updated = True
		if not getattr(ngo_settings, "footer_contact_email", None):
			ngo_settings.footer_contact_email = "ngo@support.com"
			updated = True
		if not getattr(ngo_settings, "footer_contact_phone", None):
			ngo_settings.footer_contact_phone = "+91 1234567890"
			updated = True
		if updated:
			ngo_settings.save(ignore_permissions=True)
			frappe.db.commit()  # nosemgrep
	except Exception as e:
		frappe.log_error(f"Error setting NGO Settings: {e}")
