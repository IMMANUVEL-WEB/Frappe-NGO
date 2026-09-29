import frappe
from frappe.utils import today, add_days, date_diff, getdate
from frappe.utils.user import get_users_with_role

def compliance_doc_expiry_alert():
	today_date = getdate(today())
	expiring_docs = frappe.db.sql("""
		SELECT
			cd.name            AS row_name,
			cd.parent          AS project,
			cd.document_type,
			cd.document_title,
			cd.reference_number,
			cd.expiry_date,
			cd.doc_status,
			p.project_name,
			p.custom_project_code AS project_code
		FROM
			`tabCompliance Doc` cd
		JOIN
			`tabProject` p ON p.name = cd.parent
		WHERE
			cd.doc_status NOT IN ('Expired', 'Cancelled')
			AND cd.expiry_date IS NOT NULL
			AND cd.expiry_date <= %(sixty_days)s
			AND p.custom_project_phase NOT IN ('Closed')
		ORDER BY
			cd.expiry_date ASC
	""", {
		"sixty_days": add_days(today_date, 60)
	}, as_dict=True)

	if not expiring_docs:
		return

	projects = {}
	for row in expiring_docs:
		days_left = date_diff(row.expiry_date, today_date)
		row["days_left"] = days_left
		if days_left <= 0:
			row["urgency"] = "EXPIRED"
		elif days_left <= 30:
			row["urgency"] = "URGENT"
		else:
			row["urgency"] = "WARNING"

		proj_key = row.project
		if proj_key not in projects:
			projects[proj_key] = {
				"project_name": row.project_name,
				"project_code": row.project_code or row.project,
				"docs": []
			}
		projects[proj_key]["docs"].append(row)

	admin_users = get_users_with_role("Projects Manager") or get_users_with_role("System Manager")
	finance_users = get_users_with_role("Finance Manager") or get_users_with_role("Accounts Manager")

	for proj_key, proj in projects.items():
		urgencies = [d["urgency"] for d in proj["docs"]]
		top_urgency = "EXPIRED" if "EXPIRED" in urgencies else "URGENT" if "URGENT" in urgencies else "WARNING"

		recipients = list(set(admin_users + (finance_users if top_urgency in ["URGENT", "EXPIRED"] else [])))
		if not recipients:
			continue

		prefix_map = {
			"WARNING": "[60-Day Warning]",
			"URGENT": "[30-Day URGENT]",
			"EXPIRED": "[EXPIRED]"
		}
		subject = f"{prefix_map[top_urgency]} Compliance documents expiring — {proj['project_code']} {proj['project_name']}"

		rows_html = ""
		for d in proj["docs"]:
			colour = "#A32D2D" if d["urgency"] == "EXPIRED" else "#854F0B" if d["urgency"] == "URGENT" else "#3B6D11"
			days_txt = "EXPIRED" if d["days_left"] <= 0 else f"{d['days_left']} days left"
			rows_html += f"""
			<tr>
			  <td style='padding:6px 10px;border-bottom:1px solid #eee'>{d['document_type']}</td>
			  <td style='padding:6px 10px;border-bottom:1px solid #eee'>{d['document_title']}</td>
			  <td style='padding:6px 10px;border-bottom:1px solid #eee'>{d.get('reference_number') or '—'}</td>
			  <td style='padding:6px 10px;border-bottom:1px solid #eee'>{frappe.utils.formatdate(d['expiry_date'])}</td>
			  <td style='padding:6px 10px;border-bottom:1px solid #eee;color:{colour};font-weight:500'>{days_txt}</td>
			</tr>"""

		message = f"""
		<p>Dear Team,</p>
		<p>The following compliance documents for project <strong>{proj['project_code']} — {proj['project_name']}</strong> require your attention:</p>
		<table style='border-collapse:collapse;width:100%;font-size:13px'>
		  <thead>
			<tr style='background:#f5f5f5'>
			  <th style='padding:8px 10px;text-align:left'>Type</th>
			  <th style='padding:8px 10px;text-align:left'>Document</th>
			  <th style='padding:8px 10px;text-align:left'>Reference</th>
			  <th style='padding:8px 10px;text-align:left'>Expiry Date</th>
			  <th style='padding:8px 10px;text-align:left'>Status</th>
			</tr>
		  </thead>
		  <tbody>{rows_html}</tbody>
		</table>
		<p style='margin-top:16px'>
		  Please initiate renewal immediately.<br>
		  <a href='{frappe.utils.get_url()}/app/project/{proj_key}'>Open project in ERPNext →</a>
		</p>
		<p style='color:#888;font-size:12px'>This is an automated alert from NGO App.</p>
		"""

		frappe.sendmail(
			recipients=recipients,
			subject=subject,
			message=message,
			delayed=False
		)

		for d in proj["docs"]:
			if d["days_left"] <= 0 and d["doc_status"] != "Expired":
				frappe.db.set_value("Compliance Doc", d["row_name"], "doc_status", "Expired", update_modified=False)
