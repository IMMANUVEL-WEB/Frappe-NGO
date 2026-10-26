import frappe
from frappe import _
from frappe.utils import add_days, getdate, today

from ngo.api.donor_portal.auth import get_current_donor


@frappe.whitelist()
def get_notifications():
	"""
	Returns active notifications:
	- Grants expiring within 90 days
	- Project proposals pending decision
	- Compliance renewals
	"""
	donor = get_current_donor(allow_admin_preview=True)

	notifications = []
	today_date = getdate(today())
	in_90_days = add_days(today_date, 90)

	# 1. Expiring grants
	grants = frappe.get_all(
		"Donor Grant",
		filters={"donor_name": donor, "status": "Active"},
		fields=["name", "grant_title", "valid_to"],
	)
	for g in grants:
		if g.valid_to:
			v_date = getdate(g.valid_to)
			if today_date <= v_date <= in_90_days:
				days_left = (v_date - today_date).days
				notifications.append(
					{
						"type": "warning",
						"title": _("Grant Expiring Soon"),
						"message": _("Grant '{0}' expires in {1} days (on {2}).").format(
							g.grant_title or g.name, days_left, g.valid_to
						),
						"link": f"/donor-portal/grants/{g.name}",
						"created": str(today_date),
					}
				)

	# 2. Proposals awaiting decision
	proposals = frappe.get_all(
		"Project Proposal",
		filters={"donor_profile": donor, "workflow_state": "Donor Approval Pending"},
		fields=["name", "proposal_title"],
	)
	for p in proposals:
		notifications.append(
			{
				"type": "action",
				"title": _("Project Proposal Awaiting Decision"),
				"message": _("Proposal '{0}' is pending your approval/feedback.").format(
					p.proposal_title or p.name
				),
				"link": "/donor-portal",
				"created": str(today_date),
			}
		)

	return notifications


@frappe.whitelist(methods=["POST"])
def submit_query(grant: str | None = None, subject: str | None = None, message: str | None = None):
	"""
	Submits an inquiry from the donor tied to a specific grant or project.
	Creates a ToDo / Communication for the Donor Liaison desk team.
	"""
	donor = get_current_donor(allow_admin_preview=False)

	if not subject or not message:
		frappe.throw(_("Subject and message are required."), frappe.MandatoryError)

	# Create a Communication record
	comm = frappe.new_doc("Communication")
	comm.communication_type = "Communication"
	comm.communication_medium = "Email"
	comm.subject = f"[Donor Inquiry - {donor}] {subject}"
	comm.content = message
	comm.sender = frappe.session.user
	comm.sent_or_received = "Received"
	if grant and frappe.db.exists("Donor Grant", grant):
		comm.reference_doctype = "Donor Grant"
		comm.reference_name = grant
	comm.insert(ignore_permissions=True)

	# Also create ToDo for Donor Liaison team
	todo = frappe.new_doc("ToDo")
	todo.description = f"Donor Inquiry from {donor} ({frappe.session.user}):\nSubject: {subject}\n\n{message}"
	todo.priority = "High"
	todo.reference_type = comm.reference_doctype
	todo.reference_name = comm.reference_name
	todo.insert(ignore_permissions=True)

	return {
		"success": True,
		"message": _("Your inquiry has been submitted. Our team will get back to you shortly."),
	}


@frappe.whitelist()
def get_profile():
	"""
	Returns read-only profile information for the current donor organisation.
	"""
	donor = get_current_donor(allow_admin_preview=True)

	supp = frappe.get_doc("Supplier", donor)
	grants_count = frappe.db.count("Donor Grant", {"donor_name": donor, "status": "Active"})

	# Fetch primary contact
	contact_email = frappe.session.user
	contact_phone = getattr(supp, "mobile_no", "") or ""

	return {
		"donor_name": supp.supplier_name or supp.name,
		"supplier_type": supp.supplier_type,
		"country": getattr(supp, "country", "India"),
		"contact_email": contact_email,
		"contact_phone": contact_phone,
		"active_grants_count": grants_count,
		"pan": getattr(supp, "pan", ""),
		"gstin": getattr(supp, "gstin", ""),
	}
