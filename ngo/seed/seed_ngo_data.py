"""

Frappe NGO Demo Data Seeder
===========================
Generates realistic, connected, demo-ready data for Frappe NGO on top of ERPNext.
Covers:
  - Ngo Module (Project Proposal, Donor Grant, Budget Item, Compliance Doc, Custom Fields)
  - Beneficiary Management (Beneficiary, Family Members, Enrollment, Assessment,
                            Assessment Indicators, Service Type, Beneficiary Service, NGO Settings)
  - Volunteer Management (Volunteer, Volunteer Application, Volunteer Skill, Volunteer Skill Item,
                          Volunteer Availability, Volunteer Opportunity, Volunteer Assignment,
                          Volunteer Shift, Volunteer Shift Participant, Volunteer Attendance,
                          Volunteer Opportunity Interest, Volunteer Settings)
  - ERPNext Dependencies (Company, Accounts, Fiscal Years, Cost Centers, Suppliers as Donors,
                          Employees, Projects, Budgets, Journal Entries, Users & Roles)

Execution Modes:
  1. bench --site <site> execute ngo.seed.seed_ngo_data.run
  2. cd sites && ../env/bin/python ../apps/ngo/ngo/seed/seed_ngo_data.py <site> [options]
  
"""

import os
import sys
import json
import random
import argparse
from datetime import datetime, date, timedelta

# Frappe will be imported lazily or at top if running inside bench
try:
    import frappe
    from frappe.utils import add_days, add_months, today, getdate, nowdate, flt, cint
except ImportError:
    frappe = None


# ==============================================================================
# CONFIGURATION
# ==============================================================================
CONFIG = {
    "region": "Tamil Nadu",
    "country": "India",
    "currency": "INR",
    "random_seed": 42,
    "demo_password": "imman@123",
    "counts": {
        "suppliers": 10,
        "employees": 10,
        "service_types": 10,
        "volunteer_skills": 55,
        "project_proposals": 14,
        "approved_proposals": 10,
        "compliance_docs": 14,
        "donor_grants": 11,
        "payment_entries": 10,
        "budgets_per_project": 3,
        "volunteer_applications": 30,
        "approved_applications": 22,
        "volunteer_opportunities": 12,
        "volunteer_assignments": 30,
        "volunteer_shifts": 40,
        "volunteer_attendances": 65,
        "volunteer_interests": 12,
        "beneficiaries": 80,
        "beneficiary_enrollments": 100,
        "beneficiary_services": 150,
        "journal_entries": 105,
    }
}


# ==============================================================================
# PURE DATA GENERATION HELPERS (Testable without Frappe)
# ==============================================================================
DISTRICTS_TN = [
    "Chennai", "Coimbatore", "Madurai", "Tiruchirappalli", "Salem",
    "Tirunelveli", "Vellore", "Thanjavur", "Dindigul", "Cuddalore",
    "Kanchipuram", "Erode"
]

DISTRICT_COORDINATES = {
    "Chennai": [80.2707, 13.0827],
    "Coimbatore": [76.9558, 11.0168],
    "Madurai": [78.1198, 9.9252],
    "Tiruchirappalli": [78.7047, 10.7905],
    "Salem": [78.1460, 11.6643],
    "Tirunelveli": [77.7567, 8.7139],
    "Vellore": [79.1325, 12.9165],
    "Thanjavur": [79.1378, 10.7870],
    "Dindigul": [77.9803, 10.3673],
    "Cuddalore": [79.7680, 11.7480],
    "Kanchipuram": [79.7036, 12.8342],
    "Erode": [77.7172, 11.3410]
}

FIRST_NAMES_MALE = [
    "Aarav", "Arun", "Karthik", "Vijay", "Suresh", "Ramesh", "Mani", "Anand",
    "Praveen", "Dinesh", "Saravanan", "Murugan", "Senthil", "Vignesh", "Balaji",
    "Ganesh", "Sanjay", "Manoj", "Pradeep", "Rajesh", "Naveen", "Deepak"
]

FIRST_NAMES_FEMALE = [
    "Priya", "Anitha", "Lakshmi", "Deepa", "Kavitha", "Meena", "Divya", "Sangeetha",
    "Revathi", "Bhavani", "Gayathri", "Shanthi", "Malathi", "Nandhini", "Abirami",
    "Kanimozhi", "Swetha", "Vandhana", "Poornima", "Yamuna", "Sandhya", "Radhika"
]

LAST_NAMES = [
    "Raman", "Sundaram", "Natarajan", "Krishnan", "Subramanian", "Balasubramanian",
    "Venkatesan", "Chidambaram", "Swaminathan", "Shanmugam", "Ganesan", "Ramasamy",
    "Palanisamy", "Kumar", "Murugesan", "Srinivasan", "Rajendran", "Jayaraman"
]

DONOR_PROFILES = [
    {"name": "Tata Community Trust", "type": "Donor", "funding_type": "CSR"},
    {"name": "Infosys Philanthropic Foundation", "type": "Donor", "funding_type": "CSR"},
    {"name": "Azim Premji Development Initiative", "type": "Donor", "funding_type": "Domestic Grant"},
    {"name": "Reliance Rural Empowerment CSR", "type": "Donor", "funding_type": "CSR"},
    {"name": "Bill & Melinda Gates India Fund", "type": "Donor", "funding_type": "FCRA"},
    {"name": "Tamil Nadu Rural Health Mission", "type": "Donor", "funding_type": "Government"},
    {"name": "GlobalGiving UK Relief Fund", "type": "Donor", "funding_type": "FCRA"},
    {"name": "NABARD Rural Livelihood Scheme", "type": "Donor", "funding_type": "Government"},
    {"name": "Dr. K. Ramanathan Family Trust", "type": "Donor", "funding_type": "Domestic Grant"},
    {"name": "Sundaram Climate & Water Trust", "type": "Donor", "funding_type": "Domestic Grant"}
]

EMPLOYEE_ROLES = [
    ("Dr. Rajesh", "Kannan", "Program Director - Health"),
    ("Meenakshi", "Sundaram", "Senior Education Lead"),
    ("Senthil", "Nathan", "WASH Technical Specialist"),
    ("Kavitha", "Ramanathan", "Livelihoods Project Manager"),
    ("Arun", "Kumar", "Disaster Response Coordinator"),
    ("Priya", "Dharshini", "Monitoring & Evaluation Lead"),
    ("Vignesh", "Warrier", "Finance & Grants Manager"),
    ("Anand", "Babu", "Field Operations Officer"),
    ("Sangeetha", "Rajan", "Document Controller & Compliance"),
    ("Murugan", "Subbiah", "Community Liaison Officer")
]

SERVICE_TYPES_DEF = [
    {"name": "Direct Cash Assistance", "category": "Cash Assistance", "cost": 5000, "account_suffix": "Program Expenditure"},
    {"name": "Primary School Kit", "category": "Education", "cost": 1200, "account_suffix": "Program Expenditure"},
    {"name": "Higher Education Scholarship", "category": "Education", "cost": 15000, "account_suffix": "Program Expenditure"},
    {"name": "Community Health Camp Screening", "category": "Health", "cost": 450, "account_suffix": "Program Expenditure"},
    {"name": "Nutrition & Supplementary Food Pack", "category": "Health", "cost": 1800, "account_suffix": "Program Expenditure"},
    {"name": "Vocational Skill Training Course", "category": "Training", "cost": 8500, "account_suffix": "Capital Expenditure"},
    {"name": "Domestic Water Filter Kit", "category": "Other", "cost": 2800, "account_suffix": "Capital Expenditure"},
    {"name": "Household Sanitation Kit", "category": "Other", "cost": 1500, "account_suffix": "Capital Expenditure"},
    {"name": "Emergency Relief Kit", "category": "Other", "cost": 3200, "account_suffix": "Program Expenditure"},
    {"name": "Field Operations & Community Monitoring", "category": "Other", "cost": 2500, "account_suffix": "Admin Expenditure"}
]

VOLUNTEER_SKILLS_DEF = [
    # Teaching (8)
    ("Remedial Primary Maths", "Teaching", "Tutoring children in foundational numeracy"),
    ("Spoken English Coaching", "Teaching", "Fluency and conversational training for rural youth"),
    ("STEM Robotics & Science", "Teaching", "Hands-on simple science experiments for schools"),
    ("Digital Literacy Basics", "Teaching", "Teaching computer operation and internet safety"),
    ("Adult Literacy Facilitation", "Teaching", "Basic reading and signature literacy for women"),
    ("Special Needs Child Care", "Teaching", "Assistance for children with learning disabilities"),
    ("School Dropout Catch-up", "Teaching", "Bridge course instruction for out-of-school kids"),
    ("Competitive Exam Mentorship", "Teaching", "Guidance for scholarship and entry tests"),

    # Medical (8)
    ("First Aid & CPR", "Medical", "Emergency stabilization and basic life support"),
    ("Health Camp Vital Signs Screening", "Medical", "Blood pressure, pulse, oxygen screening"),
    ("Community Nutrition Assessment", "Medical", "MUAC tape and BMI screening for toddlers"),
    ("Patient Triage Assistance", "Medical", "Guiding attendees at high-volume health camps"),
    ("Pharmacy Counter Dispensing", "Medical", "Packaging and explaining prescription doses"),
    ("Hygiene & Sanitation Counseling", "Medical", "Door-to-door handwashing and water safety education"),
    ("Maternal Healthcare Guidance", "Medical", "Pre-natal nutrition counseling for young mothers"),
    ("Vision Screening Assistance", "Medical", "Snellen chart vision test assistance"),

    # IT (8)
    ("Data Entry & Form Verification", "IT", "Digitizing beneficiary records and survey forms"),
    ("Social Media Campaigning", "IT", "Creating community awareness posts and updates"),
    ("Web Portal Maintenance", "IT", "Basic CMS updates and volunteer portal help"),
    ("Event Photography & Processing", "IT", "Documenting field distribution with geo-tags"),
    ("Impact Video Editing", "IT", "Short reel and testimonial video creation"),
    ("Spreadsheet Reporting & Excel", "IT", "Compiling attendance and service count sheets"),
    ("Field App Support", "IT", "Helping grassroots field workers use mobile apps"),
    ("Poster & Banner Designing", "IT", "Canva / design tool support for campaign flyers"),

    # Fundraising (8)
    ("CSR Grant Proposal Writing", "Fundraising", "Drafting concept notes for corporate donors"),
    ("Crowdfunding Campaign Outreach", "Fundraising", "Online fundraiser messaging and updates"),
    ("Donor Thank-You Tele-calling", "Fundraising", "Personalized calls to individual contributors"),
    ("Fundraising Event Hosting", "Fundraising", "Anchor and stage coordination for gala events"),
    ("Corporate Partnership Pitching", "Fundraising", "Presenting NGO metrics to local businesses"),
    ("80G / Tax Exemption Helpdesk", "Fundraising", "Assisting donors with contribution receipts"),
    ("Major Donor Stewardship", "Fundraising", "Preparing quarterly milestone progress briefs"),
    ("Community Donation Box Drives", "Fundraising", "Managing local school and temple collection drives"),

    # Logistics (8)
    ("Relief Material Warehousing", "Logistics", "Sorting, stacking, and cataloging relief supplies"),
    ("Food & Ration Kit Packing", "Logistics", "Assembling standardized family grocery boxes"),
    ("Last-Mile Vehicle Coordination", "Logistics", "Coordinating mini-trucks for remote hamlet drops"),
    ("Loading & Unloading Supervision", "Logistics", "Safety and tally check during truck transfers"),
    ("Cold-Chain Vaccine Pack Courier", "Logistics", "Transporting temperature-controlled samples"),
    ("Water Can & Tanker Dispatch", "Logistics", "Organizing emergency drinking water distribution"),
    ("Inventory Physical Audit", "Logistics", "Verifying physical stocks against ERP register"),
    ("Disaster Kit Pre-positioning", "Logistics", "Setting up flood-rescue equipment in safe zones"),

    # Event Support (8)
    ("Event Registration Desk", "Event Support", "Checking in attendees, issuing badges"),
    ("Crowd & Queue Management", "Event Support", "Maintaining orderly queues at distribution camps"),
    ("Audio-Visual & Sound Setup", "Event Support", "Operating PA microphones and projector screens"),
    ("Tamil-English Translation", "Event Support", "Bilingual interpretation for foreign visitors"),
    ("Hospitality & Water Service", "Event Support", "Managing water stations and snacks for attendees"),
    ("Help Desk & Information Booth", "Event Support", "Guiding visitors and resolving queries"),
    ("Camp Setup & Disassembly", "Event Support", "Erecting shamianas, tables, and folding chairs"),
    ("Waste Segregation & Green Camp", "Event Support", "Ensuring zero-plastic and clean venue post event"),

    # Other (7)
    ("Water Quality Field Testing", "Other", "Using chemical test strips for TDS, fluoride, pH"),
    ("Kitchen Garden Facilitation", "Other", "Helping households grow organic greens in sacks"),
    ("Street Play & Folk Theater", "Other", "Social drama for female feticide and child marriage"),
    ("Disaster Search & Rescue Support", "Other", "Boat steering assistance and lifeline handling"),
    ("Elderly Care Companion", "Other", "Visiting isolated seniors in rural hamlets"),
    ("Youth Sports Club Coaching", "Other", "Organizing evening football and kabaddi for teens"),
    ("Gram Sabha Participation Lead", "Other", "Encouraging village residents to speak at panchayats")
]

