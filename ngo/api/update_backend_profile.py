import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_field
import os

def execute():
    # 1. Add image custom field to Volunteer if missing
    try:
        create_custom_field('Volunteer', {
            'fieldname': 'image',
            'label': 'Image',
            'fieldtype': 'Attach Image',
            'insert_after': 'full_name'
        })
        print("Added 'image' field to Volunteer doctype.")
    except Exception as e:
        print(f"Custom field might already exist or error: {e}")

    # 2. Update volunteer.py to support image and password
    path = '/home/bsoft/frappe-bench-v16/apps/ngo/ngo/api/volunteer.py'
    with open(path, 'r') as f:
        content = f.read()

    # Modify my_profile to return image
    if '"image": doc.image' not in content:
        content = content.replace(
            '"full_name": doc.full_name,',
            '"full_name": doc.full_name,\n        "image": doc.image,'
        )

    # Modify update_my_profile to handle image
    if 'def update_my_profile(phone=None, address=None, availability=None' in content:
        content = content.replace(
            'def update_my_profile(phone=None, address=None, availability=None):',
            'def update_my_profile(phone=None, address=None, availability=None, image=None):'
        )
        content = content.replace(
            'if address is not None:',
            'if image is not None:\n        doc.image = image\n        \n    if address is not None:'
        )

    # Add change_password method
    if 'def update_password' not in content:
        password_method = """
@frappe.whitelist()
def update_password(old_password, new_password):
    user = frappe.session.user
    
    if user == "Guest":
        frappe.throw("Not logged in")
        
    try:
        frappe.core.doctype.user.user.update_password(old_password, new_password)
        return "Password updated successfully"
    except frappe.AuthenticationError:
        frappe.throw("Incorrect old password", frappe.AuthenticationError)
"""
        content += password_method

    with open(path, 'w') as f:
        f.write(content)
    
    print("Backend API updated for password and image.")
