<template>
	<footer
		v-if="settings.footer_enabled !== 0 && settings.footer_enabled !== false"
		:class="[
			'mt-auto w-full transition-colors duration-300 border-t select-none',
			isDonor
				? 'bg-slate-900 text-slate-300 border-slate-800'
				: 'bg-[#03231a] text-emerald-100/90 border-emerald-950/60',
		]"
	>
		<!-- Main Footer Content Grid -->
		<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10 lg:py-12">
			<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-12 gap-8 lg:gap-10">
				<!-- Col 1: Organization Branding & Mission (5 cols on lg) -->
				<div class="lg:col-span-5 space-y-4">
					<div class="flex items-center gap-3">
						<!-- Custom Logo or Fallback Portal Emblem -->
						<template v-if="settings.footer_logo">
							<img
								:src="settings.footer_logo"
								:alt="settings.footer_organization_name"
								class="h-9 w-auto max-w-[140px] object-contain rounded"
							/>
						</template>
						<template v-else>
							<div
								:class="[
									'w-9 h-9 rounded-xl flex items-center justify-center font-bold shadow-md flex-shrink-0',
									isDonor
										? 'bg-gradient-to-tr from-emerald-600 to-teal-400 text-white shadow-emerald-500/20'
										: 'bg-emerald-900/90 border border-emerald-500/40 text-emerald-300',
								]"
							>
								<svg
									v-if="isDonor"
									class="w-5 h-5"
									viewBox="0 0 24 24"
									fill="none"
									stroke="currentColor"
									stroke-width="2"
								>
									<path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5" />
								</svg>
								<svg v-else width="20" height="20" viewBox="0 0 24 24" fill="none">
									<path
										d="M12 22V12"
										stroke="#34d399"
										stroke-width="2.2"
										stroke-linecap="round"
									/>
									<path
										d="M12 12C12 7.02944 16.0294 3 21 3C21 7.97056 16.9706 12 12 12Z"
										fill="#f59e0b"
										fill-opacity="0.95"
									/>
									<path
										d="M12 14C12 9.02944 7.97056 5 3 5C3 9.97056 7.02944 14 12 14Z"
										fill="#10b981"
									/>
								</svg>
							</div>
						</template>

						<div class="min-w-0">
							<div
								:class="[
									'font-extrabold text-base tracking-tight truncate',
									isDonor ? 'text-white' : 'text-white',
								]"
							>
								{{ settings.footer_organization_name || "Kindred ImpactSphere" }}
							</div>
							<div
								:class="[
									'text-[10px] font-semibold tracking-wider uppercase',
									isDonor ? 'text-emerald-400' : 'text-emerald-300/80',
								]"
							>
								{{ isDonor ? "Donor Impact & Governance" : "Community Volunteer Portal" }}
							</div>
						</div>
					</div>

					<!-- Slogan / Tagline -->
					<p
						v-if="settings.footer_tagline"
						:class="[
							'text-xs font-medium italic leading-relaxed',
							isDonor ? 'text-slate-400' : 'text-emerald-200/75',
						]"
					>
						&ldquo;{{ settings.footer_tagline }}&rdquo;
					</p>

					<!-- Description -->
					<p
						:class="[
							'text-xs leading-relaxed max-w-md',
							isDonor ? 'text-slate-400' : 'text-emerald-200/60',
						]"
					>
						{{
							settings.footer_description ||
							"Together, we drive community empowerment through transparent volunteer action and accountable donor partnerships."
						}}
					</p>

					<!-- Trust & Verification Pill Badge -->
					<div class="pt-1 flex flex-wrap items-center gap-2">
						<span
							:class="[
								'inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-[10px] font-semibold border',
								isDonor
									? 'bg-emerald-950/50 text-emerald-400 border-emerald-800/60'
									: 'bg-emerald-900/40 text-emerald-300 border-emerald-700/50',
							]"
						>
							<span class="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse"></span>
							{{ isDonor ? "Audited & FCRA Ready Ledger" : "Verified Changemaker Platform" }}
						</span>
						<span
							:class="[
								'inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[10px] font-medium border',
								isDonor
									? 'bg-slate-800/80 text-slate-300 border-slate-700/60'
									: 'bg-[#06382a] text-emerald-200/70 border-emerald-800/40',
							]"
						>
							{{ settings.footer_powered_by || "Kindred NGO Platform" }}
						</span>
					</div>
				</div>

				<!-- Col 2: Portal Quick Navigation (2 cols on lg) -->
				<div v-if="settings.footer_show_quick_links" class="lg:col-span-2 space-y-3">
					<h3
						:class="[
							'text-xs font-bold uppercase tracking-wider',
							isDonor ? 'text-slate-200' : 'text-emerald-300',
						]"
					>
						Portal Navigation
					</h3>
					<ul class="space-y-2 text-xs">
						<li v-for="link in navLinks" :key="link.path">
							<router-link
								:to="link.path"
								:class="[
									'transition-colors duration-150 flex items-center gap-1.5 group',
									isDonor
										? 'text-slate-400 hover:text-emerald-400'
										: 'text-emerald-200/70 hover:text-white',
								]"
							>
								<span
									:class="[
										'w-1 h-1 rounded-full transition-all group-hover:w-2',
										isDonor ? 'bg-emerald-500' : 'bg-emerald-400',
									]"
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
								:class="[
									'transition-colors duration-150 flex items-center gap-1.5 group',
									isDonor
										? 'text-slate-400 hover:text-emerald-400'
										: 'text-emerald-200/70 hover:text-white',
								]"
							>
								<span
									:class="[
										'w-1 h-1 rounded-full transition-all group-hover:w-2',
										isDonor ? 'bg-teal-400' : 'bg-amber-400',
									]"
								></span>
								<span>{{ cl.label }}</span>
							</a>
						</li>
					</ul>
				</div>

				<!-- Col 3: Resources & Governance (2 cols on lg) -->
				<div class="lg:col-span-2 space-y-3">
					<h3
						:class="[
							'text-xs font-bold uppercase tracking-wider',
							isDonor ? 'text-slate-200' : 'text-emerald-300',
						]"
					>
						Resources
					</h3>
					<ul class="space-y-2 text-xs">
						<li v-if="settings.footer_website_url">
							<a
								:href="settings.footer_website_url"
								target="_blank"
								rel="noopener noreferrer"
								:class="[
									'transition-colors duration-150 block',
									isDonor
										? 'text-slate-400 hover:text-emerald-400'
										: 'text-emerald-200/70 hover:text-white',
								]"
							>
								Main Website
							</a>
						</li>
						<li>
							<a
								:href="settings.footer_privacy_url || '/privacy'"
								:class="[
									'transition-colors duration-150 block',
									isDonor
										? 'text-slate-400 hover:text-emerald-400'
										: 'text-emerald-200/70 hover:text-white',
								]"
							>
								Privacy Policy
							</a>
						</li>
						<li>
							<a
								:href="settings.footer_terms_url || '/terms'"
								:class="[
									'transition-colors duration-150 block',
									isDonor
										? 'text-slate-400 hover:text-emerald-400'
										: 'text-emerald-200/70 hover:text-white',
								]"
							>
								Terms of Service
							</a>
						</li>
						<li>
							<a
								:href="settings.footer_support_url || '/support'"
								:class="[
									'transition-colors duration-150 block',
									isDonor
										? 'text-slate-400 hover:text-emerald-400'
										: 'text-emerald-200/70 hover:text-white',
								]"
							>
								Help & Support
							</a>
						</li>
						<li v-if="isDonor">
							<span
								:class="[
									'inline-block text-[11px] px-2 py-0.5 rounded font-mono',
									isDonor
										? 'bg-slate-800 text-slate-400 border border-slate-700/60'
										: 'bg-emerald-950 text-emerald-400',
								]"
							>
								FCRA / 80G Compliant
							</span>
						</li>
					</ul>
				</div>

				<!-- Col 4: Contact & Social (3 cols on lg) -->
				<div
					v-if="settings.footer_show_contact_info || settings.footer_show_social_links"
					class="lg:col-span-3 space-y-3"
				>
					<h3
						:class="[
							'text-xs font-bold uppercase tracking-wider',
							isDonor ? 'text-slate-200' : 'text-emerald-300',
						]"
					>
						Get In Touch
					</h3>

					<!-- Contact details -->
					<div
						v-if="settings.footer_show_contact_info"
						class="space-y-2 text-xs"
						:class="isDonor ? 'text-slate-400' : 'text-emerald-200/70'"
					>
						<div v-if="settings.footer_contact_email" class="flex items-start gap-2.5">
							<svg
								class="w-4 h-4 flex-shrink-0 mt-0.5 text-emerald-400"
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
								class="hover:underline hover:text-white transition-colors truncate"
							>
								{{ settings.footer_contact_email }}
							</a>
						</div>

						<div v-if="settings.footer_contact_phone" class="flex items-start gap-2.5">
							<svg
								class="w-4 h-4 flex-shrink-0 mt-0.5 text-emerald-400"
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
								class="hover:underline hover:text-white transition-colors"
							>
								{{ settings.footer_contact_phone }}
							</a>
						</div>

						<div v-if="settings.footer_address" class="flex items-start gap-2.5">
							<svg
								class="w-4 h-4 flex-shrink-0 mt-0.5 text-emerald-400"
								viewBox="0 0 24 24"
								fill="none"
								stroke="currentColor"
								stroke-width="2"
							>
								<path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"></path>
								<circle cx="12" cy="10" r="3"></circle>
							</svg>
							<span class="leading-relaxed">{{ settings.footer_address }}</span>
						</div>
					</div>

					<!-- Social Media Links -->
					<div v-if="settings.footer_show_social_links" class="pt-2">
						<div class="text-[11px] font-semibold mb-2" :class="isDonor ? 'text-slate-300' : 'text-emerald-200/90'">
							Follow Us
						</div>
						<div class="flex items-center gap-2">
							<!-- Facebook -->
							<a
								v-if="settings.footer_facebook_url"
								:href="settings.footer_facebook_url"
								target="_blank"
								rel="noopener noreferrer"
								aria-label="Facebook"
								:class="[
									'w-8 h-8 rounded-lg flex items-center justify-center transition-all duration-200 hover:scale-110',
									isDonor
										? 'bg-slate-800 text-slate-300 hover:bg-emerald-600 hover:text-white'
										: 'bg-emerald-900/60 text-emerald-200 hover:bg-emerald-600 hover:text-white',
								]"
							>
								<svg class="w-4 h-4 fill-current" viewBox="0 0 24 24">
									<path
										d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"
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
								:class="[
									'w-8 h-8 rounded-lg flex items-center justify-center transition-all duration-200 hover:scale-110',
									isDonor
										? 'bg-slate-800 text-slate-300 hover:bg-emerald-600 hover:text-white'
										: 'bg-emerald-900/60 text-emerald-200 hover:bg-emerald-600 hover:text-white',
								]"
							>
								<svg class="w-4 h-4 fill-current" viewBox="0 0 24 24">
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
								:class="[
									'w-8 h-8 rounded-lg flex items-center justify-center transition-all duration-200 hover:scale-110',
									isDonor
										? 'bg-slate-800 text-slate-300 hover:bg-emerald-600 hover:text-white'
										: 'bg-emerald-900/60 text-emerald-200 hover:bg-emerald-600 hover:text-white',
								]"
							>
								<svg class="w-4 h-4 fill-current" viewBox="0 0 24 24">
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
								:class="[
									'w-8 h-8 rounded-lg flex items-center justify-center transition-all duration-200 hover:scale-110',
									isDonor
										? 'bg-slate-800 text-slate-300 hover:bg-emerald-600 hover:text-white'
										: 'bg-emerald-900/60 text-emerald-200 hover:bg-emerald-600 hover:text-white',
								]"
							>
								<svg class="w-4 h-4 fill-current" viewBox="0 0 24 24">
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
								:class="[
									'w-8 h-8 rounded-lg flex items-center justify-center transition-all duration-200 hover:scale-110',
									isDonor
										? 'bg-slate-800 text-slate-300 hover:bg-rose-600 hover:text-white'
										: 'bg-emerald-900/60 text-emerald-200 hover:bg-rose-600 hover:text-white',
								]"
							>
								<svg class="w-4 h-4 fill-current" viewBox="0 0 24 24">
									<path
										d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"
									/>
								</svg>
							</a>
						</div>
					</div>
				</div>
			</div>

			<!-- Bottom Sub-Footer Bar -->
			<div
				:class="[
					'mt-10 pt-6 border-t flex flex-col sm:flex-row items-center justify-between gap-4 text-xs',
					isDonor
						? 'border-slate-800/80 text-slate-500'
						: 'border-emerald-900/50 text-emerald-300/60',
				]"
			>
				<!-- Copyright -->
				<div class="flex items-center gap-2 text-center sm:text-left">
					<span>{{
						settings.footer_copyright_text || "© 2026 Kindred ImpactSphere. All rights reserved."
					}}</span>
				</div>

				<!-- Center / Right Badges & Back to Top -->
				<div class="flex items-center gap-4">
					<span class="inline-flex items-center gap-1.5 text-[11px]">
						<span class="w-2 h-2 rounded-full bg-emerald-500"></span>
						<span>All Systems Operational</span>
					</span>

					<!-- Smooth Scroll to Top -->
					<button
						type="button"
						@click="scrollToTop"
						:class="[
							'inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg border text-[11px] font-semibold transition-all hover:-translate-y-0.5 active:translate-y-0 cursor-pointer',
							isDonor
								? 'bg-slate-800/80 border-slate-700 text-slate-300 hover:text-white hover:bg-slate-700'
								: 'bg-emerald-950 border-emerald-800/80 text-emerald-200 hover:text-white hover:bg-emerald-900',
						]"
						aria-label="Back to top"
					>
						<span>Top</span>
						<svg
							class="w-3.5 h-3.5"
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

