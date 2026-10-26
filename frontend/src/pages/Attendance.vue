<template>
	<VolunteerLayout>
		<div class="max-w-7xl mx-auto space-y-6 pb-16">
			<!-- Top Breadcrumb & Header -->
			<div class="flex flex-col lg:flex-row lg:items-center justify-between gap-4">
				<div>
					<!-- Breadcrumb -->
					<nav class="flex items-center gap-1.5 text-xs text-black-400 font-medium mb-1">
						<router-link
							to="/"
							class="hover:text-emerald-700 transition-colors flex items-center gap-1"
						>
							<svg
								class="w-3.5 h-3.5"
								viewBox="0 0 24 24"
								fill="none"
								stroke="currentColor"
								stroke-width="2"
							>
								<path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path>
								<polyline points="9 22 9 12 15 12 15 22"></polyline>
							</svg>
						</router-link>
						<span>&rsaquo;</span>
						<span class="text-black-600">Attendance</span>
					</nav>

					<h1 class="text-2xl sm:text-3xl font-extrabold text-black-900 tracking-tight">
						Attendance Record
					</h1>
					<p class="text-black-500 text-sm mt-0.5">
						Track the hours you've contributed to your community.
					</p>
				</div>

				<!-- Date Range Filter -->
				<div class="flex flex-wrap items-center gap-2 self-start lg:self-auto">
					<div class="relative">
						<input
							type="date"
							v-model="filters.from_date"
							class="bg-white border border-black-200 rounded-xl px-3.5 py-2 text-xs font-medium text-black-700 shadow-sm focus:outline-none focus:ring-2 focus:ring-emerald-600"
						/>
					</div>
					<span class="text-xs font-semibold text-black-400">to</span>
					<div class="relative">
						<input
							type="date"
							v-model="filters.to_date"
							class="bg-white border border-black-200 rounded-xl px-3.5 py-2 text-xs font-medium text-black-700 shadow-sm focus:outline-none focus:ring-2 focus:ring-emerald-600"
						/>
					</div>
					<button
						@click="applyDateFilter"
						class="px-5 py-2 bg-[#064e3b] hover:bg-[#043226] text-white text-xs font-bold rounded-xl transition-all shadow-sm"
					>
						Filter
					</button>
				</div>
			</div>

			<!-- 3 Stat Summary Cards (Present, Absent, Half Day Count & Hours) -->
			<div class="grid grid-cols-1 sm:grid-cols-3 gap-4">
				<!-- Present Card -->
				<div
					class="bg-white rounded-2xl p-5 border border-black-100 shadow-sm hover:shadow-md transition-shadow relative overflow-hidden flex items-start justify-between"
				>
					<div class="flex items-start gap-4">
						<div
							class="w-12 h-12 rounded-xl bg-emerald-50 text-emerald-600 flex items-center justify-center flex-shrink-0 border border-emerald-100/60"
						>
							<svg
								class="w-6 h-6"
								viewBox="0 0 24 24"
								fill="none"
								stroke="currentColor"
								stroke-width="2"
							>
								<path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
								<polyline points="22 4 12 14.01 9 11.01"></polyline>
							</svg>
						</div>
						<div>
							<p
								class="text-xs font-semibold text-black-500 uppercase tracking-wider"
							>
								Present
							</p>
							<h3 class="text-2xl font-black text-black-900 mt-0.5">
								{{ presentCount }}
							</h3>
							<p class="text-xs text-emerald-600 font-semibold mt-0.5">
								{{ presentHours }} hrs contributed
							</p>
						</div>
					</div>
					<div class="text-emerald-500 opacity-60">
						<svg
							class="w-4 h-4"
							viewBox="0 0 24 24"
							fill="none"
							stroke="currentColor"
							stroke-width="2"
						>
							<path d="M18 20V10M12 20V4M6 20v-6" />
						</svg>
					</div>
				</div>

				<!-- Absent Card -->
				<div
					class="bg-white rounded-2xl p-5 border border-black-100 shadow-sm hover:shadow-md transition-shadow relative overflow-hidden flex items-start justify-between"
				>
					<div class="flex items-start gap-4">
						<div
							class="w-12 h-12 rounded-xl bg-rose-50 text-rose-600 flex items-center justify-center flex-shrink-0 border border-rose-100/60"
						>
							<svg
								class="w-6 h-6"
								viewBox="0 0 24 24"
								fill="none"
								stroke="currentColor"
								stroke-width="2"
							>
								<circle cx="12" cy="12" r="10"></circle>
								<line x1="15" y1="9" x2="9" y2="15"></line>
								<line x1="9" y1="9" x2="15" y2="15"></line>
							</svg>
						</div>
						<div>
							<p
								class="text-xs font-semibold text-black-500 uppercase tracking-wider"
							>
								Absent
							</p>
							<h3 class="text-2xl font-black text-black-900 mt-0.5">
								{{ absentCount }}
							</h3>
							<p class="text-xs text-rose-500 font-medium mt-0.5">
								{{
									absentCount === 1
										? "1 day unrecorded"
										: absentCount + " days unrecorded"
								}}
							</p>
						</div>
					</div>
					<div class="text-rose-500 opacity-60">
						<svg
							class="w-4 h-4"
							viewBox="0 0 24 24"
							fill="none"
							stroke="currentColor"
							stroke-width="2"
						>
							<path d="M18 20V10M12 20V4M6 20v-6" />
						</svg>
					</div>
				</div>

				<!-- Half Day Card -->
				<div
					class="bg-white rounded-2xl p-5 border border-black-100 shadow-sm hover:shadow-md transition-shadow relative overflow-hidden flex items-start justify-between"
				>
					<div class="flex items-start gap-4">
						<div
							class="w-12 h-12 rounded-xl bg-amber-50 text-amber-600 flex items-center justify-center flex-shrink-0 border border-amber-100/60"
						>
							<svg
								class="w-6 h-6"
								viewBox="0 0 24 24"
								fill="none"
								stroke="currentColor"
								stroke-width="2"
							>
								<circle cx="12" cy="12" r="10"></circle>
								<polyline points="12 6 12 12 16 14"></polyline>
							</svg>
						</div>
						<div>
							<p
								class="text-xs font-semibold text-black-500 uppercase tracking-wider"
							>
								Half Day
							</p>
							<h3 class="text-2xl font-black text-black-900 mt-0.5">
								{{ halfDayCount }}
							</h3>
							<p class="text-xs text-amber-600 font-semibold mt-0.5">
								{{ halfDayHours }} hrs logged
							</p>
						</div>
					</div>
					<div class="text-amber-500 opacity-60">
						<svg
							class="w-4 h-4"
							viewBox="0 0 24 24"
							fill="none"
							stroke="currentColor"
							stroke-width="2"
						>
							<path d="M18 20V10M12 20V4M6 20v-6" />
						</svg>
					</div>
				</div>
			</div>

			<!-- Ocean Blue Highlight Banner (Total Hours in Selected Period) -->
			<div
				class="bg-gradient-to-r from-[#0284c7] via-[#0396d6] to-[#0ea5e9] rounded-2xl p-6 text-white shadow-md flex flex-col sm:flex-row items-center justify-between gap-6"
			>
				<div class="flex items-center gap-4">
					<div
						class="w-12 h-12 rounded-full bg-white/20 backdrop-blur-md flex items-center justify-center flex-shrink-0 border border-white/30"
					>
						<svg
							class="w-6 h-6 text-white"
							viewBox="0 0 24 24"
							fill="none"
							stroke="currentColor"
							stroke-width="2.2"
						>
							<circle cx="12" cy="12" r="10"></circle>
							<polyline points="12 6 12 12 16 14"></polyline>
						</svg>
					</div>
					<div>
						<h3 class="text-base sm:text-lg font-bold text-white">
							Total Hours in Selected Period
						</h3>
						<p class="text-xs text-sky-100/90 font-medium">
							Based on your current filter
						</p>
					</div>
				</div>

				<div class="text-center sm:text-right">
					<div class="text-3xl sm:text-4xl font-black text-white tracking-tight">
						{{ periodTotalHours }} hrs
					</div>
				</div>
			</div>

			<!-- Filter Tabs (All, Present, Absent, Half Day) & Export Button Bar -->
			<div
				class="flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-black-200 pb-3"
			>
				<!-- Status Tabs: All, Present, Absent, Half Day -->
				<div class="flex items-center gap-2 overflow-x-auto pb-1 sm:pb-0 scrollbar-none">
					<button
						v-for="tab in filterTabs"
						:key="tab.id"
						@click="activeStatusFilter = tab.id"
						class="flex items-center gap-2 px-3.5 py-2 text-sm font-semibold transition-all relative whitespace-nowrap"
						:class="[
							activeStatusFilter === tab.id
								? 'text-[#064e3b] font-bold after:content-[\'\'] after:absolute after:bottom-[-13px] after:left-0 after:right-0 after:h-0.5 after:bg-[#064e3b]'
								: 'text-black-500 hover:text-black-800',
						]"
					>
						<span>{{ tab.label }}</span>
						<span
							class="px-2 py-0.5 text-xs rounded-full font-bold"
							:class="[
								activeStatusFilter === tab.id
									? 'bg-[#064e3b] text-white'
									: 'bg-black-100 text-black-600',
							]"
						>
							{{ tab.count }}
						</span>
					</button>
				</div>

				<!-- Export Button -->
				<button
					v-if="filteredRecords.length > 0"
					@click="exportAttendance"
					class="px-4 py-2 bg-white border border-black-200 hover:bg-black-50 text-black-700 text-xs font-bold rounded-xl transition-all shadow-sm flex items-center gap-2 self-end sm:self-auto"
				>
					<svg
						class="w-4 h-4 text-black-500"
						viewBox="0 0 24 24"
						fill="none"
						stroke="currentColor"
						stroke-width="2"
					>
						<path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path>
						<polyline points="7 10 12 15 17 10"></polyline>
						<line x1="12" y1="15" x2="12" y2="3"></line>
					</svg>
					<span>Export</span>
				</button>
			</div>

			<!-- Attendance Table -->
			<div class="bg-white rounded-2xl border border-black-100 shadow-sm overflow-hidden">
				<div v-if="attendanceResource.loading" class="py-16 text-center text-black-500">
					<div
						class="w-8 h-8 border-4 border-emerald-200 border-t-emerald-600 rounded-full animate-spin mx-auto mb-2"
					></div>
					Loading attendance records...
				</div>

				<div
					v-else-if="filteredRecords.length === 0"
					class="py-16 text-center text-black-500"
				>
					<div
						class="w-16 h-16 bg-black-50 text-black-400 rounded-full flex items-center justify-center mx-auto mb-3"
					>
						<svg
							class="w-8 h-8"
							viewBox="0 0 24 24"
							fill="none"
							stroke="currentColor"
							stroke-width="2"
						>
							<circle cx="12" cy="12" r="10"></circle>
							<polyline points="12 6 12 12 16 14"></polyline>
						</svg>
					</div>
					<h4 class="text-base font-bold text-black-900 mb-1">
						No attendance records found
					</h4>
					<p class="text-xs text-black-400">
						There are no attendance logs matching your filter for this volunteer
						account.
					</p>
				</div>

				<div v-else class="overflow-x-auto">
					<table class="w-full text-left border-collapse">
						<thead>
							<tr
								class="bg-black-50/70 border-b border-black-100 text-[11px] font-bold text-black-400 uppercase tracking-wider"
							>
								<th class="py-3.5 px-4 text-center w-12">#</th>
								<th class="py-3.5 px-4">Date</th>
								<th class="py-3.5 px-6">Shift / Opportunity</th>
								<th class="py-3.5 px-6">Location</th>
								<th class="py-3.5 px-4">Hours</th>
								<th class="py-3.5 px-4">Status</th>
							</tr>
						</thead>
						<tbody
							class="divide-y divide-black-100 text-xs font-medium text-black-700"
						>
							<tr
								v-for="(row, idx) in filteredRecords"
								:key="row.name || idx"
								class="hover:bg-black-50/60 transition-colors"
							>
								<!-- # Index -->
								<td class="py-4 px-4 text-center font-bold text-black-400">
									{{ idx + 1 }}
								</td>

								<!-- Date -->
								<td
									class="py-4 px-4 whitespace-nowrap font-semibold text-black-900"
								>
									{{ formatDate(row.date) }}
								</td>

								<!-- Shift / Opportunity -->
								<td class="py-4 px-6">
									<div class="font-bold text-black-900">
										{{
											row.opportunity_title ||
											row.opportunity ||
											(row.shift
												? "Shift " + row.shift
												: "Volunteer Activity")
										}}
									</div>
									<div
										v-if="row.project_name || row.project"
										class="text-[11px] text-blue-600 font-medium flex items-center gap-1 mt-0.5"
									>
										<svg
											class="w-3 h-3 flex-shrink-0"
											viewBox="0 0 24 24"
											fill="none"
											stroke="currentColor"
											stroke-width="2"
										>
											<path
												d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"
											></path>
										</svg>
										<span>{{ row.project_name || row.project }}</span>
									</div>
								</td>

								<!-- Location -->
								<td class="py-4 px-6 text-black-600">
									{{ row.location || "—" }}
								</td>

								<!-- Hours -->
								<td class="py-4 px-4 font-bold text-black-900 whitespace-nowrap">
									{{ Number(row.total_hours || 0).toFixed(1) }} hrs
								</td>

								<!-- Status Pill -->
								<td class="py-4 px-4 whitespace-nowrap">
									<span
										class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-bold"
										:class="getStatusPillClass(row.status)"
									>
										<span
											class="w-1.5 h-1.5 rounded-full"
											:class="
												row.status === 'Present'
													? 'bg-emerald-500'
													: row.status === 'Half Day' ||
													  row.status === 'Halfday'
													? 'bg-amber-500'
													: 'bg-rose-500'
											"
										></span>
										<span>{{ row.status || "Present" }}</span>
									</span>
								</td>
							</tr>
						</tbody>
					</table>
				</div>
			</div>
		</div>
	</VolunteerLayout>
