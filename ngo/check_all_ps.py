import frappe
def check_all_ps():
    ps = frappe.db.sql("SELECT name, doc_type, field_name FROM `tabProperty Setter` WHERE field_name LIKE '%role%' OR field_name LIKE '%module%'", as_dict=True)
    cf = frappe.db.sql("SELECT name, dt, fieldname FROM `tabCustom Field` WHERE fieldname LIKE '%role%' OR fieldname LIKE '%module%'", as_dict=True)
    print("PS:", ps)
    print("CF:", cf)
