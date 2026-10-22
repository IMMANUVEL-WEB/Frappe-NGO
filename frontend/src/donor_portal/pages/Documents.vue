<template>
  <div class="space-y-6">
    <!-- Top Stat Cards (4 Cards) -->
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
      <!-- 1. Total Documents -->
      <div class="bg-white rounded-2xl p-5 border border-slate-100 shadow-xs flex flex-col justify-between hover:shadow-md transition">
        <div class="flex items-start justify-between">
          <div>
            <span class="text-[11px] font-bold uppercase tracking-wider text-slate-400">Total Documents</span>
            <div class="text-2xl font-black text-slate-900 mt-1 tracking-tight">12</div>
            <div class="text-xs text-slate-400 font-medium mt-1">Verified files available</div>
          </div>
          <div class="w-10 h-10 rounded-xl bg-emerald-50 text-emerald-600 flex items-center justify-center">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 21h10a2 2 0 002-2V9.414a1 1 0 00-.293-.707l-5.414-5.414A1 1 0 0012.586 3H7a2 2 0 00-2 2v14a2 2 0 002 2z"/>
            </svg>
          </div>
        </div>
        <div class="mt-4 w-full bg-slate-100 rounded-full h-1.5 overflow-hidden">
          <div class="bg-emerald-500 h-1.5 rounded-full w-full"></div>
        </div>
      </div>

      <!-- 2. Grant Agreements -->
      <div class="bg-white rounded-2xl p-5 border border-slate-100 shadow-xs flex flex-col justify-between hover:shadow-md transition">
        <div class="flex items-start justify-between">
          <div>
            <span class="text-[11px] font-bold uppercase tracking-wider text-slate-400">Grant Agreements</span>
            <div class="text-2xl font-black text-slate-900 mt-1 tracking-tight">6</div>
            <div class="text-xs text-slate-400 font-medium mt-1">Signed MoUs & annexures</div>
          </div>
          <div class="w-10 h-10 rounded-xl bg-blue-50 text-blue-600 flex items-center justify-center">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/>
            </svg>
          </div>
        </div>
        <div class="mt-4 w-full bg-slate-100 rounded-full h-1.5 overflow-hidden">
          <div class="bg-blue-600 h-1.5 rounded-full w-[50%]"></div>
        </div>
      </div>

      <!-- 3. Utilization Certificates -->
      <div class="bg-white rounded-2xl p-5 border border-slate-100 shadow-xs flex flex-col justify-between hover:shadow-md transition">
        <div class="flex items-start justify-between">
          <div>
            <span class="text-[11px] font-bold uppercase tracking-wider text-slate-400">UC Certificates</span>
            <div class="text-2xl font-black text-slate-900 mt-1 tracking-tight">4</div>
            <div class="text-xs text-slate-400 font-medium mt-1">CA verified expenditure</div>
          </div>
          <div class="w-10 h-10 rounded-xl bg-amber-50 text-amber-500 flex items-center justify-center">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"/>
            </svg>
          </div>
        </div>
        <div class="mt-4 w-full bg-slate-100 rounded-full h-1.5 overflow-hidden">
          <div class="bg-amber-400 h-1.5 rounded-full w-[33%]"></div>
        </div>
      </div>

      <!-- 4. Audit Reports -->
      <div class="bg-white rounded-2xl p-5 border border-slate-100 shadow-xs flex flex-col justify-between hover:shadow-md transition">
        <div class="flex items-start justify-between">
          <div>
            <span class="text-[11px] font-bold uppercase tracking-wider text-slate-400">Audit Reports</span>
            <div class="text-2xl font-black text-slate-900 mt-1 tracking-tight">2</div>
            <div class="text-xs text-slate-400 font-medium mt-1">FCRA & Statutory audits</div>
          </div>
          <div class="w-10 h-10 rounded-xl bg-purple-50 text-purple-600 flex items-center justify-center">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/>
            </svg>
          </div>
        </div>
        <div class="mt-4 w-full bg-slate-100 rounded-full h-1.5 overflow-hidden">
          <div class="bg-purple-500 h-1.5 rounded-full w-[17%]"></div>
        </div>
      </div>
    </div>

    <!-- Filter Bar -->
    <div class="bg-white rounded-2xl p-4 border border-slate-100 shadow-xs flex flex-col sm:flex-row items-center justify-between gap-3">
      <div class="flex items-center gap-3 w-full sm:w-auto flex-1">
        <div class="relative w-full sm:w-80">
          <svg class="w-4 h-4 absolute left-3.5 top-1/2 -translate-y-1/2 text-slate-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/>
          </svg>
          <input 
            type="text" 
            v-model="searchQuery" 
            placeholder="Search documents by title or grant..." 
            class="w-full pl-10 pr-4 py-2 text-xs rounded-xl border border-slate-200 focus:outline-none focus:ring-2 focus:ring-emerald-500/20 bg-slate-50/50"
          />
        </div>

        <select v-model="selectedType" class="px-3 py-2 text-xs rounded-xl border border-slate-200 bg-white text-slate-700">
          <option value="">All Document Types</option>
          <option value="Grant Agreement">Grant Agreement</option>
          <option value="Utilisation Certificate">Utilisation Certificate</option>
          <option value="Audit Report">Audit Report</option>
        </select>
      </div>
    </div>

    <!-- Documents Table Card -->
    <div class="bg-white rounded-2xl border border-slate-100 shadow-xs overflow-hidden">
      <div class="overflow-x-auto">
        <table class="w-full text-left text-xs">
          <thead class="bg-slate-50/75 border-b border-slate-100 text-[11px] font-bold text-slate-500 uppercase tracking-wider">
            <tr>
              <th class="py-3.5 px-4">#</th>
              <th class="py-3.5 px-4">Document Title</th>
              <th class="py-3.5 px-4">Type</th>
              <th class="py-3.5 px-4">Linked Grant / Initiative</th>
              <th class="py-3.5 px-3">Date</th>
              <th class="py-3.5 px-3">Format</th>
              <th class="py-3.5 px-4 text-right">Download</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-slate-100 text-slate-700">
            <tr 
              v-for="(doc, idx) in filteredDocs" 
              :key="idx"
              class="hover:bg-slate-50/60 transition group"
            >
              <td class="py-3.5 px-4 text-slate-400 font-medium">{{ idx + 1 }}</td>
              <td class="py-3.5 px-4">
                <div class="font-semibold text-slate-900">{{ doc.title }}</div>
                <div class="text-[11px] text-slate-400 font-mono">{{ doc.code }}</div>
              </td>
              <td class="py-3.5 px-4">
                <span 
                  class="inline-block px-2.5 py-0.5 rounded-full text-[11px] font-semibold"
                  :class="{
                    'bg-blue-50 text-blue-700 border border-blue-100': doc.type === 'Grant Agreement',
                    'bg-amber-50 text-amber-700 border border-amber-200': doc.type === 'Utilisation Certificate',
                    'bg-purple-50 text-purple-700 border border-purple-200': doc.type === 'Audit Report'
                  }"
                >
                  {{ doc.type }}
                </span>
              </td>
              <td class="py-3.5 px-4 text-slate-600 font-medium">{{ doc.linked }}</td>
              <td class="py-3.5 px-3 text-slate-500 whitespace-nowrap">{{ doc.date }}</td>
              <td class="py-3.5 px-3">
                <span class="px-2 py-0.5 rounded bg-slate-100 text-slate-600 font-mono text-[10px] font-bold uppercase">PDF</span>
              </td>
              <td class="py-3.5 px-4 text-right">
                <a 
                  :href="doc.url" 
                  download
                  class="inline-flex items-center space-x-1.5 px-3 py-1.5 rounded-xl bg-slate-100 hover:bg-emerald-50 hover:text-emerald-700 text-slate-700 text-xs font-semibold transition"
                >
                  <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"/>
                  </svg>
                  <span>Download</span>
                </a>
              </td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- Footer -->
      <div class="px-5 py-3.5 border-t border-slate-100 flex items-center justify-between text-xs text-slate-500">
        <div>Showing 1 - {{ filteredDocs.length }} of {{ filteredDocs.length }} documents</div>
        <div class="text-[11px] text-slate-400">All documents are digitally cryptographically signed.</div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from "vue"

