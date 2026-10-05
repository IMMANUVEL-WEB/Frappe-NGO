import frappe
from frappe import _
from frappe.model.document import Document
from frappe.query_builder.functions import Sum
from frappe.utils import flt, get_time, getdate, nowdate


def _to_seconds(value):
	"""Convert a Time field value (str / time / timedelta) to seconds since midnight."""
	t = get_time(value)
	return t.hour * 3600 + t.minute * 60 + t.second


class VolunteerAttendance(Document):
	def validate(self):
		self.validate_date()
		self.validate_duplicate()
		self.set_total_hours()

	def on_submit(self):
		update_volunteer_hours(self.volunteer)

	def on_cancel(self):
		# docstatus is already 2 here, so this row is excluded from the sum
		update_volunteer_hours(self.volunteer)

	# ---- helpers -------------------------------------------------------
	def validate_date(self):
		if getdate(self.date) > getdate(nowdate()):
			frappe.throw(_("Attendance cannot be marked for a future date."))

	def validate_duplicate(self):
		filters = {
			"volunteer": self.volunteer,
			"date": self.date,
			"docstatus": ["<", 2],
			"name": ["!=", self.name],
		}
		if self.shift:
			filters["shift"] = self.shift
		existing = frappe.db.exists("Volunteer Attendance", filters)
		if existing:
			frappe.throw(
				_("Attendance already exists for this volunteer on this date/shift: {0}").format(
					frappe.bold(existing)
				)
			)

	def set_total_hours(self):
		if self.status == "Absent":
			self.in_time = None
			self.out_time = None
			self.total_hours = 0
			return

		if not (self.in_time and self.out_time):
			frappe.throw(_("In Time and Out Time are required when status is {0}.").format(self.status))

		seconds = _to_seconds(self.out_time) - _to_seconds(self.in_time)
		if seconds <= 0:
			frappe.throw(_("Out Time must be after In Time."))

		self.total_hours = flt(seconds / 3600, 2)


def update_volunteer_hours(volunteer):
	"""Recalculate Volunteer.total_hours from all submitted attendance rows."""
	if not volunteer:
		return
	VA = frappe.qb.DocType("Volunteer Attendance")
	total = (
		frappe.qb.from_(VA)
		.select(Sum(VA.total_hours))
		.where((VA.volunteer == volunteer) & (VA.docstatus == 1))
	).run()[0][0]
	frappe.db.set_value("Volunteer", volunteer, "total_hours", flt(total, 2), update_modified=False)
