import frappe
from frappe import _

def get_donor_portal_role():
	try:
		role = frappe.db.get_single_value("NGO Settings", "donor_portal_role")
		return role or "Donor Liaison"
	except Exception:
		return "Donor Liaison"

def get_current_donor(allow_admin_preview=True):
	"""
	Derives the linked Supplier (Donor) strictly from the authenticated session.
	Returns supplier_name string or throws PermissionError.
	"""
	user = frappe.session.user
	if not user or user == "Guest":
		frappe.throw(_("Please log in to access the Donor Portal."), frappe.PermissionError)

	portal_role = get_donor_portal_role()
	roles = frappe.get_roles(user)
	is_system_user = frappe.db.get_value("User", user, "user_type") == "System User"

	# 1. Resolve Donor Supplier from Supplier's portal_users child table
	donor = frappe.db.get_value(
		"Portal User",
		{"parenttype": "Supplier", "user": user},
		"parent"
	)

	# 2. Fallback: check custom Donor Portal User doctype if present
	if not donor and frappe.db.table_exists("Donor Portal User"):
		donor = frappe.db.get_value("Donor Portal User", {"user": user, "enabled": 1}, "donor")

	if donor:
		# Verify supplier is Donor
		supplier_type = frappe.db.get_value("Supplier", donor, "supplier_type")
		if supplier_type != "Donor":
			frappe.throw(_("The linked organisation is not registered as a Donor."), frappe.PermissionError)
		return donor

	# If user is a System User / Administrator accessing portal for preview
	if is_system_user or "System Manager" in roles:
		if allow_admin_preview:
			# Return the first available active donor for preview purposes
			active_donor = frappe.db.get_value("Supplier", {"supplier_type": "Donor"}, "name")
			if active_donor:
				return active_donor
		frappe.throw(_("Admin user has no linked Donor organisation for live operations."), frappe.PermissionError)

	frappe.throw(_("Access Denied: No active Donor organisation linked to account {0}.").format(user), frappe.PermissionError)

@frappe.whitelist(allow_guest=True, methods=["GET", "POST"])
def get_portal_route():
	"""
	Whitelisted endpoint to resolve user destination and role status.
	Precedence:
	1. Donor Liaison (with linked donor or non-desk-admin) -> /donor-portal
	2. System User -> /app (Frappe Desk)
	3. Volunteer -> /frontend
	4. Else -> /
	"""
	user = frappe.session.user
	if not user or user == "Guest":
		return {"route": "/frontend/account/login", "role": "Guest"}

	user_type = frappe.db.get_value("User", user, "user_type")
	roles = frappe.get_roles(user)
	portal_role = get_donor_portal_role()

	has_donor_role = portal_role in roles
	donor = None
	if has_donor_role:
		try:
			donor = get_current_donor(allow_admin_preview=False)
		except Exception:
			pass

	# 1. Donor Liaison with linked donor or donor role takes precedence
	if has_donor_role and (donor or "System Manager" not in roles):
		return {
			"route": "/donor-portal",
			"role": portal_role,
			"donor": donor
		}

	# 2. System User -> Frappe Desk
	if user_type == "System User":
		preview_donor = None
		try:
			preview_donor = get_current_donor(allow_admin_preview=True)
		except Exception:
			pass
		return {
			"route": "/app",
			"role": "System User",
			"is_admin": True,
			"admin_donor_preview": preview_donor,
			"allow_donor_portal": True
		}

	# 3. Volunteer -> /frontend
	if "Volunteer" in roles or "Volunteer Coordinator" in roles:
		return {
			"route": "/frontend",
			"role": "Volunteer"
		}

	# 4. Fallback
	return {
		"route": "/",
		"role": "Website User"
	}

def get_website_user_home_page(user):
	"""
	Home page redirect hook called by Frappe on login.
	Source of truth for role-based redirects.
	"""
	if not user or user == "Guest":
		return None

	user_type = frappe.db.get_value("User", user, "user_type")
	roles = frappe.get_roles(user)
	portal_role = get_donor_portal_role()

	has_donor_role = portal_role in roles
	donor = None
	if has_donor_role:
		donor = frappe.db.get_value("Portal User", {"parenttype": "Supplier", "user": user}, "parent")
		if not donor and frappe.db.table_exists("Donor Portal User"):
			donor = frappe.db.get_value("Donor Portal User", {"user": user, "enabled": 1}, "donor")

	# 1. Donor Liaison with linked donor or donor role
	if has_donor_role and (donor or "System Manager" not in roles):
		return "/donor-portal"

	# 2. System User -> desk
	if user_type == "System User":
		return "desk"

	# 3. Volunteer -> /frontend
	if "Volunteer" in roles or "Volunteer Coordinator" in roles:
		return "/frontend"

	return None

# =========================================================================
# Frappe Permission Hooks (to guarantee zero /api/resource cross-tenant leaks)
# =========================================================================

def get_donor_grant_query_conditions(user):
	if not user:
		user = frappe.session.user
	if user == "Administrator" or frappe.db.get_value("User", user, "user_type") == "System User":
		return ""

	donor = frappe.db.get_value("Portal User", {"parenttype": "Supplier", "user": user}, "parent")
	if not donor and frappe.db.table_exists("Donor Portal User"):
		donor = frappe.db.get_value("Donor Portal User", {"user": user, "enabled": 1}, "donor")

	if donor:
		return f"`tabDonor Grant`.donor_name = {frappe.db.escape(donor)} AND `tabDonor Grant`.status = 'Active'"
	return "1=2"

def get_project_proposal_query_conditions(user):
	if not user:
		user = frappe.session.user
	if user == "Administrator" or frappe.db.get_value("User", user, "user_type") == "System User":
		return ""

	donor = frappe.db.get_value("Portal User", {"parenttype": "Supplier", "user": user}, "parent")
	if not donor and frappe.db.table_exists("Donor Portal User"):
		donor = frappe.db.get_value("Donor Portal User", {"user": user, "enabled": 1}, "donor")

	if donor:
		return f"`tabProject Proposal`.donor_profile = {frappe.db.escape(donor)} AND `tabProject Proposal`.docstatus = 1"
	return "1=2"

def has_donor_grant_permission(doc, user=None, permission_type=None):
	if not user:
		user = frappe.session.user
	if user == "Administrator" or frappe.db.get_value("User", user, "user_type") == "System User":
		return True

	donor = frappe.db.get_value("Portal User", {"parenttype": "Supplier", "user": user}, "parent")
	if not donor and frappe.db.table_exists("Donor Portal User"):
		donor = frappe.db.get_value("Donor Portal User", {"user": user, "enabled": 1}, "donor")

	return bool(donor and doc.donor_name == donor and doc.status == "Active")

def has_project_proposal_permission(doc, user=None, permission_type=None):
	if not user:
		user = frappe.session.user
	if user == "Administrator" or frappe.db.get_value("User", user, "user_type") == "System User":
		return True

	donor = frappe.db.get_value("Portal User", {"parenttype": "Supplier", "user": user}, "parent")
	if not donor and frappe.db.table_exists("Donor Portal User"):
		donor = frappe.db.get_value("Donor Portal User", {"user": user, "enabled": 1}, "donor")

	return bool(donor and doc.donor_profile == donor and doc.docstatus == 1)
