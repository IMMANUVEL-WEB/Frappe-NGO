<template>
	<!-- Fixed full-viewport container with NO scrolling -->
	<div
		class="fixed inset-0 w-screen h-screen overflow-hidden bg-[#f8fafc] flex flex-col justify-between font-sans selection:bg-emerald-100 selection:text-emerald-900"
	>
		<!-- Top Navigation Header (Fixed at top) -->
		<header
			class="bg-white border-b border-black-100 px-6 lg:px-10 py-2.5 shrink-0 flex items-center justify-between shadow-[0_1px_3px_rgba(0,0,0,0.03)] z-20"
		>
			<!-- Brand Logo & Title -->
			<div class="flex items-center gap-2.5">
				<template v-if="settings.login_logo">
					<img :src="settings.login_logo" alt="Logo" class="h-8 w-auto object-contain" />
				</template>
				<template v-else>
					<div
						class="w-8 h-8 rounded-xl bg-[#064e3b] flex items-center justify-center text-white shadow-sm shrink-0"
					>
						<svg
							class="w-4 h-4"
							viewBox="0 0 24 24"
							fill="none"
							stroke="currentColor"
							stroke-width="2"
							stroke-linecap="round"
							stroke-linejoin="round"
						>
							<path d="M12 2v6" />
							<path d="M12 18v4" />
							<path d="M4.93 4.93l4.24 4.24" />
							<path d="M14.83 14.83l4.24 4.24" />
							<path d="M2 12h6" />
							<path d="M18 12h4" />
							<path d="M4.93 19.07l4.24-4.24" />
							<path d="M14.83 9.17l4.24-4.24" />
							<circle cx="12" cy="12" r="3" fill="currentColor" />
						</svg>
					</div>
				</template>
				<div>
					<div
						class="font-extrabold text-black-900 text-sm lg:text-[15px] tracking-tight leading-none"
					>
						{{ settings.login_portal_title || "Non Governmental Organisation" }}
					</div>
					<div
						class="font-bold text-[#047857] text-[8px] tracking-[0.25em] uppercase leading-none mt-1"
					>
						{{ settings.login_portal_subtitle || "IMPACTSPHERE" }}
					</div>
				</div>
			</div>
		</header>

		<!-- Main Content Area: Centered, fills remaining space with NO scroll -->
		<main
			class="flex-1 min-h-0 w-full max-w-4xl xl:max-w-[880px] mx-auto px-4 py-3 sm:py-4 flex items-center justify-center overflow-hidden"
		>
			<div
				class="w-full bg-white rounded-2xl lg:rounded-3xl shadow-[0_15px_50px_-10px_rgba(6,78,59,0.12)] border border-black-100 overflow-hidden grid grid-cols-1 lg:grid-cols-2"
			>
				<!-- Left Banner: Hero Section (Image 2 Poster Style) -->
				<div
					class="relative bg-[#064e3b] flex flex-col justify-between text-white overflow-hidden rounded-t-2xl lg:rounded-t-none lg:rounded-l-3xl"
				>
					<!-- Background Subtle Radial Gradient -->
					<div
						class="absolute -top-16 -right-16 w-56 h-56 bg-emerald-400/15 rounded-full blur-2xl pointer-events-none"
					></div>

					<!-- Top Text Content -->
					<div class="p-6 sm:p-7 lg:p-8 z-10">
						<!-- Pill Badge with Globe Icon -->
						<div
							class="inline-flex items-center gap-2 px-3.5 py-1 rounded-full border border-white/35 text-white text-[10.5px] sm:text-xs font-semibold tracking-wider uppercase backdrop-blur-sm"
						>
							<svg
								class="w-3.5 h-3.5 text-white shrink-0"
								viewBox="0 0 24 24"
								fill="none"
								stroke="currentColor"
								stroke-width="2"
								stroke-linecap="round"
								stroke-linejoin="round"
							>
								<circle cx="12" cy="12" r="10" />
								<line x1="2" y1="12" x2="22" y2="12" />
								<path
									d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"
								/>
							</svg>
							<span>{{ settings.login_hero_badge || "GLOBAL NGO COMMUNITY" }}</span>
						</div>

						<!-- Headline -->
						<h1
							class="text-2xl sm:text-[26px] lg:text-[28px] font-extrabold text-white tracking-tight leading-[1.2] mt-4"
						>
							{{ settings.login_hero_title || "Empowering communities, together." }}
						</h1>

						<!-- Description -->
						<p
							class="text-emerald-100/90 text-xs sm:text-[13px] leading-relaxed mt-2.5 font-normal"
						>
							{{
								settings.login_hero_description ||
								"Support your community as a volunteer or donor, discover meaningful opportunities, and track your impact."
							}}
						</p>
					</div>

					<!-- Bottom: Edge-to-Edge Community Photo (Seamless with Card) -->
					<div
						class="relative w-full h-52 sm:h-60 lg:h-64 mt-auto overflow-hidden shrink-0"
					>
						<!-- Smooth Gradient Fade from Green Header into Photo -->
						<div
							class="absolute inset-x-0 top-0 h-16 bg-gradient-to-b from-[#064e3b] via-[#064e3b]/50 to-transparent z-10 pointer-events-none"
						></div>
						<img
							:src="settings.login_hero_image || volunteerDistribution"
							alt="Empowering communities together"
							class="w-full h-full object-cover object-top"
						/>
					</div>
				</div>

				<!-- Right Panel: Compact & Well-Balanced Login Form -->
				<div class="p-6 sm:p-8 lg:p-9 flex flex-col justify-center bg-white">
					<div class="w-full max-w-[340px] sm:max-w-[360px] mx-auto my-auto">
						<!-- Form Icon Badge -->
						<div
							class="w-10 h-10 rounded-xl bg-emerald-50 border border-emerald-100/80 flex items-center justify-center text-emerald-700 mb-2.5 shadow-sm"
						>
							<svg
								class="w-5 h-5"
								viewBox="0 0 24 24"
								fill="none"
								stroke="currentColor"
								stroke-width="2"
								stroke-linecap="round"
								stroke-linejoin="round"
							>
								<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2" />
								<circle cx="9" cy="7" r="4" />
								<path d="M22 21v-2a4 4 0 0 0-3-3.87" />
								<path d="M16 3.13a4 4 0 0 1 0 7.75" />
							</svg>
						</div>

						<!-- Form Title & Subtitle -->
						<h2
							class="text-2xl font-extrabold text-black-900 tracking-tight leading-tight"
						>
							{{ settings.login_form_title || "Welcome back, changemaker" }}
						</h2>
						<p class="text-xs text-black-500 mt-1 leading-normal">
							{{
								settings.login_form_subtitle ||
								"Log in to access your deployment shifts, impact ledger, and verified hours."
							}}
						</p>

						<!-- Main Sign-in Form -->
						<form @submit.prevent="login" class="space-y-3 mt-3.5">
							<!-- Error Banner -->
							<div
								v-if="error"
								class="bg-red-50 border border-red-200 text-red-600 px-3 py-1.5 rounded-xl text-xs font-medium flex items-center gap-2 animate-pulse"
							>
								<svg
									class="w-3.5 h-3.5 shrink-0"
									viewBox="0 0 20 20"
									fill="currentColor"
								>
									<path
										fill-rule="evenodd"
										d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z"
										clip-rule="evenodd"
									/>
								</svg>
								<span>{{ error }}</span>
							</div>

							<!-- Email Field -->
							<div class="space-y-1">
								<label
									class="block text-[10px] font-bold text-black-700 uppercase tracking-wider"
								>
									{{ settings.login_email_label || "EMAIL ADDRESS" }}
								</label>
								<div
									class="relative rounded-xl border border-black-200 focus-within:border-emerald-700 focus-within:ring-2 focus-within:ring-emerald-700/15 transition shadow-sm bg-white"
								>
									<div
										class="absolute inset-y-0 left-0 pl-3.5 flex items-center pointer-events-none text-black-400"
									>
										<svg
											class="w-4 h-4"
											viewBox="0 0 24 24"
											fill="none"
											stroke="currentColor"
											stroke-width="2"
											stroke-linecap="round"
											stroke-linejoin="round"
										>
											<rect width="20" height="16" x="2" y="4" rx="2" />
											<path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7" />
										</svg>
									</div>
									<input
										v-model="email"
										type="email"
										required
										:placeholder="
											settings.login_email_placeholder || 'you@example.com'
										"
										class="block w-full pl-10 pr-3.5 py-2 text-xs lg:text-sm text-black-900 placeholder-black-400 bg-transparent rounded-xl focus:outline-none"
									/>
								</div>
							</div>

							<!-- Password Field -->
							<div class="space-y-1">
								<div class="flex items-center justify-between">
									<label
										class="block text-[10px] font-bold text-black-700 uppercase tracking-wider"
									>
										{{ settings.login_password_label || "PASSWORD" }}
									</label>
									<a
										:href="settings.login_forgot_password_url || '#'"
										@click.prevent="handleForgotPassword"
										class="text-xs font-semibold text-amber-700 hover:text-amber-800 transition hover:underline"
									>
										{{
											settings.login_forgot_password_label ||
											"Forgot password?"
										}}
									</a>
								</div>
								<div
									class="relative rounded-xl border border-black-200 focus-within:border-emerald-700 focus-within:ring-2 focus-within:ring-emerald-700/15 transition shadow-sm bg-white"
								>
									<div
										class="absolute inset-y-0 left-0 pl-3.5 flex items-center pointer-events-none text-black-400"
									>
										<svg
											class="w-4 h-4"
											viewBox="0 0 24 24"
											fill="none"
											stroke="currentColor"
											stroke-width="2"
											stroke-linecap="round"
											stroke-linejoin="round"
										>
											<rect
												width="18"
												height="11"
												x="3"
												y="11"
												rx="2"
												ry="2"
											/>
											<path d="M7 11V7a5 5 0 0 1 10 0v4" />
										</svg>
									</div>
									<input
										v-model="password"
										:type="showPassword ? 'text' : 'password'"
										required
										placeholder="••••••••••••••••"
										class="block w-full pl-10 pr-10 py-2 text-xs lg:text-sm text-black-900 placeholder-black-400 bg-transparent rounded-xl focus:outline-none"
									/>
									<!-- Toggle Visibility -->
									<button
										type="button"
										@click="showPassword = !showPassword"
										class="absolute inset-y-0 right-0 pr-3.5 flex items-center text-black-400 hover:text-black-600 transition"
									>
										<svg
											v-if="!showPassword"
											class="w-4 h-4"
											viewBox="0 0 24 24"
											fill="none"
											stroke="currentColor"
											stroke-width="2"
											stroke-linecap="round"
											stroke-linejoin="round"
										>
											<path
												d="M2 12s3-7 10-7 10 7 10 7-3 7-10 7-10-7-10-7Z"
											/>
											<circle cx="12" cy="12" r="3" />
										</svg>
										<svg
											v-else
											class="w-4 h-4"
											viewBox="0 0 24 24"
											fill="none"
											stroke="currentColor"
											stroke-width="2"
											stroke-linecap="round"
											stroke-linejoin="round"
										>
											<path d="m15 18-.722-3.25" />
											<path d="M2 8a10.645 10.645 0 0 0 20 0" />
											<path d="m20 15-1.726-2.05" />
											<path d="m4 15 1.726-2.05" />
											<path d="m9 18 .722-3.25" />
										</svg>
									</button>
								</div>
							</div>

							<!-- Remember Me -->
							<div class="flex items-center justify-between pt-0.5">
								<label class="flex items-center gap-2 cursor-pointer select-none">
									<input
										v-model="rememberMe"
										type="checkbox"
										class="w-4 h-4 rounded text-[#064e3b] border-black-300 focus:ring-emerald-700 cursor-pointer"
									/>
									<span class="text-xs text-black-600">
										{{
											settings.login_remember_me_label ||
											"Remember this station for 30 days"
										}}
									</span>
								</label>
							</div>

							<!-- Submit Button (Primary Forest Green) -->
							<button
								type="submit"
								:disabled="loading"
								class="w-full mt-2 py-2.5 px-4 rounded-xl text-xs lg:text-sm font-bold text-white bg-[#064e3b] hover:bg-[#043d2e] focus:ring-2 focus:ring-emerald-700 focus:ring-offset-2 transition shadow-md flex items-center justify-center gap-2 disabled:opacity-70 group active:scale-[0.99]"
							>
								<span v-if="loading" class="flex items-center gap-2">
									<svg
										class="animate-spin h-4 w-4 text-white"
										viewBox="0 0 24 24"
										fill="none"
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
											d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
										></path>
									</svg>
									Authenticating...
								</span>
								<span v-else class="flex items-center gap-2">
									<span>{{
										settings.login_submit_button_label ||
										"Sign In to Dashboard"
									}}</span>
									<svg
										class="w-4 h-4 transition-transform group-hover:translate-x-1"
										viewBox="0 0 24 24"
										fill="none"
										stroke="currentColor"
										stroke-width="2"
										stroke-linecap="round"
										stroke-linejoin="round"
									>
										<path d="M5 12h14" />
										<path d="m12 5 7 7-7 7" />
									</svg>
								</span>
							</button>

							<!-- Apply to be a Volunteer Button -->
							<router-link
								:to="settings.login_apply_button_url || '/apply'"
								class="w-full py-2 px-4 rounded-xl text-xs lg:text-sm font-bold text-emerald-950 bg-emerald-50 hover:bg-emerald-100/90 border border-emerald-200/60 focus:ring-2 focus:ring-emerald-700 transition flex items-center justify-center gap-2 text-center shadow-sm"
							>
								<svg
									class="w-3.5 h-3.5 text-emerald-700"
									viewBox="0 0 24 24"
									fill="currentColor"
								>
									<path
										d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"
									/>
								</svg>
								<span>{{
									settings.login_apply_button_label || "Apply to be a Volunteer"
								}}</span>
							</router-link>
						</form>
					</div>
				</div>
			</div>
		</main>

		<!-- Bottom Page Footer (Fixed at bottom) -->
		<footer
			class="w-full max-w-6xl mx-auto px-6 py-2 shrink-0 flex flex-col sm:flex-row items-center justify-between text-[11px] text-black-500 gap-2 border-t border-black-100/80 z-20"
		>
			<div>
				{{
					settings.login_footer_copyright ||
					"© 2026 Non Governmental Organisation. All rights reserved."
				}}
			</div>
			<div class="flex items-center gap-2 sm:gap-3 flex-wrap justify-center">
				<template v-for="(link, idx) in footerLinks" :key="idx">
					<span v-if="idx > 0" class="text-black-300">•</span>
					<a href="#" class="hover:text-black-800 transition hover:underline">{{
						link
					}}</a>
				</template>
			</div>
		</footer>
	</div>
