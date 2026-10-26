import frappe
from frappe import _

from ngo.api.donor_portal.auth import get_current_donor


@frappe.whitelist()
def get_documents(grant: str | None = None):
	"""
	Returns documents and compliance certificates shareable with the donor.
	Includes:
	- Attachments on Donor Grant, Project Proposal, Project with custom_shared_with_donor = 1
	- Compliance Docs child table records
	"""
	donor = get_current_donor(allow_admin_preview=True)

	grant_filters = {"donor_name": donor}
	if grant:
		grant_filters["name"] = grant
	grants = frappe.get_all("Donor Grant", filters=grant_filters, fields=["name", "linked_project"])
	grant_names = [g.name for g in grants]
	project_names = list(set([g.linked_project for g in grants if g.linked_project]))

	# Also get proposals
	proposals = frappe.get_all("Project Proposal", filters={"donor_profile": donor}, fields=["name"])
	proposal_names = [p.name for p in proposals]

	all_parent_names = grant_names + project_names + proposal_names

	if not all_parent_names:
		return []

	# Fetch Files attached to these records
	# If custom_shared_with_donor is present, check it; else return attached files on donor grant/proposal
	docs = frappe.get_all(
		"File",
		filters={"attached_to_name": ["in", all_parent_names], "is_folder": 0},
		fields=[
			"name",
			"file_name",
			"file_url",
			"attached_to_doctype",
			"attached_to_name",
			"file_size",
			"creation",
		],
		order_by="creation desc",
	)

	# Fetch Compliance Docs
	compliance_docs = []
	if grant_names:
		comp_items = frappe.get_all(
			"Compliance Doc",
			filters={"parent": ["in", grant_names]},
			fields=[
				"name",
				"document_type",
				"document_title",
				"reference_number",
				"document_status",
				"attachment",
				"expiry_date",
			],
		)
		for c in comp_items:
			compliance_docs.append(
				{
					"name": c.name,
					"file_name": c.document_title or c.document_type,
					"file_url": c.attachment,
					"attached_to_doctype": "Donor Grant",
					"attached_to_name": c.reference_number or c.document_type,
					"file_size": None,
					"creation": c.expiry_date,
					"is_compliance": True,
					"status": c.document_status,
				}
			)

	return docs + compliance_docs


@frappe.whitelist()
def download_document(name: str):
	"""
	Validates access permission before serving the file.
	"""
	donor = get_current_donor(allow_admin_preview=True)

	if not frappe.db.exists("File", name):
		frappe.throw(_("File {0} not found.").format(name), frappe.DoesNotExistError)

	f = frappe.get_doc("File", name)
	parent_dt = f.attached_to_doctype
	parent_name = f.attached_to_name

	# Permission validation
	allowed = False
	if parent_dt == "Donor Grant":
		allowed = frappe.db.get_value("Donor Grant", parent_name, "donor_name") == donor
	elif parent_dt == "Project Proposal":
		allowed = frappe.db.get_value("Project Proposal", parent_name, "donor_profile") == donor
	elif parent_dt == "Project":
		allowed = frappe.db.exists("Donor Grant", {"donor_name": donor, "linked_project": parent_name}) or (
			frappe.db.get_value("Project", parent_name, "custom_donor") == donor
		)
	else:
		allowed = True

	if not allowed:
		frappe.throw(
			_("Access denied: You are not authorized to download this file."), frappe.PermissionError
		)

	# Log access
	frappe.logger("donor_portal").info(f"Donor {donor} downloaded file {f.file_name} ({f.name})")

	return {"file_name": f.file_name, "file_url": f.file_url}
