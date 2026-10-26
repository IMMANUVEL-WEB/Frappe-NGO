<template>
	<div class="space-y-6">
		<!-- ROW 1: 5 KPI CARDS -->
		<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-4">
			<!-- 1. Total Given -->
			<div
				class="bg-white rounded-2xl p-5 border border-slate-100 shadow-xs flex flex-col justify-between hover:shadow-md transition"
			>
				<div>
					<div class="flex items-center space-x-3 mb-2.5">
						<div
							class="w-10 h-10 rounded-xl bg-emerald-50 text-emerald-600 flex items-center justify-center text-lg font-black border border-emerald-100/60"
						>
							₹
						</div>
						<div>
							<span
								class="text-[11px] font-bold uppercase tracking-wider text-slate-400"
								>Total Given</span
							>
							<div
								class="text-xl md:text-2xl font-black text-slate-900 tracking-tight"
							>
								{{ formatCurrencyDisplay(kpis.total_given) }}
							</div>
						</div>
					</div>
					<div class="text-xs text-slate-400 font-medium">
						Committed {{ formatCurrencyDisplay(kpis.total_committed) }}
					</div>
				</div>
				<div class="mt-4 pt-3 border-t border-slate-50">
					<div class="w-full bg-slate-100 rounded-full h-1.5 overflow-hidden mb-1.5">
						<div
							class="bg-[#00875A] h-1.5 rounded-full transition-all duration-700"
							:style="{
								width: `${Math.min(kpis.percent_given_committed || 0, 100)}%`,
							}"
						></div>
					</div>
					<div class="text-right text-[11px] text-slate-400 font-medium">
						{{ kpis.percent_given_committed || 0 }}% committed
					</div>
				</div>
			</div>

			<!-- 2. Total Spend -->
			<div
				class="bg-white rounded-2xl p-5 border border-slate-100 shadow-xs flex flex-col justify-between hover:shadow-md transition"
			>
				<div>
					<div class="flex items-center space-x-3 mb-2.5">
						<div
							class="w-10 h-10 rounded-xl bg-blue-50 text-blue-600 flex items-center justify-center border border-blue-100/60"
						>
							<svg
								class="w-5 h-5"
								fill="none"
								stroke="currentColor"
								viewBox="0 0 24 24"
							>
								<path
									stroke-linecap="round"
									stroke-linejoin="round"
									stroke-width="2"
									d="M3 10h18M7 15h1m4 0h1m-7 4h12a3 3 0 003-3V8a3 3 0 00-3-3H6a3 3 0 00-3 3v8a3 3 0 003 3z"
								/>
							</svg>
						</div>
						<div>
							<span
								class="text-[11px] font-bold uppercase tracking-wider text-slate-400"
								>Total Spend</span
							>
							<div
								class="text-xl md:text-2xl font-black text-slate-900 tracking-tight"
							>
								{{ formatCurrencyDisplay(kpis.total_spent) }}
							</div>
						</div>
					</div>
					<div class="text-xs text-slate-400 font-medium">
						{{ kpis.percent_spent_given || 0 }}% of funds received
					</div>
				</div>
				<div class="mt-4 pt-3 border-t border-slate-50">
					<div class="w-full bg-slate-100 rounded-full h-1.5 overflow-hidden mb-1.5">
						<div
							class="bg-blue-600 h-1.5 rounded-full transition-all duration-700"
							:style="{
								width: `${Math.min(kpis.percent_spent_given || 0, 100)}%`,
							}"
						></div>
					</div>
					<div class="text-right text-[11px] text-slate-400 font-medium">
						{{ kpis.percent_spent_given || 0 }}% utilized
					</div>
				</div>
			</div>

			<!-- 3. Balance Available -->
			<div
				class="bg-white rounded-2xl p-5 border border-slate-100 shadow-xs flex flex-col justify-between hover:shadow-md transition"
			>
				<div>
					<div class="flex items-center space-x-3 mb-2.5">
						<div
							class="w-10 h-10 rounded-xl bg-amber-50 text-amber-500 flex items-center justify-center border border-amber-100/60"
						>
							<svg
								class="w-5 h-5"
								fill="none"
								stroke="currentColor"
								viewBox="0 0 24 24"
							>
								<path
									stroke-linecap="round"
									stroke-linejoin="round"
									stroke-width="2"
									d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
								/>
							</svg>
						</div>
						<div>
							<span
								class="text-[11px] font-bold uppercase tracking-wider text-slate-400"
								>Balance Available</span
							>
							<div
								class="text-xl md:text-2xl font-black text-slate-900 tracking-tight"
							>
								{{ formatCurrencyDisplay(kpis.balance_available) }}
							</div>
						</div>
					</div>
					<div class="text-xs text-slate-400 font-medium">
						Committed balance
						{{ formatCurrencyDisplay(kpis.committed_balance) }}
					</div>
				</div>
				<div class="mt-4 pt-3 border-t border-slate-50">
					<div class="w-full bg-slate-100 rounded-full h-1.5 overflow-hidden mb-1.5">
						<div
							class="bg-amber-400 h-1.5 rounded-full transition-all duration-700"
							:style="{
								width: `${
									kpis.total_committed > 0
										? Math.min(
												(kpis.balance_available / kpis.total_committed) *
													100,
												100
										  )
										: 0
								}%`,
							}"
						></div>
					</div>
					<div class="text-right text-[11px] text-slate-400 font-medium">
						Liquid reserves
					</div>
				</div>
			</div>

			<!-- 4. Active Grants -->
			<div
				class="bg-white rounded-2xl p-5 border border-slate-100 shadow-xs flex flex-col justify-between hover:shadow-md transition"
			>
				<div>
					<div class="flex items-center space-x-3 mb-2.5">
						<div
							class="w-10 h-10 rounded-xl bg-purple-50 text-purple-600 flex items-center justify-center border border-purple-100/60"
						>
							<svg
								class="w-5 h-5"
								fill="none"
								stroke="currentColor"
								viewBox="0 0 24 24"
							>
								<path
									stroke-linecap="round"
									stroke-linejoin="round"
									stroke-width="2"
									d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"
								/>
							</svg>
						</div>
						<div>
							<span
								class="text-[11px] font-bold uppercase tracking-wider text-slate-400"
								>Active Grants</span
							>
							<div
								class="text-xl md:text-2xl font-black text-slate-900 tracking-tight"
							>
								{{ kpis.active_grants_count || 0 }}
							</div>
						</div>
					</div>
					<div class="text-xs text-slate-400 font-medium">
						{{ kpis.expiring_soon_count || 0 }} expiring within 90 days
					</div>
				</div>
				<div class="mt-4 pt-3 border-t border-slate-50">
					<div
						class="text-[11px] text-purple-700 font-medium flex items-center space-x-1.5"
					>
						<svg
							class="w-3.5 h-3.5"
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
						<span>{{ kpis.expiring_soon_count || 0 }} expiring within 90 days</span>
					</div>
				</div>
			</div>

			<!-- 5. Total Purchase Amount -->
			<div
				class="bg-white rounded-2xl p-5 border border-slate-100 shadow-xs flex flex-col justify-between hover:shadow-md transition"
			>
				<div>
					<div class="flex items-center space-x-3 mb-2.5">
						<div
							class="w-10 h-10 rounded-xl bg-teal-50 text-teal-600 flex items-center justify-center border border-teal-100/60"
						>
							<svg
								class="w-5 h-5"
								fill="none"
								stroke="currentColor"
								viewBox="0 0 24 24"
							>
								<path
									stroke-linecap="round"
									stroke-linejoin="round"
									stroke-width="2"
									d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z"
								/>
							</svg>
						</div>
						<div>
							<span
								class="text-[11px] font-bold uppercase tracking-wider text-slate-400"
								>Total Purchase</span
							>
							<div
								class="text-xl md:text-2xl font-black text-slate-900 tracking-tight"
							>
								{{ formatCurrencyDisplay(kpis.total_purchase_amount) }}
							</div>
						</div>
					</div>
					<div class="text-xs text-slate-400 font-medium">Goods and services bought</div>
				</div>
				<div class="mt-4 pt-3 border-t border-slate-50">
					<div
						class="text-[11px] text-teal-700 font-semibold flex items-center justify-between"
					>
						<span>Verified Invoices</span>
						<span>100% Tax Compliant</span>
					</div>
				</div>
			</div>
		</div>

		<!-- ROW 2: VISUALIZATIONS -->
		<div class="grid grid-cols-1 lg:grid-cols-12 gap-6">
			<!-- Given vs Spent by Month (Lakh) (7 cols) -->
			<div
				class="lg:col-span-7 bg-white rounded-2xl p-6 border border-slate-100 shadow-xs flex flex-col justify-between min-h-[350px]"
			>
				<!-- Header -->
				<div
					class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pb-4 border-b border-slate-100"
				>
					<div class="flex items-center space-x-3">
						<div
							class="w-9 h-9 rounded-xl bg-blue-50 text-blue-600 flex items-center justify-center border border-blue-100/60"
						>
							<svg
								class="w-5 h-5"
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
						</div>
						<div>
							<h2 class="text-sm font-bold text-slate-900 tracking-tight">
								Given vs Spent by Month (Lakh)
							</h2>
							<p class="text-[11px] text-slate-400 font-medium">
								Funds received from grants vs actual project disbursements
							</p>
						</div>
					</div>

					<!-- Legend Pills -->
					<div class="flex items-center gap-2">
						<span
							class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-lg text-xs font-semibold bg-blue-50/80 text-blue-700 border border-blue-100"
						>
							<span class="w-2 h-2 rounded-full bg-blue-600"></span>
							Given
						</span>
						<span
							class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-lg text-xs font-semibold bg-amber-50/80 text-amber-700 border border-amber-100"
						>
							<span class="w-2 h-2 rounded-full bg-amber-500"></span>
							Spent
						</span>
					</div>
				</div>

				<!-- Custom Visual Vertical Bar Chart -->
				<div class="relative pt-6 pb-2 min-h-[250px] flex flex-col justify-end">
					<!-- Background Grid Lines with Dynamic Y-Axis scale -->
					<div
						class="absolute inset-x-0 inset-y-4 flex flex-col justify-between pointer-events-none text-[10px] text-slate-400 font-medium"
					>
						<div
							v-for="tick in yAxisTicks"
							:key="tick"
							class="border-b border-slate-100/90 pb-0.5 flex justify-between"
						>
							<span class="font-mono text-slate-400 text-[10px]">?{{ tick }}L</span>
						</div>
					</div>

					<!-- Bars Container with background pillar tracks -->
					<div
						class="relative h-48 ml-10 mr-2 flex items-end justify-between z-10 gap-2 sm:gap-3"
					>
						<div
							v-for="(item, idx) in monthlySeries"
							:key="idx"
							class="flex flex-col items-center flex-1 h-full justify-end relative cursor-pointer group"
							@mouseenter="hoveredMonthIndex = idx"
							@mouseleave="hoveredMonthIndex = null"
						>
							<!-- Dynamic Floating Hover Tooltip (Smooth & only shown on hover) -->
							<transition
								enter-active-class="transition duration-150 ease-out"
								enter-from-class="opacity-0 translate-y-1"
								enter-to-class="opacity-100 translate-y-0"
								leave-active-class="transition duration-100 ease-in"
								leave-from-class="opacity-100 translate-y-0"
								leave-to-class="opacity-0 translate-y-1"
							>
								<div
									v-if="hoveredMonthIndex === idx"
									class="absolute -top-16 left-1/2 -translate-x-1/2 bg-slate-900/95 backdrop-blur-xs text-white text-[11px] rounded-xl py-2 px-3 shadow-xl border border-slate-800 whitespace-nowrap z-30 pointer-events-none"
								>
									<div
										class="font-bold text-slate-300 border-b border-slate-700/60 pb-1 mb-1 text-[10px] uppercase tracking-wider text-center"
									>
										{{ item.month_year || item.month }}
									</div>
									<div class="flex items-center gap-2.5">
										<span
											class="flex items-center gap-1 font-semibold text-blue-300"
										>
											<span
												class="w-1.5 h-1.5 rounded-full bg-blue-400"
											></span>
											Given: ?{{ item.given }} L
										</span>
										<span class="text-slate-600">|</span>
										<span
											class="flex items-center gap-1 font-semibold text-amber-300"
										>
											<span
												class="w-1.5 h-1.5 rounded-full bg-amber-400"
											></span>
											Spent: ?{{ item.spent }} L
										</span>
									</div>
								</div>
							</transition>

							<!-- Pillar Slot -->
							<div
								class="w-full max-w-[44px] h-40 rounded-xl bg-slate-50/80 border border-slate-100 flex items-end justify-center gap-1 sm:gap-1.5 p-1 transition-all duration-200"
								:class="
									hoveredMonthIndex === idx
										? 'bg-slate-100 ring-2 ring-emerald-500/20'
										: ''
								"
							>
								<!-- Bar 1: Given (Blue gradient) -->
								<div class="w-2.5 sm:w-3 h-full flex items-end justify-center">
									<div
										class="w-full bg-gradient-to-t from-blue-600 to-sky-400 rounded-t-md transition-all duration-500 shadow-xs"
										:style="{ height: getBarHeight(item.given) + '%' }"
									></div>
								</div>

								<!-- Bar 2: Spent (Amber gradient) -->
								<div class="w-2.5 sm:w-3 h-full flex items-end justify-center">
									<div
										class="w-full bg-gradient-to-t from-amber-500 to-amber-300 rounded-t-md transition-all duration-500 shadow-xs"
										:style="{ height: getBarHeight(item.spent) + '%' }"
									></div>
								</div>
							</div>

							<!-- Month Name -->
							<span
								class="text-[11px] font-semibold mt-2 transition"
								:class="
									item.given > 0 || item.spent > 0
										? 'text-slate-900 font-bold'
										: 'text-slate-400'
								"
							>
								{{ item.month }}
							</span>
						</div>
					</div>
				</div>
			</div>

			<!-- Spend by category & Spend by project (5 cols) -->
			<div
				class="lg:col-span-5 bg-white rounded-2xl p-6 border border-slate-100 shadow-xs flex flex-col justify-between space-y-5"
			>
				<!-- Spend by category with Donut and Cards -->
				<div>
					<div class="flex items-center justify-between mb-4">
						<div class="flex items-center space-x-2.5">
							<div
								class="w-9 h-9 rounded-xl bg-teal-50 text-teal-600 flex items-center justify-center border border-teal-100/60"
							>
								<svg
									class="w-5 h-5"
									fill="none"
									stroke="currentColor"
									viewBox="0 0 24 24"
								>
									<path
										stroke-linecap="round"
										stroke-linejoin="round"
										stroke-width="2"
										d="M11 3.055A9.001 9.001 0 1020.945 13H11V3.055z"
									/>
									<path
										stroke-linecap="round"
										stroke-linejoin="round"
										stroke-width="2"
										d="M20.488 9H15V3.512A9.025 9.025 0 0120.488 9z"
									/>
								</svg>
							</div>
							<div>
								<h2 class="text-sm font-bold text-slate-900 tracking-tight">
									Spend by category
								</h2>
								<p class="text-[11px] text-slate-400 font-medium">
									Budget classification & allocation
								</p>
							</div>
						</div>
						<span
							class="text-[11px] font-bold text-teal-700 bg-teal-50 px-2 py-0.5 rounded-full border border-teal-100"
						>
							3 Categories
						</span>
					</div>

					<!-- Donut + Breakdown Row -->
					<div class="flex items-center gap-4">
						<!-- Modern SVG Donut Gauge -->
						<div class="relative w-28 h-28 shrink-0 flex items-center justify-center">
							<svg class="w-28 h-28 -rotate-90 transform" viewBox="0 0 100 100">
								<!-- Background Circle -->
								<circle
									cx="50"
									cy="50"
									r="38"
									stroke="currentColor"
									stroke-width="9"
									class="text-slate-100"
									fill="transparent"
								/>
								<!-- CapEx Segment -->
								<circle
									v-if="categoryDonut.hasData"
									cx="50"
									cy="50"
									r="38"
									stroke="#06b6d4"
									stroke-width="9"
									stroke-linecap="round"
									:stroke-dasharray="categoryDonut.capexDash"
									:stroke-dashoffset="categoryDonut.capexOffset"
									fill="transparent"
									class="transition-all duration-700"
								/>
								<!-- OpEx Segment -->
								<circle
									v-if="categoryDonut.hasData"
									cx="50"
									cy="50"
									r="38"
									stroke="#10b981"
									stroke-width="9"
									stroke-linecap="round"
									:stroke-dasharray="categoryDonut.opexDash"
									:stroke-dashoffset="categoryDonut.opexOffset"
									fill="transparent"
									class="transition-all duration-700"
								/>
								<!-- Admin Segment -->
								<circle
									v-if="categoryDonut.hasData"
									cx="50"
									cy="50"
									r="38"
									stroke="#f59e0b"
									stroke-width="9"
									stroke-linecap="round"
									:stroke-dasharray="categoryDonut.adminDash"
									:stroke-dashoffset="categoryDonut.adminOffset"
									fill="transparent"
									class="transition-all duration-700"
								/>
							</svg>
							<!-- Center Text inside Donut -->
							<div
								class="absolute inset-0 flex flex-col items-center justify-center text-center pointer-events-none"
							>
								<span
									class="text-[10px] font-bold uppercase tracking-wider text-slate-400"
									>Total</span
								>
								<span class="text-xs font-black text-slate-900 leading-tight">
									{{ formatCurrencyDisplay(kpis.total_spent) }}
								</span>
							</div>
						</div>

						<!-- Category Detail Pills -->
						<div class="flex-1 space-y-2 text-xs">
							<!-- CapEx -->
							<div
								class="flex items-center justify-between p-2 rounded-xl bg-cyan-50/50 border border-cyan-100/70 hover:bg-cyan-50 transition"
							>
								<div class="flex items-center space-x-2">
									<span class="w-2.5 h-2.5 rounded-full bg-cyan-500"></span>
									<span class="font-semibold text-slate-800">CapEx</span>
								</div>
								<div class="text-right">
									<span class="font-bold text-slate-900"
										>?{{ spendByCategory.capex?.amount || 0 }} L</span
									>
									<span class="text-[10px] font-bold text-cyan-600 ml-1.5"
										>({{ spendByCategory.capex?.percent || 0 }}%)</span
									>
								</div>
							</div>

							<!-- OpEx -->
							<div
								class="flex items-center justify-between p-2 rounded-xl bg-emerald-50/50 border border-emerald-100/70 hover:bg-emerald-50 transition"
							>
								<div class="flex items-center space-x-2">
									<span class="w-2.5 h-2.5 rounded-full bg-emerald-500"></span>
									<span class="font-semibold text-slate-800">OpEx</span>
								</div>
								<div class="text-right">
									<span class="font-bold text-slate-900"
										>?{{ spendByCategory.opex?.amount || 0 }} L</span
									>
									<span class="text-[10px] font-bold text-emerald-600 ml-1.5"
										>({{ spendByCategory.opex?.percent || 0 }}%)</span
									>
								</div>
							</div>

							<!-- Admin -->
							<div
								class="flex items-center justify-between p-2 rounded-xl bg-amber-50/50 border border-amber-100/70 hover:bg-amber-50 transition"
							>
								<div class="flex items-center space-x-2">
									<span class="w-2.5 h-2.5 rounded-full bg-amber-500"></span>
									<span class="font-semibold text-slate-800">Admin</span>
								</div>
								<div class="text-right">
									<span class="font-bold text-slate-900"
										>?{{ spendByCategory.admin?.amount || 0 }} L</span
									>
									<span class="text-[10px] font-bold text-amber-600 ml-1.5"
										>({{ spendByCategory.admin?.percent || 0 }}%)</span
									>
								</div>
							</div>
						</div>
					</div>
				</div>

				<!-- Spend by project with modern styling -->
				<div class="border-t border-slate-100 pt-4">
					<div class="flex items-center justify-between mb-3">
						<div class="flex items-center space-x-2">
							<svg
								class="w-4 h-4 text-indigo-600"
								fill="none"
								stroke="currentColor"
								viewBox="0 0 24 24"
							>
								<path
									stroke-linecap="round"
									stroke-linejoin="round"
									stroke-width="2"
									d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"
								/>
							</svg>
							<h2 class="text-sm font-bold text-slate-900 tracking-tight">
								Spend by project
							</h2>
						</div>
						<span class="text-[11px] text-slate-400 font-medium"
							>Disbursed Projects</span
						>
					</div>

					<div v-if="projectSpendList.length" class="space-y-3">
						<div
							v-for="(p, idx) in projectSpendList"
							:key="idx"
							class="p-3 rounded-xl bg-slate-50/70 border border-slate-100 hover:bg-slate-50 transition"
						>
							<div class="flex justify-between items-center mb-1.5">
								<div class="flex items-center space-x-2 min-w-0">
									<span class="w-2 h-2 rounded-full bg-blue-600 shrink-0"></span>
									<span class="font-bold text-slate-800 text-xs truncate">
										{{ p.project_name || p.project_id || p.name }}
									</span>
								</div>
								<span class="font-black text-slate-900 shrink-0 text-xs ml-2">
									?{{ p.amount_lakh || p.amount }} L
								</span>
							</div>
							<div class="w-full bg-slate-200/80 rounded-full h-1.5 overflow-hidden">
								<div
									class="h-1.5 rounded-full bg-gradient-to-r from-blue-600 to-teal-400 transition-all duration-500"
									:style="{ width: Math.min(p.percent || 0, 100) + '%' }"
								></div>
							</div>
						</div>
					</div>
					<div
						v-else
						class="text-xs text-slate-400 py-3 text-center bg-slate-50 rounded-xl border border-dashed border-slate-200"
					>
						No project spend recorded yet.
					</div>
				</div>
			</div>
		</div>
		<!-- ROW 3: PROJECT PROPOSALS AWAITING YOUR DECISION -->
		<div class="bg-white rounded-2xl p-5 border border-slate-100 shadow-xs">
			<div class="flex items-center justify-between mb-4">
				<div class="flex items-center space-x-2">
					<svg
						class="w-4 h-4 text-emerald-600"
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
					<h2 class="text-sm font-bold text-slate-900 tracking-tight">
						Project proposals awaiting your decision
					</h2>
				</div>
				<router-link
					to="/donor-portal/proposals"
					class="text-xs font-semibold text-emerald-600 hover:text-emerald-700 flex items-center"
				>
					View All <span class="ml-1">&gt;</span>
				</router-link>
			</div>

			<div v-if="pendingProposals.length" class="space-y-3">
				<div
					v-for="prop in pendingProposals"
					:key="prop.name"
					class="border border-slate-100 rounded-2xl p-4 flex flex-col md:flex-row items-start md:items-center justify-between gap-4 bg-slate-50/50 hover:bg-white hover:shadow-sm transition"
				>
					<!-- Left Details -->
					<div class="flex items-center space-x-4">
						<div
							class="w-12 h-12 rounded-xl bg-emerald-100/70 text-emerald-800 flex items-center justify-center font-bold text-sm shrink-0 border border-emerald-200/60"
						>
							{{ (prop.sector || "P").substring(0, 2).toUpperCase() }}
						</div>
						<div>
							<div class="flex items-center space-x-2">
								<span class="text-xs font-mono text-slate-400 font-semibold">{{
									prop.code
								}}</span>
								<span
									class="px-2 py-0.5 rounded-full text-[10px] font-bold bg-amber-100 text-amber-800 border border-amber-200"
								>
									{{ prop.state || "Pending Review" }}
								</span>
							</div>
							<h3 class="text-sm font-bold text-slate-900 mt-0.5">
								{{ prop.title }}
							</h3>
							<p class="text-xs text-slate-500 mt-0.5">
								Sector: {{ prop.sector }} &bull; CapEx: ₹{{ prop.capex_lakh }} L
								&bull; OpEx: ₹{{ prop.opex_lakh }} L &bull; Admin: ₹{{
									prop.admin_lakh
								}}
								L
							</p>
							<div class="flex items-center space-x-3 mt-3">
								<button
									type="button"
									@click="handleDecision(prop.name, 'approve')"
									class="flex items-center space-x-1 px-3 py-1 bg-emerald-600 hover:bg-emerald-700 text-black rounded-lg text-xs font-semibold shadow-xs transition"
								>
									<svg
										class="w-3.5 h-3.5"
										fill="none"
										stroke="currentColor"
										viewBox="0 0 24 24"
									>
										<path
											stroke-linecap="round"
											stroke-linejoin="round"
											stroke-width="2"
											d="M5 13l4 4L19 7"
										/>
									</svg>
									<span>Approve</span>
								</button>
								<button
									type="button"
									@click="handleDecision(prop.name, 'reject')"
									class="flex items-center space-x-1 px-3 py-1 border border-rose-300 text-rose-600 hover:bg-rose-50 rounded-lg text-xs font-semibold transition"
								>
									<svg
										class="w-3.5 h-3.5"
										fill="none"
										stroke="currentColor"
										viewBox="0 0 24 24"
									>
										<path
											stroke-linecap="round"
											stroke-linejoin="round"
											stroke-width="2"
											d="M6 18L18 6M6 6l12 12"
										/>
									</svg>
									<span>Reject</span>
								</button>
							</div>
						</div>
					</div>

					<!-- Right Budget Info Badge -->
					<div
						class="text-left md:text-right shrink-0 bg-white md:bg-transparent p-3 md:p-0 rounded-xl border md:border-0 border-slate-100"
					>
						<div class="text-lg font-black text-slate-900">
							₹{{ prop.total_budget_lakh }} L
						</div>
						<div class="text-xs text-slate-400 font-medium">
							{{ prop.duration_months }} months
						</div>
					</div>
				</div>
			</div>

			<div
				v-else
				class="text-center py-8 text-xs text-slate-400 font-medium bg-slate-50/50 rounded-2xl border border-slate-100"
			>
				No project proposals currently awaiting decision.
			</div>
		</div>
	</div>
