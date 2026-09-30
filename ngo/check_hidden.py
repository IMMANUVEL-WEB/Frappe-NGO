import frappe
def check_hidden_ps():
    ps = frappe.db.sql("SELECT name, doc_type, field_name FROM `tabProperty Setter` WHERE property='hidden' AND value='1'", as_dict=True)
    for p in ps:
        if 'role' in p['field_name'] or 'user' in p['doc_type'].lower():
            print("Found Hidden:", p)
    cf = frappe.db.sql("SELECT name, dt, fieldname FROM `tabCustom Field` WHERE hidden=1", as_dict=True)
    for c in cf:
        if 'role' in c['fieldname'] or 'user' in c['dt'].lower():
            print("Found Custom Field Hidden:", c)
