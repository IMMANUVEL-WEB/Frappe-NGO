import frappe
from frappe.model.document import Document
from frappe.utils import flt

class BeneficiaryService(Document):
	def validate(self):
		self.amount = flt(self.qty) * flt(self.rate)
