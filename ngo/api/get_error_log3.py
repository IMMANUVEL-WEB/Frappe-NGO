import frappe

def execute():
    logs = frappe.get_all("Error Log", fields=["method", "error"], order_by="creation desc", limit=1)
    if logs:
        print(logs[0].method)
        print("===")
        print(logs[0].error)
    else:
        print("No error logs found.")
