app_name = "ngo"
app_title = "Ngo"
app_publisher = "bsoft"
app_description = "Non Governmental Organization Management"
app_email = "bsoft@BSOFT-CH-L-06"
app_license = "mit"

# Apps
# ------------------
required_apps = ["erpnext"]

# Includes in <head>
# ------------------
doctype_js = {
	"Project": "public/js/project.js",
	"Payment Entry": "public/js/payment_entry.js"
}

# Document Events
# ---------------
doc_events = {
	"Project": {
		"before_save": "ngo.project_events.validate_closure_data"
	},
	"Supplier": {
		"after_insert": "ngo.supplier_events.create_supplier_cost_center"
	}
}

# Scheduled Tasks
# ---------------
scheduler_events = {
	"daily": [
		"ngo.tasks.compliance_doc_expiry_alert"
	]
}

# Fixtures
# --------
# Ordered strictly to ensure dependencies resolve on clean install:
# Roles -> Workflow States -> Workflow Action Masters -> Workflows -> Custom Fields -> Property Setters -> Reports -> Dashboard Charts -> Dashboards -> Print Formats -> Notifications
fixtures = [
	# 1. Custom Roles needed for Workflows and DocTypes
	{
		"dt": "Role",
		"filters": [
			["name", "in", [
				"Program Manager",
				"Donor Liaison",
				"Internal Reviewer",
				"Employee Self Service"
			]]
		]
	},

	# 2. Workflow States
	{
		"dt": "Workflow State",
		"filters": [
			["name", "in", [
				"Draft",
				"Internal Review",
				"Donor Approval Pending",
				"Approved",
				"Rejected"
			]]
		]
	},

	# 3. Workflow Action Masters
	{
		"dt": "Workflow Action Master",
		"filters": [
			["name", "in", [
				"Submit for Review",
				"Send to Donor",
				"Mark as Approved",
				"Reject",
				"Revise and Resubmit"
			]]
		]
	},

	# 4. Workflows
	{
		"dt": "Workflow",
		"filters": [
			["name", "in", [
				"Project Proposal Approval"
			]]
		]
	},

	# 5. Custom Fields on Standard ERPNext DocTypes
	{
		"dt": "Custom Field",
		"filters": [
			["name", "in", [
				"Project-custom_project_code",
				"Project-custom_sector",
				"Project-custom_geography",
				"Project-custom_donor",
				"Project-custom_funding_type",
				"Project-custom_source_proposal",
				"Project-custom_capex_budget",
				"Project-custom_opex_budget",
				"Project-custom_admin_budget",
				"Project-custom_total_budget",
				"Project-custom_fcra_receipt_no",
				"Project-custom_compliance_documents",
				"Project-custom_project_phase",
				"Project-custom_reason_for_suspended",
				"Project-custom_impact_metrics",
				"Project-custom_closure_summary",
				"Supplier-custom_cost_center",
				"Payment Entry-custom_destination",
				"Journal Entry-custom_donor_grant",
				"Journal Entry-custom_compliance_tag"
			]]
		]
	},

	# 6. Property Setters on Standard ERPNext DocTypes
	{
		"dt": "Property Setter",
		"filters": [
			["name", "in", [
				"Project-main-field_order",
				"Supplier-main-field_order",
				"Payment Entry-main-field_order",
				"Journal Entry-main-field_order",
				"Budget-budget_against-options",
				"Project-naming_series-options",
				"Budget-naming_series-options",
				"Supplier-naming_series-options",
				"Payment Entry-naming_series-options",
				"Journal Entry-naming_series-options"
			]]
		]
	},

	# 7. Reports
	{
		"dt": "Report",
		"filters": [
			["name", "in", [
				"Pipeline project",
				"Project Proposal Status",
				"Budget utilization"
			]]
		]
	},

	# 8. Dashboard Charts
	{
		"dt": "Dashboard Chart",
		"filters": [
			["chart_name", "in", [
				"Projects by Status",
				"Active Projects Count",
				"Projects by Funding Type",
				"Total Budget by Project",
				"Projects by Phase",
				"Proposal Pipeline",
				"Budget vs Actual by Grant",
				"Total Active Grants",
				"Spending by Compliance Tag",
				"Payment Receipts Over Time",
				"Expenses by Account (Monthly)"
			]]
		]
	},

	# 9. Dashboards
	{
		"dt": "Dashboard",
		"filters": [
			["name", "in", [
				"Caritas India — Project Dashboard",
				"Caritas India — Finance Dashboard"
			]]
		]
	},

	# 10. Print Formats
	{
		"dt": "Print Format",
		"filters": [
			["name", "in", [
				"Project Proposal - Domestic Grant",
				"Project Proposal - CSR",
				"Project Proposal - FCRA"
			]]
		]
	},

	# 11. Notifications
	{
		"dt": "Notification",
		"filters": [
			["name", "in", [
				"Internal review in project proposal",
				"Approval pending",
				"Grant Expiry Alert",
				"Donor Grant",
				"New Project Arrived"
			]]
		]
	}
]
