import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import cint, getdate

# Statuses that occupy a vacancy. Completed / Withdrawn free the slot.
ACTIVE_STATUSES = ("Assigned", "Active")


class VolunteerAssignment(Document):
	def validate(self):
		self.validate_dates()
		self.validate_volunteer()
		self.validate_duplicate()
		self.validate_vacancy()

	def on_update(self):
		# runs after both insert and save
		update_opportunity_filled_count(self.opportunity)
		before = self.get_doc_before_save()
		if before and before.opportunity != self.opportunity:
			update_opportunity_filled_count(before.opportunity)  # opportunity was changed

	def on_trash(self):
		update_opportunity_filled_count(self.opportunity, exclude=self.name)

	# ---- validations ---------------------------------------------------
	def validate_dates(self):
		if self.to_date and getdate(self.to_date) < getdate(self.from_date):
			frappe.throw(_("To Date cannot be before From Date."))

	def validate_volunteer(self):
		if self.status in ACTIVE_STATUSES:
			vol_status = frappe.db.get_value("Volunteer", self.volunteer, "status")
			if vol_status != "Active":
				frappe.throw(_("Volunteer {0} is {1} and cannot be assigned.").format(self.volunteer, vol_status))

	def validate_duplicate(self):
		if self.status not in ACTIVE_STATUSES:
			return
		existing = frappe.db.exists(
			"Volunteer Assignment",
			{
				"volunteer": self.volunteer,
				"opportunity": self.opportunity,
				"status": ["in", ACTIVE_STATUSES],
				"name": ["!=", self.name],
			},
		)
		if existing:
			frappe.throw(_("Volunteer is already assigned to this opportunity ({0}).").format(existing))

	def validate_vacancy(self):
		if self.status not in ACTIVE_STATUSES:
			return
		opp = frappe.db.get_value(
			"Volunteer Opportunity", self.opportunity, ["vacancies", "status"], as_dict=True
		)
		if opp.status in ("Closed", "Cancelled"):
			frappe.throw(_("Opportunity {0} is {1}.").format(self.opportunity, opp.status))
		if get_filled_count(self.opportunity, exclude=self.name) >= cint(opp.vacancies):
			frappe.throw(_("No vacancies left for opportunity {0}.").format(self.opportunity))


def get_filled_count(opportunity, exclude=None):
	filters = {"opportunity": opportunity, "status": ["in", ACTIVE_STATUSES]}
	if exclude:
		filters["name"] = ["!=", exclude]
	return frappe.db.count("Volunteer Assignment", filters)


def update_opportunity_filled_count(opportunity, exclude=None):
	"""Set filled_count, then flip Open <-> Filled. Closed / Cancelled are never touched."""
	if not opportunity:
		return
	opp = frappe.db.get_value(
		"Volunteer Opportunity", opportunity, ["vacancies", "status"], as_dict=True
	)
	if not opp:
		return

	filled = get_filled_count(opportunity, exclude)
	values = {"filled_count": filled}
	if opp.status == "Open" and filled >= cint(opp.vacancies):
		values["status"] = "Filled"
	elif opp.status == "Filled" and filled < cint(opp.vacancies):
		values["status"] = "Open"

	frappe.db.set_value("Volunteer Opportunity", opportunity, values)