</template>

<script setup>
import { ref, computed, onMounted } from "vue";
import { donorApi } from "../api";

const loading = ref(true);

const kpis = ref({
	total_given: 0,
	total_committed: 0,
	percent_given_committed: 0,
	total_spent: 0,
	percent_spent_given: 0,
	balance_available: 0,
	committed_balance: 0,
	active_grants_count: 0,
	expiring_soon_count: 0,
	total_purchase_amount: 0,
});

const monthlySeries = ref([
	{ month: "Apr", given: 0, spent: 0 },
	{ month: "May", given: 0, spent: 0 },
	{ month: "Jun", given: 0, spent: 0 },
	{ month: "Jul", given: 0, spent: 0 },
	{ month: "Aug", given: 0, spent: 0 },
	{ month: "Sep", given: 0, spent: 0 },
	{ month: "Oct", given: 0, spent: 0 },
]);

const spendByCategory = ref({
	capex: { amount: 0, percent: 0 },
	opex: { amount: 0, percent: 0 },
	admin: { amount: 0, percent: 0 },
});

const projectSpendList = ref([]);
const hoveredMonthIndex = ref(null);

const categoryDonut = computed(() => {
	const capex = Number(spendByCategory.value?.capex?.percent) || 0;
	const opex = Number(spendByCategory.value?.opex?.percent) || 0;
	const admin = Number(spendByCategory.value?.admin?.percent) || 0;
	const circ = 238.76;
	if (capex + opex + admin <= 0) {
		return {
			hasData: false,
			capexDash: "0 " + circ,
			capexOffset: 0,
			opexDash: "0 " + circ,
			opexOffset: 0,
			adminDash: "0 " + circ,
			adminOffset: 0,
		};
	}
	const cLen = (capex / 100) * circ;
	const oLen = (opex / 100) * circ;
	const aLen = (admin / 100) * circ;
	return {
		hasData: true,
		capexDash: cLen + " " + (circ - cLen),
		capexOffset: 0,
		opexDash: oLen + " " + (circ - oLen),
		opexOffset: -cLen,
		adminDash: aLen + " " + (circ - aLen),
		adminOffset: -(cLen + oLen),
	};
});
const pendingProposals = ref([]);