</template>

<script setup>
import { createResource } from "frappe-ui";
import { computed, ref } from "vue";
import VolunteerLayout from "../components/VolunteerLayout.vue";

const activeStatusFilter = ref("all");
const filters = ref({
	from_date: "",
	to_date: "",
});

// Real backend resource for attendance
const attendanceResource = createResource({
	url: "ngo.api.volunteer.my_attendance",
	method: "GET",
	auto: true,
});

// Real attendance records
const attendanceRecords = computed(() => {
	if (attendanceResource.data && Array.isArray(attendanceResource.data.data)) {
		return attendanceResource.data.data;
	}
	return [];
});

// Filter tabs with dynamic counts for Present, Absent, Half Day
const filterTabs = computed(() => {
	const records = attendanceRecords.value;
	return [
		{ id: "all", label: "All", count: records.length },
		{
			id: "Present",
			label: "Present",
			count: records.filter((r) => r.status === "Present").length,
		},
		{
			id: "Absent",
			label: "Absent",
			count: records.filter((r) => r.status === "Absent").length,
		},
		{
			id: "Half Day",
			label: "Half Day",
			count: records.filter((r) => r.status === "Half Day" || r.status === "Halfday").length,
		},
	];
});

// Filtered rows
const filteredRecords = computed(() => {
	let list = [...attendanceRecords.value];
	if (activeStatusFilter.value !== "all") {
		if (activeStatusFilter.value === "Half Day") {
			list = list.filter((r) => r.status === "Half Day" || r.status === "Halfday");
		} else {
			list = list.filter((r) => r.status === activeStatusFilter.value);
		}
	}
	return list;
});

