import frappe
from frappe.model.document import Document
from frappe.utils import getdate, today, date_diff
from frappe import _

class Beneficiary(Document):
	def validate(self):
		self.calculate_ages()
		self.check_duplicate_id()
		self.check_duplicate_warning()

	def calculate_ages(self):
		self.age = self.get_age_string(self.date_of_birth)
		
		for member in self.family_members:
			member.age = self.get_age_string(member.date_of_birth)

	def get_age_string(self, dob):
		if not dob:
			return ""
		
		dob_date = getdate(dob)
		today_date = getdate(today())
		
		if dob_date > today_date:
			frappe.throw(_("Date of Birth cannot be in the future."))
			
		years = today_date.year - dob_date.year - ((today_date.month, today_date.day) < (dob_date.month, dob_date.day))
		
		if years < 2:
			months = (today_date.year - dob_date.year) * 12 + (today_date.month - dob_date.month)
			if today_date.day < dob_date.day:
				months -= 1
			return f"{months} months"
		else:
			return f"{years} years"

	def check_duplicate_id(self):
		if self.national_id_type and self.national_id_number:
			existing = frappe.db.exists(
				"Beneficiary", 
				{
					"national_id_type": self.national_id_type,
					"national_id_number": self.national_id_number,
					"name": ("!=", self.name)
				}
			)
			if existing:
				frappe.throw(_("Beneficiary with this National ID already exists: {0}").format(existing))

	def check_duplicate_warning(self):
		if self.full_name and self.date_of_birth and self.territory:
			existing = frappe.db.exists(
				"Beneficiary",
				{
					"full_name": self.full_name,
					"date_of_birth": self.date_of_birth,
					"territory": self.territory,
					"name": ("!=", self.name)
				}
			)
			if existing:
				frappe.msgprint(_("Warning: A beneficiary with the same name, date of birth, and territory already exists ({0})").format(existing), alert=True)
