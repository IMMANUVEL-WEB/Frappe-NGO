import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import cint, getdate


class VolunteerOpportunity(Document):
	def validate(self):
		if self.end_date and self.start_date and getdate(self.end_date) < getdate(self.start_date):
			frappe.throw(_("End Date cannot be before Start Date."))

		if cint(self.vacancies) < cint(self.filled_count):
			frappe.throw(
				_("Vacancies ({0}) cannot be less than already filled positions ({1}).").format(
					self.vacancies, self.filled_count
				)
			)

		# keep status in step when vacancies are edited
		if self.status == "Open" and cint(self.filled_count) >= cint(self.vacancies) > 0:
			self.status = "Filled"
		elif self.status == "Filled" and cint(self.filled_count) < cint(self.vacancies):
			self.status = "Open"