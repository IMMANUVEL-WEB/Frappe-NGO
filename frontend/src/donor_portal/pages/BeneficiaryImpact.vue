<template>
	<div class="space-y-6">
		<!-- Top Stat Cards (4 Cards) -->
		<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
			<!-- 1. Total Beneficiaries -->
			<div
				class="bg-white rounded-2xl p-5 border border-slate-100 shadow-xs flex flex-col justify-between hover:shadow-md transition"
			>
				<div class="flex items-start justify-between">
					<div>
						<span class="text-[11px] font-bold uppercase tracking-wider text-slate-400"
							>Total Beneficiaries</span
						>
						<div class="text-2xl font-black text-slate-900 mt-1 tracking-tight">
							{{ Number(impactData.total_beneficiaries || 0).toLocaleString() }}
						</div>
						<div class="text-xs text-slate-400 font-medium mt-1">
							Direct community impact
						</div>
					</div>
					<div
						class="w-10 h-10 rounded-xl bg-emerald-50 text-emerald-600 flex items-center justify-center"
					>
						<svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								stroke-width="2"
								d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z"
							/>
						</svg>
					</div>
				</div>
				<div class="mt-4 w-full bg-slate-100 rounded-full h-1.5 overflow-hidden">
					<div class="bg-emerald-500 h-1.5 rounded-full w-full"></div>
				</div>
			</div>

			<!-- 2. Services Delivered -->
			<div
				class="bg-white rounded-2xl p-5 border border-slate-100 shadow-xs flex flex-col justify-between hover:shadow-md transition"
			>
				<div class="flex items-start justify-between">
					<div>
						<span class="text-[11px] font-bold uppercase tracking-wider text-slate-400"
							>Services Delivered</span
						>
						<div class="text-2xl font-black text-slate-900 mt-1 tracking-tight">
							{{ Number(impactData.services_delivered || 0).toLocaleString() }}
						</div>
						<div class="text-xs text-slate-400 font-medium mt-1">
							Medical, food, educational aid
						</div>
					</div>
					<div
						class="w-10 h-10 rounded-xl bg-blue-50 text-blue-600 flex items-center justify-center"
					>
						<svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								stroke-width="2"
								d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"
							/>
						</svg>
					</div>
				</div>
				<div class="mt-4 w-full bg-slate-100 rounded-full h-1.5 overflow-hidden">
					<div class="bg-blue-600 h-1.5 rounded-full w-[85%]"></div>
				</div>
			</div>

			<!-- 3. Active Districts / Territories -->
			<div
				class="bg-white rounded-2xl p-5 border border-slate-100 shadow-xs flex flex-col justify-between hover:shadow-md transition"
			>
				<div class="flex items-start justify-between">
					<div>
						<span class="text-[11px] font-bold uppercase tracking-wider text-slate-400"
							>Active Territories</span
						>
						<div class="text-2xl font-black text-slate-900 mt-1 tracking-tight">
							{{ districtList.length }}
						</div>
						<div class="text-xs text-slate-400 font-medium mt-1">
							Outreach locations
						</div>
					</div>
					<div
						class="w-10 h-10 rounded-xl bg-amber-50 text-amber-500 flex items-center justify-center"
					>
						<svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								stroke-width="2"
								d="M3.055 11H5a2 2 0 012 2v1a2 2 0 002 2 2 2 0 012 2v2.945M8 3.935V5.5A2.5 2.5 0 0010.5 8h.5a2 2 0 012 2 2 2 0 104 0 2 2 0 012-2h1.064M15 20.488V18a2 2 0 012-2h3.064M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
							/>
						</svg>
					</div>
				</div>
				<div class="mt-4 w-full bg-slate-100 rounded-full h-1.5 overflow-hidden">
					<div class="bg-amber-400 h-1.5 rounded-full w-[60%]"></div>
				</div>
			</div>

			<!-- 4. Verification Rate -->
			<div
				class="bg-white rounded-2xl p-5 border border-slate-100 shadow-xs flex flex-col justify-between hover:shadow-md transition"
			>
				<div class="flex items-start justify-between">
					<div>
						<span class="text-[11px] font-bold uppercase tracking-wider text-slate-400"
							>Audit Verification</span
						>
						<div class="text-2xl font-black text-slate-900 mt-1 tracking-tight">
							100%
						</div>
						<div class="text-xs text-slate-400 font-medium mt-1">
							Zero PII Leakage Compliant
						</div>
					</div>
					<div
						class="w-10 h-10 rounded-xl bg-purple-50 text-purple-600 flex items-center justify-center"
					>
						<svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								stroke-width="2"
								d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"
							/>
						</svg>
					</div>
				</div>
				<div class="mt-4 w-full bg-slate-100 rounded-full h-1.5 overflow-hidden">
					<div class="bg-purple-500 h-1.5 rounded-full w-full"></div>
				</div>
			</div>
		</div>

		<!-- Middle Section: Breakdown Cards -->
		<div class="grid grid-cols-1 lg:grid-cols-12 gap-6">
			<!-- Sector / Service Impact Distribution (7 cols) -->
			<div class="lg:col-span-7 bg-white rounded-2xl p-5 border border-slate-100 shadow-xs">
				<div class="flex items-center space-x-2 mb-4">
					<div class="w-2.5 h-2.5 rounded-full bg-emerald-500"></div>
					<h3 class="text-sm font-bold text-slate-900 tracking-tight">
						Impact Reach by Aid / Service Type
					</h3>
				</div>

				<div v-if="loading" class="py-12 text-center text-xs text-slate-400">
					Loading impact metrics...
				</div>

				<div
					v-else-if="serviceImpactList.length === 0"
					class="py-12 text-center text-xs text-slate-400"
				>
					No service delivery records found yet.
				</div>

				<div v-else class="space-y-4">
					<div
						v-for="item in serviceImpactList"
						:key="item.service_type"
						class="space-y-1 text-xs"
					>
						<div class="flex justify-between items-center">
							<span class="font-semibold text-slate-800">{{
								item.service_type
							}}</span>
							<span class="font-bold text-slate-900">
								{{ item.count.toLocaleString() }} deliveries
								<span class="text-slate-400 font-normal"
									>({{ item.percent }}%)</span
								>
							</span>
						</div>
						<div class="w-full bg-slate-100 rounded-full h-2 overflow-hidden">
							<div
								class="h-2 rounded-full transition-all duration-500"
								:class="item.barColor"
								:style="{ width: `${item.percent}%` }"
							></div>
						</div>
					</div>
				</div>
			</div>

			<!-- Regional Outreach Map & District List (5 cols) -->
			<div
				class="lg:col-span-5 bg-white rounded-2xl p-5 border border-slate-100 shadow-xs flex flex-col justify-between"
			>
				<div>
					<div class="flex items-center space-x-2 mb-4">
						<div class="w-2.5 h-2.5 rounded-full bg-emerald-500"></div>
						<h3 class="text-sm font-bold text-slate-900 tracking-tight">
							Territory Outreach
						</h3>
					</div>

					<div v-if="loading" class="py-12 text-center text-xs text-slate-400">
						Loading territories...
					</div>

					<div
						v-else-if="districtList.length === 0"
						class="py-12 text-center text-xs text-slate-400"
					>
						No regional distribution records yet.
					</div>

					<div v-else class="space-y-2.5 text-xs">
						<div
							v-for="dist in districtList"
							:key="dist.name"
							class="p-2.5 rounded-xl bg-slate-50 flex items-center justify-between"
						>
							<div class="flex items-center space-x-2.5">
								<span class="w-2 h-2 rounded-full" :class="dist.dotColor"></span>
								<span class="font-semibold text-slate-800">{{ dist.name }}</span>
							</div>
							<span class="font-bold text-slate-900"
								>{{ dist.count.toLocaleString() }} reach</span
							>
						</div>
					</div>
				</div>

				<div
					class="mt-4 pt-3 border-t border-slate-100 text-[11px] text-slate-400 flex items-center justify-between"
				>
					<span>State Centroid Verified</span>
					<span>Demographics Aggregated</span>
				</div>
			</div>
		</div>

		<!-- Aid Items Breakdown Table -->
		<div
			v-if="impactData.aid_items && impactData.aid_items.length > 0"
			class="bg-white rounded-2xl border border-slate-100 shadow-xs overflow-hidden"
		>
			<div class="p-4 border-b border-slate-100 flex items-center space-x-2">
				<div class="w-2.5 h-2.5 rounded-full bg-emerald-500"></div>
				<h3 class="text-sm font-bold text-slate-900 tracking-tight">
					Detailed Aid Deliveries
				</h3>
			</div>
			<div class="overflow-x-auto">
				<table class="w-full text-left text-xs">
					<thead
						class="bg-slate-50/75 border-b border-slate-100 text-[11px] font-bold text-slate-500 uppercase tracking-wider"
					>
						<tr>
							<th class="py-3 px-4">#</th>
							<th class="py-3 px-4">Service / Aid Type</th>
							<th class="py-3 px-4">Units Disbursed</th>
							<th class="py-3 px-4">Total Amount (₹)</th>
						</tr>
					</thead>
					<tbody class="divide-y divide-slate-100 text-slate-700">
						<tr
							v-for="(item, idx) in impactData.aid_items"
							:key="idx"
							class="hover:bg-slate-50/60"
						>
							<td class="py-3 px-4 text-slate-400">{{ idx + 1 }}</td>
							<td class="py-3 px-4 font-semibold text-slate-900">
								{{ item.service_type }}
							</td>
							<td class="py-3 px-4">{{ item.units }} units</td>
							<td class="py-3 px-4 font-semibold text-emerald-600">
								₹{{ Number(item.amount || 0).toLocaleString("en-IN") }}
							</td>
						</tr>
					</tbody>
				</table>
			</div>
		</div>
	</div>
