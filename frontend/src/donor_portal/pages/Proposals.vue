<template>
  <div class="space-y-6">
    <!-- Top Stat Cards (4 Cards) -->
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
      <!-- 1. Total Proposals -->
      <div class="bg-white rounded-2xl p-5 border border-slate-100 shadow-xs flex flex-col justify-between hover:shadow-md transition">
        <div class="flex items-start justify-between">
          <div>
            <span class="text-[11px] font-bold uppercase tracking-wider text-slate-400">Total Proposals</span>
            <div class="text-2xl font-black text-slate-900 mt-1 tracking-tight">{{ stats.total }}</div>
            <div class="text-xs text-slate-400 font-medium mt-1">All proposals submitted</div>
          </div>
          <div class="w-10 h-10 rounded-xl bg-emerald-50 text-emerald-600 flex items-center justify-center">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/>
            </svg>
          </div>
        </div>
        <div class="mt-4 w-full bg-slate-100 rounded-full h-1.5 overflow-hidden">
          <div class="bg-emerald-500 h-1.5 rounded-full w-full"></div>
        </div>
      </div>

      <!-- 2. Approved -->
      <div class="bg-white rounded-2xl p-5 border border-slate-100 shadow-xs flex flex-col justify-between hover:shadow-md transition">
        <div class="flex items-start justify-between">
          <div>
            <span class="text-[11px] font-bold uppercase tracking-wider text-slate-400">Approved</span>
            <div class="text-2xl font-black text-slate-900 mt-1 tracking-tight">{{ stats.approved }}</div>
            <div class="text-xs text-slate-400 font-medium mt-1">{{ stats.approvedPercent }}% of total proposals</div>
          </div>
          <div class="w-10 h-10 rounded-xl bg-blue-50 text-blue-600 flex items-center justify-center">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>
            </svg>
          </div>
        </div>
        <div class="mt-4 w-full bg-slate-100 rounded-full h-1.5 overflow-hidden">
          <div 
            class="bg-blue-600 h-1.5 rounded-full transition-all duration-500" 
            :style="{ width: `${stats.approvedPercent}%` }"
          ></div>
        </div>
      </div>

      <!-- 3. Pending -->
      <div class="bg-white rounded-2xl p-5 border border-slate-100 shadow-xs flex flex-col justify-between hover:shadow-md transition">
        <div class="flex items-start justify-between">
          <div>
            <span class="text-[11px] font-bold uppercase tracking-wider text-slate-400">Pending Review</span>
            <div class="text-2xl font-black text-slate-900 mt-1 tracking-tight">{{ stats.pending }}</div>
            <div class="text-xs text-slate-400 font-medium mt-1">Awaiting decision</div>
          </div>
          <div class="w-10 h-10 rounded-xl bg-amber-50 text-amber-500 flex items-center justify-center">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/>
            </svg>
          </div>
        </div>
        <div class="mt-4 w-full bg-slate-100 rounded-full h-1.5 overflow-hidden">
          <div 
            class="bg-amber-400 h-1.5 rounded-full transition-all duration-500" 
            :style="{ width: `${stats.pendingPercent}%` }"
          ></div>
        </div>
      </div>

      <!-- 4. Rejected -->
      <div class="bg-white rounded-2xl p-5 border border-slate-100 shadow-xs flex flex-col justify-between hover:shadow-md transition">
        <div class="flex items-start justify-between">
          <div>
            <span class="text-[11px] font-bold uppercase tracking-wider text-slate-400">Rejected / Needs Revision</span>
            <div class="text-2xl font-black text-slate-900 mt-1 tracking-tight">{{ stats.rejected }}</div>
            <div class="text-xs text-slate-400 font-medium mt-1">{{ stats.rejectedPercent }}% not approved</div>
          </div>
          <div class="w-10 h-10 rounded-xl bg-purple-50 text-purple-600 flex items-center justify-center">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z"/>
            </svg>
          </div>
        </div>
        <div class="mt-4 w-full bg-slate-100 rounded-full h-1.5 overflow-hidden">
          <div 
            class="bg-purple-500 h-1.5 rounded-full transition-all duration-500" 
            :style="{ width: `${stats.rejectedPercent}%` }"
          ></div>
        </div>
      </div>
    </div>

    <!-- Search, Filters and New Proposal Button -->
    <div class="bg-white rounded-2xl p-4 border border-slate-100 shadow-xs flex flex-col lg:flex-row items-center justify-between gap-3">
      <div class="flex flex-col sm:flex-row items-center gap-3 w-full lg:w-auto flex-1">
        <!-- Search Input -->
        <div class="relative w-full sm:w-80">
          <svg class="w-4 h-4 absolute left-3.5 top-1/2 -translate-y-1/2 text-slate-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/>
          </svg>
          <input 
            type="text" 
            v-model="searchQuery" 
            placeholder="Search by title, code or sector..." 
            class="w-full pl-10 pr-4 py-2 text-xs rounded-xl border border-slate-200 focus:outline-none focus:ring-2 focus:ring-emerald-500/20 focus:border-emerald-500 bg-slate-50/50"
          />
        </div>

        <!-- Filters -->
        <div class="flex items-center gap-2 w-full sm:w-auto">
          <select 
            v-model="selectedSector" 
            class="px-3 py-2 text-xs rounded-xl border border-slate-200 focus:outline-none focus:ring-2 focus:ring-emerald-500/20 bg-white text-slate-700"
          >
            <option value="">All Sectors</option>
            <option v-for="sec in uniqueSectors" :key="sec" :value="sec">{{ sec }}</option>
          </select>

          <select 
            v-model="selectedStatus" 
            class="px-3 py-2 text-xs rounded-xl border border-slate-200 focus:outline-none focus:ring-2 focus:ring-emerald-500/20 bg-white text-slate-700"
          >
            <option value="">All Status</option>
            <option v-for="st in uniqueStatuses" :key="st" :value="st">{{ st }}</option>
          </select>
        </div>
      </div>
    </div>

    <!-- Main Content: Two Columns -->
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-6">
      <!-- Left Column: Proposals Table (8 cols) -->
      <div class="lg:col-span-8 bg-white rounded-2xl border border-slate-100 shadow-xs overflow-hidden flex flex-col justify-between">
        <!-- Loading -->
        <div v-if="loading" class="py-16 text-center text-slate-400 text-xs font-medium">
          Loading proposals...
        </div>

        <!-- Empty -->
        <div v-else-if="filteredProposals.length === 0" class="py-16 text-center text-slate-400">
          <svg class="w-10 h-10 mx-auto mb-2 text-slate-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/>
          </svg>
          <p class="text-sm font-semibold text-slate-600">No proposals found</p>
          <p class="text-xs text-slate-400 mt-1">There are no project proposals linked to your profile matching the filters.</p>
        </div>

        <div v-else class="overflow-x-auto">
          <table class="w-full text-left text-xs">
            <thead class="bg-slate-50/75 border-b border-slate-100 text-[11px] font-bold text-slate-500 uppercase tracking-wider">
              <tr>
                <th class="py-3 px-4">#</th>
                <th class="py-3 px-4">Proposal Title</th>
                <th class="py-3 px-3">Code</th>
                <th class="py-3 px-3">Sector</th>
                <th class="py-3 px-3">Budget (Lakh)</th>
                <th class="py-3 px-3">Status</th>
                <th class="py-3 px-3">Submitted On</th>
                <th class="py-3 px-3 text-right">Actions</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-slate-100 text-slate-700">
              <tr 
                v-for="(row, idx) in paginatedProposals" 
                :key="row.name || row.code"
                class="hover:bg-slate-50/60 transition group"
              >
                <td class="py-3.5 px-4 text-slate-400 font-medium">{{ (currentPage - 1) * pageSize + idx + 1 }}</td>
                <td class="py-3.5 px-4 font-semibold text-slate-900 max-w-xs truncate">
                  {{ row.title }}
                </td>
                <td class="py-3.5 px-3 font-mono text-[11px] text-slate-500">{{ row.code || row.name }}</td>
                <td class="py-3.5 px-3">
                  <span 
                    class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-[11px] font-medium"
                    :class="getSectorClass(row.sector)"
                  >
                    <component :is="getSectorIcon(row.sector)" class="w-3 h-3" />
                    {{ row.sector || 'General' }}
                  </span>
                </td>
                <td class="py-3.5 px-3 font-semibold text-slate-900">₹{{ row.budget_lakh ? Number(row.budget_lakh).toFixed(2) + ' L' : '0.00 L' }}</td>
                <td class="py-3.5 px-3">
                  <span 
                    class="inline-block px-2.5 py-0.5 rounded-full text-[11px] font-semibold"
                    :class="{
                      'bg-emerald-50 text-emerald-700 border border-emerald-100': row.status === 'Approved',
                      'bg-amber-50 text-amber-700 border border-amber-200': row.status === 'Under Review' || row.status === 'Draft' || row.status === 'Pending',
                      'bg-rose-50 text-rose-700 border border-rose-200': row.status === 'Rejected'
                    }"
                  >
                    {{ row.status }}
                  </span>
                </td>
                <td class="py-3.5 px-3 text-slate-500 whitespace-nowrap">{{ formatDate(row.created_at || row.submittedOn) }}</td>
                <td class="py-3.5 px-3 text-right relative">
                  <div class="flex items-center justify-end space-x-1">
                    <button 
                      v-if="row.status === 'Under Review' || row.status === 'Pending'"
                      @click="makeDecision(row, 'approve')"
                      class="px-2.5 py-1 text-[11px] font-semibold rounded-lg bg-emerald-50 text-emerald-700 hover:bg-emerald-100 transition"
                    >
                      Approve
                    </button>
                    <button 
                      v-if="row.status === 'Under Review' || row.status === 'Pending'"
                      @click="makeDecision(row, 'reject')"
                      class="px-2.5 py-1 text-[11px] font-semibold rounded-lg bg-rose-50 text-rose-700 hover:bg-rose-100 transition"
                    >
                      Reject
                    </button>
                    <button 
                      @click="openDetail(row)"
                      class="p-1 rounded-lg hover:bg-slate-100 text-slate-400 hover:text-slate-700 transition"
                      title="View Details"
                    >
                      <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/>
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"/>
                      </svg>
                    </button>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>

        <!-- Pagination Footer -->
        <div v-if="filteredProposals.length > 0" class="px-5 py-3.5 border-t border-slate-100 flex items-center justify-between text-xs text-slate-500">
          <div>
            Showing {{ (currentPage - 1) * pageSize + 1 }} - {{ Math.min(currentPage * pageSize, filteredProposals.length) }} of {{ filteredProposals.length }} proposals
          </div>
          <div v-if="totalPages > 1" class="flex items-center space-x-1.5">
            <button 
              type="button" 
              :disabled="currentPage === 1"
              @click="currentPage--"
              class="w-7 h-7 rounded-lg border border-slate-200 flex items-center justify-center hover:bg-slate-50 disabled:opacity-40 disabled:cursor-not-allowed"
            >
              &lt;
            </button>
            <button 
              v-for="p in totalPages" 
              :key="p"
              @click="currentPage = p"
              class="w-7 h-7 rounded-lg flex items-center justify-center font-semibold text-xs transition"
              :class="currentPage === p ? 'bg-[#00875A] text-white' : 'border border-slate-200 hover:bg-slate-50 text-slate-700'"
            >
              {{ p }}
            </button>
            <button 
              type="button" 
              :disabled="currentPage === totalPages"
              @click="currentPage++"
              class="w-7 h-7 rounded-lg border border-slate-200 flex items-center justify-center hover:bg-slate-50 disabled:opacity-40 disabled:cursor-not-allowed"
            >
              &gt;
            </button>
          </div>
        </div>
      </div>

      <!-- Right Column: Charts & Recent Activity (4 cols) -->
      <div class="lg:col-span-4 space-y-6">
        <!-- 1. Proposals by Sector -->
        <div class="bg-white rounded-2xl p-5 border border-slate-100 shadow-xs">
          <div class="flex items-center space-x-2 mb-4">
            <div class="w-2.5 h-2.5 rounded-full bg-emerald-500"></div>
            <h3 class="text-sm font-bold text-slate-900 tracking-tight">Proposals by Sector</h3>
          </div>

          <div v-if="sectorDistribution.length === 0" class="py-8 text-center text-xs text-slate-400">
            No sector data available
          </div>

          <div v-else class="space-y-3 text-xs">
            <div v-for="item in sectorDistribution" :key="item.sector" class="space-y-1">
              <div class="flex items-center justify-between text-slate-700">
                <span class="flex items-center gap-2">
                  <span class="w-2 h-2 rounded-full" :class="item.dotColor"></span>
                  <span class="font-medium text-slate-800">{{ item.sector }}</span>
                </span>
                <span class="font-semibold text-slate-900">
                  {{ item.count }} <span class="text-slate-400 font-normal">({{ item.percent }}%)</span>
                </span>
              </div>
              <div class="w-full bg-slate-100 rounded-full h-1.5 overflow-hidden">
                <div 
                  class="h-1.5 rounded-full transition-all duration-500" 
                  :class="item.barColor" 
                  :style="{ width: `${item.percent}%` }"
                ></div>
              </div>
            </div>
          </div>
        </div>

        <!-- 2. Recent Proposals -->
        <div class="bg-white rounded-2xl p-5 border border-slate-100 shadow-xs">
          <div class="flex items-center justify-between mb-4">
            <div class="flex items-center space-x-2">
              <div class="w-2.5 h-2.5 rounded-full bg-emerald-500"></div>
              <h3 class="text-sm font-bold text-slate-900 tracking-tight">Recent Proposals</h3>
            </div>
          </div>

          <div v-if="proposalsData.length === 0" class="py-6 text-center text-xs text-slate-400">
            No proposal activity yet
          </div>

          <div v-else class="space-y-4">
            <div 
              v-for="item in proposalsData.slice(0, 4)" 
              :key="item.name || item.code"
              class="flex items-start space-x-3 text-xs"
            >
              <div 
                class="w-7 h-7 rounded-full flex items-center justify-center shrink-0 mt-0.5"
                :class="item.status === 'Approved' ? 'bg-emerald-50 text-emerald-600' : 'bg-amber-50 text-amber-500'"
              >
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>
                </svg>
              </div>
              <div class="flex-1 min-w-0">
                <div class="font-semibold text-slate-900 truncate">{{ item.title }}</div>
                <div class="text-[11px] text-slate-500">{{ item.code || item.name }} &bull; {{ item.status }}</div>
              </div>
              <div class="text-[10px] text-slate-400 whitespace-nowrap">{{ formatDate(item.created_at || item.submittedOn) }}</div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Detail Modal -->
    <div v-if="selectedProposal" class="fixed inset-0 z-50 flex items-center justify-center bg-black/40 backdrop-blur-xs p-4">
      <div class="bg-white rounded-2xl max-w-lg w-full p-6 shadow-xl border border-slate-100 space-y-4">
        <div class="flex items-center justify-between border-b border-slate-100 pb-3">
          <div>
            <h3 class="text-base font-bold text-slate-900">{{ selectedProposal.title }}</h3>
            <span class="text-xs font-mono text-slate-400">{{ selectedProposal.code || selectedProposal.name }}</span>
          </div>
          <button @click="selectedProposal = null" class="text-slate-400 hover:text-slate-600 text-lg leading-none">&times;</button>
        </div>

        <div class="grid grid-cols-2 gap-3 text-xs">
          <div class="p-3 rounded-xl bg-slate-50">
            <span class="text-slate-400 font-medium">Sector</span>
            <div class="text-sm font-semibold text-slate-900 mt-0.5">{{ selectedProposal.sector || 'General' }}</div>
          </div>
          <div class="p-3 rounded-xl bg-slate-50">
            <span class="text-slate-400 font-medium">Total Budget</span>
            <div class="text-sm font-semibold text-slate-900 mt-0.5">₹{{ selectedProposal.budget_lakh }} L</div>
          </div>
          <div class="p-3 rounded-xl bg-slate-50">
            <span class="text-slate-400 font-medium">CapEx / OpEx / Admin</span>
            <div class="text-sm font-semibold text-slate-900 mt-0.5">₹{{ selectedProposal.capex_lakh }}L / ₹{{ selectedProposal.opex_lakh }}L / ₹{{ selectedProposal.admin_lakh }}L</div>
          </div>
          <div class="p-3 rounded-xl bg-slate-50">
            <span class="text-slate-400 font-medium">Status</span>
            <div class="text-sm font-semibold text-slate-900 mt-0.5">{{ selectedProposal.status }}</div>
          </div>
        </div>

        <div class="flex justify-end pt-2">
          <button @click="selectedProposal = null" class="px-4 py-2 rounded-xl bg-slate-100 hover:bg-slate-200 text-xs font-semibold text-slate-700 transition">
            Close
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed, h, onMounted, ref } from "vue"
import { donorApi } from "../api"

