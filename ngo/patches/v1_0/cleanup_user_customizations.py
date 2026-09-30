import frappe

def execute():
    # Remove any Property Setters or Custom Fields on User that hide role fields
    frappe.db.delete("Property Setter", {
        "doc_type": "User",
        "field_name": ("in", ["role_profile_name", "role_profiles", "roles", "roles_html", "roles_section", "sb1", "modules_html", "module_profile", "sb_allow_modules"])
    })
    
    frappe.db.delete("Custom Field", {
        "dt": "User",
        "fieldname": ("in", ["role_profile_name", "role_profiles", "roles", "roles_html", "roles_section", "sb1", "modules_html", "module_profile", "sb_allow_modules"])
    })
    
    frappe.clear_cache(doctype="User")
