export async function get(method) {
	const response = await fetch(`/api/method/${method}`, {
		method: "GET",
		headers: {
			Accept: "application/json",
		},
	})
	if (response.status === 401 || response.status === 403) {
		const data = await response.json().catch(() => ({}))
		throw data
	}
	const data = await response.json()
	if (data.exc) {
		throw data
	}
	return data.message
}

// Donor Portal API Client
export async function call(method, params = {}) {
	const headers = {
		"Content-Type": "application/json",
		Accept: "application/json",
	}

	// Add CSRF token from window.csrf_token if present
	if (window.csrf_token && window.csrf_token !== "None") {
		headers["X-Frappe-CSRF-Token"] = window.csrf_token
	}

	const response = await fetch(`/api/method/${method}`, {
		method: "POST",
		headers,
		body: JSON.stringify(params),
	})

	if (response.status === 401 || response.status === 403) {
		const data = await response.json().catch(() => ({}))
		if (data.exc_type === "PermissionError" || response.status === 401) {
			console.warn("Unauthorized / Permission Error on:", method)
		}
		throw data
	}

	const data = await response.json()
	if (data.exc) {
		console.error("API Error on", method, data.exc)
		throw data
	}
	return data.message
}

export const donorApi = {
	getRoute: () => get("ngo.api.donor_portal.auth.get_portal_route"),
	getDashboard: () => call("ngo.api.donor_portal.dashboard.get_dashboard"),
	getGrants: () => call("ngo.api.donor_portal.grants.get_grants"),
	getGrantDetail: (grant) =>
		call("ngo.api.donor_portal.grants.get_grant_detail", { grant }),
	getSpendBreakdown: (params) =>
		call("ngo.api.donor_portal.finance.get_spend_breakdown", params),
	getTransactions: (params) =>
		call("ngo.api.donor_portal.finance.get_transactions", params),
	getProjects: () => call("ngo.api.donor_portal.projects.get_projects"),
	getProposals: () => call("ngo.api.donor_portal.projects.get_proposals"),
	getProjectDetail: (project) =>
		call("ngo.api.donor_portal.projects.get_project_detail", { project }),
	approveProposal: (proposal) =>
		call("ngo.api.donor_portal.projects.approve_proposal", { proposal }),
	rejectProposal: (proposal, reason) =>
		call("ngo.api.donor_portal.projects.reject_proposal", { proposal, reason }),
	getImpact: (params) => call("ngo.api.donor_portal.impact.get_impact", params),
	getProcurement: (params) =>
		call("ngo.api.donor_portal.procurement.get_procurement", params),
	getDocuments: (params) =>
		call("ngo.api.donor_portal.documents.get_documents", params),
	getNotifications: () =>
		call("ngo.api.donor_portal.notifications.get_notifications"),
	submitQuery: (params) =>
		call("ngo.api.donor_portal.notifications.submit_query", params),
	getProfile: () => call("ngo.api.donor_portal.notifications.get_profile"),
}
