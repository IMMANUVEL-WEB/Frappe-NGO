import frappe
from frappe import _
from frappe.utils import flt
from collections import defaultdict
from ngo.api.donor_portal.auth import get_current_donor

@frappe.whitelist()
def get_impact(project=None):
	"""
	Returns strictly anonymized aggregates for beneficiaries, services, and district coordinates.
	NEVER returns beneficiary names, phone numbers, IDs or exact personal addresses.
	"""
	donor = get_current_donor(allow_admin_preview=True)

	grant_filters = {"donor_name": donor}
	if project:
		grant_filters["linked_project"] = project
	grants = frappe.get_all("Donor Grant", filters=grant_filters, fields=["linked_project"])
	projects = list(set([g.linked_project for g in grants if g.linked_project]))

	if project and project not in projects:
		# Check if donor is custom_donor on project
		if frappe.db.get_value("Project", project, "custom_donor") == donor:
			projects.append(project)

	if not projects:
		return {
			"total_beneficiaries": 0,
			"services_delivered": 0,
			"by_service_type": [],
			"by_district": [],
			"aid_items": [],
			"geojson": {"type": "FeatureCollection", "features": []}
		}

	# 1. Total distinct beneficiaries served
	ben_count_res = frappe.db.sql("""
		SELECT COUNT(DISTINCT beneficiary) as total, COUNT(*) as services_count
		FROM `tabBeneficiary Service`
		WHERE project IN %(projects)s AND docstatus = 1
	""", {"projects": tuple(projects)}, as_dict=True)
	total_beneficiaries = ben_count_res[0].total if ben_count_res else 0
	services_count = ben_count_res[0].services_count if ben_count_res else 0

	# 2. Aggregates by Service Type
	by_service = frappe.db.sql("""
		SELECT service_type, COUNT(*) as count, SUM(qty) as total_qty, SUM(amount) as total_amount
		FROM `tabBeneficiary Service`
		WHERE project IN %(projects)s AND docstatus = 1
		GROUP BY service_type
		ORDER BY count DESC
	""", {"projects": tuple(projects)}, as_dict=True)

	# 3. Location aggregates (Coarse District/Territory level from Beneficiary Enrollment)
	by_district = frappe.db.sql("""
		SELECT be.territory, COUNT(DISTINCT bs.beneficiary) as beneficiary_count
		FROM `tabBeneficiary Service` bs
		JOIN `tabBeneficiary Enrollment` be ON be.name = bs.enrollment
		WHERE bs.project IN %(projects)s AND bs.docstatus = 1
		GROUP BY be.territory
	""", {"projects": tuple(projects)}, as_dict=True)

	# Coarse Centroids for Indian territories (District/State level)
	COARSE_COORDINATES = {
		"Bihar": [85.1376, 25.5941],
		"Patna": [85.1376, 25.5941],
		"Gaya": [85.0002, 24.7955],
		"Assam": [92.9376, 26.2006],
		"Guwahati": [91.7362, 26.1445],
		"Odisha": [85.8245, 20.2961],
		"Puri": [85.8312, 19.8135],
		"Tamil Nadu": [80.2707, 13.0827],
		"Madurai": [78.1198, 9.9252],
		"Chennai": [80.2707, 13.0827],
		"Maharashtra": [73.8567, 18.5204],
		"India": [78.9629, 20.5937]
	}

	features = []
	for d in by_district:
		t_name = d.territory or "India"
		coords = COARSE_COORDINATES.get(t_name, [78.9629, 20.5937])
		features.append({
			"type": "Feature",
			"geometry": {
				"type": "Point",
				"coordinates": coords
			},
			"properties": {
				"district": t_name,
				"beneficiaries": d.beneficiary_count
			}
		})

	# If no specific territory data, add a general centroid
	if not features and total_beneficiaries > 0:
		features.append({
			"type": "Feature",
			"geometry": {"type": "Point", "coordinates": [85.1376, 25.5941]},
			"properties": {"district": "Project Region", "beneficiaries": total_beneficiaries}
		})

	# 4. Aid items distributed
	aid_items = []
	for s in by_service:
		aid_items.append({
			"service_type": s.service_type,
			"units": flt(s.total_qty) or flt(s.count),
			"amount": flt(s.total_amount)
		})

	return {
		"total_beneficiaries": total_beneficiaries,
		"services_delivered": services_count,
		"by_service_type": by_service,
		"by_district": by_district,
		"aid_items": aid_items,
		"geojson": {
			"type": "FeatureCollection",
			"features": features
		}
	}
