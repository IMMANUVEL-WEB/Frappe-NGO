import { userResource } from "@/data/user"
import { createRouter, createWebHistory } from "vue-router"
import { session } from "./data/session"

const routes = [
	{
		path: "/opportunities",
		name: "Opportunities",
		component: () => import("@/pages/Opportunities.vue"),
	},
	{
		path: "/profile",
		name: "Profile",
		component: () => import("@/pages/Profile.vue"),
	},
	{
		path: "/attendance",
		name: "Attendance",
		component: () => import("@/pages/Attendance.vue"),
	},
	{
		path: "/shifts",
		name: "Shifts",
		component: () => import("@/pages/Shifts.vue"),
	},
	{
		path: "/assignments",
		name: "Assignments",
		component: () => import("@/pages/Assignments.vue"),
	},
	{
		path: "/",
		name: "Dashboard",
		component: () => import("@/pages/Dashboard.vue"),
	},
	{
		name: "Login",
		path: "/account/login",
		component: () => import("@/pages/Login.vue"),
	},
]

const router = createRouter({
	history: createWebHistory("/frontend"),
	routes,
})

router.beforeEach(async (to, from, next) => {
	let isLoggedIn = session.isLoggedIn
	try {
		await userResource.promise
	} catch (error) {
		isLoggedIn = false
	}

	if (to.name === "Login" && isLoggedIn) {
		next({ name: "Dashboard" })
	} else if (to.name !== "Login" && !isLoggedIn) {
		next({ name: "Login" })
	} else {
		next()
	}
})

export default router