PROPOSALS_DEF = [
    # 10 that will be approved -> Projects (using CSR and FCRA which exist in both Proposal and Project)
    {"title": "Rural Maternal Health and Telemedicine Hub", "sector": "Health", "funding_type": "CSR", "donor_idx": 0, "capex": 1200000, "opex": 2800000, "admin": 500000, "duration_m": 12},
    {"title": "Digital Classrooms for Government Tribal Schools", "sector": "Education", "funding_type": "CSR", "donor_idx": 1, "capex": 1800000, "opex": 1400000, "admin": 300000, "duration_m": 12},
    {"title": "Safe Community Drinking Water Filtration RO Plants", "sector": "WASH", "funding_type": "FCRA", "donor_idx": 4, "capex": 2400000, "opex": 1100000, "admin": 400000, "duration_m": 18},
    {"title": "Women SHG Organic Spice Processing and Micro-Enterprise", "sector": "Livelihoods", "funding_type": "CSR", "donor_idx": 2, "capex": 900000, "opex": 2100000, "admin": 350000, "duration_m": 12},
    {"title": "Coastal Cyclone Preparedness and Emergency Relief Reserve", "sector": "Disaster Relief", "funding_type": "FCRA", "donor_idx": 5, "capex": 1500000, "opex": 3500000, "admin": 500000, "duration_m": 24},
    {"title": "Panchayat Level Water Stewardship & Governance", "sector": "Governance", "funding_type": "CSR", "donor_idx": 9, "capex": 400000, "opex": 1600000, "admin": 250000, "duration_m": 12},
    {"title": "Pediatric Malnutrition Eradication in Salem District", "sector": "Health", "funding_type": "CSR", "donor_idx": 3, "capex": 500000, "opex": 2500000, "admin": 300000, "duration_m": 12},
    {"title": "Youth Electric Vehicle Technician Apprenticeship", "sector": "Livelihoods", "funding_type": "CSR", "donor_idx": 8, "capex": 1400000, "opex": 1900000, "admin": 350000, "duration_m": 10},
    {"title": "Girls Higher Secondary STEM Scholarship and Mentorship", "sector": "Education", "funding_type": "CSR", "donor_idx": 8, "capex": 300000, "opex": 3200000, "admin": 400000, "duration_m": 24},
    {"title": "Delta Region Post-Flood Sanitation and Bio-Toilet Restoration", "sector": "WASH", "funding_type": "FCRA", "donor_idx": 6, "capex": 2200000, "opex": 1800000, "admin": 450000, "duration_m": 14},

    # 4 non-approved (2 Internal Review, 1 Donor Approval Pending, 1 Rejected)
    {"title": "Community Solar Cold Storage for Smallholder Farmers", "sector": "Livelihoods", "funding_type": "CSR", "donor_idx": 0, "capex": 3500000, "opex": 1200000, "admin": 300000, "duration_m": 12, "target_state": "Internal Review"},
    {"title": "Urban Slum Mobile Library and Learning Labs", "sector": "Education", "funding_type": "Domestic Grant", "donor_idx": 2, "capex": 800000, "opex": 1200000, "admin": 200000, "duration_m": 12, "target_state": "Internal Review"},
    {"title": "Traditional Fisherfolk Marine Safety and GPS Warning", "sector": "Governance", "funding_type": "FCRA", "donor_idx": 4, "capex": 1600000, "opex": 900000, "admin": 250000, "duration_m": 12, "target_state": "Donor Approval Pending"},
    {"title": "Commercial Bio-fertilizer Factory Pilot", "sector": "Livelihoods", "funding_type": "Internal", "donor_idx": 0, "capex": 6000000, "opex": 4000000, "admin": 1000000, "duration_m": 12, "target_state": "Rejected", "rejection_notes": "Project deviates from non-profit charter; commercial production model unviable without equity partner."}
]

OPPORTUNITIES_DEF = [
    {"title": "Weekend Remedial Maths Tutor", "vacancies": 6, "skills": ["Remedial Primary Maths", "Spoken English Coaching"], "loc": "Madurai Learning Center"},
    {"title": "General Health Camp Registration Desk", "vacancies": 4, "skills": ["Event Registration Desk", "Tamil-English Translation"], "loc": "Vellore Rural Clinic"},
    {"title": "Community RO Water Filter Installer", "vacancies": 3, "skills": ["Water Quality Field Testing", "Camp Setup & Disassembly"], "loc": "Salem Panchayat Hall"},
    {"title": "Flood Relief Ration Kit Packing Lead", "vacancies": 5, "skills": ["Food & Ration Kit Packing", "Relief Material Warehousing"], "loc": "Cuddalore Relief Depot"},
    {"title": "Evening Digital Skills Instructor", "vacancies": 4, "skills": ["Digital Literacy Basics", "Spreadsheet Reporting & Excel"], "loc": "Chennai Community Lab"},
    {"title": "Field Nutrition Survey Assistant", "vacancies": 3, "skills": ["Community Nutrition Assessment", "Data Entry & Form Verification"], "loc": "Dindigul Primary Health Post"},
    {"title": "Women Micro-Enterprise Marketing Mentor", "vacancies": 3, "skills": ["Social Media Campaigning", "Corporate Partnership Pitching"], "loc": "Coimbatore SHG Cluster"},
    {"title": "Mobile Science Lab Experiment Guide", "vacancies": 4, "skills": ["STEM Robotics & Science", "Youth Sports Club Coaching"], "loc": "Tiruchirappalli Schools"},
    {"title": "Sanitation Drive Door-to-Door Facilitator", "vacancies": 5, "skills": ["Hygiene & Sanitation Counseling", "Street Play & Folk Theater"], "loc": "Thanjavur Village Hub"},
    {"title": "Emergency Blood Donation Camp Support", "vacancies": 4, "skills": ["First Aid & CPR", "Patient Triage Assistance"], "loc": "Tirunelveli District Hospital"},
    {"title": "Field Impact Photography & Documentation", "vacancies": 2, "skills": ["Event Photography & Processing", "Impact Video Editing"], "loc": "Kanchipuram Heritage Field", "status": "Closed"},
    {"title": "Commercial Factory Operations Volunteer", "vacancies": 2, "skills": ["Inventory Physical Audit"], "loc": "Erode Industrial Zone", "status": "Cancelled"}
]

BENEFICIARY_INDICATORS = {
    "Health": [
        ("Hemoglobin Level", "g/dL", 12.0, 9.2, 11.4),
        ("BMI Screening", "kg/m2", 21.0, 16.5, 19.8),
        ("Monthly Medical Out-of-Pocket Expense", "INR", 200.0, 1200.0, 350.0),
        ("Adherence to Prescribed Supplements", "%", 95.0, 40.0, 90.0)
    ],
    "Education": [
        ("School Monthly Attendance", "%", 90.0, 62.0, 88.0),
        ("Quarterly Math Assessment Score", "%", 75.0, 38.0, 72.0),
        ("English Reading Fluency (Words/min)", "wpm", 70.0, 28.0, 64.0),
        ("Homework Completion Rate", "%", 90.0, 45.0, 85.0)
    ],
    "WASH": [
        ("Potable Water Consumed Daily", "Liters", 25.0, 8.0, 22.0),
        ("Incidence of Waterborne Illness (Days/year)", "days", 0.0, 14.0, 2.0),
        ("Household Latrine Usage Frequency", "%", 100.0, 20.0, 95.0),
        ("Soap Handwashing Compliance", "%", 100.0, 35.0, 92.0)
    ],
    "Livelihoods": [
        ("Monthly Net Household Income", "INR", 18000.0, 7500.0, 15500.0),
        ("Self-Employment Weekly Hours", "Hours", 35.0, 10.0, 32.0),
        ("Monthly Personal Savings Rate", "INR", 2500.0, 0.0, 2200.0),
        ("Market Linkage Buyer Contracts", "Count", 3.0, 0.0, 2.0)
    ],
    "Disaster Relief": [
        ("Essential Relief Supplies Index", "%", 100.0, 15.0, 100.0),
        ("Temporary Shelter Safety Score", "%", 90.0, 30.0, 88.0),
        ("Access to Emergency Potable Water", "Liters", 30.0, 5.0, 28.0),
        ("Post-Disaster Livelihood Recovery Rate", "%", 80.0, 10.0, 75.0)
    ],
    "Governance": [
        ("Gram Sabha Meeting Attendance", "%", 80.0, 15.0, 75.0),
        ("Awareness of Welfare Entitlements", "%", 90.0, 25.0, 85.0),
        ("Public Grievance Petitions Resolved", "%", 70.0, 10.0, 60.0),
        ("Community Asset Maintenance Rating", "Score/10", 8.0, 3.0, 7.5)
    ]
}


# ==============================================================================
# MANIFEST MANAGER
# ==============================================================================
class SeedManifest:
    def __init__(self, site_name=None):
        self.site_name = site_name or (frappe.local.site if frappe else "default")
        self.records = []
        self.manifest_file = frappe.get_site_path("ngo_seed_manifest.json") if frappe else "ngo_seed_manifest.json"

    def add(self, doctype, name, submittable=False):
        self.records.append({
            "doctype": doctype,
            "name": name,
            "submittable": bool(submittable),
            "created_at": datetime.now().isoformat()
        })

    def save(self):
        if not frappe:
            return
        # Load existing if any, append without duplicates
        existing = []
        if os.path.exists(self.manifest_file):
            try:
                with open(self.manifest_file, "r") as f:
                    existing = json.load(f)
            except Exception:
                existing = []
        seen = {(r["doctype"], r["name"]) for r in existing}
        for r in self.records:
            if (r["doctype"], r["name"]) not in seen:
                existing.append(r)
                seen.add((r["doctype"], r["name"]))
        with open(self.manifest_file, "w") as f:
            json.dump(existing, f, indent=2)

    def load(self):
        if os.path.exists(self.manifest_file):
            try:
                with open(self.manifest_file, "r") as f:
                    return json.load(f)
            except Exception:
                return []
        return []

    def clear(self):
        if os.path.exists(self.manifest_file):
            os.remove(self.manifest_file)
        self.records = []


