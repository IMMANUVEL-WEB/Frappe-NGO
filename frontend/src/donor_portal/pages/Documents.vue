<template>
	<div class="space-y-6">
		<!-- Top Stat Cards (4 Cards) -->
		<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
			<!-- 1. Total Documents -->
			<div
				class="bg-white rounded-2xl p-5 border border-slate-100 shadow-xs flex flex-col justify-between hover:shadow-md transition"
			>
				<div class="flex items-start justify-between">
					<div>
						<span class="text-[11px] font-bold uppercase tracking-wider text-slate-400"
							>Total Documents</span
						>
						<div class="text-2xl font-black text-slate-900 mt-1 tracking-tight">
							{{ docs.length }}
						</div>
						<div class="text-xs text-slate-400 font-medium mt-1">
							Verified files available
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
								d="M7 21h10a2 2 0 002-2V9.414a1 1 0 00-.293-.707l-5.414-5.414A1 1 0 0012.586 3H7a2 2 0 00-2 2v14a2 2 0 002 2z"
							/>
						</svg>
					</div>
				</div>
				<div class="mt-4 w-full bg-slate-100 rounded-full h-1.5 overflow-hidden">
					<div class="bg-emerald-500 h-1.5 rounded-full w-full"></div>
				</div>
			</div>

			<!-- 2. Grant Agreements -->
			<div
				class="bg-white rounded-2xl p-5 border border-slate-100 shadow-xs flex flex-col justify-between hover:shadow-md transition"
			>
				<div class="flex items-start justify-between">
					<div>
						<span class="text-[11px] font-bold uppercase tracking-wider text-slate-400"
							>Grant Documents</span
						>
						<div class="text-2xl font-black text-slate-900 mt-1 tracking-tight">
							{{ stats.grantDocs }}
						</div>
						<div class="text-xs text-slate-400 font-medium mt-1">
							Grant agreements & orders
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
								d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"
							/>
						</svg>
					</div>
				</div>
				<div class="mt-4 w-full bg-slate-100 rounded-full h-1.5 overflow-hidden">
					<div
						class="bg-blue-600 h-1.5 rounded-full transition-all duration-500"
						:style="{ width: `${stats.grantDocsPercent}%` }"
					></div>
				</div>
			</div>

			<!-- 3. Proposals & Projects -->
			<div
				class="bg-white rounded-2xl p-5 border border-slate-100 shadow-xs flex flex-col justify-between hover:shadow-md transition"
			>
				<div class="flex items-start justify-between">
					<div>
						<span class="text-[11px] font-bold uppercase tracking-wider text-slate-400"
							>Proposal & Project Files</span
						>
						<div class="text-2xl font-black text-slate-900 mt-1 tracking-tight">
							{{ stats.proposalDocs }}
						</div>
						<div class="text-xs text-slate-400 font-medium mt-1">
							Proposal dossiers & designs
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
								d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"
							/>
						</svg>
					</div>
				</div>
				<div class="mt-4 w-full bg-slate-100 rounded-full h-1.5 overflow-hidden">
					<div
						class="bg-amber-400 h-1.5 rounded-full transition-all duration-500"
						:style="{ width: `${stats.proposalDocsPercent}%` }"
					></div>
				</div>
			</div>

			<!-- 4. Compliance & Certificates -->
			<div
				class="bg-white rounded-2xl p-5 border border-slate-100 shadow-xs flex flex-col justify-between hover:shadow-md transition"
			>
				<div class="flex items-start justify-between">
					<div>
						<span class="text-[11px] font-bold uppercase tracking-wider text-slate-400"
							>Compliance & Reports</span
						>
						<div class="text-2xl font-black text-slate-900 mt-1 tracking-tight">
							{{ stats.complianceDocs }}
						</div>
						<div class="text-xs text-slate-400 font-medium mt-1">
							Audit & compliance certificates
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
								d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"
							/>
						</svg>
					</div>
				</div>
				<div class="mt-4 w-full bg-slate-100 rounded-full h-1.5 overflow-hidden">
					<div
						class="bg-purple-500 h-1.5 rounded-full transition-all duration-500"
						:style="{ width: `${stats.complianceDocsPercent}%` }"
					></div>
				</div>
			</div>
		</div>

		<!-- Filter Bar -->
		<div
			class="bg-white rounded-2xl p-4 border border-slate-100 shadow-xs flex flex-col sm:flex-row items-center justify-between gap-3"
		>
			<div class="flex items-center gap-3 w-full sm:w-auto flex-1">
				<div class="relative w-full sm:w-80">
					<svg
						class="w-4 h-4 absolute left-3.5 top-1/2 -translate-y-1/2 text-slate-400"
						fill="none"
						stroke="currentColor"
						viewBox="0 0 24 24"
					>
						<path
							stroke-linecap="round"
							stroke-linejoin="round"
							stroke-width="2"
							d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
						/>
					</svg>
					<input
						type="text"
						v-model="searchQuery"
						placeholder="Search documents by file name or record..."
						class="w-full pl-10 pr-4 py-2 text-xs rounded-xl border border-slate-200 focus:outline-none focus:ring-2 focus:ring-emerald-500/20 bg-slate-50/50"
					/>
				</div>

				<select
					v-model="selectedType"
					class="px-3 py-2 text-xs rounded-xl border border-slate-200 bg-white text-slate-700"
				>
					<option value="">All Document Types</option>
					<option v-for="t in uniqueTypes" :key="t" :value="t">{{ t }}</option>
				</select>
			</div>
		</div>

		<!-- Documents Table Card -->
		<div class="bg-white rounded-2xl border border-slate-100 shadow-xs overflow-hidden">
			<!-- Loading State -->
			<div v-if="loading" class="py-16 text-center text-slate-400 text-xs font-medium">
				Loading documents...
			</div>

			<!-- Empty State -->
			<div v-else-if="filteredDocs.length === 0" class="py-16 text-center text-slate-400">
				<svg
					class="w-10 h-10 mx-auto mb-2 text-slate-300"
					fill="none"
					stroke="currentColor"
					viewBox="0 0 24 24"
				>
					<path
						stroke-linecap="round"
						stroke-linejoin="round"
						stroke-width="1.5"
						d="M7 21h10a2 2 0 002-2V9.414a1 1 0 00-.293-.707l-5.414-5.414A1 1 0 0012.586 3H7a2 2 0 00-2 2v14a2 2 0 002 2z"
					/>
				</svg>
				<p class="text-sm font-semibold text-slate-600">No documents found</p>
				<p class="text-xs text-slate-400 mt-1">
					There are no shared documents linked to your profile matching the query.
				</p>
			</div>

			<div v-else class="overflow-x-auto">
				<table class="w-full text-left text-xs">
					<thead
						class="bg-slate-50/75 border-b border-slate-100 text-[11px] font-bold text-slate-500 uppercase tracking-wider"
					>
						<tr>
							<th class="py-3.5 px-4">#</th>
							<th class="py-3.5 px-4">Document / File Name</th>
							<th class="py-3.5 px-4">Type / Source</th>
							<th class="py-3.5 px-4">Linked Record</th>
							<th class="py-3.5 px-3">Date</th>
							<th class="py-3.5 px-3">Size</th>
							<th class="py-3.5 px-4 text-right">Download</th>
						</tr>
					</thead>
					<tbody class="divide-y divide-slate-100 text-slate-700">
						<tr
							v-for="(doc, idx) in filteredDocs"
							:key="doc.name || idx"
							class="hover:bg-slate-50/60 transition group"
						>
							<td class="py-3.5 px-4 text-slate-400 font-medium">{{ idx + 1 }}</td>
							<td class="py-3.5 px-4">
								<div class="font-semibold text-slate-900">
									{{ doc.file_name || doc.name }}
								</div>
								<div class="text-[11px] text-slate-400 font-mono">
									{{ doc.name }}
								</div>
							</td>
							<td class="py-3.5 px-4">
								<span
									class="inline-block px-2.5 py-0.5 rounded-full text-[11px] font-semibold"
									:class="{
										'bg-blue-50 text-blue-700 border border-blue-100':
											doc.attached_to_doctype === 'Donor Grant',
										'bg-amber-50 text-amber-700 border border-amber-200':
											doc.attached_to_doctype === 'Project Proposal',
										'bg-purple-50 text-purple-700 border border-purple-200':
											doc.attached_to_doctype === 'Project' ||
											doc.is_compliance,
									}"
								>
									{{ doc.attached_to_doctype || "Document" }}
								</span>
							</td>
							<td class="py-3.5 px-4 text-slate-600 font-medium">
								{{ doc.attached_to_name || "-" }}
							</td>
							<td class="py-3.5 px-3 text-slate-500 whitespace-nowrap">
								{{ formatDate(doc.creation) }}
							</td>
							<td class="py-3.5 px-3 text-slate-500 font-mono">
								{{ formatFileSize(doc.file_size) }}
							</td>
							<td class="py-3.5 px-4 text-right">
								<a
									:href="doc.file_url"
									target="_blank"
									download
									class="inline-flex items-center space-x-1.5 px-3 py-1.5 rounded-xl border border-slate-200 text-slate-700 font-semibold hover:bg-slate-50 hover:text-emerald-600 transition"
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
											d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"
										/>
									</svg>
									<span>Download</span>
								</a>
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
const searchQuery = ref("");
const selectedType = ref("");

