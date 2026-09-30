import json
import frappe
def get_user_fields():
    meta = frappe.get_meta('User')
    for f in meta.fields:
        if f.fieldtype == 'Section Break':
            print(f"Section: {f.fieldname} ({f.label}) - hidden: {f.hidden}")
        if 'role' in f.fieldname or 'module' in f.fieldname:
            print(f"Field: {f.fieldname} - hidden: {f.hidden}")
