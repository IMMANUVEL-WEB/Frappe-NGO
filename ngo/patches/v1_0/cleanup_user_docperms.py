import frappe

def execute():
    # Delete custom docperms for User
    frappe.db.delete("Custom DocPerm", {"parent": "User"})
    # Reset perms will clear cache and restore standard
    frappe.permissions.reset_perms("User")
    frappe.clear_cache(doctype="User")