# ==============================================================================
# SEED LOADER ENGINE
# ==============================================================================
class NGOSeeder:
    def __init__(self, dry_run=False, force=False, seed=42, skip_budgets=False, skip_journal_entries=False):
        self.dry_run = dry_run
        self.force = force
        self.seed = seed
        self.skip_budgets = skip_budgets
        self.skip_journal_entries = skip_journal_entries
        self.rng = random.Random(seed)
        self.manifest = SeedManifest()
        self.counts = {}
        self.already_exists_counts = {}
        self.failures = []

        # Runtime dynamic cache
        self.company = None
        self.abbr = None
        self.currency = CONFIG["currency"]
        self.cash_account = None
        self.payable_account = None
        self.capex_account = None
        self.program_account = None
        self.admin_account = None
        self.expense_accounts = {}
        self.donors = []
        self.employees = []
        self.proposals = []
        self.projects = []
        self.donor_grants = []
        self.service_types = []
        self.volunteers = []
        self.opportunities = []
        self.shifts = []
        self.beneficiaries = []
        self.enrollments = []

    def log(self, msg, level="INFO"):
        prefix = f"[{level}]"
        print(f"{prefix:<8} {msg}")

    def record_created(self, doctype, name, submittable=False):
        self.counts[doctype] = self.counts.get(doctype, 0) + 1
        self.manifest.add(doctype, name, submittable)

    def record_exists(self, doctype):
        self.already_exists_counts[doctype] = self.already_exists_counts.get(doctype, 0) + 1

    def resolve_environment(self):
        """Detect company, abbreviation, default cash and expense groups."""
        company_name = CONFIG.get("company_name")
        if not company_name:
            # Detect default from user default or first company
            company_name = frappe.defaults.get_user_default("Company")
            if not company_name:
                companies = frappe.get_all("Company", limit=1, pluck="name")
                company_name = companies[0] if companies else "Bosco Soft"

        comp_doc = frappe.get_doc("Company", company_name)
        self.company = comp_doc.name
        self.abbr = comp_doc.abbr
        self.currency = comp_doc.default_currency or "INR"

        # Resolve Cash Account
        self.cash_account = comp_doc.default_cash_account
        if not self.cash_account:
            cash_accs = frappe.get_all("Account", filters={"company": self.company, "account_type": "Cash", "is_group": 0}, pluck="name")
            self.cash_account = cash_accs[0] if cash_accs else f"Cash - {self.abbr}"

        # Resolve Payable Account (for Donor Payment Entries)
        self.payable_account = comp_doc.default_payable_account
        if not self.payable_account:
            pay_accs = frappe.get_all("Account", filters={"company": self.company, "account_type": "Payable", "is_group": 0}, pluck="name")
            self.payable_account = pay_accs[0] if pay_accs else f"Creditors - {self.abbr}"

        self.capex_account = f"Capital Expenditure - {self.abbr}"
        self.program_account = f"Program Expenditure - {self.abbr}"
        self.admin_account = f"Admin Expenditure - {self.abbr}"

        self.log(f"Company: '{self.company}' (Abbr: {self.abbr}, Currency: {self.currency})")
        self.log(f"Default Cash Account: '{self.cash_account}'")
        self.log(f"Budget Accounts: CapEx='{self.capex_account}', Program='{self.program_account}', Admin='{self.admin_account}'")

    def ensure_fiscal_years(self):
        """Ensure current and past 6 months fiscal years exist."""
        today_d = getdate(today())
        # Check current year (e.g. 2026-2027)
        years_needed = [
            ("2025-2026", date(2025, 4, 1), date(2026, 3, 31)),
            ("2026-2027", date(2026, 4, 1), date(2027, 3, 31)),
            ("2027-2028", date(2027, 4, 1), date(2028, 3, 31))
        ]
        for fy_name, start_d, end_d in years_needed:
            if not frappe.db.exists("Fiscal Year", fy_name):
                if not self.dry_run:
                    fy = frappe.get_doc({
                        "doctype": "Fiscal Year",
                        "year": fy_name,
                        "year_start_date": start_d,
                        "year_end_date": end_d
                    })
                    fy.append("companies", {"company": self.company})
                    fy.insert(ignore_permissions=True)
                    self.record_created("Fiscal Year", fy.name)
                self.log(f"Created Fiscal Year: {fy_name}")
            else:
                self.record_exists("Fiscal Year")

    # --------------------------------------------------------------------------
    # SECTION A: Prerequisites and Masters
    # --------------------------------------------------------------------------
    def seed_section_a(self):
        self.log("--- Section A: Prerequisites, Masters, Settings & Donors ---")

        # 1. Single Settings
        if not self.dry_run:
            ngo_set = frappe.get_single("NGO Settings")
            ngo_set.company = self.company
            ngo_set.default_credit_account = self.cash_account
            ngo_set.save(ignore_permissions=True)
            self.counts["NGO Settings"] = 1

            vol_set = frappe.get_single("Volunteer Settings")
            vol_set.primary_color = "#2563eb"
            vol_set.secondary_color = "#0891b2"
            vol_set.login_color = "#1e3a8a"
            vol_set.sidebar_color = "#1f2937"
            vol_set.save(ignore_permissions=True)
            self.counts["Volunteer Settings"] = 1
        else:
            self.counts["NGO Settings"] = 1
            self.counts["Volunteer Settings"] = 1

        # 2. Territories
        # Ensure India exists under All Territories
        if not frappe.db.exists("Territory", "India"):
            if not self.dry_run:
                frappe.get_doc({
                    "doctype": "Territory",
                    "territory_name": "India",
                    "parent_territory": "All Territories",
                    "is_group": 1
                }).insert(ignore_permissions=True)
                self.record_created("Territory", "India")
            else:
                self.record_created("Territory", "India")
        else:
            self.record_exists("Territory")

        for district in DISTRICTS_TN:
            if not frappe.db.exists("Territory", district):
                if not self.dry_run:
                    t = frappe.get_doc({
                        "doctype": "Territory",
                        "territory_name": district,
                        "parent_territory": "India",
                        "is_group": 0
                    })
                    t.insert(ignore_permissions=True)
                    self.record_created("Territory", t.name)
                else:
                    self.record_created("Territory", district)
            else:
                self.record_exists("Territory")

        # 3. Parent Donor Cost Center
        parent_donor_cc_name = f"Donors - {self.abbr}"
        root_cc = frappe.get_all("Cost Center", filters={"company": self.company, "is_group": 1, "parent_cost_center": ["in", ["", None]]}, pluck="name")
        root_cc_name = root_cc[0] if root_cc else f"{self.company} - {self.abbr}"

        if not frappe.db.exists("Cost Center", {"cost_center_name": "Donors", "company": self.company}):
            if not self.dry_run:
                cc = frappe.get_doc({
                    "doctype": "Cost Center",
                    "cost_center_name": "Donors",
                    "company": self.company,
                    "parent_cost_center": root_cc_name,
                    "is_group": 1
                })
                cc.insert(ignore_permissions=True)
                self.record_created("Cost Center", cc.name)
                parent_donor_cc_name = cc.name
            else:
                self.record_created("Cost Center", parent_donor_cc_name)
        else:
            parent_donor_cc_name = frappe.db.get_value("Cost Center", {"cost_center_name": "Donors", "company": self.company}, "name")
            self.record_exists("Cost Center")

        # 4. Only the 3 Core Budget Expense Accounts (Dynamic with Company Abbreviation)
        exp_parent = frappe.db.get_value("Account", {"company": self.company, "account_name": "Indirect Expenses", "is_group": 1}, "name") if frappe else None
        if not exp_parent:
            exp_parent = (frappe.db.get_value("Account", {"company": self.company, "account_name": "Expenses", "is_group": 1}, "name") if frappe else None) or f"Expenses - {self.abbr}"

        three_core_accounts = [
            ("Capital Expenditure", self.capex_account),
            ("Program Expenditure", self.program_account),
            ("Admin Expenditure", self.admin_account)
        ]
        for acc_base, acc_full_name in three_core_accounts:
            if not frappe.db.exists("Account", acc_full_name):
                if not self.dry_run:
                    acc = frappe.get_doc({
                        "doctype": "Account",
                        "account_name": acc_base,
                        "company": self.company,
                        "parent_account": exp_parent,
                        "root_type": "Expense",
                        "account_type": "Expense Account",
                        "is_group": 0
                    })
                    acc.insert(ignore_permissions=True)
                    self.record_created("Account", acc.name)
                else:
                    self.record_created("Account", acc_full_name)
            else:
                self.record_exists("Account")
            self.expense_accounts[acc_base] = acc_full_name

        # 5. Suppliers as Donors (10)
        # Ensure Supplier Group "Donor" exists
        if not frappe.db.exists("Supplier Group", "Donor"):
            if not self.dry_run:
                sg = frappe.get_doc({
                    "doctype": "Supplier Group",
                    "supplier_group_name": "Donor",
                    "is_group": 0
                })
                sg.insert(ignore_permissions=True)
                self.record_created("Supplier Group", "Donor")
            else:
                self.record_created("Supplier Group", "Donor")
        else:
            self.record_exists("Supplier Group")

        # Hook `create_supplier_cost_center` in supplier_events.py creates child CC under parent CC with 'Donor'
        for donor_info in DONOR_PROFILES:
            s_name = donor_info["name"]
            if not frappe.db.exists("Supplier", s_name):
                if not self.dry_run:
                    s = frappe.get_doc({
                        "doctype": "Supplier",
                        "supplier_name": s_name,
                        "supplier_group": "Donor",
                        "supplier_type": "Donor",
                        "country": "India",
                        "company": self.company
                    })
                    s.insert(ignore_permissions=True)
                    self.record_created("Supplier", s.name)
                    # Supplier after_insert hook created Cost Center
                    s.reload()
                    self.donors.append(s.name)
                else:
                    self.record_created("Supplier", s_name)
                    self.donors.append(s_name)
            else:
                self.donors.append(s_name)
                self.record_exists("Supplier")

        # 6. Employees (10) for proposal_owner
        for fn, ln, role_title in EMPLOYEE_ROLES:
            full_emp_name = f"{fn} {ln}"
            emp_exists = frappe.db.exists("Employee", {"employee_name": full_emp_name, "company": self.company})
            if not emp_exists:
                if not self.dry_run:
                    if role_title and not frappe.db.exists("Designation", role_title):
                        desig = frappe.get_doc({
                            "doctype": "Designation",
                            "designation_name": role_title
                        })
                        desig.insert(ignore_permissions=True)
                        self.record_created("Designation", desig.name)

                    emp = frappe.get_doc({
                        "doctype": "Employee",
                        "first_name": fn,
                        "last_name": ln,
                        "employee_name": full_emp_name,
                        "gender": "Female" if fn in FIRST_NAMES_FEMALE else "Male",
                        "company": self.company,
                        "status": "Active",
                        "date_of_birth": "1990-05-15",
                        "date_of_joining": "2024-01-10",
                        "designation": role_title
                    })
                    emp.insert(ignore_permissions=True)
                    self.record_created("Employee", emp.name)
                    self.employees.append(emp.name)
                else:
                    self.record_created("Employee", full_emp_name)
                    self.employees.append(full_emp_name)
            else:
                self.employees.append(emp_exists)
                self.record_exists("Employee")

        # 7. Demo Users with specific Roles
        demo_users_def = [
            ("pm.demo@example.com", "Priya", "Program Lead", ["Program Manager", "Desk User"]),
            ("reviewer.demo@example.com", "Ramesh", "Reviewer Lead", ["Internal Reviewer", "Desk User"]),
            ("donor.demo@example.com", "Anand", "Donor Liaison", ["Donor Liaison", "Desk User"]),
            ("coordinator.demo@example.com", "Kavitha", "Coordinator", ["Volunteer Coordinator", "Projects Manager", "Desk User"]),
            ("admin.demo@example.com", "Arun", "NGO Admin", ["System Manager", "Desk User", "NGO Manager"]),
            ("volunteer.demo@example.com", "Vijay", "Volunteer Demo", ["Volunteer"])
        ]
        for email, fn, ln, roles in demo_users_def:
            if not frappe.db.exists("User", email):
                if not self.dry_run:
                    u = frappe.get_doc({
                        "doctype": "User",
                        "email": email,
                        "first_name": fn,
                        "last_name": ln,
                        "send_welcome_email": 0,
                        "user_type": "System User" if "Desk User" in roles or "System Manager" in roles else "Website User",
                        "roles": [{"role": r} for r in roles]
                    })
                    u.insert(ignore_permissions=True)
                    frappe.utils.password.update_password(email, "imman@123")
                    self.record_created("User", email)
                else:
                    self.record_created("User", email)
            else:
                if not self.dry_run:
                    frappe.utils.password.update_password(email, "imman@123")
                self.record_exists("User")

        # 8. Service Types (10)
        for st_def in SERVICE_TYPES_DEF:
            st_name = st_def["name"]
            if not frappe.db.exists("Service Type", st_name):
                exp_acc = self.expense_accounts.get(st_def["account_suffix"])
                if not self.dry_run:
                    st = frappe.get_doc({
                        "doctype": "Service Type",
                        "service_type_name": st_name,
                        "category": st_def["category"],
                        "accounting_mode": "Journal Entry",
                        "default_expense_account": exp_acc,
                        "standard_cost": st_def["cost"],
                        "is_active": 1,
                        "description": f"Standard demo service for {st_name}"
                    })
                    st.insert(ignore_permissions=True)
                    self.record_created("Service Type", st.name)
                    self.service_types.append(st.name)
                else:
                    self.record_created("Service Type", st_name)
                    self.service_types.append(st_name)
            else:
                if not self.dry_run:
                    cur_exp = self.expense_accounts.get(st_def["account_suffix"])
                    frappe.db.set_value("Service Type", st_name, "default_expense_account", cur_exp, update_modified=False)
                self.service_types.append(st_name)
                self.record_exists("Service Type")

        # 9. Volunteer Skills (55)
        for s_name, cat, desc in VOLUNTEER_SKILLS_DEF:
            if not frappe.db.exists("Volunteer Skill", s_name):
                if not self.dry_run:
                    sk = frappe.get_doc({
                        "doctype": "Volunteer Skill",
                        "skill_name": s_name,
                        "category": cat,
                        "description": desc
                    })
                    sk.insert(ignore_permissions=True)
                    self.record_created("Volunteer Skill", sk.name)
                else:
                    self.record_created("Volunteer Skill", s_name)
            else:
                self.record_exists("Volunteer Skill")

        if not self.dry_run:
            frappe.db.commit()

    # --------------------------------------------------------------------------
    # SECTION B: Projects and Funding
    # --------------------------------------------------------------------------
    def seed_section_b(self):
        self.log("--- Section B: Project Proposals, Projects, Grants & Budgets ---")

        today_d = getdate(today())

        for idx, p_def in enumerate(PROPOSALS_DEF):
            title = p_def["title"]
            prop_name = frappe.db.exists("Project Proposal", {"proposal_title": title})
            donor_name = self.donors[p_def["donor_idx"] % len(self.donors)]
            owner = self.employees[idx % len(self.employees)]

            # Target state
            target_state = p_def.get("target_state", "Approved")

            # Dates
            start_offset = -60 + (idx * 15)
            p_start = add_days(today_d, start_offset)
            p_end = add_months(p_start, p_def["duration_m"])

            if not prop_name:
                if not self.dry_run:
                    proposal = frappe.new_doc("Project Proposal")
                    proposal.proposal_title = title
                    proposal.sector = p_def["sector"]
                    proposal.proposal_owner = owner
                    proposal.donor_profile = donor_name
                    proposal.funding_type = p_def["funding_type"]
                    proposal.proposed_start_date = p_start
                    proposal.proposed_end_date = p_end
                    proposal.fcra_receipt_no = f"FCRA-TN-2026-{idx+1001}" if p_def["funding_type"] == "FCRA" else ""

                    # Geography (GeoJSON FeatureCollection Point)
                    district = DISTRICTS_TN[idx % len(DISTRICTS_TN)]
                    coords = DISTRICT_COORDINATES.get(district, [80.2707, 13.0827])
                    geo_payload = {
                        "type": "FeatureCollection",
                        "features": [
                            {
                                "type": "Feature",
                                "geometry": {
                                    "type": "Point",
                                    "coordinates": coords
                                }
                            }
                        ]
                    }
                    proposal.geography = json.dumps(geo_payload, separators=(',', ':'))

                    # Child Budget Items
                    proposal.append("budget_breakdown", {"category": "CapEx", "description": "Capital assets & machinery", "amount": p_def["capex"]})
                    proposal.append("budget_breakdown", {"category": "OpEx", "description": "Field implementation expenses", "amount": p_def["opex"]})
                    proposal.append("budget_breakdown", {"category": "Admin", "description": "Operational overhead & monitoring", "amount": p_def["admin"]})

                    proposal.insert(ignore_permissions=True)
                    self.record_created("Project Proposal", proposal.name)

                    # Workflow traversal
                    if target_state in ("Internal Review", "Donor Approval Pending", "Approved", "Rejected"):
                        frappe.model.workflow.apply_workflow(proposal, "Submit for Review")

                    if target_state in ("Donor Approval Pending", "Approved"):
                        frappe.model.workflow.apply_workflow(proposal, "Send to Donor")

                    if target_state == "Approved":
                        frappe.model.workflow.apply_workflow(proposal, "Mark as Approved")
                        # Proposal on_submit auto-created Project!
                        proposal.reload()
                        if proposal.linked_project:
                            self.record_created("Project", proposal.linked_project)
                            self.projects.append(proposal.linked_project)
                    elif target_state == "Rejected":
                        # Reviewer rejects from Internal Review or Donor Liaison rejects from Donor Approval Pending
                        proposal.approval_notes = p_def.get("rejection_notes", "Proposal rejected during internal compliance review.")
                        frappe.model.workflow.apply_workflow(proposal, "Reject")

                    self.proposals.append(proposal.name)
                else:
                    self.record_created("Project Proposal", title)
                    if target_state == "Approved":
                        self.record_created("Project", f"Auto-Project: {title}")
                        self.projects.append(f"Auto-Project: {title}")
                    self.proposals.append(title)
            else:
                if not self.dry_run:
                    district = DISTRICTS_TN[idx % len(DISTRICTS_TN)]
                    coords = DISTRICT_COORDINATES.get(district, [80.2707, 13.0827])
                    geo_payload = {
                        "type": "FeatureCollection",
                        "features": [{
                            "type": "Feature",
                            "geometry": {"type": "Point", "coordinates": coords}
                        }]
                    }
                    geo_str = json.dumps(geo_payload, separators=(',', ':'))
                    frappe.db.set_value("Project Proposal", prop_name, "geography", geo_str, update_modified=False)
                    linked_p = frappe.db.get_value("Project Proposal", prop_name, "linked_project")
                    if linked_p:
                        frappe.db.set_value("Project", linked_p, "custom_geography", geo_str, update_modified=False)
                self.proposals.append(prop_name)
                self.record_exists("Project Proposal")
                linked_proj = frappe.db.get_value("Project Proposal", prop_name, "linked_project")
                if linked_proj:
                    self.projects.append(linked_proj)
                    self.record_exists("Project")

        # Refine Created Projects (status, phase, compliance docs)
        if not self.dry_run:
            for p_idx, proj_name in enumerate(self.projects):
                proj = frappe.get_doc("Project", proj_name)

                # Move phases
                if p_idx == 0:
                    # One Suspended
                    proj.custom_project_phase = "Suspended"
                    proj.custom_reason_for_suspended = "Awaiting statutory FCRA quarterly renewal clearance from Ministry."
                elif p_idx == 1:
                    # One Completed (requires closure metrics per project_events.py)
                    proj.custom_impact_metrics = "<p>Successfully reached 450 households with safe potable water; reduced waterborne illnesses by 62% over 12 months.</p>"
                    proj.custom_closure_summary = "<p>All planned milestones achieved within approved budget; project audit certified without qualifications.</p>"
                    proj.status = "Completed"
                    proj.custom_project_phase = "Closed"
                else:
                    proj.custom_project_phase = "Active"
                    proj.status = "Open"

                # Compliance documents child rows
                # Types: MoU, FCRA Receipt, CSR Form 9A, Audit Certificate
                if not proj.custom_compliance_documents:
                    # Row 1: Valid MoU
                    proj.append("custom_compliance_documents", {
                        "document_type": "MoU",
                        "document_title": f"Bilateral MoU - {proj.project_name[:30]}",
                        "reference_number": f"MOU/2026/{p_idx+100}",
                        "issue_date": add_days(today_d, -90),
                        "expiry_date": add_days(today_d, 275),
                        "document_status": "Valid",
                        "remarks": "Signed by authorized trustees."
                    })
                    # Row 2: Expiring in 20 or 45 days for first 2 projects
                    exp_days = 20 if p_idx == 0 else (45 if p_idx == 1 else (-15 if p_idx == 2 else 180))
                    status_str = "Pending Renewal" if exp_days in (20, 45) else ("Expired" if exp_days < 0 else "Valid")
                    proj.append("custom_compliance_documents", {
                        "document_type": "CSR Form 9A" if p_idx % 2 == 0 else "FCRA Receipt",
                        "document_title": f"Statutory Compliance Filing #{p_idx+1}",
                        "reference_number": f"STAT/TN/{p_idx+500}",
                        "issue_date": add_days(today_d, -180),
                        "expiry_date": add_days(today_d, exp_days),
                        "document_status": status_str,
                        "remarks": "Notice served for renewal." if exp_days < 60 else "Compliant."
                    })

                proj.save(ignore_permissions=True)

        # Donor Grants (10+, one per approved project)
        for g_idx, proj_name in enumerate(self.projects):
            g_title = f"Grant for {proj_name}"
            grant_exists = frappe.db.exists("Donor Grant", {"grant_title": g_title})
            if not grant_exists:
                if not self.dry_run:
                    proj = frappe.get_doc("Project", proj_name)
                    grant = frappe.new_doc("Donor Grant")
                    grant.grant_title = g_title
                    grant.linked_project = proj_name
                    grant.donor_name = proj.custom_donor or self.donors[g_idx % len(self.donors)]
                    grant.funding_type = "CSR" if "CSR" in (proj.custom_funding_type or "") else ("FCRA" if "FCRA" in (proj.custom_funding_type or "") else "Government")
                    grant.status = "Active" if g_idx > 1 else ("Closed" if g_idx == 1 else "Draft")
                    grant.compliance_tag = "FCRA Receipt" if grant.funding_type == "FCRA" else "CSR Form"
                    grant.total_amount = proj.custom_total_budget or 5000000.0
                    grant.valid_from = proj.expected_start_date or add_days(today_d, -60)
                    grant.valid_to = proj.expected_end_date or add_months(today_d, 12)
                    grant.cost_center = proj.cost_center
                    grant.insert(ignore_permissions=True)
                    self.record_created("Donor Grant", grant.name)
                    self.donor_grants.append(grant.name)
                else:
                    self.record_created("Donor Grant", g_title)
                    self.donor_grants.append(g_title)
            else:
                self.donor_grants.append(grant_exists)
                self.record_exists("Donor Grant")

        # Donor Payment Entries (Receive mode from Donor / Supplier to Cash Account)
        for p_idx, proj_name in enumerate(self.projects):
            proj_doc = frappe.get_doc("Project", proj_name) if frappe else None
            donor = (proj_doc.custom_donor if proj_doc else None) or self.donors[p_idx % len(self.donors)]
            p_cost_center = (proj_doc.cost_center if proj_doc else None) or f"Main - {self.abbr}"
            amt = float((proj_doc.custom_total_budget if proj_doc else 0) or 4500000.0)

            pe_exists = frappe.db.exists("Payment Entry", {
                "project": proj_name,
                "party": donor,
                "payment_type": "Receive"
            }) if frappe else None

            if not pe_exists:
                if not self.dry_run:
                    try:
                        pe = frappe.new_doc("Payment Entry")
                        pe.payment_type = "Receive"
                        pe.party_type = "Supplier"
                        pe.party = donor
                        pe.party_name = donor
                        pe.company = self.company
                        pe.posting_date = (proj_doc.expected_start_date if proj_doc else None) or add_days(today_d, -60)
                        pe.mode_of_payment = "Cash"
                        pe.paid_from = self.payable_account
                        pe.paid_to = self.cash_account
                        pe.paid_amount = amt
                        pe.received_amount = amt
                        pe.project = proj_name
                        pe.cost_center = p_cost_center
                        pe.custom_destination = "Donor"
                        pe.remarks = f"Amount {self.currency} {amt:,.2f} received from {donor}"
                        pe.insert(ignore_permissions=True)
                        pe.submit()
                        self.record_created("Payment Entry", pe.name, submittable=True)
                    except Exception as pe_err:
                        self.log(f"Payment Entry creation error for {proj_name}/{donor}: {pe_err}", "WARN")
                else:
                    self.record_created("Payment Entry", f"PE-{proj_name}-{donor}", submittable=True)
            else:
                self.record_exists("Payment Entry")

        # ERPNext Budgets (3 budgets per Project: CapEx, OpEx, Admin using ONLY the 3 dynamic accounts)
        if not self.skip_budgets:
            fy_name = "2026-2027"
            capex_acc = self.capex_account
            opex_acc = self.program_account
            admin_acc = self.admin_account

            for idx, proj_name in enumerate(self.projects):
                p_def = PROPOSALS_DEF[idx % len(PROPOSALS_DEF)]
                budget_triplets = [
                    (capex_acc, float(p_def["capex"])),
                    (opex_acc, float(p_def["opex"])),
                    (admin_acc, float(p_def["admin"]))
                ]

                for b_acc, b_amt in budget_triplets:
                    if not b_acc:
                        continue
                    b_exists = frappe.db.exists("Budget", {"budget_against": "Project", "project": proj_name, "account": b_acc, "from_fiscal_year": fy_name})
                    if not b_exists:
                        if not self.dry_run:
                            try:
                                b = frappe.new_doc("Budget")
                                b.budget_against = "Project"
                                b.project = proj_name
                                b.company = self.company
                                b.account = b_acc
                                b.from_fiscal_year = fy_name
                                b.to_fiscal_year = fy_name
                                b.distribution_frequency = "Monthly"
                                b.budget_amount = b_amt
                                b.applicable_on_booking_actual_expenses = 1
                                b.action_if_annual_budget_exceeded = "Warn"
                                b.insert(ignore_permissions=True)
                                b.submit()  # Must be submitted for Budget Variance Report to track
                                self.record_created("Budget", b.name, submittable=True)
                            except Exception as be:
                                self.log(f"Skipping budget row for {proj_name}/{b_acc}: {be}", "WARN")
                        else:
                            self.record_created("Budget", f"Budget: {proj_name} - {b_acc}", submittable=True)
                    else:
                        if not self.dry_run:
                            # Ensure submitted
                            if frappe.db.get_value("Budget", b_exists, "docstatus") == 0:
                                b_doc = frappe.get_doc("Budget", b_exists)
                                b_doc.submit()
                        self.record_exists("Budget")

            # Create Project Expense Journal Entries after Budgets are created, using only the 3 accounts
            if not self.skip_journal_entries:
                for idx, proj_name in enumerate(self.projects):
                    p_def = PROPOSALS_DEF[idx % len(PROPOSALS_DEF)]
                    grant_data = frappe.db.get_value("Donor Grant", {"linked_project": proj_name}, ["name", "compliance_tag", "cost_center"], as_dict=True) if frappe else None
                    proj_doc = frappe.get_doc("Project", proj_name) if frappe else None
                    p_cost_center = (grant_data.cost_center if grant_data else None) or (proj_doc.cost_center if proj_doc else None) or f"Main - {self.abbr}"
                    g_name = grant_data.name if grant_data else "DG-2026-00001"
                    g_tag = grant_data.compliance_tag if grant_data else "CSR Form"

                    je_defs = [
                        (capex_acc, round(float(p_def["capex"]) * 0.20, 2), "CapEx Equipment Initial Deployment"),
                        (opex_acc, round(float(p_def["opex"]) * 0.25, 2), "Field Program Implementation Expense"),
                        (admin_acc, round(float(p_def["admin"]) * 0.20, 2), "Quarterly Administrative & Monitoring Expense")
                    ]

                    for acc, amt, remark_suffix in je_defs:
                        remark_text = f"Project {proj_name} - {remark_suffix}"
                        je_exists = frappe.db.exists("Journal Entry", {"user_remark": remark_text}) if frappe else None
                        if not je_exists:
                            if not self.dry_run:
                                try:
                                    je = frappe.new_doc("Journal Entry")
                                    je.voucher_type = "Journal Entry"
                                    je.company = self.company
                                    je.posting_date = add_days(today_d, - (30 + (idx * 5)))
                                    je.user_remark = remark_text
                                    je.custom_donor_grant = g_name
                                    je.custom_compliance_tag = g_tag
                                    je.append("accounts", {
                                        "account": acc,
                                        "debit_in_account_currency": amt,
                                        "debit": amt,
                                        "credit_in_account_currency": 0.0,
                                        "credit": 0.0,
                                        "cost_center": p_cost_center,
                                        "project": proj_name
                                    })
                                    je.append("accounts", {
                                        "account": self.cash_account,
                                        "debit_in_account_currency": 0.0,
                                        "debit": 0.0,
                                        "credit_in_account_currency": amt,
                                        "credit": amt,
                                        "cost_center": p_cost_center,
                                        "project": proj_name
                                    })
                                    je.insert(ignore_permissions=True)
                                    je.submit()
                                    self.record_created("Journal Entry", je.name, submittable=True)
                                except Exception as j_err:
                                    self.log(f"Project JE error for {proj_name}: {j_err}", "DEBUG")
                            else:
                                self.record_created("Journal Entry", f"JE-PROJ-{proj_name}-{acc}", submittable=True)
                        else:
                            self.record_exists("Journal Entry")

        if not self.dry_run:
            frappe.db.commit()

    # --------------------------------------------------------------------------
    # SECTION C: Volunteers & Portal Experience
    # --------------------------------------------------------------------------
    def seed_section_c(self):
        self.log("--- Section C: Volunteers, Applications, Opportunities, Shifts & Attendance ---")

        today_d = getdate(today())
        skills_list = frappe.get_all("Volunteer Skill", pluck="name") if not self.dry_run else [s[0] for s in VOLUNTEER_SKILLS_DEF]

        # 1. Volunteer Applications (30)
        # Approval creates User & Volunteer automatically via volunteer_application.py
        for i in range(CONFIG["counts"]["volunteer_applications"]):
            gender = "Female" if i % 2 == 0 else "Male"
            first = (FIRST_NAMES_FEMALE if gender == "Female" else FIRST_NAMES_MALE)[i % len(FIRST_NAMES_FEMALE)]
            last = LAST_NAMES[i % len(LAST_NAMES)]
            full_name = f"{first} {last}"
            email = "volunteer.demo@example.com" if i == 0 else f"volunteer.{first.lower()}.{last.lower()}{i}@example.com"
            phone = f"+91 94440 {i+10000}"

            app_exists = frappe.db.exists("Volunteer Application", {"email": email})
            # Desired status: 22 Approved, 5 Pending, 3 Rejected
            target_status = "Approved" if i < 22 else ("Pending" if i < 27 else "Rejected")

            if not app_exists:
                if not self.dry_run:
                    app = frappe.new_doc("Volunteer Application")
                    app.applicant_name = full_name
                    app.email = email
                    app.phone = phone
                    app.gender = gender
                    app.date_of_birth = add_days(today_d, - (20 * 365 + i * 120))
                    app.address = f"No. {i+12}, Gandhi Road, {DISTRICTS_TN[i % len(DISTRICTS_TN)]}, Tamil Nadu"
                    app.application_date = add_days(today_d, - (60 - i))
                    app.motivation = "Passionate about contributing to grassroots community welfare and education."

                    # 1-3 Skills
                    chosen_skills = self.rng.sample(skills_list, min(len(skills_list), self.rng.randint(1, 3)))
                    for sk in chosen_skills:
                        app.append("skills", {"skill": sk, "proficiency": self.rng.choice(["Beginner", "Intermediate", "Expert"])})

                    # Availability
                    for d_idx in range(self.rng.randint(1, 3)):
                        app.append("availability", {
                            "day_of_week": ["Saturday", "Sunday", "Wednesday"][d_idx],
                            "from_time": "09:00:00",
                            "to_time": "13:00:00"
                        })

                    if target_status == "Rejected":
                        app.review_remarks = "Candidate unavailable during active shift hours in this region."

                    app.insert(ignore_permissions=True)
                    self.record_created("Volunteer Application", app.name)

                    # Workflow approval
                    if target_status in ("Pending", "Approved", "Rejected"):
                        frappe.model.workflow.apply_workflow(app, "Submit for Review")

                    if target_status == "Approved":
                        frappe.model.workflow.apply_workflow(app, "Approve")
                        # This auto-created User and Volunteer!
                        app.reload()
                        if app.volunteer:
                            self.record_created("Volunteer", app.volunteer)
                            self.volunteers.append(app.volunteer)
                    elif target_status == "Rejected":
                        app.review_remarks = "Candidate unavailable during active shift hours in this region."
                        frappe.model.workflow.apply_workflow(app, "Reject")
                else:
                    self.record_created("Volunteer Application", email)
                    if target_status == "Approved":
                        self.record_created("Volunteer", f"Auto-Vol: {full_name}")
                        self.volunteers.append(f"Auto-Vol: {full_name}")
            else:
                self.record_exists("Volunteer Application")
                v_linked = frappe.db.get_value("Volunteer Application", app_exists, "volunteer")
                if v_linked and v_linked not in self.volunteers:
                    self.volunteers.append(v_linked)
                    self.record_exists("Volunteer")

        # Set demo password for demo volunteer user
        if not self.dry_run and frappe.db.exists("User", "volunteer.demo@example.com"):
            frappe.utils.password.update_password("volunteer.demo@example.com", CONFIG["demo_password"])

        # Make 2 volunteers Inactive / On Hold for variety
        if not self.dry_run and len(self.volunteers) >= 20:
            frappe.db.set_value("Volunteer", self.volunteers[-1], "status", "On Hold")
            frappe.db.set_value("Volunteer", self.volunteers[-2], "status", "Inactive")

        # 2. Volunteer Opportunities (12)
        for o_idx, opp_def in enumerate(OPPORTUNITIES_DEF):
            o_title = opp_def["title"]
            opp_exists = frappe.db.exists("Volunteer Opportunity", {"title": o_title})
            p_link = self.projects[o_idx % len(self.projects)] if self.projects else None

            if not opp_exists:
                if not self.dry_run:
                    opp = frappe.new_doc("Volunteer Opportunity")
                    opp.title = o_title
                    opp.project = p_link
                    opp.vacancies = opp_def["vacancies"]
                    opp.status = opp_def.get("status", "Open")
                    opp.start_date = add_days(today_d, -45)
                    opp.end_date = add_days(today_d, 90)
                    opp.location = opp_def["loc"]
                    opp.description = f"Volunteer mission for {o_title} across project sites."
                    for sk_name in opp_def.get("skills", []):
                        if frappe.db.exists("Volunteer Skill", sk_name):
                            opp.append("required_skills", {"skill": sk_name, "proficiency": "Intermediate"})
                    opp.insert(ignore_permissions=True)
                    self.record_created("Volunteer Opportunity", opp.name)
                    self.opportunities.append(opp.name)
                else:
                    self.record_created("Volunteer Opportunity", o_title)
                    self.opportunities.append(o_title)
            else:
                self.opportunities.append(opp_exists)
                self.record_exists("Volunteer Opportunity")

        # 3. Volunteer Assignments (30)
        # Statuses: Assigned, Active, Completed, Withdrawn.
        active_vols = [v for v in self.volunteers if frappe.db.get_value("Volunteer", v, "status") == "Active"] if not self.dry_run else self.volunteers
        # Ensure demo volunteer is in active_vols
        demo_vol = frappe.db.get_value("Volunteer", {"email": "volunteer.demo@example.com"}, "name") if not self.dry_run else None

        for a_idx in range(CONFIG["counts"]["volunteer_assignments"]):
            opp_name = self.opportunities[a_idx % len(self.opportunities)]
            opp_status = frappe.db.get_value("Volunteer Opportunity", opp_name, "status") if not self.dry_run else "Open"
            if opp_status in ("Closed", "Cancelled"):
                continue

            vol_name = demo_vol if (a_idx < 3 and demo_vol) else active_vols[a_idx % len(active_vols)]
            status = "Active" if a_idx % 4 == 0 else ("Assigned" if a_idx % 4 == 1 else ("Completed" if a_idx % 4 == 2 else "Withdrawn"))

            asgn_exists = frappe.db.exists("Volunteer Assignment", {"volunteer": vol_name, "opportunity": opp_name, "from_date": add_days(today_d, -30 + a_idx)})
            if not asgn_exists:
                if not self.dry_run:
                    try:
                        asgn = frappe.new_doc("Volunteer Assignment")
                        asgn.volunteer = vol_name
                        asgn.opportunity = opp_name
                        asgn.role = "Field Volunteer" if a_idx % 2 == 0 else "Team Coordinator"
                        asgn.from_date = add_days(today_d, -30 + a_idx)
                        asgn.to_date = add_days(asgn.from_date, 60)
                        asgn.status = status
                        asgn.insert(ignore_permissions=True)
                        self.record_created("Volunteer Assignment", asgn.name)
                    except Exception as ae:
                        self.log(f"Skipping assignment ({vol_name}/{opp_name}): {ae}", "DEBUG")
                else:
                    self.record_created("Volunteer Assignment", f"ASN-{vol_name}-{opp_name}")
            else:
                self.record_exists("Volunteer Assignment")

        # 4. Volunteer Shifts (40)
        # 30 past shifts (past 8 weeks), 10 upcoming shifts (next 2 weeks)
        for s_idx in range(CONFIG["counts"]["volunteer_shifts"]):
            opp_name = self.opportunities[s_idx % len(self.opportunities)]
            day_offset = -56 + (s_idx * 2) if s_idx < 30 else ((s_idx - 30) * 1)
            shift_date = add_days(today_d, day_offset)
            start_time = "09:00:00" if s_idx % 2 == 0 else "14:00:00"
            end_time = "13:00:00" if s_idx % 2 == 0 else "18:00:00"

            s_exists = frappe.db.exists("Volunteer Shift", {"opportunity": opp_name, "shift_date": shift_date, "start_time": start_time})
            if not s_exists:
                if not self.dry_run:
                    sh = frappe.new_doc("Volunteer Shift")
                    sh.opportunity = opp_name
                    sh.shift_date = shift_date
                    sh.start_time = start_time
                    sh.end_time = end_time
                    sh.required_count = 4
                    sh.status = "Completed" if shift_date < today_d else "Scheduled"

                    # 3-5 Participants
                    shift_participants = active_vols[s_idx:s_idx+4] if len(active_vols) >= s_idx+4 else active_vols[:4]
                    if demo_vol and s_idx % 3 == 0 and demo_vol not in shift_participants:
                        shift_participants = [demo_vol] + shift_participants[:-1]

                    for p_vol in shift_participants:
                        sh.append("participants", {
                            "volunteer": p_vol,
                            "status": "Confirmed" if shift_date >= today_d else self.rng.choice(["Confirmed", "Confirmed", "Absent", "Replaced"])
                        })
                    sh.insert(ignore_permissions=True)
                    self.record_created("Volunteer Shift", sh.name)
                    self.shifts.append((sh.name, opp_name, shift_date, start_time, end_time, shift_participants))
                else:
                    self.record_created("Volunteer Shift", f"SH-{opp_name}-{shift_date}")
                    self.shifts.append((f"SH-{opp_name}", opp_name, shift_date, start_time, end_time, []))
            else:
                existing_parts = frappe.get_all("Volunteer Shift Participant", filters={"parent": s_exists}, pluck="volunteer") if frappe else []
                self.shifts.append((s_exists, opp_name, shift_date, start_time, end_time, existing_parts))
                self.record_exists("Volunteer Shift")

        # 5. Volunteer Attendance (60+)
        admin_user = "coordinator.demo@example.com" if frappe.db.exists("User", "coordinator.demo@example.com") else "Administrator"
        att_count = 0
        for sh_tuple in self.shifts:
            sh_name, opp_name, s_date, st_time, end_time, participants = sh_tuple
            if s_date >= today_d:
                continue

            for p_vol in (participants or active_vols[:3]):
                if att_count >= CONFIG["counts"]["volunteer_attendances"]:
                    break
                att_exists = frappe.db.exists("Volunteer Attendance", {"volunteer": p_vol, "date": s_date, "shift": sh_name})
                if not att_exists:
                    if not self.dry_run:
                        status = "Present" if att_count % 6 != 0 else ("Half Day" if att_count % 12 != 0 else "Absent")
                        att = frappe.new_doc("Volunteer Attendance")
                        att.volunteer = p_vol
                        att.shift = sh_name
                        att.opportunity = opp_name
                        att.date = s_date
                        att.status = status
                        att.approved_by = admin_user
                        if status == "Present":
                            att.in_time = st_time
                            att.out_time = end_time
                        elif status == "Half Day":
                            att.in_time = st_time
                            att.out_time = "11:00:00" if st_time == "09:00:00" else "16:00:00"
                        att.insert(ignore_permissions=True)
                        self.record_created("Volunteer Attendance", att.name)
                        att_count += 1
                    else:
                        self.record_created("Volunteer Attendance", f"ATT-{p_vol}-{s_date}")
                        att_count += 1
                else:
                    self.record_exists("Volunteer Attendance")

        # 6. Volunteer Opportunity Interest (12)
        for i_idx in range(CONFIG["counts"]["volunteer_interests"]):
            opp_name = self.opportunities[i_idx % len(self.opportunities)]
            v_name = active_vols[(i_idx + 2) % len(active_vols)]
            int_exists = frappe.db.exists("Volunteer Opportunity Interest", {"opportunity": opp_name, "volunteer": v_name})
            if not int_exists:
                if not self.dry_run:
                    oi = frappe.new_doc("Volunteer Opportunity Interest")
                    oi.opportunity = opp_name
                    oi.volunteer = v_name
                    oi.status = "Pending" if i_idx % 3 == 0 else ("Approved" if i_idx % 3 == 1 else "Rejected")
                    oi.notes = "Eager to contribute weekend hours to this project."
                    oi.insert(ignore_permissions=True)
                    self.record_created("Volunteer Opportunity Interest", oi.name)
                else:
                    self.record_created("Volunteer Opportunity Interest", f"INT-{opp_name}-{v_name}")
            else:
                self.record_exists("Volunteer Opportunity Interest")

        if not self.dry_run:
            frappe.db.commit()

    # --------------------------------------------------------------------------
    # SECTION D: Beneficiaries & Sector-Coherent Services
    # --------------------------------------------------------------------------
    def seed_section_d(self):
        self.log("--- Section D: Beneficiaries, Enrollments, Assessments & Services ---")

        today_d = getdate(today())
        admin_user = "pm.demo@example.com" if frappe.db.exists("User", "pm.demo@example.com") else "Administrator"

        # 1. Beneficiaries (80)
        for b_idx in range(CONFIG["counts"]["beneficiaries"]):
            gender = "Female" if b_idx % 2 == 0 else ("Male" if b_idx % 5 != 0 else "Other")
            first = (FIRST_NAMES_FEMALE if gender == "Female" else FIRST_NAMES_MALE)[b_idx % len(FIRST_NAMES_FEMALE)]
            last = LAST_NAMES[(b_idx * 3) % len(LAST_NAMES)]
            full_name = f"{first} {last}"
            national_id = f"SYN-{b_idx+1001:06d}"
            dist = DISTRICTS_TN[b_idx % len(DISTRICTS_TN)]

            b_exists = frappe.db.exists("Beneficiary", {"national_id_type": "National ID", "national_id_number": national_id})

            # Sector age coherence
            if b_idx % 3 == 0:
                # Children (Education / Nutrition)
                dob = add_days(today_d, - (7 * 365 + b_idx * 40))
            elif b_idx % 3 == 1:
                # Young adults & mothers (Livelihoods / Maternal)
                dob = add_days(today_d, - (28 * 365 + b_idx * 80))
            else:
                # Adults & elderly (WASH / Health)
                dob = add_days(today_d, - (48 * 365 + b_idx * 90))

            # Consent logic: 90% consented, 2 withdrawn, 6 Inactive/Exited
            consent_given = 1 if b_idx < 72 else 0
            consent_withdrawn = 1 if b_idx in (72, 73) else 0
            b_status = "Inactive" if b_idx in (74, 75, 76) else ("Exited" if b_idx in (77, 78, 79) else "Active")

            if not b_exists:
                if not self.dry_run:
                    ben = frappe.new_doc("Beneficiary")
                    ben.full_name = full_name
                    ben.gender = gender
                    ben.date_of_birth = dob
                    ben.status = b_status
                    ben.territory = dist
                    ben.national_id_type = "National ID"
                    ben.national_id_number = national_id
                    ben.phone = f"+91 94440 {b_idx+20000}"
                    ben.address = f"Door #{b_idx+10}, South Street, {dist}, Tamil Nadu"
                    ben.consent_given = consent_given
                    ben.consent_date = add_days(today_d, -120) if consent_given else None
                    ben.consent_taken_by = admin_user if consent_given else None
                    ben.consent_withdrawn = consent_withdrawn
                    ben.withdrawal_date = add_days(today_d, -15) if consent_withdrawn else None

                    # 1-3 Family Members
                    for f_idx in range(self.rng.randint(1, 3)):
                        ben.append("family_members", {
                            "member_name": f"{FIRST_NAMES_MALE[f_idx % len(FIRST_NAMES_MALE)]} {last}",
                            "relationship": ["Spouse", "Child", "Parent"][f_idx],
                            "gender": "Male" if f_idx % 2 == 0 else "Female",
                            "date_of_birth": add_days(dob, - (f_idx * 365 * 3)),
                            "is_dependent": 1
                        })
                    ben.insert(ignore_permissions=True)
                    self.record_created("Beneficiary", ben.name)
                    self.beneficiaries.append(ben.name)
                else:
                    self.record_created("Beneficiary", full_name)
                    self.beneficiaries.append(full_name)
            else:
                self.beneficiaries.append(b_exists)
                self.record_exists("Beneficiary")

        # 2. Beneficiary Enrollments (100)
        # Unique active enrollment per beneficiary per project
        active_bens = [b for b in self.beneficiaries if frappe.db.get_value("Beneficiary", b, "status") == "Active"] if not self.dry_run else self.beneficiaries

        for e_idx in range(CONFIG["counts"]["beneficiary_enrollments"]):
            ben_name = active_bens[e_idx % len(active_bens)]
            proj_name = self.projects[e_idx % len(self.projects)]
            enr_exists = frappe.db.exists("Beneficiary Enrollment", {"beneficiary": ben_name, "project": proj_name})

            enr_status = "Active" if e_idx < 80 else ("Completed" if e_idx < 92 else "Exited")
            enr_date = add_days(today_d, - (150 - e_idx))
            exp_end = add_days(enr_date, 180)
            act_end = add_days(enr_date, 120) if enr_status in ("Completed", "Exited") else None

            if not enr_exists:
                if not self.dry_run:
                    enr = frappe.new_doc("Beneficiary Enrollment")
                    enr.beneficiary = ben_name
                    enr.project = proj_name
                    enr.enrollment_date = enr_date
                    enr.expected_end_date = exp_end
                    enr.actual_end_date = act_end
                    enr.status = enr_status
                    if enr_status == "Exited":
                        enr.exit_reason = "Relocated to neighboring district for employment."
                    enr.insert(ignore_permissions=True)
                    self.record_created("Beneficiary Enrollment", enr.name)
                    self.enrollments.append((enr.name, ben_name, proj_name, enr_date, act_end or exp_end, enr_status))
                else:
                    self.record_created("Beneficiary Enrollment", f"ENR-{ben_name}-{proj_name}")
                    self.enrollments.append((f"ENR-{ben_name}", ben_name, proj_name, enr_date, exp_end, enr_status))
            else:
                self.enrollments.append((enr_exists, ben_name, proj_name, enr_date, exp_end, enr_status))
                self.record_exists("Beneficiary Enrollment")

        # 3. Beneficiary Assessments (Baseline for all, Midline for half, Endline for Completed)
        for enr_tuple in self.enrollments:
            enr_name, ben_name, proj_name, enr_date, end_date, enr_status = enr_tuple
            p_sector = frappe.db.get_value("Project", proj_name, "custom_sector") if not self.dry_run else "Health"
            sector_ind_list = BENEFICIARY_INDICATORS.get(p_sector, BENEFICIARY_INDICATORS["Health"])

            # Baseline Assessment
            base_exists = frappe.db.exists("Beneficiary Assessment", {"enrollment": enr_name, "assessment_type": "Baseline"})
            if not base_exists:
                if not self.dry_run:
                    asm = frappe.new_doc("Beneficiary Assessment")
                    asm.beneficiary = ben_name
                    asm.enrollment = enr_name
                    asm.assessment_type = "Baseline"
                    asm.assessment_date = enr_date
                    asm.assessed_by = admin_user
                    for ind_name, unit, target, base_val, end_val in sector_ind_list:
                        asm.append("indicators", {
                            "indicator": ind_name,
                            "unit": unit,
                            "target_value": target,
                            "actual_value": base_val,
                            "remarks": "Initial baseline evaluation."
                        })
                    asm.insert(ignore_permissions=True)
                    self.record_created("Beneficiary Assessment", asm.name)
                else:
                    self.record_created("Beneficiary Assessment", f"ASM-Base-{enr_name}")
            else:
                self.record_exists("Beneficiary Assessment")

            # Midline Assessment (for enrollments older than 60 days)
            if (today_d - enr_date).days > 60:
                mid_exists = frappe.db.exists("Beneficiary Assessment", {"enrollment": enr_name, "assessment_type": "Midline"})
                if not mid_exists:
                    if not self.dry_run:
                        asm_m = frappe.new_doc("Beneficiary Assessment")
                        asm_m.beneficiary = ben_name
                        asm_m.enrollment = enr_name
                        asm_m.assessment_type = "Midline"
                        asm_m.assessment_date = add_days(enr_date, 60)
                        asm_m.assessed_by = admin_user
                        for ind_name, unit, target, base_val, end_val in sector_ind_list:
                            mid_val = round((base_val + end_val) / 2.0, 1)
                            asm_m.append("indicators", {
                                "indicator": ind_name,
                                "unit": unit,
                                "target_value": target,
                                "actual_value": mid_val,
                                "remarks": "Mid-term evaluation showing positive trajectory."
                            })
                        asm_m.insert(ignore_permissions=True)
                        self.record_created("Beneficiary Assessment", asm_m.name)
                    else:
                        self.record_created("Beneficiary Assessment", f"ASM-Mid-{enr_name}")
                else:
                    self.record_exists("Beneficiary Assessment")

            # Endline Assessment (for Completed enrollments)
            if enr_status == "Completed":
                end_exists = frappe.db.exists("Beneficiary Assessment", {"enrollment": enr_name, "assessment_type": "Endline"})
                if not end_exists:
                    if not self.dry_run:
                        asm_e = frappe.new_doc("Beneficiary Assessment")
                        asm_e.beneficiary = ben_name
                        asm_e.enrollment = enr_name
                        asm_e.assessment_type = "Endline"
                        asm_e.assessment_date = end_date
                        asm_e.assessed_by = admin_user
                        for ind_name, unit, target, base_val, end_val in sector_ind_list:
                            asm_e.append("indicators", {
                                "indicator": ind_name,
                                "unit": unit,
                                "target_value": target,
                                "actual_value": end_val,
                                "remarks": "Target milestone successfully achieved at exit."
                            })
                        asm_e.insert(ignore_permissions=True)
                        self.record_created("Beneficiary Assessment", asm_e.name)
                    else:
                        self.record_created("Beneficiary Assessment", f"ASM-End-{enr_name}")
                else:
                    self.record_exists("Beneficiary Assessment")

        # 4. Beneficiary Services (150)
        # Provided only to Active consented enrollments
        active_consented_enrs = []
        if not self.dry_run:
            for enr_tuple in self.enrollments:
                enr_name, ben_name, proj_name, enr_date, end_date, enr_status = enr_tuple
                if enr_status == "Active":
                    b_doc = frappe.get_doc("Beneficiary", ben_name)
                    if b_doc.consent_given and not b_doc.consent_withdrawn:
                        active_consented_enrs.append(enr_tuple)
        else:
            active_consented_enrs = self.enrollments[:80]

        je_created_count = 0
        from ngo.beneficiary_management.doctype.beneficiary_service.beneficiary_service import make_journal_entry

        for s_idx in range(CONFIG["counts"]["beneficiary_services"]):
            enr_tuple = active_consented_enrs[s_idx % len(active_consented_enrs)]
            enr_name, ben_name, proj_name, enr_date, end_date, enr_status = enr_tuple
            st_name = self.service_types[s_idx % len(self.service_types)]

            # Service date within enrollment window (deterministic across runs)
            max_offset = max(10, min(100, (today_d - enr_date).days))
            day_offset = ((s_idx * 7) % (max_offset - 4)) + 5
            s_date = add_days(enr_date, day_offset)
            if s_date > today_d:
                s_date = today_d

            bsv_exists = frappe.db.exists("Beneficiary Service", {"enrollment": enr_name, "service_type": st_name, "service_date": s_date})
            if not bsv_exists:
                if not self.dry_run:
                    proj_doc = frappe.get_doc("Project", proj_name)
                    st_doc = frappe.get_doc("Service Type", st_name)
                    qty = 1 if "Kit" in st_name or "Grant" in st_name else self.rng.choice([1, 2, 3])
                    rate = st_doc.standard_cost or 1000.0

                    bsv = frappe.new_doc("Beneficiary Service")
                    bsv.enrollment = enr_name
                    bsv.beneficiary = ben_name
                    bsv.project = proj_name
                    bsv.service_type = st_name
                    bsv.cost_center = proj_doc.cost_center or f"Main - {self.abbr}"
                    bsv.service_date = s_date
                    bsv.qty = qty
                    bsv.rate = rate
                    bsv.insert(ignore_permissions=True)
                    bsv.submit()
                    self.record_created("Beneficiary Service", bsv.name, submittable=True)

                    # 5. Make Journal Entry for ~100 of them
                    if not self.skip_journal_entries and je_created_count < CONFIG["counts"]["journal_entries"]:
                        try:
                            je = make_journal_entry(bsv.name)
                            # Ensure custom fields custom_donor_grant and custom_compliance_tag are non-empty
                            if not je.custom_donor_grant:
                                grant = frappe.db.get_value("Donor Grant", {"linked_project": proj_name}, ["name", "compliance_tag"], as_dict=True)
                                if grant:
                                    je.custom_donor_grant = grant.name
                                    je.custom_compliance_tag = grant.compliance_tag or "CSR Form"
                                else:
                                    any_grant = frappe.db.get_value("Donor Grant", {"status": "Active"}, ["name", "compliance_tag"], as_dict=True)
                                    if any_grant:
                                        je.custom_donor_grant = any_grant.name
                                        je.custom_compliance_tag = any_grant.compliance_tag or "General"
                                    else:
                                        je.custom_compliance_tag = "General"

                            if not je.custom_compliance_tag:
                                je.custom_compliance_tag = "CSR Form"

                            je.insert(ignore_permissions=True)
                            je.submit()
                            self.record_created("Journal Entry", je.name, submittable=True)
                            frappe.db.set_value("Beneficiary Service", bsv.name, "journal_entry", je.name, update_modified=False)
                            je_created_count += 1
                        except Exception as j_err:
                            self.log(f"Journal entry creation failed for service {bsv.name}: {j_err}", "DEBUG")
                else:
                    self.record_created("Beneficiary Service", f"BSV-{enr_name}-{st_name}")
                    if not self.skip_journal_entries and je_created_count < CONFIG["counts"]["journal_entries"]:
                        self.record_created("Journal Entry", f"JE-BSV-{s_idx+1}")
                        je_created_count += 1
            else:
                self.record_exists("Beneficiary Service")

        if not self.dry_run:
            frappe.db.commit()

    # --------------------------------------------------------------------------
    # SECTION E: Verification & Reporting
    # --------------------------------------------------------------------------
    def verify(self):
        self.log("============================================================")
        self.log("                  NGO SEED VERIFICATION TABLE               ")
        self.log("============================================================")

        doctypes_to_verify = [
            ("Project Proposal", 10),
            ("Project", 10),
            ("Donor Grant", 10),
            ("Budget Item", 10),
            ("Compliance Doc", 10),
            ("Budget", 10 if not self.skip_budgets else 0),
            ("Beneficiary", 10),
            ("Beneficiary Family Member", 10),
            ("Beneficiary Enrollment", 10),
            ("Beneficiary Assessment", 10),
            ("Assessment Indicator", 10),
            ("Service Type", 10),
            ("Beneficiary Service", 10),
            ("Volunteer", 10),
            ("Volunteer Application", 10),
            ("Volunteer Skill", 10),
            ("Volunteer Skill Item", 10),
            ("Volunteer Availability", 10),
            ("Volunteer Opportunity", 10),
            ("Volunteer Assignment", 10),
            ("Volunteer Shift", 10),
            ("Volunteer Shift Participant", 10),
            ("Volunteer Attendance", 10),
            ("Volunteer Opportunity Interest", 10),
            ("Supplier", 10),
            ("Employee", 10),
            ("Payment Entry", 10),
            ("Journal Entry", 10 if not self.skip_journal_entries else 0)
        ]

        summary_rows = []
        overall_pass = True

        print(f"\n{'DocType':<32} | {'Seeded':<8} | {'Total in DB':<12} | {'Min Reqd':<8} | {'Status'}")
        print("-" * 75)

        # Calculate child rows for both live count and dry run summary
        if self.dry_run:
            self.counts["Budget Item"] = len(self.proposals) * 3
            self.counts["Compliance Doc"] = len(self.projects) * 2
            self.counts["Volunteer Skill Item"] = CONFIG["counts"]["volunteer_applications"] * 2 + CONFIG["counts"]["volunteer_opportunities"] * 2
            self.counts["Volunteer Availability"] = CONFIG["counts"]["volunteer_applications"] * 2
            self.counts["Volunteer Shift Participant"] = CONFIG["counts"]["volunteer_shifts"] * 4
            self.counts["Beneficiary Family Member"] = CONFIG["counts"]["beneficiaries"] * 2
            self.counts["Assessment Indicator"] = len(self.enrollments) * 4 * 2

        for dt, min_req in doctypes_to_verify:
            if frappe and not self.dry_run:
                if frappe.db.exists("DocType", dt):
                    total = frappe.db.count(dt)
                else:
                    total = 0
                seeded = self.counts.get(dt, total)
            else:
                seeded = self.counts.get(dt, 0)
                total = seeded

            passed = total >= min_req
            if not passed and min_req > 0:
                overall_pass = False

            status_str = "PASS" if passed else "FAIL"
            print(f"{dt:<32} | {seeded:<8} | {total:<12} | {min_req:<8} | {status_str}")
            summary_rows.append({"doctype": dt, "seeded": seeded, "total": total, "passed": passed})

        print("-" * 75)
        print(f"Overall Result: {'ALL PASS' if overall_pass else 'SOME CHECKS FAILED'}\n")

        # Budget Variance Report Verification Check
        if frappe and not self.dry_run and not self.skip_budgets:
            try:
                from erpnext.accounts.report.budget_variance_report.budget_variance_report import execute as execute_bvr
                bvr_filters = frappe._dict({
                    "company": self.company,
                    "from_fiscal_year": "2026-2027",
                    "to_fiscal_year": "2026-2027",
                    "period": "Yearly",
                    "budget_against": "Project"
                })
                bvr_cols, bvr_data, _, _ = execute_bvr(bvr_filters)
                print("\n" + "=" * 60)
                print("           BUDGET VARIANCE REPORT VERIFICATION CHECK        ")
                print("=" * 60)
                print(f"BVR Rows Tracked (FY 2026-2027, Project-wise): {len(bvr_data)}")
                if bvr_data:
                    sample_proj = bvr_data[0].get("budget_against")
                    sample_rows = [r for r in bvr_data if r.get("budget_against") == sample_proj]
                    proj_title = frappe.db.get_value("Project", sample_proj, "project_name") or sample_proj
                    print(f"Sample Project: {proj_title} ({sample_proj})")
                    print(f"  {'Account':<28} | {'Budget':<12} | {'Actual':<12} | {'Variance'}")
                    print("  " + "-" * 62)
                    for sr in sample_rows:
                        acc_short = sr.get("account", "").split(" - ")[0]
                        b_val = sr.get("budget_2026_2027", 0.0)
                        a_val = sr.get("actual_2026_2027", 0.0)
                        v_val = sr.get("variance_2026_2027", 0.0)
                        print(f"  {acc_short:<28} | ₹{b_val:>10,.2f} | ₹{a_val:>10,.2f} | ₹{v_val:>10,.2f}")
                print("=" * 60)
            except Exception as bvr_err:
                print(f"[WARN] BVR verification check exception: {bvr_err}")

        # Demo Credentials
        print("\n" + "=" * 60)
        print("                  DEMO CREDENTIALS & ACCESS                 ")
        print("=" * 60)
        print(f"Password for all demo accounts: {CONFIG['demo_password']}")
        print("  1. Volunteer Portal User:  volunteer.demo@example.com (Access at /frontend)")
        print("  2. Volunteer Coordinator:  coordinator.demo@example.com (Access at /app)")
        print("  3. Program Manager:        pm.demo@example.com (Access at /app)")
        print("  4. Internal Reviewer:      reviewer.demo@example.com (Access at /app)")
        print("  5. Donor Liaison:          donor.demo@example.com (Access at /app)")
        print("  6. System Admin:           admin.demo@example.com (Access at /app)")
        print("\nPortal & Dashboard Links:")
        print(f"  • Volunteer Portal:         {frappe.utils.get_url() if frappe else ''}/frontend")
        print(f"  • Desk:                     {frappe.utils.get_url() if frappe else ''}/app")
        print(f"  • Project Dashboard:        {frappe.utils.get_url() if frappe else ''}/app/dashboard-view/Caritas%20India%20—%20Project%20Dashboard")
        print(f"  • Volunteer Dashboard:      {frappe.utils.get_url() if frappe else ''}/app/volunteer-management")
        print("=" * 60 + "\n")

        return overall_pass, summary_rows


