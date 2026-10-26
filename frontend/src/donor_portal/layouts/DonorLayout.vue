<template>
	<div
		class="min-h-screen bg-slate-50 flex flex-col md:flex-row font-sans text-slate-800 overflow-x-hidden"
	>
		<!-- Mobile Sidebar Backdrop -->
		<div
			v-if="isMobileMenuOpen"
			class="fixed inset-0 z-40 bg-slate-900/60 backdrop-blur-sm md:hidden"
			@click="isMobileMenuOpen = false"
		></div>

		<!-- Sidebar -->
		<aside
			:class="[
				'fixed md:static inset-y-0 left-0 z-50 w-64 bg-[#0d1b2a] text-slate-200 flex flex-col justify-between transition-transform duration-300 ease-in-out shadow-xl md:shadow-none',
				isMobileMenuOpen ? 'translate-x-0' : '-translate-x-full md:translate-x-0',
			]"
		>
			<div>
				<!-- Brand Header -->
				<div class="px-6 py-6 border-b border-slate-800/80 flex items-center space-x-3">
					<div
						class="w-10 h-10 rounded-xl bg-gradient-to-tr from-emerald-600 to-teal-400 flex items-center justify-center shadow-lg shadow-emerald-500/20 text-white font-bold text-xl"
					>
						<svg
							class="w-6 h-6"
							viewBox="0 0 24 24"
							fill="none"
							stroke="currentColor"
							stroke-width="2"
						>
							<path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5" />
						</svg>
					</div>
					<div>
						<div class="text-white font-bold text-lg tracking-tight">
							{{ portalSettings?.login_portal_title || "Donor Portal" }}
						</div>
						<div class="text-xs text-slate-400 font-medium">
							{{ portalSettings?.login_portal_subtitle || "Donor Impact" }}
						</div>
					</div>
				</div>

				<!-- Navigation Menu -->
				<nav class="px-4 py-6 space-y-1.5">
					<router-link
						to="/donor-portal"
						exact
						class="nav-link"
						:class="{ 'nav-link-active': $route.path === '/donor-portal' }"
						@click="isMobileMenuOpen = false"
					>
						<svg
							class="w-5 h-5 mr-3 shrink-0"
							fill="none"
							stroke="currentColor"
							viewBox="0 0 24 24"
						>
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								stroke-width="2"
								d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"
							/>
						</svg>
						<span class="flex-1">Dashboard</span>
					</router-link>

					<router-link
						to="/donor-portal/proposals"
						class="nav-link"
						:class="{
							'nav-link-active': $route.path.startsWith('/donor-portal/proposals'),
						}"
						@click="isMobileMenuOpen = false"
					>
						<svg
							class="w-5 h-5 mr-3 shrink-0"
							fill="none"
							stroke="currentColor"
							viewBox="0 0 24 24"
						>
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								stroke-width="2"
								d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"
							/>
						</svg>
						<span class="flex-1">Project Proposals</span>
						<span
							v-if="pendingProposalsCount > 0"
							class="px-2 py-0.5 text-xs font-bold rounded-full bg-rose-500 text-white"
						>
							{{ pendingProposalsCount }}
						</span>
					</router-link>

					<router-link
						to="/donor-portal/grants"
						class="nav-link"
						:class="{
							'nav-link-active': $route.path.startsWith('/donor-portal/grants'),
						}"
						@click="isMobileMenuOpen = false"
					>
						<svg
							class="w-5 h-5 mr-3 shrink-0"
							fill="none"
							stroke="currentColor"
							viewBox="0 0 24 24"
						>
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								stroke-width="2"
								d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"
							/>
						</svg>
						<span class="flex-1">My Grants</span>
					</router-link>

					<router-link
						to="/donor-portal/fund-utilization"
						class="nav-link"
						:class="{
							'nav-link-active': $route.path.startsWith(
								'/donor-portal/fund-utilization'
							),
						}"
						@click="isMobileMenuOpen = false"
					>
						<svg
							class="w-5 h-5 mr-3 shrink-0"
							fill="none"
							stroke="currentColor"
							viewBox="0 0 24 24"
						>
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								stroke-width="2"
								d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"
							/>
						</svg>
						<span class="flex-1">Fund Utilization</span>
					</router-link>

					<router-link
						to="/donor-portal/projects"
						class="nav-link"
						:class="{
							'nav-link-active': $route.path.startsWith('/donor-portal/projects'),
						}"
						@click="isMobileMenuOpen = false"
					>
						<svg
							class="w-5 h-5 mr-3 shrink-0"
							fill="none"
							stroke="currentColor"
							viewBox="0 0 24 24"
						>
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								stroke-width="2"
								d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"
							/>
						</svg>
						<span class="flex-1">Project Progress</span>
					</router-link>

					<router-link
						to="/donor-portal/impact"
						class="nav-link"
						:class="{
							'nav-link-active': $route.path.startsWith('/donor-portal/impact'),
						}"
						@click="isMobileMenuOpen = false"
					>
						<svg
							class="w-5 h-5 mr-3 shrink-0"
							fill="none"
							stroke="currentColor"
							viewBox="0 0 24 24"
						>
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								stroke-width="2"
								d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z"
							/>
						</svg>
						<span class="flex-1">Beneficiary & Impact</span>
					</router-link>

					<router-link
						to="/donor-portal/documents"
						class="nav-link"
						:class="{
							'nav-link-active': $route.path.startsWith('/donor-portal/documents'),
						}"
						@click="isMobileMenuOpen = false"
					>
						<svg
							class="w-5 h-5 mr-3 shrink-0"
							fill="none"
							stroke="currentColor"
							viewBox="0 0 24 24"
						>
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								stroke-width="2"
								d="M7 21h10a2 2 0 002-2V9.414a1 1 0 00-.293-.707l-5.414-5.414A1 1 0 0012.586 3H7a2 2 0 00-2 2v14a2 2 0 002 2z"
							/>
						</svg>
						<span class="flex-1">Documents</span>
					</router-link>

					<router-link
						to="/donor-portal/profile"
						class="nav-link"
						:class="{
							'nav-link-active': $route.path.startsWith('/donor-portal/profile'),
						}"
						@click="isMobileMenuOpen = false"
					>
						<svg
							class="w-5 h-5 mr-3 shrink-0"
							fill="none"
							stroke="currentColor"
							viewBox="0 0 24 24"
						>
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								stroke-width="2"
								d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"
							/>
						</svg>
						<span class="flex-1">Profile</span>
					</router-link>
				</nav>
			</div>

			<!-- Footer / Back to Desk (if admin) -->
			<div class="p-4 border-t border-slate-800/80 text-xs text-slate-400">
				<div v-if="isAdmin" class="mb-2">
					<a
						href="/app"
						class="flex items-center text-emerald-400 hover:text-emerald-300 font-medium"
					>
						<svg
							class="w-4 h-4 mr-1.5"
							fill="none"
							stroke="currentColor"
							viewBox="0 0 24 24"
						>
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								stroke-width="2"
								d="M11 19l-7-7 7-7m8 14l-7-7 7-7"
							/>
						</svg>
						Return to Desk
					</a>
				</div>
				<button
					type="button"
					@click="triggerLogout"
					class="flex items-center text-white hover:text-rose-300 font-medium pt-1.5 transition cursor-pointer"
				>
					<svg
						class="w-3.5 h-3.5 mr-1.5"
						fill="none"
						stroke="currentColor"
						viewBox="0 0 24 24"
					>
						<path
							stroke-linecap="round"
							stroke-linejoin="round"
							stroke-width="2"
							d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1"
						/>
					</svg>
					Log Out
				</button>
			</div>
		</aside>

		<!-- Main Content Wrapper -->
		<div class="flex-1 flex flex-col min-w-0 overflow-y-auto">
			<!-- Top Navbar -->
			<header
				class="bg-white border-b border-slate-200/80 px-4 md:px-8 py-4 flex items-center justify-between sticky top-0 z-30 shadow-xs"
			>
				<div class="flex items-center space-x-3">
					<!-- Mobile Hamburger -->
					<button
						type="button"
						class="p-2 rounded-lg text-slate-600 hover:bg-slate-100 md:hidden"
						@click="isMobileMenuOpen = !isMobileMenuOpen"
					>
						<svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								stroke-width="2"
								d="M4 6h16M4 12h16M4 18h16"
							/>
						</svg>
					</button>

					<div>
						<h1
							class="text-xl md:text-2xl font-bold text-slate-900 tracking-tight flex items-center gap-2"
						>
							{{ currentTitle }}
							<span
								v-if="isAdmin"
								class="text-xs px-2.5 py-0.5 rounded-full font-semibold bg-amber-100 text-amber-800 border border-amber-200"
							>
								Admin Preview Mode
							</span>
						</h1>
						<p class="text-xs md:text-sm text-slate-500 font-medium">
							Your support creates lasting change
						</p>
					</div>
				</div>

				<!-- Top Right Actions -->
				<div class="flex items-center space-x-3 md:space-x-5">
					<!-- Notifications dropdown button -->
					<div class="relative">
						<button
							type="button"
							class="relative p-2 text-slate-500 hover:text-slate-800 hover:bg-slate-100 rounded-full transition"
							@click="isNotificationOpen = !isNotificationOpen"
						>
							<svg
								class="w-6 h-6"
								fill="none"
								stroke="currentColor"
								viewBox="0 0 24 24"
							>
								<path
									stroke-linecap="round"
									stroke-linejoin="round"
									stroke-width="2"
									d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9"
								/>
							</svg>
							<span
								v-if="notifications.length > 0"
								class="absolute top-1 right-1 w-4 h-4 rounded-full bg-rose-500 text-white text-[10px] font-bold flex items-center justify-center"
							>
								{{ notifications.length }}
							</span>
						</button>

						<!-- Notification Dropdown Menu -->
						<div
							v-if="isNotificationOpen"
							class="absolute right-0 mt-2 w-80 bg-white rounded-xl shadow-xl border border-slate-200 py-2 z-50 animate-in fade-in slide-in-from-top-2 duration-150"
						>
							<div
								class="px-4 py-2 border-b border-slate-100 flex items-center justify-between"
							>
								<span class="font-bold text-sm text-slate-800">Notifications</span>
								<span class="text-xs text-slate-500"
									>{{ notifications.length }} new</span
								>
							</div>
							<div class="max-h-72 overflow-y-auto divide-y divide-slate-100">
								<div
									v-for="(n, idx) in notifications"
									:key="idx"
									class="p-3 hover:bg-slate-50 transition cursor-pointer text-xs"
								>
									<div class="font-semibold text-slate-800">{{ n.title }}</div>
									<div class="text-slate-600 mt-0.5">{{ n.message }}</div>
								</div>
								<div
									v-if="notifications.length === 0"
									class="p-4 text-center text-xs text-slate-400"
								>
									No pending alerts or notifications.
								</div>
							</div>
						</div>
					</div>

					<!-- User Logout -->
					<div class="flex items-center space-x-2 pl-2 border-l border-slate-200">
						<button
							type="button"
							@click="triggerLogout"
							class="flex items-center space-x-1.5 px-3 py-1.5 rounded-lg text-slate-700 hover:bg-slate-100 transition text-sm font-semibold"
						>
							<svg
								class="w-5 h-5 text-slate-500"
								fill="none"
								stroke="currentColor"
								viewBox="0 0 24 24"
							>
								<path
									stroke-linecap="round"
									stroke-linejoin="round"
									stroke-width="2"
									d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1"
								/>
							</svg>
							<span>Logout</span>
						</button>
					</div>
				</div>
			</header>

			<!-- Main Router View -->
			<main class="flex-1 p-4 md:p-8 overflow-x-hidden">
				<router-view />
			</main>

			<!-- Configurable Portal Footer -->
			<PortalFooter portalType="donor" />
		</div>
	</div>

	<!-- Logout Confirmation Modal Popup -->
	<teleport to="body">
		<transition
			enter-active-class="transition duration-200 ease-out"
			enter-from-class="opacity-0"
			enter-to-class="opacity-100"
			leave-active-class="transition duration-150 ease-in"
			leave-from-class="opacity-100"
			leave-to-class="opacity-0"
		>
			<div
				v-if="showLogoutModal"
				class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-900/60 backdrop-blur-xs"
				@click.self="cancelLogout"
			>
				<div
					class="bg-white rounded-2xl shadow-2xl border border-slate-100 max-w-sm w-full p-6 text-center transform transition-all animate-in fade-in zoom-in-95 duration-150"
					role="dialog"
					aria-modal="true"
				>
					<!-- Warning/Signout Icon -->
					<div
						class="w-14 h-14 mx-auto mb-4 rounded-full bg-rose-50 border border-rose-100 flex items-center justify-center text-rose-600"
					>
						<svg class="w-7 h-7" fill="none" stroke="currentColor" viewBox="0 0 24 24">
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								stroke-width="2"
								d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1"
							/>
						</svg>
					</div>

					<h3 class="text-lg font-bold text-slate-900 mb-1">Confirm Logout</h3>
					<p class="text-sm text-slate-500 mb-6 leading-relaxed">
						Are you sure you want to log out of the Donor Portal?
					</p>

					<div class="flex items-center gap-3">
						<button
							type="button"
							:disabled="loggingOut"
							@click="cancelLogout"
							class="flex-1 py-2.5 px-4 rounded-xl border border-slate-200 text-slate-700 font-semibold text-sm hover:bg-slate-50 active:bg-slate-100 transition disabled:opacity-50 cursor-pointer"
						>
							Cancel
						</button>
						<button
							type="button"
							:disabled="loggingOut"
							@click="confirmLogout"
							class="flex-1 py-2.5 px-4 rounded-xl bg-rose-600 hover:bg-rose-700 active:bg-rose-800 text-black font-semibold text-sm shadow-md shadow-rose-600/20 transition disabled:opacity-50 flex items-center justify-center gap-2 cursor-pointer"
						>
							<svg
								v-if="loggingOut"
								class="animate-spin h-4 w-4 text-white"
								xmlns="http://www.w3.org/2000/svg"
								fill="none"
								viewBox="0 0 24 24"
							>
								<circle
									class="opacity-25"
									cx="12"
									cy="12"
									r="10"
									stroke="currentColor"
									stroke-width="4"
								></circle>
								<path
									class="opacity-75"
									fill="currentColor"
									d="M4 12a8 8 0 018-8v8H4z"
								></path>
							</svg>
							<span>{{ loggingOut ? "Logging out..." : "Log Out" }}</span>
						</button>
					</div>
				</div>
			</div>
		</transition>
	</teleport>
