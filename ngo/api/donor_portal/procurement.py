import frappe
from frappe import _
from frappe.utils import flt

from ngo.api.donor_portal.auth import get_current_donor


@frappe.whitelist()
def get_procurement(grant=None):
	"""
	Returns purchases and material goods procured under the donor's projects.
	Protected by NGO Settings.donor_portal_show_procurement flag.
	"""
	donor = get_current_donor(allow_admin_preview=True)

	# Check feature flag
	show_proc = frappe.db.get_single_value("NGO Settings", "donor_portal_show_procurement")
	if show_proc is not None and not bool(show_proc):
		return {"enabled": False, "items": []}

	grant_filters = {"donor_name": donor, "status": "Active"}
	if grant:
		grant_filters["name"] = grant
	grants = frappe.get_all("Donor Grant", filters=grant_filters, fields=["name", "linked_project"])
	projects = list(set([g.linked_project for g in grants if g.linked_project]))

	if not projects:
		return {"enabled": True, "items": []}

	# Query Purchase Invoice items
	items = frappe.db.sql(
		"""
		SELECT
			pii.item_code, pii.item_name, pii.qty, pii.rate, pii.amount,
			pii.uom, pi.name as invoice_no, pi.posting_date, pi.status, pi.project
		FROM `tabPurchase Invoice Item` pii
		JOIN `tabPurchase Invoice` pi ON pi.name = pii.parent
		WHERE pi.project IN %(projects)s AND pi.docstatus = 1
		ORDER BY pi.posting_date DESC
		LIMIT 50
	""",
		{"projects": tuple(projects)},
		as_dict=True,
	)

	return {"enabled": True, "items": items}
