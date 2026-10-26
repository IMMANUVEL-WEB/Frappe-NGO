import { userResource } from "@/data/user";
import { createRouter, createWebHistory } from "vue-router";
import { session } from "./data/session";
import { donorApi } from "./donor_portal/api";

const routes = [
	// ==================== VOLUNTEER PORTAL ROUTES (UNTOUCHED) ====================
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
		name: "Apply",
		path: "/apply",
		component: () => import("@/pages/Apply.vue"),
	},
	{
		name: "Login",
		path: "/account/login",
		component: () => import("@/pages/Login.vue"),
	},

	// ==================== DONOR PORTAL ROUTES ====================
	{
		path: "/donor-portal",
		alias: ["/donor_portal", "/frontend/donor-portal", "/frontend/donor_portal"],
		component: () => import("@/donor_portal/layouts/DonorLayout.vue"),
		children: [
			{
				path: "",
				name: "DonorDashboard",
				component: () => import("@/donor_portal/pages/Dashboard.vue"),
			},
			{
				path: "grants",
				name: "DonorGrants",
				component: () => import("@/donor_portal/pages/Grants.vue"),
			},
			{
				path: "grants/:id",
				name: "DonorGrantDetail",
				component: () => import("@/donor_portal/pages/GrantDetail.vue"),
			},
			{
				path: "proposals",
				name: "DonorProposals",
				component: () => import("@/donor_portal/pages/Proposals.vue"),
			},
			{
				path: "fund-utilization",
				name: "DonorFundUtilization",
				component: () => import("@/donor_portal/pages/FundUtilization.vue"),
			},
			{
				path: "projects",
				name: "DonorProjects",
				component: () => import("@/donor_portal/pages/ProjectProgress.vue"),
			},
			{
				path: "impact",
				name: "DonorImpact",
				component: () => import("@/donor_portal/pages/BeneficiaryImpact.vue"),
			},
			{
				path: "documents",
				name: "DonorDocuments",
				component: () => import("@/donor_portal/pages/Documents.vue"),
			},
			{
				path: "profile",
				name: "DonorProfile",
				component: () => import("@/donor_portal/pages/Profile.vue"),
			},
		],
	},
	{
		path: "/donor_portal/:subpath(.*)*",
		redirect: (to) => {
			const sub = to.params.subpath;
			return sub ? `/donor-portal/${sub}` : "/donor-portal";
		},
	},
	{
		path: "/:catchAll(.*)*",
		redirect: (to) => {
			if (window.location.pathname.toLowerCase().includes("donor")) {
				return "/donor-portal";
			}
			return "/";
		},
	},
];

// Determine base history cleanly based on current URL
const pathname = window.location.pathname.toLowerCase();
const isDonorUrl = pathname.includes("donor");
const base = isDonorUrl ? "" : "/frontend";

const router = createRouter({
	history: createWebHistory(base),
	routes,
});

let cachedPortalRoute = null;

router.beforeEach(async (to, from, next) => {
	let isLoggedIn = session.isLoggedIn;
	try {
		await userResource.promise;
	} catch (error) {
		isLoggedIn = false;
	}

	const isDonorRoute = to.path.includes("donor");

	// Allow unauthenticated preview on donor portal routes so it never renders blank
	if (isDonorRoute) {
		next();
		return;
	}

	// If not logged in and accessing protected volunteer pages
	if (!isLoggedIn) {
		if (to.name !== "Login" && to.name !== "Apply") {
			next({ name: "Login" });
			return;
		}
		next();
		return;
	}

	// If user is logged in, resolve role-based redirect
	try {
		if (!cachedPortalRoute) {
			const res = await fetch("/api/method/ngo.api.donor_portal.auth.get_portal_route");
			const json = await res.json();
			cachedPortalRoute = json?.message;
		}

		if (cachedPortalRoute) {
			const isDonorUser = cachedPortalRoute.role === "Donor Liaison";
			const isSystemUser =
				cachedPortalRoute.is_admin || cachedPortalRoute.role === "System User";

			// If on Login page, redirect to appropriate destination
			if (to.name === "Login") {
				if (isDonorUser && !isSystemUser) {
					window.location.href = "/donor-portal";
					return;
				}
				if (isSystemUser) {
					window.location.href = "/app";
					return;
				}
				next({ name: "Dashboard" });
				return;
			}

			// If a Donor Liaison visits volunteer portal pages (e.g. "/" or "/assignments"), immediately redirect to donor portal
			if (!isDonorRoute && isDonorUser && !isSystemUser && to.name !== "Apply") {
				window.location.href = "/donor-portal";
				return;
			}
		}
	} catch (e) {
		console.warn("Cross-portal guard error:", e);
	}

	next();
});

export default router;
