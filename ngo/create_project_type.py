import frappe

def create_project_type():
    if not frappe.db.exists("Project Type", "Donor Project"):
        frappe.get_doc({
            "doctype": "Project Type",
            "project_type": "Donor Project"
        }).insert(ignore_permissions=True)
        print("Created Project Type 'Donor Project'")
    else:
        print("Project Type 'Donor Project' already exists")
    
    frappe.db.commit()
