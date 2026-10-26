
import unittest

import frappe
from frappe.tests.utils import FrappeTestCase

from ngo.api.donor_portal.auth import (
    get_current_donor,
    get_portal_route,
    get_website_user_home_page,
    has_donor_grant_permission,
    has_project_proposal_permission,
)
from ngo.api.donor_portal.dashboard import get_dashboard
from ngo.api.donor_portal.finance import get_spend_breakdown, get_transactions
from ngo.api.donor_portal.grants import get_grant_detail, get_grants
from ngo.api.donor_portal.impact import get_impact
from ngo.api.donor_portal.projects import (
    approve_proposal,
    get_projects,
    reject_proposal,
)


class TestDonorPortal(FrappeTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        # --------------------------------------------------
        # 1. Resolve a valid Company for Project creation
        # --------------------------------------------------
        company = frappe.defaults.get_user_default("Company")

        if not company:
            companies = frappe.get_all(
                "Company",
                pluck="name",
                limit=1,
            )
            company = companies[0] if companies else None

        if not company:
            frappe.throw(
                "Donor portal tests require an existing Company. "
                "Create a Company before running these tests."
            )

        cls.company = company

        # --------------------------------------------------
        # 2. Create test donors
        # --------------------------------------------------
        cls.donor_a_name = "Test Donor Alpha Foundation"
        cls.donor_b_name = "Test Donor Beta Trust"

        for donor_name in (cls.donor_a_name, cls.donor_b_name):
            if not frappe.db.exists("Supplier", donor_name):
                supplier = frappe.new_doc("Supplier")
                supplier.supplier_name = donor_name
                supplier.supplier_group = "All Supplier Groups"
                supplier.supplier_type = "Donor"
                supplier.insert(ignore_permissions=True)

        # --------------------------------------------------
        # 3. Create donor portal users and link to donors
        # --------------------------------------------------
        cls.user_a = "donor_alpha@test.com"
        cls.user_b = "donor_beta@test.com"

        donor_users = [
            (cls.user_a, cls.donor_a_name),
            (cls.user_b, cls.donor_b_name),
        ]

        for user_email, donor_name in donor_users:
            if not frappe.db.exists("User", user_email):
                user = frappe.new_doc("User")
                user.email = user_email
                user.first_name = user_email.split("@")[0]
                user.user_type = "Website User"
                user.send_welcome_email = 0
                user.insert(ignore_permissions=True)

            user_doc = frappe.get_doc("User", user_email)
            if not user_doc.has_role("Donor Liaison"):
                user_doc.add_roles("Donor Liaison")

            if not frappe.db.exists(
                "Portal User",
                {"parent": donor_name, "user": user_email},
            ):
                supplier = frappe.get_doc("Supplier", donor_name)
                supplier.append(
                    "portal_users",
                    {"user": user_email},
                )
                supplier.save(ignore_permissions=True)

        # --------------------------------------------------
        # 4. Create a volunteer test user
        # --------------------------------------------------
        cls.vol_user = "volunteer_tester@test.com"

        if not frappe.db.exists("User", cls.vol_user):
            user = frappe.new_doc("User")
            user.email = cls.vol_user
            user.first_name = "Volunteer"
            user.user_type = "Website User"
            user.send_welcome_email = 0
            user.insert(ignore_permissions=True)

        volunteer = frappe.get_doc("User", cls.vol_user)
        if not volunteer.has_role("Volunteer"):
            volunteer.add_roles("Volunteer")

        # --------------------------------------------------
        # 5. Create separate projects for each donor
        # --------------------------------------------------
        cls.proj_a = "PROJ-ALPHA-TEST"
        cls.proj_b = "PROJ-BETA-TEST"

        existing_p_a = frappe.db.get_value(
            "Project",
            {"project_name": cls.proj_a},
            "name",
        )

        if existing_p_a:
            cls.proj_a_docname = existing_p_a
        else:
            project = frappe.new_doc("Project")
            project.project_name = cls.proj_a
            project.company = cls.company
            project.custom_donor = cls.donor_a_name
            project.insert(ignore_permissions=True)
            cls.proj_a_docname = project.name

        existing_p_b = frappe.db.get_value(
            "Project",
            {"project_name": cls.proj_b},
            "name",
        )

        if existing_p_b:
            cls.proj_b_docname = existing_p_b
        else:
            project = frappe.new_doc("Project")
            project.project_name = cls.proj_b
            project.company = cls.company
            project.custom_donor = cls.donor_b_name
            project.insert(ignore_permissions=True)
            cls.proj_b_docname = project.name

        # --------------------------------------------------
        # 6. Create a test grant for Donor A
        # --------------------------------------------------
        cls.grant_a1 = "DG-TEST-ALPHA-01"

        existing_grant_a = frappe.db.get_value(
            "Donor Grant",
            {"grant_id": cls.grant_a1},
            "name",
        )

        if existing_grant_a:
            cls.grant_a_docname = existing_grant_a
        else:
            grant = frappe.new_doc("Donor Grant")
            grant.grant_id = cls.grant_a1
            grant.grant_title = "Alpha Education Support 2026"
            grant.donor_name = cls.donor_a_name
            grant.linked_project = cls.proj_a_docname
            grant.total_amount = 5000000.0
            grant.status = "Active"
            grant.currency = "INR"
            grant.insert(ignore_permissions=True)
            cls.grant_a_docname = grant.name

        # --------------------------------------------------
        # 7. Create a test grant for Donor B
        # --------------------------------------------------
        cls.grant_b1 = "DG-TEST-BETA-01"

        existing_grant_b = frappe.db.get_value(
            "Donor Grant",
            {"grant_id": cls.grant_b1},
            "name",
        )

        if existing_grant_b:
            cls.grant_b_docname = existing_grant_b
        else:
            grant = frappe.new_doc("Donor Grant")
            grant.grant_id = cls.grant_b1
            grant.grant_title = "Beta Healthcare Grant 2026"
            grant.donor_name = cls.donor_b_name
            grant.linked_project = cls.proj_b_docname
            grant.total_amount = 3000000.0
            grant.status = "Active"
            grant.currency = "INR"
            grant.insert(ignore_permissions=True)
            cls.grant_b_docname = grant.name

        frappe.db.commit()

    # Keep your existing test methods below this line.
