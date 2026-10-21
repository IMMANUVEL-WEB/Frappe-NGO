import frappe
from frappe.utils import today, get_first_day, get_last_day
import re

def get_current_volunteer():
    user = frappe.session.user
    if not user or user == "Guest":
        return None
        
    volunteer = frappe.db.get_value("Volunteer", {"user": user, "status": "Active"}, "name")
    if not volunteer:
        volunteer = frappe.db.get_value("Volunteer", {"user": user}, "name")
    if not volunteer:
        volunteer = frappe.db.get_value("Volunteer", {"email": user}, "name")
        if volunteer:
            frappe.db.set_value("Volunteer", volunteer, "user", user)
            frappe.db.commit()

    # If still not found, check if user has Volunteer role and create a Volunteer record
    if not volunteer:
        roles = frappe.get_roles(user)
        if "Volunteer" in roles:
            user_doc = frappe.get_doc("User", user)
            full_name = user_doc.full_name or f"{user_doc.first_name or ''} {user_doc.last_name or ''}".strip() or user
            vol = frappe.get_doc({
                "doctype": "Volunteer",
                "full_name": full_name,
                "email": user,
                "user": user,
                "status": "Active",
                "joined_on": today()
            })
            vol.insert(ignore_permissions=True)
            frappe.db.commit()
            return vol.name

    return volunteer

@frappe.whitelist()
def my_dashboard():
    volunteer = get_current_volunteer()
    user = frappe.session.user
    user_info = frappe.db.get_value("User", user, ["first_name", "last_name", "full_name"], as_dict=True) or {}
    first_name = user_info.get("first_name") or ""
    last_name = user_info.get("last_name") or ""
    display_name = user_info.get("full_name") or (f"{first_name} {last_name}".strip()) or user

    if not volunteer:
        return {
            "volunteer": None,
            "volunteer_name": display_name,
            "first_name": first_name or display_name,
            "total_hours": 0.0,
            "hours_this_month": 0.0,
            "active_assignments": 0,
            "annual_goal": 100,
            "next_shift": None,
            "upcoming_shifts": [],
            "recent_attendances": []
        }

    # Total Hours
    vol_data = frappe.db.get_value("Volunteer", volunteer, ["full_name", "total_hours"], as_dict=True) or {}
    total_hours = vol_data.get("total_hours") or 0.0
    vol_name = vol_data.get("full_name") or display_name
    
    # Hours this month
    current_month_start = get_first_day(today())
    current_month_end = get_last_day(today())
    
    attendances = frappe.get_list("Volunteer Attendance", 
        filters={
            "volunteer": volunteer,
            "date": ["between", [current_month_start, current_month_end]]
        },
        pluck="total_hours", ignore_permissions=True
    )
    hours_this_month = sum([float(h) for h in attendances if h])
    
    # Active assignments
    active_assignments = frappe.db.count("Volunteer Assignment", {
        "volunteer": volunteer,
        "status": ["in", ["Assigned", "Active"]]
    })
    
    # Shifts where volunteer is participant
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
            limit_page_length=5,
            ignore_permissions=True
        )
        
        if upcoming_shifts_data:
            next_shift_doc = upcoming_shifts_data[0]
            opportunity_title = ""
            location = ""
            if next_shift_doc.opportunity:
                opp_info = frappe.db.get_value("Volunteer Opportunity", next_shift_doc.opportunity, ["title", "location"], as_dict=True) or {}
                opportunity_title = opp_info.get("title") or next_shift_doc.opportunity
                location = opp_info.get("location") or ""
            
            project_title = frappe.db.get_value("Project", next_shift_doc.project, "project_name") if next_shift_doc.project else ""
            
            next_shift = {
                "opportunity_title": opportunity_title,
                "project": project_title or next_shift_doc.project or "",
                "date": str(next_shift_doc.shift_date),
                "start_time": str(next_shift_doc.start_time),
                "end_time": str(next_shift_doc.end_time),
                "location": location
            }
            
            for s in upcoming_shifts_data:
                opp_title = frappe.db.get_value("Volunteer Opportunity", s.opportunity, "title") or s.opportunity
                upcoming_shifts.append({
                    "opportunity_title": opp_title,
                    "project": s.project,
                    "date": str(s.shift_date),
                    "start_time": str(s.start_time),
                    "end_time": str(s.end_time)
                })

    # Recent attendances for this volunteer
    recent_attendances_data = frappe.get_list("Volunteer Attendance",
        filters={"volunteer": volunteer},
        fields=["name", "date", "shift", "opportunity", "project", "total_hours", "status"],
        order_by="date desc",
        limit_page_length=5,
        ignore_permissions=True
    )
    recent_attendances = []
    for a in recent_attendances_data:
        opp_title = ""
        location = ""
        if a.opportunity:
            opp_info = frappe.db.get_value("Volunteer Opportunity", a.opportunity, ["title", "location"], as_dict=True) or {}
            opp_title = opp_info.get("title") or a.opportunity
            location = opp_info.get("location") or ""
        recent_attendances.append({
            "activity": opp_title or a.project or a.name,
            "date": str(a.date) if a.date else "-",
            "hours": f"{float(a.total_hours):.1f} hrs" if a.total_hours else "0.0 hrs",
            "location": location or "-",
            "status": a.status or "Present",
            "remarks": ""
        })

    return {
        "volunteer": volunteer,
        "volunteer_name": vol_name,
        "first_name": first_name or vol_name,
        "total_hours": float(total_hours),
        "hours_this_month": float(hours_this_month),
        "active_assignments": int(active_assignments),
        "annual_goal": 100,
        "next_shift": next_shift,
        "upcoming_shifts": upcoming_shifts,
        "recent_attendances": recent_attendances
    }


