import frappe

def check_db():
    print("CF: ", frappe.get_all('Custom Field', filters={'dt': 'User'}, fields=['name', 'hidden', 'depends_on', 'fieldname']))
    print("PS: ", frappe.get_all('Property Setter', filters={'doc_type': 'User'}, fields=['name', 'field_name', 'property', 'value']))
