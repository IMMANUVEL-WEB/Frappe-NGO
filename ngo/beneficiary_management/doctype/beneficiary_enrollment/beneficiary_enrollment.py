import frappe
from frappe import _
from frappe.model.document import Document


class BeneficiaryEnrollment(Document):
	def validate(self):
		if self.actual_end_date and self.actual_end_date < self.enrollment_date:
			frappe.throw(_("Actual End Date cannot be before Enrollment Date"))

		if self.expected_end_date and self.expected_end_date < self.enrollment_date:
			frappe.throw(_("Expected End Date cannot be before Enrollment Date"))

		if self.status == "Active":
			existing = frappe.db.exists(
				"Beneficiary Enrollment",
				{
					"beneficiary": self.beneficiary,
					"project": self.project,
					"status": "Active",
					"name": ("!=", self.name),
				},
			)
			if existing:
				frappe.throw(_("Beneficiary is already actively enrolled in this Project."))
