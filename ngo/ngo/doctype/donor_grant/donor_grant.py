import frappe
from frappe.model.document import Document

class DonorGrant(Document):
	def before_save(self):
		if not self.grant_id:
			self.grant_id = self.name