const loading = ref(true)
const searchQuery = ref("")
const selectedSector = ref("")
const selectedStatus = ref("")
const currentPage = ref(1)
const pageSize = 8

const proposalsData = ref([])
const selectedProposal = ref(null)

onMounted(async () => {
  await loadProposals()
})

async function loadProposals() {
  try {
    loading.value = true
    const res = await donorApi.getProposals()
    if (Array.isArray(res)) {
      proposalsData.value = res
    }
  } catch (err) {
    console.error("Failed to fetch proposals:", err)
  } finally {
    loading.value = false
  }
}

// Stats
const stats = computed(() => {
  const total = proposalsData.value.length
  let approved = 0
  let pending = 0
  let rejected = 0

  proposalsData.value.forEach(p => {
    const st = (p.status || "").toLowerCase()
    if (st === "approved") approved++
    else if (st === "rejected") rejected++
    else pending++
  })

  return {
    total,
    approved,
    approvedPercent: total > 0 ? Math.round((approved / total) * 100) : 0,
    pending,
    pendingPercent: total > 0 ? Math.round((pending / total) * 100) : 0,
    rejected,
    rejectedPercent: total > 0 ? Math.round((rejected / total) * 100) : 0
  }
})

// Unique filters
const uniqueSectors = computed(() => {
  const set = new Set()
  proposalsData.value.forEach(p => {
    if (p.sector) set.add(p.sector)
  })
  return Array.from(set)
})

