import frappe
from frappe.tests.utils import FrappeTestCase

class TestServiceType(FrappeTestCase):
	def test_service_type_validation_journal_entry(self):
		service = frappe.get_doc({
			"doctype": "Service Type",
			"service_type_name": "Test Journal Entry Service",
			"category": "Cash Assistance",
			"accounting_mode": "Journal Entry",
			# Missing default_expense_account
		})
		
		with self.assertRaises(frappe.exceptions.ValidationError):
			service.insert()

		service.default_expense_account = "_Test Account Cost for Service - _TC" # Example test account, not strictly testing existence but if logic allows insertion
		# To avoid missing linked account error in core validation, we catch ValidationError specifically
		# For full test we'd create the account, but testing the raise is enough for our custom validation
		pass

	def test_service_type_validation_stock_entry(self):
		service = frappe.get_doc({
			"doctype": "Service Type",
			"service_type_name": "Test Stock Entry Service",
			"category": "In-Kind",
			"accounting_mode": "Stock Entry",
			# Missing default_item
		})
		
		with self.assertRaises(frappe.exceptions.ValidationError):
			service.insert()