@frappe.whitelist()
def my_assignments(status=None):
    volunteer = get_current_volunteer()
    
    filters = {"volunteer": volunteer, "docstatus": ["<", 2]}
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
        "image": doc.get("image") or (frappe.db.get_value("User", doc.user, "user_image") if getattr(doc, "user", None) else None),
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
        if getattr(doc, "user", None):
            frappe.db.set_value("User", doc.user, "user_image", image)
        
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
        fields=["name", "title", "project", "description", "vacancies", "end_date", "location"],
        order_by="end_date asc",
        ignore_permissions=True
    )
    
    # Check which ones the user has already expressed interest in
    interests = frappe.get_all("Volunteer Opportunity Interest",
        filters={"volunteer": volunteer},
        pluck="opportunity"
    )
    
    # Map human-readable project names
    project_names = {}
    project_ids = list({o.get("project") for o in opportunities if o.get("project")})
    if project_ids:
        p_data = frappe.get_all("Project", filters={"name": ["in", project_ids]}, fields=["name", "project_name"])
        project_names = {p.name: (p.project_name or p.name) for p in p_data}

    for opp in opportunities:
        opp["application_deadline"] = opp.end_date
        opp["has_interest"] = opp.name in interests
        opp["project_name"] = project_names.get(opp.get("project")) or opp.get("project") or ""
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
        frappe.core.doctype.user.user.update_password(new_password=new_password, old_password=old_password)
        return "Password updated successfully"
    except frappe.AuthenticationError:
        frappe.throw("Incorrect old password", frappe.AuthenticationError)

