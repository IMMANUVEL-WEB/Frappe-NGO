import frappe
from frappe.model.document import Document

class ProjectProposal(Document):
	def before_save(self):
		if not self.proposal_code:
			self.proposal_code = self.name

		# Auto-calculate total budget server-side as well
		self.total_budget = sum((flt(row.amount) for row in (self.budget_breakdown or [])), 0.0)

	def on_submit(self):
		if self.docstatus == 1 and not self.linked_project:
			capex = 0
			opex = 0
			admin = 0
			for row in (self.budget_breakdown or []):
				amount = flt(row.amount)
				if row.category == "CapEx":
					capex += amount
				elif row.category == "OpEx":
					opex += amount
				elif row.category == "Admin":
					admin += amount
			total_budget = capex + opex + admin

			donor_cost_center = None
			if self.donor_profile:
				donor_cost_center = frappe.db.get_value(
					"Supplier",
					self.donor_profile,
					"custom_cost_center"
				)

			# Ensure Project Type "Donor Project" exists
			if not frappe.db.exists("Project Type", "Donor Project"):
				pt = frappe.get_doc({
					"doctype": "Project Type",
					"project_type": "Donor Project"
				})
				pt.insert(ignore_permissions=True)

			company = frappe.defaults.get_user_default("Company")
			if not company:
				companies = frappe.get_all("Company", limit=1, pluck="name")
				company = companies[0] if companies else None

			project = frappe.new_doc("Project")
			project.project_name = self.proposal_title
			project.company = company
			project.status = "Open"
			project.is_active = "Yes"
			project.expected_start_date = self.proposed_start_date
			project.expected_end_date = self.proposed_end_date
			project.project_type = "Donor Project"

			project.custom_project_code = self.proposal_code
			project.custom_sector = self.sector
			project.custom_geography = str(self.geography or "")
			project.custom_donor = self.donor_profile
			project.custom_funding_type = self.funding_type
			project.custom_source_proposal = self.name
			project.custom_fcra_receipt_no = self.fcra_receipt_no or ""
			project.custom_capex_budget = capex
			project.custom_opex_budget = opex
			project.custom_admin_budget = admin
			project.custom_total_budget = total_budget
			project.custom_project_phase = "Planning"
			if donor_cost_center:
				project.cost_center = donor_cost_center

			project.insert(ignore_permissions=True)

			frappe.db.set_value(
				"Project Proposal",
				self.name,
				"linked_project",
				project.name,
				update_modified=False
			)
			self.linked_project = project.name

			frappe.msgprint(
				msg=f"Project <b>{project.name}</b> created successfully.<br>Cost Center: <b>{donor_cost_center}</b>",
				title="Project Created",
				indicator="green"
			)

def flt(val):
	try:
		return float(val or 0.0)
	except (ValueError, TypeError):
		return 0.0
