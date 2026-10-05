import frappe

def execute():
    perms = frappe.get_all("Custom DocPerm", 
        filters={"parent": "Volunteer Shift", "role": "Volunteer User"}, 
        fields=["read", "if_owner", "write"]
    )
    if perms:
        print(f"Custom DocPerms for Volunteer Shift: {perms}")
    else:
        # Check standard DocPerm
        std_perms = frappe.get_all("DocPerm", 
            filters={"parent": "Volunteer Shift", "role": "Volunteer User"}, 
            fields=["read", "if_owner", "write"]
        )
        print(f"Standard DocPerms for Volunteer Shift: {std_perms}")
