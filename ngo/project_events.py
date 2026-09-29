import frappe

def validate_closure_data(doc, method=None):
	if doc.status == "Completed":
		if not doc.get("custom_impact_metrics"):
			frappe.throw(
				msg="<b>Impact Metrics</b> is required before marking this project as Completed. Please fill it in.",
				title="Closure Data Required"
			)
		if not doc.get("custom_closure_summary"):
			frappe.throw(
				msg="<b>Closure Summary</b> is required before marking this project as Completed. Please fill it in.",
				title="Closure Data Required"
			)
		doc.custom_project_phase = "Closed"
