import frappe
from frappe.model.document import Document
from frappe.utils import flt, getdate, nowdate
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
			frappe.throw(
				_("Service Date cannot be before the Enrollment Date ({0})").format(start_date)
			)

		end_date = enrollment.actual_end_date or enrollment.expected_end_date
		if end_date and service_date > getdate(end_date):
			frappe.throw(
				_("Service Date cannot be after the Enrollment End Date ({0})").format(end_date)
			)

		beneficiary = frappe.get_doc("Beneficiary", self.beneficiary)
		if not beneficiary.consent_given:
			frappe.throw(_("Cannot provide service. Beneficiary has not given consent."))

		if beneficiary.consent_withdrawn:
			frappe.throw(_("Cannot provide service. Beneficiary has withdrawn consent."))


@frappe.whitelist()
def make_journal_entry(source_name, target_doc=None):
	service = frappe.get_doc("Beneficiary Service", source_name)

	company = None
	if service.cost_center:
		company = frappe.db.get_value("Cost Center", service.cost_center, "company")
	if not company and service.project:
		company = frappe.db.get_value("Project", service.project, "company")
	if not company:
		company = frappe.defaults.get_user_default("Company") or frappe.db.get_single_value(
			"Global Defaults", "default_company"
		)

	if not service.service_type:
		frappe.throw(_("Please select a Service Type first."))

	expense_account = frappe.db.get_value(
		"Service Type", service.service_type, "default_expense_account"
	)
	if not expense_account:
		frappe.throw(
			_("Please configure 'Default Expense Account' in Service Type '{0}'").format(
				service.service_type
			)
		)

	cash_account = frappe.db.get_value("Company", company, "default_cash_account")
	if not cash_account:
		cash_account = frappe.db.get_value(
			"Account", {"company": company, "account_type": "Cash", "is_group": 0}, "name"
		)
	if not cash_account:
		frappe.throw(_("Please configure 'Default Cash Account' for Company '{0}'").format(company))

	company_currency = frappe.get_cached_value("Company", company, "default_currency")
	expense_account_currency = (
		frappe.db.get_value("Account", expense_account, "account_currency") or company_currency
	)
	cash_account_currency = (
		frappe.db.get_value("Account", cash_account, "account_currency") or company_currency
	)

	amount = flt(service.amount)

	je = frappe.new_doc("Journal Entry")
	je.voucher_type = "Journal Entry"
	je.company = company
	je.posting_date = service.service_date or nowdate()
	je.user_remark = _("Beneficiary Service: {0} for {1}").format(
		service.name, service.beneficiary or ""
	)

	# Populate custom mandatory fields from linked project or active grant if present
	donor_grant = None
	if service.project:
		donor_grant = frappe.db.get_value(
			"Donor Grant", {"linked_project": service.project}, ["name", "compliance_tag"], as_dict=True
		)
	if not donor_grant and service.cost_center:
		donor_grant = frappe.db.get_value(
			"Donor Grant", {"cost_center": service.cost_center}, ["name", "compliance_tag"], as_dict=True
		)
	if not donor_grant:
		donor_grant = frappe.db.get_value(
			"Donor Grant", {"status": "Active"}, ["name", "compliance_tag"], as_dict=True
		)

	if donor_grant:
		je.custom_donor_grant = donor_grant.name
		je.custom_compliance_tag = donor_grant.compliance_tag or "General"
	else:
		je.custom_compliance_tag = "General"

	# 1. Debit respective Service Type Expense Account
	je.append(
		"accounts",
		{
			"account": expense_account,
			"account_currency": expense_account_currency,
			"exchange_rate": 1.0,
			"debit_in_account_currency": amount,
			"debit": amount,
			"credit_in_account_currency": 0.0,
			"credit": 0.0,
			"cost_center": service.cost_center,
			"project": service.project,
		},
	)

	# 2. Credit Default Cash Account
	je.append(
		"accounts",
		{
			"account": cash_account,
			"account_currency": cash_account_currency,
			"exchange_rate": 1.0,
			"debit_in_account_currency": 0.0,
			"debit": 0.0,
			"credit_in_account_currency": amount,
			"credit": amount,
			"cost_center": service.cost_center,
			"project": service.project,
		},
	)

	je.total_debit = amount
	je.total_credit = amount
	je.difference = 0.0

	return je