# ==============================================================================
# RESET MANAGER
# ==============================================================================
def reset_seeded_data():
    """Removes records recorded in manifest or cleans up seeded demo data safely in reverse dependency order."""
    if not frappe:
        print("[ERROR] Frappe not initialized.")
        return

    manifest = SeedManifest()
    records = manifest.load()

    # Mute emails and background indexing during reset
    orig_mute_emails = getattr(frappe.flags, "mute_emails", False)
    orig_in_test = getattr(frappe.flags, "in_test", False)
    frappe.flags.mute_emails = True
    frappe.flags.in_test = True

    cancelled = 0
    deleted = 0
    skipped = 0

    try:
        if records:
            print(f"[INFO] Resetting {len(records)} seeded records from manifest in reverse creation order...")
            for r in reversed(records):
                dt = r["doctype"]
                name = r["name"]

                if not frappe.db.exists(dt, name):
                    skipped += 1
                    continue

                try:
                    if dt == "Journal Entry":
                        frappe.db.delete("GL Entry", {"voucher_no": name})
                    doc = frappe.get_doc(dt, name)
                    if doc.docstatus == 1:
                        doc.cancel()
                        cancelled += 1

                    frappe.delete_doc(dt, name, force=1, ignore_permissions=True)
                    deleted += 1
                except Exception as e:
                    print(f"[WARN] Failed to delete {dt} {name}: {e}")

            manifest.clear()
            frappe.db.commit()
            print(f"[SUCCESS] Manifest reset complete! Cancelled: {cancelled}, Deleted: {deleted}, Skipped: {skipped}")

        # Safe fallback cleanup to guarantee clean site
        # Clear redis job backlog so delete_dynamic_links never throws QueueOverloaded
        try:
            r_conn = frappe.utils.background_jobs.get_redis_conn()
            for k in r_conn.keys("*rq:queue*") + r_conn.keys("*rq:job*"):
                r_conn.delete(k)
        except Exception:
            pass

        # 1. Beneficiary Services (must be deleted before Journal Entries to free Link constraints)
        for bs in frappe.get_all("Beneficiary Service", pluck="name"):
            try:
                frappe.db.set_value("Beneficiary Service", bs, "journal_entry", None, update_modified=False)
                doc = frappe.get_doc("Beneficiary Service", bs)
                if doc.docstatus == 1:
                    doc.cancel()
                frappe.delete_doc("Beneficiary Service", bs, force=1, ignore_permissions=True)
                deleted += 1
            except Exception:
                pass

        # 2. Journal Entries
        jes = frappe.get_all("Journal Entry", filters={"custom_donor_grant": ["is", "set"]}, pluck="name")
        jes += frappe.get_all("Journal Entry", filters={"user_remark": ["like", "Beneficiary Service:%"]}, pluck="name")
        for je in set(jes):
            try:
                frappe.db.delete("GL Entry", {"voucher_no": je})
                doc = frappe.get_doc("Journal Entry", je)
                if doc.docstatus == 1:
                    doc.cancel()
                frappe.delete_doc("Journal Entry", je, force=1, ignore_permissions=True)
                deleted += 1
            except Exception:
                pass
        for bs in frappe.get_all("Beneficiary Service", pluck="name"):
            try:
                doc = frappe.get_doc("Beneficiary Service", bs)
                if doc.docstatus == 1:
                    doc.cancel()
                frappe.delete_doc("Beneficiary Service", bs, force=1, ignore_permissions=True)
                deleted += 1
            except Exception:
                pass

        # 3. Beneficiary Assessments
        for ba in frappe.get_all("Beneficiary Assessment", pluck="name"):
            try:
                frappe.delete_doc("Beneficiary Assessment", ba, force=1, ignore_permissions=True)
                deleted += 1
            except Exception:
                pass

        # 4. Beneficiary Enrollments
        for be in frappe.get_all("Beneficiary Enrollment", pluck="name"):
            try:
                frappe.delete_doc("Beneficiary Enrollment", be, force=1, ignore_permissions=True)
                deleted += 1
            except Exception:
                pass

        # 5. Beneficiaries
        for b in frappe.get_all("Beneficiary", pluck="name"):
            try:
                frappe.delete_doc("Beneficiary", b, force=1, ignore_permissions=True)
                deleted += 1
            except Exception:
                pass

        # 6. Volunteer Attendance
        for va in frappe.get_all("Volunteer Attendance", pluck="name"):
            try:
                frappe.delete_doc("Volunteer Attendance", va, force=1, ignore_permissions=True)
                deleted += 1
            except Exception:
                pass

        # 7. Volunteer Shifts
        for vs in frappe.get_all("Volunteer Shift", pluck="name"):
            try:
                frappe.delete_doc("Volunteer Shift", vs, force=1, ignore_permissions=True)
                deleted += 1
            except Exception:
                pass

        # 8. Volunteer Assignments
        for vas in frappe.get_all("Volunteer Assignment", pluck="name"):
            try:
                frappe.delete_doc("Volunteer Assignment", vas, force=1, ignore_permissions=True)
                deleted += 1
            except Exception:
                pass

        # 9. Volunteer Opportunity Interests
        for voi in frappe.get_all("Volunteer Opportunity Interest", pluck="name"):
            try:
                frappe.delete_doc("Volunteer Opportunity Interest", voi, force=1, ignore_permissions=True)
                deleted += 1
            except Exception:
                pass

        # 10. Volunteer Opportunities
        for vo in frappe.get_all("Volunteer Opportunity", pluck="name"):
            try:
                frappe.delete_doc("Volunteer Opportunity", vo, force=1, ignore_permissions=True)
                deleted += 1
            except Exception:
                pass

        # 11. Volunteer Applications
        for vapp in frappe.get_all("Volunteer Application", pluck="name"):
            try:
                doc = frappe.get_doc("Volunteer Application", vapp)
                if doc.docstatus == 1:
                    doc.cancel()
                frappe.delete_doc("Volunteer Application", vapp, force=1, ignore_permissions=True)
                deleted += 1
            except Exception:
                pass

        # 12. Volunteers (Preserve VOL-00001)
        for v in frappe.get_all("Volunteer", pluck="name"):
            if v != "VOL-00001":
                try:
                    frappe.delete_doc("Volunteer", v, force=1, ignore_permissions=True)
                    deleted += 1
                except Exception:
                    pass

        # Payment Entries (Donor funding receipts)
        for pe in frappe.get_all("Payment Entry", filters={"custom_destination": "Donor"}, pluck="name"):
            try:
                frappe.db.delete("GL Entry", {"voucher_no": pe})
                doc = frappe.get_doc("Payment Entry", pe)
                if doc.docstatus == 1:
                    doc.cancel()
                frappe.delete_doc("Payment Entry", pe, force=1, ignore_permissions=True)
                deleted += 1
            except Exception:
                pass

        # 13. Budgets
        for bg in frappe.get_all("Budget", pluck="name"):
            try:
                doc = frappe.get_doc("Budget", bg)
                if doc.docstatus == 1:
                    doc.cancel()
                frappe.delete_doc("Budget", bg, force=1, ignore_permissions=True)
                deleted += 1
            except Exception:
                pass

        # 14. Donor Grants
        for dg in frappe.get_all("Donor Grant", pluck="name"):
            try:
                frappe.delete_doc("Donor Grant", dg, force=1, ignore_permissions=True)
                deleted += 1
            except Exception:
                pass

        # 15. Projects
        for p in frappe.get_all("Project", pluck="name"):
            try:
                frappe.delete_doc("Project", p, force=1, ignore_permissions=True)
                deleted += 1
            except Exception:
                pass

        # 16. Project Proposals
        for pp in frappe.get_all("Project Proposal", pluck="name"):
            try:
                doc = frappe.get_doc("Project Proposal", pp)
                if doc.docstatus == 1:
                    doc.cancel()
                frappe.delete_doc("Project Proposal", pp, force=1, ignore_permissions=True)
                deleted += 1
            except Exception:
                pass

        # 17. Service Types
        for st in frappe.get_all("Service Type", pluck="name"):
            try:
                frappe.delete_doc("Service Type", st, force=1, ignore_permissions=True)
                deleted += 1
            except Exception:
                pass

        # 18. Volunteer Skills
        for sk in frappe.get_all("Volunteer Skill", pluck="name"):
            try:
                frappe.delete_doc("Volunteer Skill", sk, force=1, ignore_permissions=True)
                deleted += 1
            except Exception:
                pass

        # 19. Suppliers (Donor) and child Cost Centers
        for sup in frappe.get_all("Supplier", filters={"supplier_type": "Donor"}, pluck="name"):
            try:
                cc_name = frappe.db.get_value("Cost Center", {"cost_center_name": sup})
                if cc_name:
                    frappe.delete_doc("Cost Center", cc_name, force=1, ignore_permissions=True)
                frappe.delete_doc("Supplier", sup, force=1, ignore_permissions=True)
                deleted += 1
            except Exception:
                pass

        # 20. Employees
        demo_emp_names = [f"{fn} {ln}" for fn, ln, _ in EMPLOYEE_ROLES]
        for emp in frappe.get_all("Employee", filters={"employee_name": ["in", demo_emp_names]}, pluck="name"):
            try:
                frappe.delete_doc("Employee", emp, force=1, ignore_permissions=True)
                deleted += 1
            except Exception:
                pass

        # 21. Demo Users
        for u in frappe.get_all("User", filters={"email": ["like", "%@example.com"]}, pluck="name"):
            try:
                frappe.delete_doc("User", u, force=1, ignore_permissions=True)
                deleted += 1
            except Exception:
                pass

        manifest.clear()
        frappe.db.commit()
        print(f"[SUCCESS] Complete reset finished! Total deleted/cleaned: {deleted}")
    finally:
        frappe.flags.mute_emails = orig_mute_emails
        frappe.flags.in_test = orig_in_test
        frappe.flags.in_test = orig_in_test


