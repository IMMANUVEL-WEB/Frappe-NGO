import router from "@/router"
import { createResource } from "frappe-ui"

export const userResource = createResource({
	url: "frappe.auth.get_logged_user",
	method: "GET",
	cache: "User",
	onError(error) {
		if (error && error.exc_type === "AuthenticationError") {
			router.push({ name: "LoginPage" })
		}
	},
})
