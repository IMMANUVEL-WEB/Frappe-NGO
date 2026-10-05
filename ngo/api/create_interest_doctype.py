import frappe

def execute():
    if not frappe.db.exists("DocType", "Volunteer Opportunity Interest"):
        doc = frappe.get_doc({
            "doctype": "DocType",
            "name": "Volunteer Opportunity Interest",
            "module": "Volunteer Management",
            "custom": 0,
            "naming_rule": "Expression",
            "autoname": "format:VOI-{opportunity}-{volunteer}-{####}",
            "is_submittable": 0,
            "fields": [
                {
                    "fieldname": "volunteer",
                    "fieldtype": "Link",
                    "label": "Volunteer",
                    "options": "Volunteer",
                    "reqd": 1,
                    "in_list_view": 1
                },
                {
                    "fieldname": "opportunity",
                    "fieldtype": "Link",
                    "label": "Volunteer Opportunity",
                    "options": "Volunteer Opportunity",
                    "reqd": 1,
                    "in_list_view": 1
                },
                {
                    "fieldname": "status",
                    "fieldtype": "Select",
                    "label": "Status",
                    "options": "Pending\nApproved\nRejected",
                    "default": "Pending",
                    "in_list_view": 1
                },
                {
                    "fieldname": "notes",
                    "fieldtype": "Small Text",
                    "label": "Notes"
                }
            ],
            "permissions": [
                {
                    "role": "System Manager",
                    "read": 1,
                    "write": 1,
                    "create": 1,
                    "delete": 1
                }
            ]
        })
        doc.insert(ignore_permissions=True)
        print("Successfully created Volunteer Opportunity Interest DocType")
    else:
        print("DocType already exists")