const uniqueStatuses = computed(() => {
  const set = new Set()
  proposalsData.value.forEach(p => {
    if (p.status) set.add(p.status)
  })
  return Array.from(set)
})

// Sector Distribution
const sectorDistribution = computed(() => {
  const counts = {}
  proposalsData.value.forEach(p => {
    const sec = p.sector || "Other"
    counts[sec] = (counts[sec] || 0) + 1
  })

  const total = proposalsData.value.length
  const colors = [
    { dot: "bg-emerald-500", bar: "bg-emerald-500" },
    { dot: "bg-blue-600", bar: "bg-blue-600" },
    { dot: "bg-purple-600", bar: "bg-purple-600" },
    { dot: "bg-amber-400", bar: "bg-amber-400" },
    { dot: "bg-rose-500", bar: "bg-rose-500" },
  ]

  return Object.keys(counts).map((sec, idx) => {
    const cnt = counts[sec]
    const c = colors[idx % colors.length]
    return {
      sector: sec,
      count: cnt,
      percent: total > 0 ? Math.round((cnt / total) * 100) : 0,
      dotColor: c.dot,
      barColor: c.bar
    }
  })
})

// Filtered & Paginated
const filteredProposals = computed(() => {
  return proposalsData.value.filter(p => {
    const title = (p.title || "").toLowerCase()
    const code = (p.code || p.name || "").toLowerCase()
    const q = searchQuery.value.toLowerCase().trim()

    const matchesSearch = !q || title.includes(q) || code.includes(q)
    const matchesSector = !selectedSector.value || p.sector === selectedSector.value
    const matchesStatus = !selectedStatus.value || p.status === selectedStatus.value

    return matchesSearch && matchesSector && matchesStatus
  })
})

