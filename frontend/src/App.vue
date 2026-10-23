<template>
  <div>
    <router-view />
  </div>
</template>

<script setup>
import { createResource } from "frappe-ui"

const settings = createResource({
	url: "ngo.api.volunteer.get_portal_settings",
	method: "GET",
	auto: true,
	onError(err) {
		console.warn("Could not load portal settings:", err)
	},
	onSuccess(data) {
		if (data) {
			if (data.primary_color) {
				document.documentElement.style.setProperty(
					"--primary-color",
					data.primary_color,
				)
			}
			if (data.secondary_color) {
				document.documentElement.style.setProperty(
					"--secondary-color",
					data.secondary_color,
				)
			}
			if (data.login_color) {
				document.documentElement.style.setProperty(
					"--login-color",
					data.login_color,
				)
			}
			if (data.sidebar_color) {
				document.documentElement.style.setProperty(
					"--sidebar-color",
					data.sidebar_color,
				)
			}
		}
	},
})
</script>
