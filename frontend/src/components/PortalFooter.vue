<template>
	<footer
		v-if="settings.footer_enabled !== 0 && settings.footer_enabled !== false"
		class="w-full transition-all duration-300 border-t select-none relative overflow-hidden"
		:class="[
			isDonor
				? 'portal-footer-donor bg-[#0d1b2a] border-[#1b2b40]'
				: 'portal-footer-volunteer bg-[#043226] border-[#0a4838]',
		]"
	>
		<!-- Subtle decorative background pattern -->
		<div
			class="absolute inset-0 pointer-events-none opacity-[0.04]"
			style="
				background-image: radial-gradient(#ffffff 1px, transparent 1px);
				background-size: 20px 20px;
			"
		></div>

		<!-- Main 3-Column Footer Grid -->
		<div class="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10 lg:py-12">
			<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-12 gap-8 lg:gap-12">
				<!-- Column 1: Brand Info & Copyright (5 cols on lg) -->
				<div class="lg:col-span-5 space-y-4">
					<!-- Brand Logo & Title -->
					<div class="flex items-center gap-3">
						<template v-if="settings.footer_logo">
							<img
								:src="settings.footer_logo"
								:alt="settings.footer_organization_name"
								class="h-9 w-auto max-w-[140px] object-contain rounded"
							/>
						</template>
						<template v-else>
							<!-- Stylish Emblem -->
							<div
								class="w-9 h-9 rounded-lg flex items-center justify-center font-bold text-white shadow-sm flex-shrink-0 transition-transform hover:scale-105"
								:class="isDonor ? 'bg-[#059669]' : 'bg-[#10b981]'"
							>
								<svg
									class="w-5 h-5 text-white"
									viewBox="0 0 24 24"
									fill="currentColor"
								>
									<path
										d="M17 8C8 10 5.9 16.17 3.82 21.34L5.71 22l1-2.3A4.49 4.49 0 0 0 8 20C19 20 22 3 22 3c-1 2-8 2.25-13 3.25S2 11.5 2 13.5s1.75 3.75 1.75 3.75C7 8 17 8 17 8z"
									/>
								</svg>
							</div>
						</template>

						<div class="min-w-0">
							<div
								class="footer-title font-extrabold text-xl tracking-tight leading-tight truncate text-white"
							>
								{{
									settings.footer_organization_name ||
									"Non Governmental Organisation"
								}}
							</div>
							<div
								class="footer-subtitle text-[10px] font-semibold tracking-wider uppercase mt-0.5"
								:class="isDonor ? 'text-[#2dd4bf]' : 'text-[#34d399]'"
							>
								{{
									isDonor
										? "Donor Impact & Governance"
										: "Community Volunteer Portal"
								}}
							</div>
						</div>
					</div>

					<!-- Slogan / Tagline -->
					<p
						v-if="settings.footer_tagline"
						class="footer-tagline text-xs italic leading-relaxed"
						:class="isDonor ? 'text-[#cbd5e1]' : 'text-[#d1fae5]'"
					>
						&ldquo;{{ settings.footer_tagline }}&rdquo;
					</p>

					<!-- Description -->
					<p
						class="footer-description text-xs leading-relaxed max-w-md"
						:class="isDonor ? 'text-[#e2e8f0]' : 'text-[#e2e8f0]'"
					>
						{{
							settings.footer_description ||
							"Non governmental organisation helps organisations to get a better quality service by tapping into the skills of a global volunteer community."
						}}
					</p>

					<!-- Trust & Verification Badges -->
					<div class="flex flex-wrap items-center gap-2 pt-1">
						<span
							class="footer-badge inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-[10px] font-semibold border"
							:class="[
								isDonor
									? 'bg-[#07111b] text-[#5eead4] border-[#1b2b40]'
									: 'bg-[#022119] text-[#6ee7b7] border-[#0a4838]',
							]"
						>
							<span
								class="w-1.5 h-1.5 rounded-full animate-pulse"
								:class="isDonor ? 'bg-[#2dd4bf]' : 'bg-[#34d399]'"
							></span>
							{{
								isDonor
									? "Audited & FCRA Ready Ledger"
									: "Verified Changemaker Platform"
							}}
						</span>
						<span
							class="footer-badge inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[10px] font-medium border"
							:class="[
								isDonor
									? 'bg-[#07111b] text-[#e2e8f0] border-[#1b2b40]'
									: 'bg-[#022119] text-[#e2e8f0] border-[#0a4838]',
							]"
						>
							{{
								settings.footer_powered_by ||
								"Non Governmental Organisation Platform"
							}}
						</span>
					</div>

					<!-- Copyright Notice -->
					<div
						class="footer-copyright pt-2 text-xs"
						:class="isDonor ? 'text-[#94a3b8]' : 'text-[#a7f3d0]'"
					>
						<span>{{
							settings.footer_copyright_text ||
							"© 2026 Non Governmental Organisation. All rights reserved."
						}}</span>
					</div>
				</div>

				<!-- Column 2: Info (Navigation) (3 cols on lg) -->
				<div v-if="settings.footer_show_quick_links" class="lg:col-span-3 space-y-3.5">
					<h3 class="text-sm font-bold tracking-normal text-white">Info</h3>
					<ul class="space-y-2 text-xs">
						<li v-for="link in navLinks" :key="link.path">
							<router-link
								:to="link.path"
								class="footer-nav-link transition-all duration-150 inline-flex items-center gap-2 group hover:translate-x-1 font-normal"
								:class="[
									isDonor
										? 'text-[#cbd5e1] hover:text-[#2dd4bf]'
										: 'text-[#d1fae5] hover:text-white',
								]"
							>
								<span
									class="w-1.5 h-1.5 rounded-full transition-all group-hover:w-2.5"
									:class="isDonor ? 'bg-[#2dd4bf]' : 'bg-[#34d399]'"
								></span>
								<span>{{ link.label }}</span>
							</router-link>
						</li>
						<!-- Custom configured links -->
						<li v-for="(cl, cIdx) in parsedCustomLinks" :key="'custom-' + cIdx">
							<a
								:href="cl.url || '#'"
								target="_blank"
								rel="noopener noreferrer"
								class="footer-nav-link transition-all duration-150 inline-flex items-center gap-2 group hover:translate-x-1 font-normal"
								:class="[
									isDonor
										? 'text-[#cbd5e1] hover:text-[#2dd4bf]'
										: 'text-[#d1fae5] hover:text-white',
								]"
							>
								<span
									class="w-1.5 h-1.5 rounded-full transition-all group-hover:w-2.5"
									:class="isDonor ? 'bg-[#2dd4bf]' : 'bg-[#34d399]'"
								></span>
								<span>{{ cl.label }}</span>
							</a>
						</li>
					</ul>
				</div>

				<!-- Column 3: Information (Contact, Legal, Social Icons) (4 cols on lg) -->
				<div class="lg:col-span-4 space-y-3.5">
					<h3 class="text-sm font-bold tracking-normal text-white">Information</h3>

					<div class="space-y-2.5 text-xs">
						<!-- Email -->
						<div
							v-if="settings.footer_contact_email"
							class="flex items-center gap-2.5"
						>
							<svg
								class="w-4 h-4 flex-shrink-0"
								:class="isDonor ? 'text-[#2dd4bf]' : 'text-[#34d399]'"
								viewBox="0 0 24 24"
								fill="none"
								stroke="currentColor"
								stroke-width="2"
							>
								<rect x="2" y="4" width="20" height="16" rx="2"></rect>
								<path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"></path>
							</svg>
							<a
								:href="'mailto:' + settings.footer_contact_email"
								class="footer-contact-link transition-colors duration-150 truncate hover:underline"
								:class="[
									isDonor
										? 'text-[#cbd5e1] hover:text-white'
										: 'text-[#d1fae5] hover:text-white',
								]"
							>
								{{ settings.footer_contact_email }}
							</a>
						</div>

						<!-- Phone -->
						<div
							v-if="settings.footer_contact_phone"
							class="flex items-center gap-2.5"
						>
							<svg
								class="w-4 h-4 flex-shrink-0"
								:class="isDonor ? 'text-[#2dd4bf]' : 'text-[#34d399]'"
								viewBox="0 0 24 24"
								fill="none"
								stroke="currentColor"
								stroke-width="2"
							>
								<path
									d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"
								></path>
							</svg>
							<a
								:href="'tel:' + settings.footer_contact_phone"
								class="footer-contact-link transition-colors duration-150 hover:underline"
								:class="[
									isDonor
										? 'text-[#cbd5e1] hover:text-white'
										: 'text-[#d1fae5] hover:text-white',
								]"
							>
								{{ settings.footer_contact_phone }}
							</a>
						</div>

						<!-- Terms & Conditions -->
						<div>
							<a
								:href="settings.footer_terms_url || '/terms'"
								class="footer-contact-link transition-colors duration-150 inline-block hover:underline"
								:class="[
									isDonor
										? 'text-[#cbd5e1] hover:text-white'
										: 'text-[#d1fae5] hover:text-white',
								]"
							>
								Terms &amp; Conditions
							</a>
						</div>

						<!-- Privacy -->
						<div>
							<a
								:href="settings.footer_privacy_url || '/privacy'"
								class="footer-contact-link transition-colors duration-150 inline-block hover:underline"
								:class="[
									isDonor
										? 'text-[#cbd5e1] hover:text-white'
										: 'text-[#d1fae5] hover:text-white',
								]"
							>
								Privacy
							</a>
						</div>

						<!-- Documentation -->
						<div v-if="settings.footer_support_url || settings.footer_website_url">
							<a
								:href="
									settings.footer_support_url ||
									settings.footer_website_url ||
									'/support'
								"
								target="_blank"
								rel="noopener noreferrer"
								class="footer-contact-link transition-colors duration-150 inline-block hover:underline"
								:class="[
									isDonor
										? 'text-[#cbd5e1] hover:text-white'
										: 'text-[#d1fae5] hover:text-white',
								]"
							>
								Our Documentation
							</a>
						</div>
					</div>

					<!-- Social Icons Row & Back to Top -->
					<div
						class="pt-4 flex flex-wrap items-center justify-between gap-4 border-t"
						:class="isDonor ? 'border-[#1b2b40]' : 'border-[#0a4838]'"
					>
						<!-- Social Media Icons -->
						<div
							v-if="settings.footer_show_social_links"
							class="flex items-center gap-3"
						>
							<!-- Facebook -->
							<a
								v-if="settings.footer_facebook_url"
								:href="settings.footer_facebook_url"
								target="_blank"
								rel="noopener noreferrer"
								aria-label="Facebook"
								class="w-7 h-7 rounded-md flex items-center justify-center transition-all duration-200 hover:scale-110 shadow-2xs border"
								:class="[
									isDonor
										? 'bg-[#07111b] border-[#1b2b40] text-[#2dd4bf] hover:bg-[#2dd4bf] hover:text-[#0d1b2a]'
										: 'bg-[#022119] border-[#0a4838] text-[#34d399] hover:bg-[#34d399] hover:text-[#043226]',
								]"
							>
								<svg class="w-3.5 h-3.5 fill-current" viewBox="0 0 24 24">
									<path
										d="M9 8H6v4h3v12h5V12h3.642L18 8h-4V6.333C14 5.374 14.5 5 15.5 5H18V0h-3.808C10.595 0 9 1.583 9 4.615V8z"
									/>
								</svg>
							</a>

							<!-- Twitter / X -->
							<a
								v-if="settings.footer_twitter_url"
								:href="settings.footer_twitter_url"
								target="_blank"
								rel="noopener noreferrer"
								aria-label="Twitter / X"
								class="w-7 h-7 rounded-md flex items-center justify-center transition-all duration-200 hover:scale-110 shadow-2xs border"
								:class="[
									isDonor
										? 'bg-[#07111b] border-[#1b2b40] text-[#2dd4bf] hover:bg-[#2dd4bf] hover:text-[#0d1b2a]'
										: 'bg-[#022119] border-[#0a4838] text-[#34d399] hover:bg-[#34d399] hover:text-[#043226]',
								]"
							>
								<svg class="w-3.5 h-3.5 fill-current" viewBox="0 0 24 24">
									<path
										d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"
									/>
								</svg>
							</a>

							<!-- LinkedIn -->
							<a
								v-if="settings.footer_linkedin_url"
								:href="settings.footer_linkedin_url"
								target="_blank"
								rel="noopener noreferrer"
								aria-label="LinkedIn"
								class="w-7 h-7 rounded-md flex items-center justify-center transition-all duration-200 hover:scale-110 shadow-2xs border"
								:class="[
									isDonor
										? 'bg-[#07111b] border-[#1b2b40] text-[#2dd4bf] hover:bg-[#2dd4bf] hover:text-[#0d1b2a]'
										: 'bg-[#022119] border-[#0a4838] text-[#34d399] hover:bg-[#34d399] hover:text-[#043226]',
								]"
							>
								<svg class="w-3.5 h-3.5 fill-current" viewBox="0 0 24 24">
									<path
										d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"
									/>
								</svg>
							</a>

							<!-- Instagram -->
							<a
								v-if="settings.footer_instagram_url"
								:href="settings.footer_instagram_url"
								target="_blank"
								rel="noopener noreferrer"
								aria-label="Instagram"
								class="w-7 h-7 rounded-md flex items-center justify-center transition-all duration-200 hover:scale-110 shadow-2xs border"
								:class="[
									isDonor
										? 'bg-[#07111b] border-[#1b2b40] text-[#2dd4bf] hover:bg-[#2dd4bf] hover:text-[#0d1b2a]'
										: 'bg-[#022119] border-[#0a4838] text-[#34d399] hover:bg-[#34d399] hover:text-[#043226]',
								]"
							>
								<svg class="w-3.5 h-3.5 fill-current" viewBox="0 0 24 24">
									<path
										d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"
									/>
								</svg>
							</a>

							<!-- YouTube -->
							<a
								v-if="settings.footer_youtube_url"
								:href="settings.footer_youtube_url"
								target="_blank"
								rel="noopener noreferrer"
								aria-label="YouTube"
								class="w-7 h-7 rounded-md flex items-center justify-center transition-all duration-200 hover:scale-110 shadow-2xs border"
								:class="[
									isDonor
										? 'bg-[#07111b] border-[#1b2b40] text-rose-400 hover:bg-rose-500 hover:text-white'
										: 'bg-[#022119] border-[#0a4838] text-rose-400 hover:bg-rose-500 hover:text-white',
								]"
							>
								<svg class="w-3.5 h-3.5 fill-current" viewBox="0 0 24 24">
									<path
										d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"
									/>
								</svg>
							</a>
						</div>

						<!-- Back to Top smooth scroll button -->
						<button
							type="button"
							@click="scrollToTop"
							class="inline-flex items-center gap-1 px-2.5 py-1 rounded-md text-[11px] font-medium transition-all hover:-translate-y-0.5 active:translate-y-0 cursor-pointer border"
							:class="[
								isDonor
									? 'bg-[#07111b] border-[#1b2b40] text-[#cbd5e1] hover:text-white hover:bg-[#132235]'
									: 'bg-[#022119] border-[#0a4838] text-[#d1fae5] hover:text-white hover:bg-[#073d2f]',
							]"
							aria-label="Back to top"
						>
							<span>Top</span>
							<svg
								class="w-3 h-3"
								viewBox="0 0 24 24"
								fill="none"
								stroke="currentColor"
								stroke-width="2.5"
							>
								<polyline points="18 15 12 9 6 15"></polyline>
							</svg>
						</button>
					</div>
				</div>
			</div>
		</div>
	</footer>