const totalPages = computed(() => Math.ceil(filteredProposals.value.length / pageSize) || 1)

const paginatedProposals = computed(() => {
  const start = (currentPage.value - 1) * pageSize
  return filteredProposals.value.slice(start, start + pageSize)
})

// Decisions
async function makeDecision(row, action) {
  try {
    if (action === "approve") {
      await donorApi.approveProposal(row.name || row.code)
      alert("Proposal approved successfully.")
    } else {
      const reason = prompt("Please provide reason for rejection:")
      if (!reason) return
      await donorApi.rejectProposal(row.name || row.code, reason)
      alert("Proposal rejected.")
    }
    await loadProposals()
  } catch (e) {
    alert(e.message || "Action failed.")
  }
}

function openDetail(row) {
  selectedProposal.value = row
}

function formatDate(val) {
  if (!val) return "-"
  return String(val).split(" ")[0]
}

function getSectorClass(sector) {
  switch (sector) {
    case "WASH": return "bg-blue-50 text-blue-700 border border-blue-100"
    case "Education": return "bg-purple-50 text-purple-700 border border-purple-100"
    case "Health": return "bg-rose-50 text-rose-700 border border-rose-100"
    case "Disaster Relief": return "bg-amber-50 text-amber-700 border border-amber-100"
    case "Livelihoods": return "bg-emerald-50 text-emerald-700 border border-emerald-100"
    default: return "bg-slate-50 text-slate-700 border border-slate-200"
  }
}

function getSectorIcon(sector) {
  return {
    render() {
      return h("svg", { class: "w-3 h-3", fill: "currentColor", viewBox: "0 0 20 20" }, [
        h("path", {
          fillRule: "evenodd",
          d: "M10 18a8 8 0 100-16 8 8 0 000 16zm1-11a1 1 0 10-2 0v2H7a1 1 0 100 2h2v2a1 1 0 102 0v-2h2a1 1 0 100-2h-2V7z",
          clipRule: "evenodd"
        })
      ])
    }
  }
}
</script>
