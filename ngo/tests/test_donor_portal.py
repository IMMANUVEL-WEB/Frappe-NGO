import unittest
import frappe
from frappe.tests.utils import FrappeTestCase
from ngo.api.donor_portal.auth import (
	get_portal_route,
	get_website_user_home_page,
	get_current_donor,
	has_donor_grant_permission,
	has_project_proposal_permission
)
from ngo.api.donor_portal.dashboard import get_dashboard
from ngo.api.donor_portal.grants import get_grants, get_grant_detail
from ngo.api.donor_portal.finance import get_spend_breakdown, get_transactions
from ngo.api.donor_portal.impact import get_impact
from ngo.api.donor_portal.projects import get_projects, approve_proposal, reject_proposal

class TestDonorPortal(FrappeTestCase):
	@classmethod
	def setUpClass(cls):
		super().setUpClass()
		cls.donor_a_name = "Test Donor Alpha Foundation"
		cls.donor_b_name = "Test Donor Beta Trust"

		for dname in [cls.donor_a_name, cls.donor_b_name]:
			if not frappe.db.exists("Supplier", dname):
				s = frappe.new_doc("Supplier")
				s.supplier_name = dname
				s.supplier_group = "All Supplier Groups"
				s.supplier_type = "Donor"
				s.insert(ignore_permissions=True)

		cls.user_a = "donor_alpha@test.com"
		cls.user_b = "donor_beta@test.com"

		for u_email, dname in [(cls.user_a, cls.donor_a_name), (cls.user_b, cls.donor_b_name)]:
			if not frappe.db.exists("User", u_email):
				u = frappe.new_doc("User")
				u.email = u_email
				u.first_name = u_email.split("@")[0]
				u.user_type = "Website User"
				u.send_welcome_email = 0
				u.insert(ignore_permissions=True)
				u.add_roles("Donor Liaison")

			if not frappe.db.exists("Portal User", {"parent": dname, "user": u_email}):
				supp = frappe.get_doc("Supplier", dname)
				supp.append("portal_users", {"user": u_email})
				supp.save(ignore_permissions=True)

		cls.vol_user = "volunteer_tester@test.com"
		if not frappe.db.exists("User", cls.vol_user):
			u = frappe.new_doc("User")
			u.email = cls.vol_user
			u.first_name = "Volunteer"
			u.user_type = "Website User"
			u.send_welcome_email = 0
			u.insert(ignore_permissions=True)
			u.add_roles("Volunteer")

		# Create distinct test projects for Alpha and Beta
		cls.proj_a = "PROJ-ALPHA-TEST"
		existing_p_a = frappe.db.get_value("Project", {"project_name": cls.proj_a}, "name")
		if not existing_p_a:
			p = frappe.new_doc("Project")
			p.project_name = cls.proj_a
			p.custom_donor = cls.donor_a_name
			p.insert(ignore_permissions=True)
			cls.proj_a_docname = p.name
		else:
			cls.proj_a_docname = existing_p_a

		cls.proj_b = "PROJ-BETA-TEST"
		existing_p_b = frappe.db.get_value("Project", {"project_name": cls.proj_b}, "name")
		if not existing_p_b:
			p = frappe.new_doc("Project")
			p.project_name = cls.proj_b
			p.custom_donor = cls.donor_b_name
			p.insert(ignore_permissions=True)
			cls.proj_b_docname = p.name
		else:
			cls.proj_b_docname = existing_p_b

		# Create Test Grants for Donor A
		cls.grant_a1 = "DG-TEST-ALPHA-01"
		if not frappe.db.exists("Donor Grant", {"grant_id": cls.grant_a1}):
			g = frappe.new_doc("Donor Grant")
			g.grant_id = cls.grant_a1
			g.grant_title = "Alpha Education Support 2026"
			g.donor_name = cls.donor_a_name
			g.linked_project = cls.proj_a_docname
			g.total_amount = 5000000.0
			g.status = "Active"
			g.currency = "INR"
			g.insert(ignore_permissions=True)
			cls.grant_a_docname = g.name
		else:
			cls.grant_a_docname = frappe.db.get_value("Donor Grant", {"grant_id": cls.grant_a1}, "name")

		# Create Test Grant for Donor B
		cls.grant_b1 = "DG-TEST-BETA-01"
		if not frappe.db.exists("Donor Grant", {"grant_id": cls.grant_b1}):
			g = frappe.new_doc("Donor Grant")
			g.grant_id = cls.grant_b1
			g.grant_title = "Beta Healthcare Grant 2026"
			g.donor_name = cls.donor_b_name
			g.linked_project = cls.proj_b_docname
			g.total_amount = 3000000.0
			g.status = "Active"
			g.currency = "INR"
			g.insert(ignore_permissions=True)
			cls.grant_b_docname = g.name
		else:
			cls.grant_b_docname = frappe.db.get_value("Donor Grant", {"grant_id": cls.grant_b1}, "name")

		frappe.db.commit()

	def test_01_role_based_redirect(self):
		"""Test Priority 1, 2, 3 role redirects"""
		# Priority 1: System User -> /app
		frappe.set_user("Administrator")
		self.assertEqual(get_website_user_home_page("Administrator"), "desk")
		route_admin = get_portal_route()
		self.assertEqual(route_admin["route"], "/app")

		# Priority 2: Donor Liaison -> /donor-portal
		frappe.set_user(self.user_a)
		self.assertEqual(get_website_user_home_page(self.user_a), "/donor-portal")
		route_donor = get_portal_route()
		self.assertEqual(route_donor["route"], "/donor-portal")

		# Priority 3: Volunteer -> /frontend
		frappe.set_user(self.vol_user)
		self.assertEqual(get_website_user_home_page(self.vol_user), "/frontend")
		route_vol = get_portal_route()
		self.assertEqual(route_vol["route"], "/frontend")

	def test_02_donor_data_isolation(self):
		"""Assert strict ownership isolation: Donor A cannot see Donor B data"""
		frappe.set_user(self.user_a)
		self.assertEqual(get_current_donor(), self.donor_a_name)

		# Fetch grants as Donor A
		grants_a = get_grants()
		grant_names_a = [g["name"] for g in grants_a]
		self.assertIn(self.grant_a_docname, grant_names_a)
		self.assertNotIn(self.grant_b_docname, grant_names_a)

		# Fetch grants as Donor B
		frappe.set_user(self.user_b)
		self.assertEqual(get_current_donor(), self.donor_b_name)
		grants_b = get_grants()
		grant_names_b = [g["name"] for g in grants_b]
		self.assertIn(self.grant_b_docname, grant_names_b)
		self.assertNotIn(self.grant_a_docname, grant_names_b)

	def test_03_cross_access_permission_error(self):
		"""Attempting to access Donor B grant as Donor A must throw PermissionError"""
		frappe.set_user(self.user_a)
		with self.assertRaises(frappe.PermissionError):
			get_grant_detail(self.grant_b_docname)

	def test_04_impact_pii_absence(self):
		"""get_impact must return aggregates only, no beneficiary names or phone numbers"""
		frappe.set_user(self.user_a)
		impact = get_impact()
		self.assertIn("total_beneficiaries", impact)
		self.assertIn("by_service_type", impact)
		self.assertIn("by_district", impact)

		# Ensure no sensitive PII fields are returned
		raw_json = frappe.as_json(impact)
		self.assertNotIn("phone", raw_json)
		self.assertNotIn("national_id", raw_json)
		self.assertNotIn("first_name", raw_json)
		self.assertNotIn("beneficiary_name", raw_json)
