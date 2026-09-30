import frappe
from frappe.model.document import Document
from frappe import _
from frappe.utils import getdate

class BeneficiaryAssessment(Document):
	def validate(self):
		if not self.enrollment:
			return

		enrollment = frappe.get_doc("Beneficiary Enrollment", self.enrollment)
		if getdate(self.assessment_date) < getdate(enrollment.enrollment_date):
			frappe.throw(_("Assessment Date cannot be before the Enrollment Date ({0})").format(enrollment.enrollment_date))

		if self.assessment_type == "Baseline":
			existing_baseline = frappe.db.exists(
				"Beneficiary Assessment",
				{
					"enrollment": self.enrollment,
					"assessment_type": "Baseline",
					"name": ("!=", self.name)
				}
			)
			if existing_baseline:
				frappe.throw(_("A Baseline assessment already exists for this Enrollment."))

		elif self.assessment_type == "Endline":
			existing_baseline = frappe.db.exists(
				"Beneficiary Assessment",
				{
					"enrollment": self.enrollment,
					"assessment_type": "Baseline"
				}
			)
			if not existing_baseline:
				frappe.throw(_("An Endline assessment requires an existing Baseline assessment for this Enrollment."))
