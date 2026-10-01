import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import today


class VolunteerApplication(Document):
	def validate(self):
		self.validate_pending_duplicate()

		if self.status == "Rejected" and not self.review_remarks:
			frappe.throw(_("Please enter Review Remarks when rejecting an application."))

		if self.status in ("Approved", "Rejected") and not self.reviewed_by:
			self.reviewed_by = frappe.session.user

	def on_submit(self):
		# Workflow: Pending -> Approve (submit) -> status = Approved
		if self.status == "Approved":
			self.create_volunteer()

	# ---- helpers -------------------------------------------------------
	def validate_pending_duplicate(self):
		if self.status != "Pending":
			return
		existing = frappe.db.exists(
			"Volunteer Application",
			{"email": self.email, "status": "Pending", "name": ["!=", self.name], "docstatus": 0},
		)
		if existing:
			frappe.throw(_("A pending application already exists for {0}: {1}").format(self.email, existing))

	def create_volunteer(self):
		if self.volunteer:
			return

		# reuse an existing volunteer with the same email instead of duplicating
		existing = frappe.db.get_value("Volunteer", {"email": self.email}, "name")
		if existing:
			self.db_set("volunteer", existing)
			frappe.msgprint(_("Linked to existing Volunteer {0}.").format(existing), alert=True)
			return

		vol = frappe.new_doc("Volunteer")
		vol.update(
			{
				"full_name": self.applicant_name,
				"email": self.email,
				"phone": self.phone,
				"address": self.address,
				"date_of_birth": self.date_of_birth,
				"gender": self.gender,
				"joined_on": today(),
				"status": "Active",
			}
		)
		for row in self.skills:
			vol.append("skills", {"skill": row.skill, "proficiency": row.proficiency})
		for row in self.availability:
			vol.append(
				"availability",
				{"day_of_week": row.day_of_week, "from_time": row.from_time, "to_time": row.to_time},
			)
		vol.insert(ignore_permissions=True)

		self.db_set("volunteer", vol.name)
		frappe.msgprint(
			_("Volunteer {0} created.").format(frappe.utils.get_link_to_form("Volunteer", vol.name)),
			alert=True,
		)