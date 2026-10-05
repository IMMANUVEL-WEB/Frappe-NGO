import frappe

def execute():
    if not frappe.db.exists("Role", "Volunteer User"):
        role = frappe.get_doc({
            "doctype": "Role",
            "role_name": "Volunteer User"
        })
        role.insert(ignore_permissions=True)
        print("Created Role: Volunteer User")
        
    if not frappe.db.exists("Custom DocPerm", {"parent": "Volunteer Opportunity Interest", "role": "Volunteer User"}):
        perm = frappe.get_doc({
            "doctype": "Custom DocPerm",
            "parent": "Volunteer Opportunity Interest",
            "parenttype": "DocType",
            "role": "Volunteer User",
            "read": 1,
            "write": 1,
            "create": 1
        })
        perm.insert(ignore_permissions=True)
        print("Added Volunteer User permissions")
    else:
        print("Permissions already exist")