const docs = ref([]);

onMounted(async () => {
	try {
		const res = await donorApi.getDocuments();
		if (Array.isArray(res)) {
			docs.value = res;
		}
	} catch (err) {
		console.error("Failed to load documents:", err);
	} finally {
		loading.value = false;
	}
});

// Unique Types
const uniqueTypes = computed(() => {
	const set = new Set();
	docs.value.forEach((d) => {
		if (d.attached_to_doctype) set.add(d.attached_to_doctype);
	});
	return Array.from(set);
});

// Stats
const stats = computed(() => {
	const total = docs.value.length;
	let grantDocs = 0;
	let proposalDocs = 0;
	let complianceDocs = 0;

	docs.value.forEach((d) => {
		const dt = d.attached_to_doctype;
		if (dt === "Donor Grant") grantDocs++;
		else if (dt === "Project Proposal" || dt === "Project") proposalDocs++;
		else complianceDocs++;
	});

	return {
		grantDocs,
		grantDocsPercent: total > 0 ? Math.round((grantDocs / total) * 100) : 0,
		proposalDocs,
		proposalDocsPercent: total > 0 ? Math.round((proposalDocs / total) * 100) : 0,
		complianceDocs,
		complianceDocsPercent: total > 0 ? Math.round((complianceDocs / total) * 100) : 0,
	};
});

// Filtered Docs
const filteredDocs = computed(() => {
	return docs.value.filter((doc) => {
		const fn = (doc.file_name || "").toLowerCase();
		const rec = (doc.attached_to_name || "").toLowerCase();
		const q = searchQuery.value.toLowerCase().trim();

		const matchesSearch = !q || fn.includes(q) || rec.includes(q);
		const matchesType = !selectedType.value || doc.attached_to_doctype === selectedType.value;

		return matchesSearch && matchesType;
	});
});

function formatDate(val) {
	if (!val) return "-";
	return String(val).split(" ")[0];
}

function formatFileSize(bytes) {
	if (!bytes) return "-";
	const b = Number(bytes);
	if (b < 1024) return b + " B";
	if (b < 1024 * 1024) return (b / 1024).toFixed(1) + " KB";
	return (b / (1024 * 1024)).toFixed(1) + " MB";
}
</script>