</template>

<script setup>
import { computed, onMounted, ref } from "vue";
import { donorApi } from "../api";

const loading = ref(true);
const impactData = ref({
	total_beneficiaries: 0,
	services_delivered: 0,
	by_service_type: [],
	by_district: [],
	aid_items: [],
});

onMounted(async () => {
	try {
		const res = await donorApi.getImpact();
		if (res) {
			impactData.value = res;
		}
	} catch (err) {
		console.error("Failed to load impact metrics:", err);
	} finally {
		loading.value = false;
	}
});

// Service Impact List
const serviceImpactList = computed(() => {
	const items = impactData.value.by_service_type || [];
	let total = 0;
	items.forEach((i) => {
		total += Number(i.count || 0);
	});

	const colors = [
		"bg-rose-500",
		"bg-purple-600",
		"bg-blue-600",
		"bg-emerald-500",
		"bg-amber-400",
	];

	return items.map((item, idx) => {
		const cnt = Number(item.count || 0);
		return {
			service_type: item.service_type || "General Support",
			count: cnt,
			percent: total > 0 ? Math.round((cnt / total) * 100) : 0,
			barColor: colors[idx % colors.length],
		};
	});
});

// District List
const districtList = computed(() => {
	const items = impactData.value.by_district || [];
	const colors = [
		"bg-blue-500",
		"bg-emerald-500",
		"bg-rose-500",
		"bg-purple-500",
		"bg-amber-500",
	];

	return items.map((item, idx) => {
		return {
			name: item.territory || "National / Regional Outreach",
			count: Number(item.beneficiary_count || 0),
			dotColor: colors[idx % colors.length],
		};
	});
});
</script>
