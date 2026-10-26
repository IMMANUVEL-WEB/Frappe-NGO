<template>
	<!-- Full-viewport responsive container matching Login page -->
	<div
		class="fixed inset-0 w-screen h-screen overflow-hidden bg-[#f8fafc] flex flex-col justify-between font-sans selection:bg-emerald-100 selection:text-emerald-900"
	>
		<!-- Top Navigation Header -->
		<header
			class="bg-white border-b border-black-100 px-6 lg:px-10 py-2.5 shrink-0 flex items-center justify-between shadow-[0_1px_3px_rgba(0,0,0,0.03)] z-20"
		>
			<!-- Brand Logo & Title -->
			<router-link to="/account/login" class="flex items-center gap-2.5 group">
				<template v-if="settings.login_logo">
					<img :src="settings.login_logo" alt="Logo" class="h-8 w-auto object-contain" />
				</template>
				<template v-else>
					<div
						class="w-8 h-8 rounded-xl bg-[#064e3b] flex items-center justify-center text-white shadow-sm shrink-0 border border-emerald-500/30"
					>
						<svg class="w-4 h-4" viewBox="0 0 24 24" fill="none">
							<path
								d="M12 22V12"
								stroke="#34d399"
								stroke-width="2"
								stroke-linecap="round"
							/>
							<path
								d="M12 12C12 7.02944 16.0294 3 21 3C21 7.97056 16.9706 12 12 12Z"
								fill="#f59e0b"
							/>
							<path
								d="M12 14C12 9.02944 7.97056 5 3 5C3 9.97056 7.02944 14 12 14Z"
								fill="#10b981"
							/>
						</svg>
					</div>
				</template>
				<div>
					<div
						class="font-extrabold text-black-900 text-sm lg:text-[15px] tracking-tight leading-none group-hover:text-emerald-800 transition-colors"
					>
						{{ settings.login_portal_title || "Non Governmental Organisation" }}
					</div>
					<div
						class="font-bold text-[#047857] text-[8px] tracking-[0.25em] uppercase leading-none mt-1"
					>
						{{ settings.login_portal_subtitle || "IMPACTSPHERE" }}
					</div>
				</div>
			</router-link>

			<!-- Header Right: Clean Sign In button -->
			<div class="flex items-center gap-3">
				<router-link
					to="/account/login"
					class="flex items-center gap-1.5 px-3 py-1 text-xs font-semibold text-black-700 hover:text-emerald-800 bg-white hover:bg-black-50 border border-black-200 rounded-lg transition shadow-sm"
				>
					<svg
						class="w-3.5 h-3.5 text-black-500"
						viewBox="0 0 24 24"
						fill="none"
						stroke="currentColor"
						stroke-width="2"
						stroke-linecap="round"
						stroke-linejoin="round"
					>
						<path d="M15 3h4a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2h-4"></path>
						<polyline points="10 17 15 12 10 7"></polyline>
						<line x1="15" y1="12" x2="3" y2="12"></line>
					</svg>
					<span>Sign In</span>
				</router-link>
			</div>
		</header>

		<!-- Main Content Area: Matching Login Modal Width & Height -->
		<main
			class="flex-1 min-h-0 w-full max-w-4xl xl:max-w-[880px] mx-auto px-4 py-3 sm:py-4 flex items-center justify-center overflow-hidden"
		>
			<div
				class="w-full max-h-[calc(100vh-105px)] bg-white rounded-2xl lg:rounded-3xl shadow-[0_15px_50px_-10px_rgba(6,78,59,0.12)] border border-black-100 overflow-hidden grid grid-cols-1 lg:grid-cols-2"
			>
				<!-- Left Side: Hero Banner (Matching Image 1 / Login Style) -->
				<div
					class="relative bg-[#064e3b] flex flex-col justify-between text-white overflow-hidden rounded-t-2xl lg:rounded-t-none lg:rounded-l-3xl"
				>
					<!-- Background Subtle Radial Gradient -->
					<div
						class="absolute -top-16 -right-16 w-56 h-56 bg-emerald-400/15 rounded-full blur-2xl pointer-events-none"
					></div>

					<!-- Top Text Content -->
					<div class="p-6 sm:p-7 lg:p-8 z-10">
						<!-- Pill Badge with Icon -->
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
							<span>{{ settings.apply_hero_badge || "VOLUNTEER ENROLLMENT" }}</span>
						</div>

						<!-- Headline -->
						<h1
							class="text-2xl sm:text-[26px] lg:text-[28px] font-extrabold text-white tracking-tight leading-[1.2] mt-4"
						>
							{{
								settings.apply_hero_title || "Step Forward. Create Lasting Impact."
							}}
						</h1>

						<!-- Description -->
						<p
							class="text-emerald-100/90 text-xs sm:text-[13px] leading-relaxed mt-2.5 font-normal"
						>
							{{
								settings.apply_hero_description ||
								"Join our dedicated volunteer community. Whether tutoring students, planting saplings, or coordinating local relief drives, your time drives tangible community change."
							}}
						</p>
					</div>

					<!-- Bottom: Edge-to-Edge Photo with Top Gradient Fade -->
					<div
						class="relative w-full h-52 sm:h-60 lg:h-64 mt-auto overflow-hidden shrink-0"
					>
						<div
							class="absolute inset-x-0 top-0 h-16 bg-gradient-to-b from-[#064e3b] via-[#064e3b]/50 to-transparent z-10 pointer-events-none"
						></div>
						<img
							:src="settings.apply_hero_image || volunteersPlanting"
							alt="Volunteers in action"
							class="w-full h-full object-cover object-center"
						/>
					</div>
				</div>

				<!-- Right Side: Application Form with smooth vertical scrolling -->
				<div
					class="p-6 sm:p-7 lg:p-8 overflow-y-auto max-h-[calc(100vh-105px)] bg-white flex flex-col justify-between"
				>
					<div>
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
							{{ settings.apply_form_title || "Apply to be a Volunteer" }}
						</h2>
						<p class="text-xs text-black-500 mt-1 leading-normal">
							{{
								settings.apply_form_subtitle ||
								"Fields marked with an asterisk (*) are mandatory."
							}}
						</p>

						<!-- Success State Message -->
						<div
							v-if="success"
							class="mt-4 p-6 rounded-2xl bg-emerald-50 border border-emerald-200 text-center space-y-3"
						>
							<div
								class="w-12 h-12 bg-emerald-100 text-emerald-700 rounded-full flex items-center justify-center mx-auto"
							>
								<svg
									class="w-6 h-6"
									viewBox="0 0 24 24"
									fill="none"
									stroke="currentColor"
									stroke-width="2"
									stroke-linecap="round"
									stroke-linejoin="round"
								>
									<polyline points="20 6 9 17 4 12" />
								</svg>
							</div>
							<h3 class="text-base font-bold text-emerald-950">
								Application Submitted!
							</h3>
							<p class="text-xs text-emerald-800 leading-relaxed">
								Thank you for applying to be a volunteer. Our administrative team
								will review your application and send updates to your registered
								email address.
							</p>
							<div class="pt-2">
								<router-link
									to="/account/login"
									class="inline-flex items-center justify-center px-4 py-2 rounded-xl text-xs font-bold text-white bg-[#064e3b] hover:bg-[#043d2e] transition shadow-sm"
								>
									Return to Sign In
								</router-link>
							</div>
						</div>

						<!-- Main Application Form -->
						<form v-else @submit.prevent="submitForm" class="space-y-3 mt-3.5">
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

							<!-- Row 1: Full Name & Email Address -->
							<div class="grid grid-cols-1 sm:grid-cols-2 gap-2.5">
								<div class="space-y-1">
									<label
										class="block text-[10px] font-bold text-black-700 uppercase tracking-wider"
									>
										Full Name <span class="text-red-500">*</span>
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
												<path
													d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"
												/>
												<circle cx="12" cy="7" r="4" />
											</svg>
										</div>
										<input
											v-model="form.applicant_name"
											type="text"
											required
											placeholder="John Doe"
											class="block w-full pl-10 pr-3.5 py-2 text-xs lg:text-sm text-black-900 placeholder-black-400 bg-transparent rounded-xl focus:outline-none"
										/>
									</div>
								</div>

								<div class="space-y-1">
									<label
										class="block text-[10px] font-bold text-black-700 uppercase tracking-wider"
									>
										Email Address <span class="text-red-500">*</span>
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
												<path
													d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"
												/>
											</svg>
										</div>
										<input
											v-model="form.email"
											type="email"
											required
											placeholder="you@example.com"
											class="block w-full pl-10 pr-3.5 py-2 text-xs lg:text-sm text-black-900 placeholder-black-400 bg-transparent rounded-xl focus:outline-none"
										/>
									</div>
								</div>
							</div>

							<!-- Row 2: Phone Number & Date of Birth -->
							<div class="grid grid-cols-1 sm:grid-cols-2 gap-2.5">
								<div class="space-y-1">
									<label
										class="block text-[10px] font-bold text-black-700 uppercase tracking-wider"
									>
										Phone Number <span class="text-red-500">*</span>
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
												<path
													d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"
												/>
											</svg>
										</div>
										<input
											v-model="form.phone"
											type="tel"
											maxlength="15"
											required
											@input="onPhoneInput"
											placeholder="9876543210"
											class="block w-full pl-10 pr-3.5 py-2 text-xs lg:text-sm text-black-900 placeholder-black-400 bg-transparent rounded-xl focus:outline-none"
										/>
									</div>
								</div>

								<div class="space-y-1">
									<label
										class="block text-[10px] font-bold text-black-700 uppercase tracking-wider"
									>
										Date of Birth <span class="text-red-500">*</span>
									</label>
									<FrappeDatePicker
										v-model="form.date_of_birth"
										placeholder="YYYY-MM-DD"
										:required="true"
									/>
								</div>
							</div>

							<!-- Row 3: Gender (Full Width Evenly Split across 3 columns) -->
							<div class="space-y-1">
								<label
									class="block text-[10px] font-bold text-black-700 uppercase tracking-wider"
								>
									Gender <span class="text-red-500">*</span>
								</label>
								<div class="grid grid-cols-3 w-full py-1.5 px-3.5">
									<label
										v-for="option in ['Male', 'Female', 'Other']"
										:key="option"
										class="flex items-center gap-2 cursor-pointer text-xs lg:text-sm text-black-700 hover:text-black-900 select-none"
									>
										<input
											type="radio"
											name="gender"
											:value="option"
											v-model="form.gender"
											required
											class="w-4 h-4 text-emerald-700 border-black-300 focus:ring-emerald-700 focus:ring-2 accent-emerald-700 cursor-pointer"
										/>
										<span>{{ option }}</span>
									</label>
								</div>
							</div>

							<!-- Row 4: Residential Address -->
							<div class="space-y-1">
								<label
									class="block text-[10px] font-bold text-black-700 uppercase tracking-wider"
								>
									Residential Address <span class="text-red-500">*</span>
								</label>
								<div
									class="relative rounded-xl border border-black-200 focus-within:border-emerald-700 focus-within:ring-2 focus-within:ring-emerald-700/15 transition shadow-sm bg-white"
								>
									<textarea
										v-model="form.address"
										required
										rows="2"
										placeholder="Enter your street address, city, and pincode..."
										class="block w-full px-3.5 py-2 text-xs lg:text-sm text-black-900 placeholder-black-400 bg-transparent rounded-xl focus:outline-none resize-none"
									></textarea>
								</div>
							</div>

							<!-- Row 5: Skills & Interests -->
							<div class="space-y-1.5 pt-1">
								<div class="flex items-center justify-between">
									<label
										class="block text-[10px] font-bold text-black-700 uppercase tracking-wider"
									>
										Skills & Interests <span class="text-red-500">*</span>
									</label>
									<button
										type="button"
										@click="addSkill"
										class="text-[11px] font-bold text-emerald-700 hover:text-emerald-900 flex items-center gap-1 hover:underline"
									>
										+ Add Skill
									</button>
								</div>
								<div
									v-for="(skillItem, idx) in form.skills"
									:key="idx"
									class="flex items-center gap-2"
								>
									<select
										v-model="skillItem.skill"
										required
										class="flex-1 px-3 py-1.5 text-xs text-black-900 bg-white border border-black-200 rounded-xl focus:border-emerald-700 focus:outline-none"
									>
										<option value="" disabled>Select a Skill...</option>
										<option
											v-for="s in availableSkills"
											:key="s.name"
											:value="s.name"
										>
											{{ s.label || s.name }}
										</option>
									</select>
									<select
										v-model="skillItem.proficiency"
										class="w-28 px-2 py-1.5 text-xs text-black-900 bg-white border border-black-200 rounded-xl focus:border-emerald-700 focus:outline-none"
									>
										<option value="Beginner">Beginner</option>
										<option value="Intermediate">Intermediate</option>
										<option value="Expert">Expert</option>
									</select>
									<button
										v-if="form.skills.length > 1"
										type="button"
										@click="removeSkill(idx)"
										class="p-1.5 text-black-400 hover:text-red-600 rounded-lg hover:bg-red-50 transition"
									>
										<svg
											class="w-4 h-4"
											viewBox="0 0 24 24"
											fill="none"
											stroke="currentColor"
											stroke-width="2"
										>
											<line x1="18" y1="6" x2="6" y2="18" />
											<line x1="6" y1="6" x2="18" y2="18" />
										</svg>
									</button>
								</div>
							</div>

							<!-- Row 6: Weekly Availability -->
							<div class="space-y-1.5 pt-1">
								<div class="flex items-center justify-between">
									<label
										class="block text-[10px] font-bold text-black-700 uppercase tracking-wider"
									>
										Weekly Availability (Optional)
									</label>
									<button
										type="button"
										@click="addAvailability"
										class="text-[11px] font-bold text-emerald-700 hover:text-emerald-900 flex items-center gap-1 hover:underline"
									>
										+ Add Availability
									</button>
								</div>
								<div
									v-if="form.availability.length === 0"
									class="text-[11px] text-red-400 italic"
								>
									No availability slots added. Click "+ Add Availability" to
									specify open hours.
								</div>
								<div
									v-for="(slot, idx) in form.availability"
									:key="idx"
									class="flex items-center gap-2"
								>
									<select
										v-model="slot.day_of_week"
										required
										class="w-28 px-2 py-1.5 text-xs text-black-900 bg-white border border-black-200 rounded-xl focus:border-emerald-700 focus:outline-none"
									>
										<option value="" disabled>Day</option>
										<option value="Monday">Monday</option>
										<option value="Tuesday">Tuesday</option>
										<option value="Wednesday">Wednesday</option>
										<option value="Thursday">Thursday</option>
										<option value="Friday">Friday</option>
										<option value="Saturday">Saturday</option>
										<option value="Sunday">Sunday</option>
									</select>
									<input
										v-model="slot.from_time"
										type="time"
										required
										class="flex-1 px-2 py-1.5 text-xs text-black-900 bg-white border border-black-200 rounded-xl focus:border-emerald-700 focus:outline-none"
									/>
									<span class="text-xs text-black-400">to</span>
									<input
										v-model="slot.to_time"
										type="time"
										required
										class="flex-1 px-2 py-1.5 text-xs text-black-900 bg-white border border-black-200 rounded-xl focus:border-emerald-700 focus:outline-none"
									/>
									<button
										type="button"
										@click="removeAvailability(idx)"
										class="p-1.5 text-black-400 hover:text-red-600 rounded-lg hover:bg-red-50 transition"
									>
										<svg
											class="w-4 h-4"
											viewBox="0 0 24 24"
											fill="none"
											stroke="currentColor"
											stroke-width="2"
										>
											<line x1="18" y1="6" x2="6" y2="18" />
											<line x1="6" y1="6" x2="18" y2="18" />
										</svg>
									</button>
								</div>
							</div>

							<!-- Submit Button -->
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
									Submitting Application...
								</span>
								<span v-else class="flex items-center gap-2">
									<span>{{
										settings.apply_submit_button_label || "Submit Application"
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

							<!-- Secondary Sign In Button -->
							<router-link
								to="/account/login"
								class="w-full py-2 px-4 rounded-xl text-xs lg:text-sm font-bold text-emerald-950 bg-emerald-50 hover:bg-emerald-100/90 border border-emerald-200/60 focus:ring-2 focus:ring-emerald-700 transition flex items-center justify-center gap-2 text-center shadow-sm"
							>
								<svg
									class="w-3.5 h-3.5 text-emerald-700"
									viewBox="0 0 24 24"
									fill="none"
									stroke="currentColor"
									stroke-width="2"
								>
									<path d="M15 3h4a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2h-4"></path>
									<polyline points="10 17 15 12 10 7"></polyline>
									<line x1="15" y1="12" x2="3" y2="12"></line>
								</svg>
								<span>{{
									settings.apply_login_button_label ||
									"Already registered? Sign In to Dashboard"
								}}</span>
							</router-link>
						</form>
					</div>
				</div>
			</div>
		</main>

		<!-- Bottom Page Footer -->
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
import volunteersPlanting from "@/assets/volunteers_planting.jpg";
import FrappeDatePicker from "@/components/FrappeDatePicker.vue";
import { call, createResource } from "frappe-ui";
import { computed, onMounted, ref } from "vue";

const availableSkills = ref([]);

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

onMounted(async () => {
	try {
		const res = await call("ngo.api.volunteer.get_all_skills");
		const raw = Array.isArray(res) ? res : res?.message || [];
		availableSkills.value = raw.map((s) => {
			if (typeof s === "string") return { name: s, label: s };
			return { name: s.name, label: s.skill_name || s.name };
		});
	} catch (err) {
		console.warn("Failed to load skills list:", err);
	}
});

const form = ref({
	applicant_name: "",
	email: "",
	phone: "",
	date_of_birth: "",
	gender: "",
	address: "",
	skills: [{ skill: "", proficiency: "Beginner" }],
	availability: [],
});

const loading = ref(false);
const error = ref("");
const success = ref(false);

// Phone input handler: strictly allow numbers only
function onPhoneInput(e) {
	if (form.value.phone) {
		form.value.phone = form.value.phone.replace(/[^0-9]/g, "");
	}
}

function addSkill() {
	form.value.skills.push({ skill: "", proficiency: "Beginner" });
}

function removeSkill(index) {
	form.value.skills.splice(index, 1);
}

function addAvailability() {
	form.value.availability.push({ day_of_week: "", from_time: "", to_time: "" });
}

function removeAvailability(index) {
	form.value.availability.splice(index, 1);
}

function validateEmail(email) {
	return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
}

async function submitForm() {
	error.value = "";

	// 1. Full Name validation
	if (!form.value.applicant_name || !form.value.applicant_name.trim()) {
		error.value = "Full Name is mandatory.";
		return;
	}

	// 2. Email Address validation
	if (!form.value.email || !form.value.email.trim() || !validateEmail(form.value.email.trim())) {
		error.value = "A valid Email Address is mandatory.";
		return;
	}

	// 3. Phone Number: Mandatory & numbers only
	if (!form.value.phone || !form.value.phone.trim()) {
		error.value = "Phone Number is mandatory.";
		return;
	}
	const cleanPhone = form.value.phone.trim();
	if (!/^\d+$/.test(cleanPhone)) {
		error.value = "Phone Number must contain only digits.";
		return;
	}
	if (cleanPhone.length < 7 || cleanPhone.length > 15) {
		error.value = "Phone Number must be between 7 and 15 digits.";
		return;
	}

	// 4. Date of Birth: Mandatory
	if (!form.value.date_of_birth) {
		error.value = "Date of Birth is mandatory.";
		return;
	}

	// 5. Gender: Mandatory
	if (!form.value.gender) {
		error.value = "Gender is mandatory. Please select your gender.";
		return;
	}

	// 6. Address: Mandatory
	if (!form.value.address || !form.value.address.trim()) {
		error.value = "Residential Address is mandatory.";
		return;
	}

	// 7. Skills & Interests: Mandatory (at least one skill with a value selected)
	if (!form.value.skills || form.value.skills.length === 0) {
		error.value = "Skills & Interests are mandatory. Please add at least one skill.";
		return;
	}
	const validSkills = form.value.skills.filter((s) => s.skill && s.skill.trim());
	if (validSkills.length === 0) {
		error.value = "Please select a skill from the dropdown for your skill entry.";
		return;
	}

	loading.value = true;

	try {
		const res = await call("ngo.api.volunteer.submit_application", {
			applicant_name: form.value.applicant_name.trim(),
			email: form.value.email.trim(),
			phone: cleanPhone,
			date_of_birth: form.value.date_of_birth,
			gender: form.value.gender,
			address: form.value.address.trim(),
			skills: JSON.stringify(validSkills),
			availability: JSON.stringify(form.value.availability || []),
		});

		if (res && res.status === "error") {
			error.value = res.message;
		} else {
			success.value = true;
		}
	} catch (err) {
		error.value = err.message || err.exc || "Failed to submit application. Please try again.";
	} finally {
		loading.value = false;
	}
}
</script>
