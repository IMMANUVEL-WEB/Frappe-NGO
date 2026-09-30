import frappe
from frappe.model.document import Document
from frappe import _

class ServiceType(Document):
	def validate(self):
		if self.accounting_mode == "Stock Entry" and not self.default_item:
			frappe.throw(_("Default Item is required when Accounting Mode is Stock Entry"))
		if self.accounting_mode == "Journal Entry" and not self.default_expense_account:
			frappe.throw(_("Default Expense Account is required when Accounting Mode is Journal Entry"))