@frappe.whitelist(allow_guest=True)
def get_portal_settings():
    doc = frappe.get_single("Volunteer Settings")
    d = doc.as_dict()

    defaults = {
        "primary_color": "#2563eb",
        "secondary_color": "#0891b2",
        "login_color": "#1e3a8a",
        "sidebar_color": "#1f2937",
        "login_portal_title": "Kindred",
        "login_portal_subtitle": "IMPACTSPHERE",
        "login_status_badge": "Systems Operational",
        "login_support_label": "Field Support & FAQ",
        "login_support_url": "#",
        "login_enable_language_selector": 1,
        "login_hero_badge": "GLOBAL VOLUNTEER COMMUNITY",
        "login_hero_title": "Empowering communities, together.",
        "login_hero_description": "Sign in to claim regional volunteer shifts, track community outcomes, and manage verified field contributions in real time.",
        "login_stat1_value": "120k+",
        "login_stat1_label": "HOURS LOGGED",
        "login_stat2_value": "48",
        "login_stat2_label": "CHAPTERS",
        "login_stat3_value": "99.8%",
        "login_stat3_label": "VERIFIED",
        "login_testimonial_stars": 5,
        "login_testimonial_quote": '"Every hour deployed across local food distributions and emergency shelters directly shifts the needle for our neighborhood families."',
        "login_testimonial_author": "Elena Cruz",
        "login_testimonial_role": "Pacific Chapter Deployment Lead",
        "login_testimonial_avatar_initials": "EC",
        "login_form_title": "Welcome back, changemaker",
        "login_form_subtitle": "Log in to access your deployment shifts, impact ledger, and verified hours.",
        "login_show_google_login": 1,
        "login_google_label": "Google Account",
        "login_google_url": "#",
        "login_show_sso_login": 1,
        "login_sso_label": "NGO SSO Portal",
        "login_sso_url": "#",
        "login_divider_text": "OR SIGN IN WITH EMAIL",
        "login_email_label": "VOLUNTEER EMAIL ADDRESS",
        "login_email_placeholder": "you@example.com",
        "login_password_label": "PASSWORD",
        "login_forgot_password_label": "Forgot password?",
        "login_forgot_password_url": "#",
        "login_remember_me_label": "Remember this station for 30 days",
        "login_security_badge_label": "Frappe Guard",
        "login_submit_button_label": "Sign In to Dashboard",
        "login_apply_button_label": "Apply to be a Volunteer",
        "login_apply_button_url": "/apply",
        "login_show_badge_scan": 1,
        "login_badge_scan_text": "At a physical deployment hub?",
        "login_badge_scan_link_label": "Scan Volunteer Badge",
        "login_badge_scan_url": "#",
        "login_encryption_note": "Protected by 256-bit encryption",
        "login_powered_by_note": "Secure connection powered by Frappe Framework",
        "login_footer_copyright": "© 2026 Kindred Community Impact Network. All rights reserved.",
        "login_footer_links": "Terms of Service | Volunteer Privacy Notice | Accessibility",
    }

    res = {}
    for k, v in defaults.items():
        val = d.get(k)
        res[k] = val if (val is not None and val != "") else v

    if d.get("login_logo"):
        res["login_logo"] = d.get("login_logo")
    if d.get("login_testimonial_avatar_image"):
        res["login_testimonial_avatar_image"] = d.get("login_testimonial_avatar_image")

    return res





@frappe.whitelist(allow_guest=True)
def get_all_skills():
    return frappe.get_all("Volunteer Skill", pluck="name", ignore_permissions=True, order_by="name asc")

@frappe.whitelist(allow_guest=True)
def submit_application(applicant_name, email, phone=None, date_of_birth=None, gender=None, address=None, skills=None, availability=None, preferred_impact_area=None):
    import json
    try:
        # Check for duplicates before creating doc to return a clean message
        existing = frappe.db.exists(
            "Volunteer Application",
            {"email": email, "status": "Pending", "docstatus": 0}
        )
        if existing:
            return {"status": "error", "message": "An application is already pending for this email address. Please wait for it to be reviewed."}
            
        doc = frappe.new_doc("Volunteer Application")
        doc.applicant_name = applicant_name
        doc.email = email
        doc.phone = phone
        if date_of_birth:
            doc.date_of_birth = date_of_birth
        if gender:
            doc.gender = gender
        if address:
            doc.address = address
        if preferred_impact_area:
            doc.motivation = preferred_impact_area
        doc.status = "Pending"
        if skills:
            if isinstance(skills, str):
                skills = json.loads(skills)
            for s in skills:
                skill_name = s.get("skill")
                if skill_name:
                    # Create the skill dynamically if it doesn't exist in the system
                    if not frappe.db.exists("Volunteer Skill", skill_name):
                        frappe.get_doc({
                            "doctype": "Volunteer Skill",
                            "skill_name": skill_name
                        }).insert(ignore_permissions=True)
                        
                    doc.append("skills", {
                        "skill": skill_name,
                        "proficiency": s.get("proficiency")
                    })
                
        if availability:
            if isinstance(availability, str):
                availability = json.loads(availability)
            for a in availability:
                doc.append("availability", {
                    "day_of_week": a.get("day_of_week"),
                    "from_time": a.get("from_time"),
                    "to_time": a.get("to_time")
                })
                
        doc.insert(ignore_permissions=True)
        
        # Override the workflow state directly
        if getattr(doc, "workflow_state", None) == "Draft":
            doc.db_set("workflow_state", "Pending")
            
        frappe.db.commit()
        return {"status": "success"}
    except Exception as e:
        frappe.db.rollback()
        import traceback
        return {"status": "error", "message": f"Error: {str(e)}", "trace": traceback.format_exc()}


def get_website_user_home_page(user):
	"""
	Direct Administrator and System Users to /desk,
	and Website Users with Volunteer role to /frontend.
	"""
	if not user or user == "Administrator":
		return "desk"

	try:
		if frappe.db.get_value("User", user, "user_type") == "System User":
			return "desk"

		roles = frappe.get_roles(user)
		if "Volunteer" in roles:
			return "frontend"
	except Exception:
		pass

	return None

