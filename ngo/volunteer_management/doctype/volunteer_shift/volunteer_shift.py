# Copyright (c) 2026, bsoft and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import time_diff_in_seconds


class VolunteerShift(Document):
	pass


@frappe.whitelist()
def make_volunteer_attendance(source_name, volunteer=None):
	shift = frappe.get_doc("Volunteer Shift", source_name)
	attendance = frappe.new_doc("Volunteer Attendance")
	attendance.shift = shift.name
	attendance.opportunity = shift.opportunity
	attendance.project = shift.project
	attendance.date = shift.shift_date or frappe.utils.today()
	attendance.in_time = shift.start_time
	attendance.out_time = shift.end_time
	attendance.status = "Present"

	# Calculate hours if start and end time exist
	if shift.start_time and shift.end_time:
		try:
			diff = time_diff_in_seconds(shift.end_time, shift.start_time)
			if diff > 0:
				attendance.total_hours = round(diff / 3600.0, 2)
			else:
				attendance.total_hours = 0.0
		except Exception:
			attendance.total_hours = 0.0
	else:
		attendance.total_hours = 0.0

	# Pick volunteer
	selected_volunteer = volunteer
	if not selected_volunteer and shift.participants:
		selected_volunteer = shift.participants[0].volunteer

	if selected_volunteer:
		attendance.volunteer = selected_volunteer
		attendance.volunteer_name = (
			frappe.db.get_value("Volunteer", selected_volunteer, "full_name") or selected_volunteer
		)

	return attendance.as_dict()