</template>

<script setup>
import PortalFooter from "../../components/PortalFooter.vue";
import { computed, onMounted, ref } from "vue";
import { useRoute, useRouter } from "vue-router";
import { session } from "../../data/session";
import { donorApi } from "../api";

const route = useRoute();
const router = useRouter();

const portalSettings = ref({
	login_portal_title: "Donor Portal",
	login_portal_subtitle: "Donor Impact & Grants",
});
const isMobileMenuOpen = ref(false);
const showLogoutModal = ref(false);
const loggingOut = ref(false);

function triggerLogout() {
	showLogoutModal.value = true;
	isMobileMenuOpen.value = false;
}

function cancelLogout() {
	showLogoutModal.value = false;
}
const isNotificationOpen = ref(false);
const isAdmin = ref(false);
const pendingProposalsCount = ref(0);
const notifications = ref([]);

const currentTitle = computed(() => {
	if (route.path.includes("grants")) return "My Grants";
	if (route.path.includes("fund-utilization")) return "Fund Utilization";
	if (route.path.includes("projects")) return "Project Progress";
	if (route.path.includes("impact")) return "Beneficiary & Impact";
	if (route.path.includes("documents")) return "Documents & Compliance";
	if (route.path.includes("profile")) return "Donor Profile";
	if (route.path.includes("proposals")) return "Project Proposals";
	return "Dashboard";
});