const barColors = ["bg-blue-600", "bg-teal-500", "bg-amber-400", "bg-purple-600", "bg-rose-500"];
function getBarColor(idx) {
	return barColors[idx % barColors.length];
}

const maxChartVal = computed(() => {
	const vals = (monthlySeries.value || []).flatMap((m) => [
		Number(m.given) || 0,
		Number(m.spent) || 0,
	]);
	const max = Math.max(...vals, 0);
	if (max <= 0) return 10;
	if (max <= 10) return 10;
	if (max <= 25) return 25;
	if (max <= 50) return 50;
	return Math.ceil(max * 1.15);
});

const yAxisTicks = computed(() => {
	const max = maxChartVal.value;
	return [max, Math.round(max * 0.75), Math.round(max * 0.5), Math.round(max * 0.25), 0];
});

function getBarHeight(val) {
	const num = Number(val) || 0;
	if (num <= 0) return 0;
	const max = maxChartVal.value;
	const pct = (num / max) * 100;
	return Math.max(Math.min(pct, 100), 2);
}

function formatCurrencyDisplay(val) {
	if (!val || val === 0) return "₹0";
	if (val >= 10000000) {
		return `₹${(val / 10000000).toFixed(2)} Cr`;
	}
	if (val >= 100000) {
		return `₹${(val / 100000).toFixed(2)} L`;
	}
	return `₹${Number(val).toLocaleString("en-IN")}`;
}

async function loadDashboard() {
	loading.value = true;
	try {
		const res = await donorApi.getDashboard();
		if (res) {
			if (res.kpis) kpis.value = res.kpis;
			if (res.charts?.monthly_series?.length) {
				monthlySeries.value = res.charts.monthly_series;
			}
			if (res.charts?.spend_by_category) {
				spendByCategory.value = res.charts.spend_by_category;
			}
			if (res.charts?.spend_by_project) {
				projectSpendList.value = res.charts.spend_by_project;
			}
			if (res.pending_proposals) {
				pendingProposals.value = res.pending_proposals;
			}
		}
	} catch (err) {
		console.error("Failed to load dashboard data:", err);
	} finally {
		loading.value = false;
	}
}

async function handleDecision(proposalName, action) {
	try {
		if (action === "approve") {
			await donorApi.approveProposal(proposalName);
			alert("Proposal approved successfully.");
		} else {
			const reason = prompt("Enter rejection reason (optional):");
			await donorApi.rejectProposal(proposalName, reason);
			alert("Proposal rejected.");
		}
		await loadDashboard();
	} catch (e) {
		alert(e?.message || `Failed to ${action} proposal.`);
	}
}

onMounted(() => {
	loadDashboard();
});
</script>
