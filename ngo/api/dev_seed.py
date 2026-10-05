import frappe
from frappe.utils import today, add_days

def execute():
    print("Running dev_seed...")
    
    # Clear existing data for a clean slate
    frappe.db.sql("DELETE FROM `tabVolunteer Opportunity Interest`")
    frappe.db.sql("DELETE FROM `tabVolunteer Attendance`")
    frappe.db.sql("DELETE FROM `tabVolunteer Shift Participant`")
    frappe.db.sql("DELETE FROM `tabVolunteer Shift`")
    frappe.db.sql("DELETE FROM `tabVolunteer Assignment`")
    frappe.db.sql("DELETE FROM `tabVolunteer`")
    frappe.db.sql("DELETE FROM `tabVolunteer Opportunity`")
    frappe.db.sql("DELETE FROM `tabProject`")
    frappe.db.commit()
    print("Cleared existing test records.")
    
    # 1. Project
    project = frappe.get_doc({
        "doctype": "Project",
        "project_name": "Community Clean Up 2026",
        "status": "Open"
    }).insert(ignore_permissions=True)
    
    # 2. Opportunity
    opp = frappe.get_doc({
        "doctype": "Volunteer Opportunity",
        "title": "Park Cleaning Drive",
        "project": project.name,
        "description": "<p>Help us clean Central Park.</p>",
        "status": "Open",
        "vacancies": 5,
        "location": "Central Park",
        "application_deadline": add_days(today(), 10)
    }).insert(ignore_permissions=True)
    
    # 3. User
    email = "ravi@gmail.com"
    if not frappe.db.exists("User", email):
        user = frappe.get_doc({
            "doctype": "User",
            "email": email,
            "first_name": "Ravi Test",
            "send_welcome_email": 0
        })
        user.insert(ignore_permissions=True)
        user.add_roles("Volunteer User")
    
    # 4. Volunteer
    vol = frappe.get_doc({
        "doctype": "Volunteer",
        "full_name": "Ravi Test",
        "user": email,
        "status": "Active",
        "phone": "555-0101",
        "address": "123 Main St"
    }).insert(ignore_permissions=True)
    
    # 5. Assignment
    assignment = frappe.get_doc({
        "doctype": "Volunteer Assignment",
        "volunteer": vol.name,
        "opportunity": opp.name,
        "project": project.name,
        "from_date": today(),
        "status": "Active",
        "role": "Cleaner"
    }).insert(ignore_permissions=True)
    
    # 6. Shift
    shift = frappe.get_doc({
        "doctype": "Volunteer Shift",
        "opportunity": opp.name,
        "project": project.name,
        "shift_date": add_days(today(), 1),
        "start_time": "09:00:00",
        "end_time": "13:00:00",
        "status": "Scheduled"
    }).insert(ignore_permissions=True)
    
    # Add volunteer as participant to shift
    frappe.get_doc({
        "doctype": "Volunteer Shift Participant",
        "parent": shift.name,
        "parenttype": "Volunteer Shift",
        "parentfield": "participants",
        "volunteer": vol.name,
        "status": "Confirmed" # Allowed: Confirmed, Absent, Replaced
    }).insert(ignore_permissions=True)
    
    # 7. Past Shift and Attendance
    past_shift = frappe.get_doc({
        "doctype": "Volunteer Shift",
        "opportunity": opp.name,
        "project": project.name,
        "shift_date": add_days(today(), -2),
        "start_time": "09:00:00",
        "end_time": "13:00:00",
        "status": "Completed"
    }).insert(ignore_permissions=True)
    
    frappe.get_doc({
        "doctype": "Volunteer Shift Participant",
        "parent": past_shift.name,
        "parenttype": "Volunteer Shift",
        "parentfield": "participants",
        "volunteer": vol.name,
        "status": "Confirmed"
    }).insert(ignore_permissions=True)
    
    att = frappe.get_doc({
        "doctype": "Volunteer Attendance",
        "volunteer": vol.name,
        "shift": past_shift.name,
        "opportunity": opp.name,
        "project": project.name,
        "date": past_shift.shift_date,
        "in_time": "09:00:00",
        "out_time": "13:00:00",
        "total_hours": 4,
        "status": "Present", # For attendance
        "docstatus": 1 # Submitted
    }).insert(ignore_permissions=True)
    
    frappe.db.commit()
    print("dev_seed complete. Successfully created mock environment for ravi@gmail.com")