# ==============================================================================
# MAIN RUNNER & ENTRY POINTS
# ==============================================================================
def run(reset=0, dry_run=0, force=0, seed=42, skip_budgets=0, skip_journal_entries=0):
    """Entry point for bench execute."""
    reset = cint(reset)
    dry_run = cint(dry_run)
    force = cint(force)
    seed = cint(seed)
    skip_budgets = cint(skip_budgets)
    skip_journal_entries = cint(skip_journal_entries)

    # 1. Safety verification
    dev_mode = frappe.conf.get("developer_mode")
    if not dev_mode and not force:
        print("\n[ERROR] Site is not in developer_mode. Refusing to run unless force=1 is passed.")
        print("Hint: pass force=1 to override, or enable developer_mode in site_config.json.\n")
        return False

    if reset:
        reset_seeded_data()
        return True

    # 2. Execution under Administrator with muted emails and test flag to prevent Redis backlog
    frappe.set_user("Administrator")
    orig_mute_emails = getattr(frappe.flags, "mute_emails", False)
    orig_in_test = getattr(frappe.flags, "in_test", False)
    frappe.flags.mute_emails = True
    frappe.flags.in_test = True

    try:
        seeder = NGOSeeder(
            dry_run=bool(dry_run),
            force=bool(force),
            seed=seed,
            skip_budgets=bool(skip_budgets),
            skip_journal_entries=bool(skip_journal_entries)
        )

        print(f"\n{'='*60}")
        print(f"      STARTING NGO DEMO DATA SEEDING (Site: {frappe.local.site})")
        print(f"{'='*60}")

        seeder.resolve_environment()
        seeder.ensure_fiscal_years()
        seeder.seed_section_a()
        seeder.seed_section_b()
        seeder.seed_section_c()
        seeder.seed_section_d()

        if not dry_run:
            seeder.manifest.save()

        success, _ = seeder.verify()
        return success
    finally:
        frappe.flags.mute_emails = orig_mute_emails
        frappe.flags.in_test = orig_in_test


