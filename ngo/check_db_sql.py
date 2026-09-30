import frappe

def check_sql():
    ps = frappe.db.sql("SELECT * FROM `tabProperty Setter` WHERE doc_type='User'", as_dict=True)
    cf = frappe.db.sql("SELECT * FROM `tabCustom Field` WHERE dt='User'", as_dict=True)
    print("PS SQL:", ps)
    print("CF SQL:", cf)