</template>

<script setup>
import volunteerDistribution from "@/assets/volunteer_distribution.jpg";
import { createResource } from "frappe-ui";
import { computed, ref } from "vue";
import { useRouter } from "vue-router";
import { session } from "../data/session";

const router = useRouter();
const email = ref("");
const password = ref("");
const rememberMe = ref(true);
const showPassword = ref(false);
const loading = ref(false);
const error = ref("");

// Load portal settings dynamically from Frappe backend
const settingsResource = createResource({
	url: "ngo.api.volunteer.get_portal_settings",
	method: "GET",
	auto: true,
});

const settings = computed(() => settingsResource.data || {});

const footerLinks = computed(() => {
	const raw =
		settings.value.login_footer_links ||
		"Terms of Service | Volunteer Privacy Notice | Accessibility";
	return raw
		.split(/[|,•]/)
		.map((s) => s.trim())
		.filter(Boolean);
});

function handleForgotPassword() {
	if (
		settings.value.login_forgot_password_url &&
		settings.value.login_forgot_password_url !== "#"
	) {
		window.location.href = settings.value.login_forgot_password_url;
	} else {
		// Default Frappe forgot password route
		window.location.href = "/update-password";
	}
}

async function login() {
	loading.value = true;
	error.value = "";

	try {
		const loginRes = await session.login.submit({
			email: email.value,
			password: password.value,
		});

		if (session.login.error) {
			throw new Error(session.login.error);
		}

		// Role-based redirect on successful authentication
		let destination = loginRes?.home_page || session.login?.data?.home_page;
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

		try {
			const routeRes = await fetch("/api/method/ngo.api.donor_portal.auth.get_portal_route");
			const json = await routeRes.json();
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
		} catch (routeErr) {
			console.warn("Role redirect fallback:", routeErr);
		}
	} catch (err) {
		const rawError = String(err.message || session.login.error || err || "");
		if (
			rawError.includes("AuthenticationError") ||
			rawError.includes("Invalid Login") ||
			rawError.includes("401")
		) {
			error.value = "Invalid email or password. Please check your credentials.";
		} else {
			error.value = "An error occurred during login. Please try again later.";
		}
	} finally {
		loading.value = false;
	}
}
</script>
