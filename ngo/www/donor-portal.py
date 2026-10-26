import frappe
from frappe.sessions import get_csrf_token


def get_context(context):
	context.no_cache = 1
	try:
		csrf_token = get_csrf_token()
	except Exception:
		csrf_token = getattr(getattr(frappe, "session", None), "data", {}).get("csrf_token", "")

	context.csrf_token = csrf_token
	context.boot = {
		"csrf_token": csrf_token,
		"site_name": frappe.local.site,
		"user": frappe.session.user if getattr(frappe, "session", None) else "Guest",
		"read_only_mode": frappe.flags.read_only,
	}
	return context