</template>

<script setup>
import { computed, onMounted, ref } from "vue";

const props = defineProps({
	portalType: {
		type: String,
		default: "volunteer", // "volunteer" or "donor"
	},
});

const isDonor = computed(() => {
	if (props.portalType === "donor") return true;
	if (typeof window !== "undefined") {
		return window.location.pathname.includes("donor");
	}
	return false;
});

const settings = ref({
	footer_enabled: 1,
	footer_organization_name: "Non Governmental Organisation",
	footer_tagline: "People helping people creates a stronger tomorrow.",
	footer_description:
		"Non Governmental Organisation helps organisations to get a better quality service by tapping into the skills of a global volunteer community.",
	footer_logo: "",
	footer_copyright_text: "© 2026 Non Governmental Organisation. All rights reserved.",
	footer_powered_by: "Non Governmental Organisation NGO Platform",
	footer_show_quick_links: 1,
	footer_show_social_links: 1,
	footer_show_contact_info: 1,
	footer_contact_email: "support@nongovernmentalorganization.org",
	footer_contact_phone: "+91 1234567890",
	footer_address: "100 Impact Way, Social Innovation Hub, CA 94105",
	footer_privacy_url: "/privacy",
	footer_terms_url: "/terms",
	footer_support_url: "/support",
	footer_website_url: "https://impactsphere.org",
	footer_facebook_url: "https://facebook.com",
	footer_twitter_url: "https://x.com",
	footer_linkedin_url: "https://linkedin.com",
	footer_instagram_url: "https://instagram.com",
	footer_youtube_url: "",
	footer_custom_links: "",
});

