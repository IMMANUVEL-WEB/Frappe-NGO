import frappe
from frappe.utils import today, get_first_day, get_last_day
import re

def get_current_volunteer():
    volunteer = frappe.db.get_value("Volunteer", {"user": frappe.session.user, "status": "Active"}, "name")
    if not volunteer:
        frappe.throw("No active volunteer profile is linked to this account")
    return volunteer

@frappe.whitelist()
def my_dashboard():
    volunteer = get_current_volunteer()
    
    # Total Hours
    total_hours = frappe.db.get_value("Volunteer", volunteer, "total_hours") or 0.0
    
    # Hours this month
    current_month_start = get_first_day(today())
    current_month_end = get_last_day(today())
    
    attendances = frappe.get_list("Volunteer Attendance", 
        filters={
            "volunteer": volunteer,
            "docstatus": 1,
            "date": ["between", [current_month_start, current_month_end]]
        },
        pluck="total_hours"
    )
    hours_this_month = sum([h for h in attendances if h])
    
    # Active assignments
    active_assignments = frappe.db.count("Volunteer Assignment", {
        "volunteer": volunteer,
        "status": ["in", ["Assigned", "Active"]]
    })
    
    # Shifts where volunteer is participant
    # Note: Use get_all for child tables to avoid PermissionError
    shifts = frappe.get_all("Volunteer Shift Participant",
        filters={"volunteer": volunteer},
        pluck="parent"
    )
    
    next_shift = None
    upcoming_shifts = []
    
    if shifts:
        upcoming_shifts_data = frappe.get_list("Volunteer Shift",
            filters={
                "name": ["in", shifts],
                "status": "Scheduled",
                "shift_date": [">=", today()]
            },
            fields=["name", "opportunity", "project", "shift_date", "start_time", "end_time"],
            order_by="shift_date asc, start_time asc",
            limit_page_length=5
        )
        
        if upcoming_shifts_data:
            next_shift_doc = upcoming_shifts_data[0]
            opportunity_title = frappe.db.get_value("Volunteer Opportunity", next_shift_doc.opportunity, "title")
            next_shift = {
                "opportunity_title": opportunity_title,
                "project": next_shift_doc.project,
                "date": next_shift_doc.shift_date,
                "start_time": next_shift_doc.start_time,
                "end_time": next_shift_doc.end_time
            }
            
            for s in upcoming_shifts_data:
                opp_title = frappe.db.get_value("Volunteer Opportunity", s.opportunity, "title")
                upcoming_shifts.append({
                    "opportunity_title": opp_title,
                    "project": s.project,
                    "date": s.shift_date,
                    "start_time": s.start_time,
                    "end_time": s.end_time
                })

    return {
        "total_hours": total_hours,
        "hours_this_month": hours_this_month,
        "active_assignments": active_assignments,
        "next_shift": next_shift,
        "upcoming_shifts": upcoming_shifts
    }

@frappe.whitelist()
def my_assignments(status=None):
    volunteer = get_current_volunteer()
    
    filters = {"volunteer": volunteer}
    if status:
        filters["status"] = status
        
    assignments = frappe.get_list("Volunteer Assignment",
        filters=filters,
        fields=["name", "opportunity", "project", "role", "from_date", "to_date", "status"],
        order_by="from_date desc",
        ignore_permissions=True
    )
    
    for a in assignments:
        a["opportunity_title"] = frappe.db.get_value("Volunteer Opportunity", a.opportunity, "title") or a.opportunity
        
    return assignments

@frappe.whitelist()
def my_shifts(period="upcoming"):
    volunteer = get_current_volunteer()
    
    # Get all shift names where the volunteer is a participant
    # Use get_all to bypass child table permission check limitation
    participants = frappe.get_all("Volunteer Shift Participant",
        filters={"volunteer": volunteer},
        fields=["parent", "status"]
    )
    
    if not participants:
        return []
        
    shift_names = [p.parent for p in participants]
    participant_status_map = {p.parent: p.status for p in participants}
    
    filters = {"name": ["in", shift_names]}
    
    if period == "upcoming":
        filters["shift_date"] = [">=", today()]
        order = "shift_date asc, start_time asc"
    else:
        filters["shift_date"] = ["<", today()]
        order = "shift_date desc, start_time desc"
        
    shifts = frappe.get_list("Volunteer Shift",
        filters=filters,
        fields=["name", "opportunity", "project", "shift_date", "start_time", "end_time", "status"],
        order_by=order,
        ignore_permissions=True
    )
    
    for s in shifts:
        s["opportunity_title"] = frappe.db.get_value("Volunteer Opportunity", s.opportunity, "title") or s.opportunity
        s["participant_status"] = participant_status_map.get(s.name)
        
    return shifts

