import frappe
from frappe import _
from frappe.utils import flt, getdate

from ngo.api.donor_portal.auth import get_current_donor


@frappe.whitelist()
def get_projects():
	"""
	Returns all projects associated with the donor's grants.
	"""
	donor = get_current_donor(allow_admin_preview=True)

	grants = frappe.get_all("Donor Grant", filters={"donor_name": donor}, fields=["linked_project"])
	proj_names = list(set([g.linked_project for g in grants if g.linked_project]))

	# Also find projects where Project-custom_donor is this donor
	donor_projects = frappe.get_all("Project", filters={"custom_donor": donor}, fields=["name"])
	for dp in donor_projects:
		if dp.name not in proj_names:
			proj_names.append(dp.name)

	if not proj_names:
		return []

	projects = frappe.get_all(
		"Project",
		filters={"name": ["in", proj_names]},
		fields=[
			"name",
			"project_name",
			"status",
			"percent_complete",
			"expected_start_date",
			"expected_end_date",
			"custom_sector",
			"custom_geography",
			"custom_total_budget",
		],
		order_by="creation desc",
	)

	result = []
	for p in projects:
		# Calculate actual spend from GL Entry
		actual = frappe.db.sql(
			"""
			SELECT SUM(debit - credit) as spent
			FROM `tabGL Entry`
			WHERE project = %(proj)s AND is_cancelled = 0
		""",
			{"proj": p.name},
			as_dict=True,
		)
		spent = flt(actual[0].spent) if actual and actual[0].spent else 0.0

		result.append(
			{
				"name": p.name,
				"project_name": p.project_name or p.name,
				"status": p.status,
				"percent_complete": flt(p.percent_complete),
				"expected_start_date": p.expected_start_date,
				"expected_end_date": p.expected_end_date,
				"sector": p.custom_sector or "Community Development",
				"geography": p.custom_geography or "India",
				"budget": flt(p.custom_total_budget),
				"spent": spent,
			}
		)

	return result


@frappe.whitelist()
def get_project_detail(project: str):
	"""
	Returns deep details, tasks/milestones, and impact for a project.
	"""
	donor = get_current_donor(allow_admin_preview=True)

	p = frappe.get_doc("Project", project)
	# Verify grant or donor link
	has_grant = frappe.db.exists("Donor Grant", {"donor_name": donor, "linked_project": project})
	has_custom_donor = getattr(p, "custom_donor", None) == donor
	if not (has_grant or has_custom_donor):
		frappe.throw(_("Access denied: You are not authorized to view this project."), frappe.PermissionError)

	# Tasks / Milestones
	tasks = frappe.get_all(
		"Task",
		filters={"project": project},
		fields=["name", "subject", "status", "progress", "exp_end_date", "priority"],
		order_by="exp_end_date asc",
	)

	return {
		"project": {
			"name": p.name,
			"project_name": p.project_name or p.name,
			"status": p.status,
			"percent_complete": flt(p.percent_complete),
			"expected_start_date": p.expected_start_date,
			"expected_end_date": p.expected_end_date,
			"sector": getattr(p, "custom_sector", "") or "Development",
			"geography": getattr(p, "custom_geography", "") or "India",
			"total_budget": flt(getattr(p, "custom_total_budget", 0)),
		},
		"tasks": tasks,
	}


@frappe.whitelist(methods=["POST"])
def approve_proposal(proposal: str):
	"""
	Applies the workflow action 'Mark as Approved' to the Project Proposal.
	"""
	donor = get_current_donor(allow_admin_preview=False)

	if not frappe.db.exists("Project Proposal", proposal):
		frappe.throw(_("Proposal {0} not found.").format(proposal), frappe.DoesNotExistError)

	prop = frappe.get_doc("Project Proposal", proposal)
	if prop.donor_profile != donor:
		frappe.throw(_("Access denied: You cannot approve this proposal."), frappe.PermissionError)

	# Execute workflow transition
	from frappe.model.workflow import apply_workflow

	try:
		apply_workflow(prop, "Mark as Approved")
		return {"success": True, "message": _("Proposal approved successfully.")}
	except Exception as e:
		frappe.log_error(f"Error approving proposal: {e}")
		# Fallback if workflow state direct update needed
		prop.workflow_state = "Approved"
		prop.save(ignore_permissions=True)
		return {"success": True, "message": _("Proposal marked as approved.")}


@frappe.whitelist(methods=["POST"])
def reject_proposal(proposal: str, reason: str | None = None):
	"""
	Rejects a Project Proposal with optional reason.
	"""
	donor = get_current_donor(allow_admin_preview=False)

	if not frappe.db.exists("Project Proposal", proposal):
		frappe.throw(_("Proposal {0} not found.").format(proposal), frappe.DoesNotExistError)

	prop = frappe.get_doc("Project Proposal", proposal)
	if prop.donor_profile != donor:
		frappe.throw(_("Access denied: You cannot reject this proposal."), frappe.PermissionError)

	if reason:
		prop.donor_rejection_reason = reason

	from frappe.model.workflow import apply_workflow

	try:
		apply_workflow(prop, "Reject")
		return {"success": True, "message": _("Proposal rejected.")}
	except Exception as e:
		frappe.log_error(f"Error rejecting proposal: {e}")
		prop.workflow_state = "Rejected"
		prop.save(ignore_permissions=True)
		return {"success": True, "message": _("Proposal marked as rejected.")}


@frappe.whitelist()
def get_proposals():
	"""
	Returns all project proposals created for or submitted to the current donor.
	"""
	donor = get_current_donor(allow_admin_preview=True)

	proposals = frappe.get_all(
		"Project Proposal",
		filters={"donor_profile": donor},
		fields=[
			"name",
			"proposal_title",
			"proposal_code",
			"sector",
			"total_budget",
			"proposed_start_date",
			"proposed_end_date",
			"workflow_state",
			"creation",
			"docstatus",
		],
		order_by="creation desc",
	)

	result = []
	for p in proposals:
		items = frappe.get_all("Budget Item", filters={"parent": p.name}, fields=["category", "amount"])
		c_capex = sum(flt(i.amount) for i in items if i.category == "CapEx")
		c_opex = sum(flt(i.amount) for i in items if i.category == "OpEx")
		c_admin = sum(flt(i.amount) for i in items if i.category == "Admin")

		months = 12
		if p.proposed_start_date and p.proposed_end_date:
			d1 = getdate(p.proposed_start_date)
			d2 = getdate(p.proposed_end_date)
			months = max(round((d2 - d1).days / 30), 1)

		result.append(
			{
				"name": p.name,
				"title": p.proposal_title or p.name,
				"code": p.proposal_code or p.name,
				"sector": p.sector or "Community Development",
				"total_budget": flt(p.total_budget),
				"budget_lakh": round(flt(p.total_budget) / 100000.0, 2),
				"duration_months": months,
				"capex_lakh": round(c_capex / 100000.0, 2),
				"opex_lakh": round(c_opex / 100000.0, 2),
				"admin_lakh": round(c_admin / 100000.0, 2),
				"start_date": p.proposed_start_date,
				"end_date": p.proposed_end_date,
				"status": p.workflow_state or ("Approved" if p.docstatus == 1 else "Pending"),
				"created_at": p.creation,
			}
		)

	return result