const navLinks = computed(() => {
	if (isDonor.value) {
		return [
			{ path: "/donor-portal", label: "Dashboard" },
			{ path: "/donor-portal/proposals", label: "Project Proposals" },
			{ path: "/donor-portal/grants", label: "My Grants" },
			{ path: "/donor-portal/fund-utilization", label: "Fund Utilization" },
			{ path: "/donor-portal/impact", label: "Beneficiary & Impact" },
			{ path: "/donor-portal/documents", label: "Documents & Compliance" },
			{ path: "/donor-portal/profile", label: "Donor Profile" },
		];
	}
	return [
		{ path: "/", label: "Dashboard" },
		{ path: "/opportunities", label: "Opportunities" },
		{ path: "/assignments", label: "My Assignments" },
		{ path: "/shifts", label: "My Shifts" },
		{ path: "/attendance", label: "Attendance" },
		{ path: "/profile", label: "Profile Settings" },
	];
});

const parsedCustomLinks = computed(() => {
	if (!settings.value.footer_custom_links) return [];
	try {
		if (typeof settings.value.footer_custom_links === "string") {
			return JSON.parse(settings.value.footer_custom_links);
		}
		return settings.value.footer_custom_links;
	} catch (e) {
		return [];
	}
});

const scrollToTop = () => {
	if (typeof window !== "undefined") {
		window.scrollTo({
			top: 0,
			behavior: "smooth",
		});
	}
};