@frappe.whitelist()
def my_attendance(from_date=None, to_date=None):
    volunteer = get_current_volunteer()
    
    filters = {
        "volunteer": volunteer,
        "docstatus": 1
    }
    
    date_filter = []
    if from_date:
        date_filter.append([">=", from_date])
    if to_date:
        date_filter.append(["<=", to_date])
        
    if len(date_filter) == 2:
        filters["date"] = ["between", [from_date, to_date]]
    elif len(date_filter) == 1:
        filters["date"] = date_filter[0]
        
    attendances = frappe.get_list("Volunteer Attendance",
        filters=filters,
        fields=["name", "date", "shift", "opportunity", "project", "in_time", "out_time", "total_hours", "status"],
        order_by="date desc",
        ignore_permissions=True
    )
    
    period_total = 0.0
    for a in attendances:
        if a.total_hours:
            period_total += float(a.total_hours)
        if a.opportunity:
            a["opportunity_title"] = frappe.db.get_value("Volunteer Opportunity", a.opportunity, "title") or a.opportunity
        else:
            a["opportunity_title"] = ""
            
    return {
        "data": attendances,
        "period_total": period_total
    }

import re

@frappe.whitelist()
def my_profile():
    volunteer = get_current_volunteer()
    doc = frappe.get_doc("Volunteer", volunteer)
    
    return {
        "full_name": doc.full_name,
        "image": doc.image,
        "email": doc.email,
        "phone": doc.phone,
        "address": doc.address,
        "date_of_birth": doc.date_of_birth,
        "gender": doc.gender,
        "status": doc.status,
        "joined_on": doc.joined_on,
        "total_hours": doc.total_hours,
        "skills": [{"skill": s.skill, "proficiency": s.proficiency} for s in doc.skills],
        "availability": [{"day_of_week": a.day_of_week, "from_time": a.from_time, "to_time": a.to_time} for a in doc.availability]
    }

@frappe.whitelist()
def update_my_profile(phone=None, address=None, availability=None, image=None):
    volunteer = get_current_volunteer()
    doc = frappe.get_doc("Volunteer", volunteer)
    
    if phone:
        if not re.match(r'^\+?[\d\s-]{10,}$', phone):
            frappe.throw("Invalid phone number format")
        doc.phone = phone
        
    if image is not None:
        doc.image = image
        
    if address is not None:
        doc.address = address
        
    if availability is not None:
        if isinstance(availability, str):
            import json
            availability = json.loads(availability)
            
        valid_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        
        # Clear existing
        doc.set("availability", [])
        
        for row in availability:
            if row.get("day_of_week") not in valid_days:
                frappe.throw(f"Invalid day of week: {row.get('day_of_week')}")
            
            from_time = row.get("from_time")
            to_time = row.get("to_time")
            
            if from_time and to_time and str(from_time) >= str(to_time):
                frappe.throw(f"From Time must be before To Time on {row.get('day_of_week')}")
                
            doc.append("availability", {
                "day_of_week": row.get("day_of_week"),
                "from_time": from_time,
                "to_time": to_time
            })
            
    doc.flags.ignore_permissions = True
    doc.save()
    return "Success"

@frappe.whitelist()
def open_opportunities():
    volunteer = get_current_volunteer()
    
    opportunities = frappe.get_list("Volunteer Opportunity",
        filters={"status": "Open"},
        fields=["name", "title", "project", "description", "vacancies", "application_deadline", "location"],
        order_by="application_deadline asc",
        ignore_permissions=True
    )
    
    # Check which ones the user has already expressed interest in
    interests = frappe.get_all("Volunteer Opportunity Interest",
        filters={"volunteer": volunteer},
        pluck="opportunity"
    )
    
    for opp in opportunities:
        opp["has_interest"] = opp.name in interests
        # Fetch required skills
        skills = frappe.get_all("Volunteer Skill Item", filters={"parent": opp.name, "parenttype": "Volunteer Opportunity"}, pluck="skill")
        opp["required_skills"] = ", ".join(skills) if skills else ""

        
    return opportunities

@frappe.whitelist()
def submit_interest(opportunity):
    volunteer = get_current_volunteer()
    
    if not frappe.db.exists("Volunteer Opportunity", opportunity):
        frappe.throw("Invalid Opportunity")
        
    exists = frappe.db.exists("Volunteer Opportunity Interest", {
        "volunteer": volunteer,
        "opportunity": opportunity
    })
    
    if exists:
        return "Already submitted"
        
    doc = frappe.get_doc({
        "doctype": "Volunteer Opportunity Interest",
        "volunteer": volunteer,
        "opportunity": opportunity,
        "status": "Pending"
    })
    doc.insert(ignore_permissions=True)
    return "Success"

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
