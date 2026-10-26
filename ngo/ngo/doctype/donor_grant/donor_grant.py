import frappe
from frappe import _
from frappe.model.document import Document


class DonorGrant(Document):
	def validate(self):
		self.validate_duplicate_project()

	def validate_duplicate_project(self):
		if not self.linked_project:
			return

		filters = {
			"linked_project": self.linked_project,
			"docstatus": ("<", 2),
		}
		if self.name:
			filters["name"] = ("!=", self.name)

		existing_grant = frappe.db.get_value("Donor Grant", filters, "name")
		if existing_grant:
			frappe.throw(
				_("A Project {1} is already linked to Donor Grant ({0}) .").format(
					frappe.bold(existing_grant),
					frappe.bold(self.linked_project),
				),
				frappe.DuplicateEntryError,
				title=_("Duplicate Project"),
			)

	def before_save(self):
		if not self.grant_id:
			self.grant_id = self.name