// Period total hours based on current filtered view
const periodTotalHours = computed(() => {
	const sum = filteredRecords.value.reduce((acc, r) => acc + (Number(r.total_hours) || 0), 0);
	return Math.round(sum * 10) / 10;
});

// Present metrics
const presentCount = computed(() => {
	return attendanceRecords.value.filter((r) => r.status === "Present").length;
});
const presentHours = computed(() => {
	const sum = attendanceRecords.value
		.filter((r) => r.status === "Present")
		.reduce((acc, r) => acc + (Number(r.total_hours) || 0), 0);
	return Math.round(sum * 10) / 10;
});

// Absent metrics
const absentCount = computed(() => {
	return attendanceRecords.value.filter((r) => r.status === "Absent").length;
});

// Half Day metrics
const halfDayCount = computed(() => {
	return attendanceRecords.value.filter((r) => r.status === "Half Day" || r.status === "Halfday")
		.length;
});
const halfDayHours = computed(() => {
	const sum = attendanceRecords.value
		.filter((r) => r.status === "Half Day" || r.status === "Halfday")
		.reduce((acc, r) => acc + (Number(r.total_hours) || 0), 0);
	return Math.round(sum * 10) / 10;
});

function getStatusPillClass(status) {
	if (status === "Present") return "bg-emerald-100 text-emerald-800 border border-emerald-200";
	if (status === "Half Day" || status === "Halfday")
		return "bg-amber-100 text-amber-800 border border-amber-200";
	if (status === "Absent") return "bg-rose-100 text-rose-800 border border-rose-200";
	return "bg-black-100 text-black-700";
}

function formatDate(dateStr) {
	if (!dateStr) return "-";
	const d = new Date(dateStr);
	return d.toLocaleDateString("en-US", {
		month: "short",
		day: "2-digit",
		year: "numeric",
	});
}

function applyDateFilter() {
	const p = {};
	if (filters.value.from_date) p.from_date = filters.value.from_date;
	if (filters.value.to_date) p.to_date = filters.value.to_date;
	attendanceResource.params = p;
	attendanceResource.fetch();
}

function exportAttendance() {
	const rows = filteredRecords.value;
	if (!rows || rows.length === 0) return;
	let csv = "Date,Shift,Opportunity,Project,Location,Hours,Status\n";
	rows.forEach((r) => {
		csv += `"${r.date}","${r.shift || ""}","${r.opportunity_title || ""}","${
			r.project_name || ""
		}","${r.location || ""}","${r.total_hours || 0}","${r.status || ""}"\n`;
	});
	const blob = new Blob([csv], { type: "text/csv" });
	const url = window.URL.createObjectURL(blob);
	const a = document.createElement("a");
	a.setAttribute("href", url);
	a.setAttribute("download", "attendance_records.csv");
	a.click();
}
</script>