def main():
    """Entry point for direct CLI invocation."""
    parser = argparse.ArgumentParser(description="Seed Frappe NGO demo data on ERPNext.")
    parser.add_argument("site", help="Target Frappe site name (e.g. test.local)")
    parser.add_argument("--reset", action="store_true", help="Cancel and delete only seeded records from manifest")
    parser.add_argument("--dry-run", action="store_true", help="Simulate seeding plan without writing to DB")
    parser.add_argument("--force", action="store_true", help="Allow running on a site without developer_mode")
    parser.add_argument("--seed", type=int, default=42, help="Random seed (default 42)")
    parser.add_argument("--skip-budgets", action="store_true", help="Skip creating ERPNext Budget records")
    parser.add_argument("--skip-journal-entries", action="store_true", help="Skip creating Journal Entry records")

    args = parser.parse_args()

    # Initialize Frappe
    import frappe
    frappe.init(args.site)
    frappe.connect()

    try:
        run(
            reset=1 if args.reset else 0,
            dry_run=1 if args.dry_run else 0,
            force=1 if args.force else 0,
            seed=args.seed,
            skip_budgets=1 if args.skip_budgets else 0,
            skip_journal_entries=1 if args.skip_journal_entries else 0
        )
    finally:
        frappe.destroy()


if __name__ == "__main__":
    main()
