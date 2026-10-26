import router from "@/router";
import { createResource } from "frappe-ui";
import { computed, reactive } from "vue";

import { userResource } from "./user";

export function sessionUser() {
	const cookies = new URLSearchParams(document.cookie.split("; ").join("&"));
	let _sessionUser = cookies.get("user_id");
	if (_sessionUser === "Guest") {
		_sessionUser = null;
	}
	return _sessionUser;
}

export const session = reactive({
	login: createResource({
		url: "login",
		makeParams({ email, password }) {
			return {
				usr: email,
				pwd: password,
			};
		},
		async onSuccess(data) {
			userResource.reload();
			session.user = sessionUser();
			session.login.reset();

			// Check home_page directly from login response
			let destination = data?.home_page;
			if (destination) {
				if (destination.startsWith("/")) destination = destination.slice(1);
				if (destination === "donor-portal" || destination === "donor_portal") {
					window.location.href = "/donor-portal";
					return;
				}
				if (destination === "desk" || destination === "app") {
					window.location.href = "/app";
					return;
				}
			}

			// Role-based destination redirect via GET (CSRF-safe)
			try {
				const res = await fetch("/api/method/ngo.api.donor_portal.auth.get_portal_route");
				const json = await res.json();
				const route = json?.message?.route;
				if (route) {
					if (route.includes("donor")) {
						window.location.href = "/donor-portal";
						return;
					}
					if (route === "/app") {
						window.location.href = "/app";
						return;
					}
				}
			} catch (e) {
				console.warn("Could not determine role redirect:", e);
			}

			router.replace("/");
		},
	}),
	logout: createResource({
		url: "logout",
		onSuccess() {
			userResource.reset();
			session.user = sessionUser();
			router.replace({ name: "Login" });
		},
	}),
	user: sessionUser(),
	isLoggedIn: computed(() => !!session.user),
});