const searchQuery = ref("")
const selectedType = ref("")

const docs = ref([
  {
    title: "Clean Water Access Initiative MoU 2026",
    code: "MOU-GI-2026-001",
    type: "Grant Agreement",
    linked: "Clean Water Access Initiative",
    date: "05 Oct 2026",
    url: "#"
  },
  {
    title: "Education for Rural Children Grant Deed",
    code: "MOU-GI-2026-002",
    type: "Grant Agreement",
    linked: "Quality Education for Rural Children",
    date: "12 Sep 2026",
    url: "#"
  },
  {
    title: "Q3 2026 Utilisation Certificate (CA Signed)",
    code: "UC-Q3-2026-WASH",
    type: "Utilisation Certificate",
    linked: "Clean Water Access Initiative",
    date: "01 Oct 2026",
    url: "#"
  },
  {
    title: "Health & Wellness MoU & CapEx Schedule",
    code: "MOU-GI-2026-003",
    type: "Grant Agreement",
    linked: "Community Health & Wellness Program",
    date: "12 Oct 2026",
    url: "#"
  },
  {
    title: "Disaster Emergency Grant Sanction Order",
    code: "SAN-GI-2026-004",
    type: "Grant Agreement",
    linked: "Disaster Relief Response",
    date: "20 Sep 2026",
    url: "#"
  },
  {
    title: "FY 2025-26 Annual Statutory Audit Statement",
    code: "AUD-STAT-2026",
    type: "Audit Report",
    linked: "All Active Initiatives",
    date: "15 Aug 2026",
    url: "#"
  }
])

const filteredDocs = computed(() => {
  return docs.value.filter(d => {
    const matchSearch = !searchQuery.value ||
      d.title.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
      d.code.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
      d.linked.toLowerCase().includes(searchQuery.value.toLowerCase())
    const matchType = !selectedType.value || d.type === selectedType.value
    return matchSearch && matchType
  })
})
</script>
