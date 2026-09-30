import frappe
from frappe.model.document import Document
from frappe.utils import flt, getdate
from frappe import _

class BeneficiaryService(Document):
	def validate(self):
		self.amount = flt(self.qty) * flt(self.rate)
		self.validate_enrollment_and_consent()

	def validate_enrollment_and_consent(self):
		if not self.enrollment:
			return

		enrollment = frappe.get_doc("Beneficiary Enrollment", self.enrollment)
		
		if enrollment.status != "Active":
			frappe.throw(_("Service can only be provided for an Active enrollment."))

		service_date = getdate(self.service_date)
		start_date = getdate(enrollment.enrollment_date)
		
		if service_date < start_date:
			frappe.throw(_("Service Date cannot be before the Enrollment Date ({0})").format(start_date))

		end_date = enrollment.actual_end_date or enrollment.expected_end_date
		if end_date and service_date > getdate(end_date):
			frappe.throw(_("Service Date cannot be after the Enrollment End Date ({0})").format(end_date))

		beneficiary = frappe.get_doc("Beneficiary", self.beneficiary)
		if not beneficiary.consent_given:
			frappe.throw(_("Cannot provide service. Beneficiary has not given consent."))
		
		if beneficiary.consent_withdrawn:
			frappe.throw(_("Cannot provide service. Beneficiary has withdrawn consent."))
