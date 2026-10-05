import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_field

def execute():
    create_custom_field('Volunteer Opportunity', {
        'fieldname': 'application_deadline',
        'label': 'Application Deadline',
        'fieldtype': 'Date',
        'insert_after': 'end_date'
    })
    print("Added application_deadline field to Volunteer Opportunity")