onMounted(async () => {
	try {
		const sRes = await fetch("/api/method/ngo.api.volunteer.get_portal_settings");
		const sJson = await sRes.json();
		if (sJson?.message) {
			portalSettings.value = { ...portalSettings.value, ...sJson.message };
		}
	} catch (err) {
		// defaults already initialized
	}
	try {
		const routeInfo = await donorApi.getRoute();
		if (routeInfo && routeInfo.is_admin) {
			isAdmin.value = true;
		}
	} catch (e) {
		console.error("Error fetching route info:", e);
	}

	try {
		const notifs = await donorApi.getNotifications();
		if (notifs) {
			notifications.value = notifs;
		}
	} catch (e) {
		console.error("Error fetching notifications:", e);
	}

	try {
		const props = await donorApi.getProposals();
		if (Array.isArray(props)) {
			pendingProposalsCount.value = props.filter((p) => {
				const s = (p.status || "").toLowerCase().trim();
				return (
					s === "donor approval pending" ||
					s === "pending review" ||
					s === "pending" ||
					s === "under review" ||
					s === "draft"
				);
			}).length;
		}
	} catch (e) {
		console.error("Error fetching pending proposals count:", e);
	}
});

async function confirmLogout() {
	loggingOut.value = true;
	try {
		if (session?.logout?.submit) {
			await session.logout.submit();
		}
	} catch (e) {
		console.warn("Session logout submit warning:", e);
	}

	try {
		const headers = { "Content-Type": "application/json" };
		if (window.csrf_token && window.csrf_token !== "None") {
			headers["X-Frappe-CSRF-Token"] = window.csrf_token;
		}
		await fetch("/api/method/logout", { method: "POST", headers });
	} catch (e) {
		console.warn("Direct logout fetch warning:", e);
	}

	// Clear local cookies explicitly
	document.cookie = "user_id=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
	document.cookie = "sid=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
	document.cookie = "system_user=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
	document.cookie = "full_name=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";

	window.location.href = "/frontend/account/login";
}
</script>

<style scoped>
.nav-link {
	display: flex;
	align-items: center;
	padding: 0.65rem 0.95rem;
	border-radius: 0.65rem;
	font-size: 0.875rem;
	font-weight: 500;
	color: #94a3b8;
	transition: all 0.15s ease-in-out;
}

.nav-link:hover {
	background-color: rgba(255, 255, 255, 0.06);
	color: #ffffff;
}

.nav-link-active {
	background-color: #059669 !important;
	color: #ffffff !important;
	box-shadow: 0 4px 12px rgba(5, 150, 105, 0.25);
	font-weight: 600;
}
</style>
