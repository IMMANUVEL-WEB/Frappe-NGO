import frappe
from frappe import _


def validate_closure_data(doc, method=None):
	if doc.status == "Completed":
		if not doc.get("custom_impact_metrics"):
			frappe.throw(
				msg=_(
					"<b>Impact Metrics</b> is required before marking this project as Completed. Please fill it in."
				),
				title=_("Closure Data Required"),
			)
		if not doc.get("custom_closure_summary"):
			frappe.throw(
				msg=_(
					"<b>Closure Summary</b> is required before marking this project as Completed. Please fill it in."
				),
				title=_("Closure Data Required"),
			)
		doc.custom_project_phase = "Closed"