const fetchFooterSettings = async () => {
	try {
		const res = await fetch(
			"/api/method/ngo.ngo.doctype.portal_settings.portal_settings.get_portal_settings"
		);
		if (!res.ok) return;
		const data = await res.json();
		if (data && data.message) {
			const msg = data.message;
			Object.keys(msg).forEach((key) => {
				if (key.startsWith("footer_") && msg[key] !== null && msg[key] !== undefined) {
					settings.value[key] = msg[key];
				}
			});
		}
	} catch (err) {
		// Graceful fallback to default values
	}
};

onMounted(() => {
	fetchFooterSettings();
});
</script>

<style scoped>
/* Scoped visibility guarantees for Volunteer Portal */
.portal-footer-volunteer,
.portal-footer-volunteer p,
.portal-footer-volunteer span:not(.animate-pulse),
.portal-footer-volunteer a {
	color: #d1fae5;
}
.portal-footer-volunteer .footer-title,
.portal-footer-volunteer h3 {
	color: #ffffff !important;
}
.portal-footer-volunteer .footer-subtitle {
	color: #34d399 !important;
}
.portal-footer-volunteer .footer-description {
	color: #e2e8f0 !important;
}
.portal-footer-volunteer .footer-copyright {
	color: #a7f3d0 !important;
}
.portal-footer-volunteer a:hover {
	color: #ffffff !important;
}

/* Scoped visibility guarantees for Donor Portal */
.portal-footer-donor,
.portal-footer-donor p,
.portal-footer-donor span:not(.animate-pulse),
.portal-footer-donor a {
	color: #cbd5e1;
}
.portal-footer-donor .footer-title,
.portal-footer-donor h3 {
	color: #ffffff !important;
}
.portal-footer-donor .footer-subtitle {
	color: #2dd4bf !important;
}
.portal-footer-donor .footer-description {
	color: #e2e8f0 !important;
}
.portal-footer-donor .footer-copyright {
	color: #94a3b8 !important;
}
.portal-footer-donor a:hover {
	color: #ffffff !important;
}
</style>
