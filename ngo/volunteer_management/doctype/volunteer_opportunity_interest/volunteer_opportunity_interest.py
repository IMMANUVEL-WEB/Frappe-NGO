# Copyright (c) 2026, bsoft and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class VolunteerOpportunityInterest(Document):
	pass


@frappe.whitelist()
def make_volunteer_shift(source_name: str):
	interest = frappe.get_doc("Volunteer Opportunity Interest", source_name)
	shift = frappe.new_doc("Volunteer Shift")
	shift.opportunity = interest.opportunity
	if interest.opportunity:
		shift.project = frappe.db.get_value("Volunteer Opportunity", interest.opportunity, "project")
		start_date = frappe.db.get_value("Volunteer Opportunity", interest.opportunity, "start_date")
		shift.shift_date = start_date or frappe.utils.today()
	else:
		shift.shift_date = frappe.utils.today()
	shift.status = "Scheduled"
	shift.required_count = 1
	if interest.volunteer:
		vol_name = frappe.db.get_value("Volunteer", interest.volunteer, "full_name") or interest.volunteer
		shift.append(
			"participants",
			{"volunteer": interest.volunteer, "volunteer_name": vol_name, "status": "Confirmed"},
		)
	return shift.as_dict()