const isDonor = computed(() => props.portalType === "donor");

const settings = ref({
	footer_enabled: 1,
	footer_organization_name: "Kindred ImpactSphere",
	footer_tagline: "People helping people creates a stronger tomorrow.",
	footer_description:
		"Together, we drive community empowerment through transparent volunteer action and accountable donor partnerships.",
	footer_logo: "",
	footer_copyright_text: "© 2026 Kindred ImpactSphere. All rights reserved.",
	footer_powered_by: "Kindred NGO Platform",
	footer_show_quick_links: 1,
	footer_show_social_links: 1,
	footer_show_contact_info: 1,
	footer_contact_email: "support@impactsphere.org",
	footer_contact_phone: "+1 (800) 555-0199",
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
		const raw = settings.value.footer_custom_links;
		const parsed = typeof raw === "string" ? JSON.parse(raw) : raw;
		return Array.isArray(parsed) ? parsed : [];
	} catch (e) {
		return [];
	}
});

function scrollToTop() {
	window.scrollTo({ top: 0, behavior: "smooth" });
	const mainWrapper = document.querySelector(".overflow-y-auto");
	if (mainWrapper) {
		mainWrapper.scrollTo({ top: 0, behavior: "smooth" });
	}
}

onMounted(async () => {
	try {
		const res = await fetch("/api/method/ngo.api.volunteer.get_portal_footer_settings");
		const data = await res.json();
		if (data?.message) {
			settings.value = { ...settings.value, ...data.message };
		}
	} catch (e) {
		console.warn("Portal footer settings fallback in use:", e);
	}
});
</script>
