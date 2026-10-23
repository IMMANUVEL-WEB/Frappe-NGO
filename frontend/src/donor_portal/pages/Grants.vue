<template>
  <div class="space-y-6">
    <!-- Top Stat Cards (4 Cards) -->
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
      <!-- 1. Total Grants -->
      <div class="bg-white rounded-2xl p-5 border border-slate-100 shadow-xs flex flex-col justify-between hover:shadow-md transition">
        <div class="flex items-start justify-between">
          <div>
            <span class="text-[11px] font-bold uppercase tracking-wider text-slate-400">Total Grants Value</span>
            <div class="text-2xl font-black text-slate-900 mt-1 tracking-tight">₹{{ stats.totalAmountFormatted }}</div>
            <div class="text-xs text-slate-400 font-medium mt-1">{{ grants.length }} total grant(s) allocated</div>
          </div>
          <div class="w-10 h-10 rounded-xl bg-emerald-50 text-emerald-600 flex items-center justify-center">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"/>
            </svg>
          </div>
        </div>
        <div class="mt-4 w-full bg-slate-100 rounded-full h-1.5 overflow-hidden">
          <div class="bg-emerald-500 h-1.5 rounded-full w-full"></div>
        </div>
      </div>

      <!-- 2. Active Grants -->
      <div class="bg-white rounded-2xl p-5 border border-slate-100 shadow-xs flex flex-col justify-between hover:shadow-md transition">
        <div class="flex items-start justify-between">
          <div>
            <span class="text-[11px] font-bold uppercase tracking-wider text-slate-400">Active Grants</span>
            <div class="text-2xl font-black text-slate-900 mt-1 tracking-tight">{{ stats.activeCount }}</div>
            <div class="text-xs text-slate-400 font-medium mt-1">Ongoing active projects</div>
          </div>
          <div class="w-10 h-10 rounded-xl bg-blue-50 text-blue-600 flex items-center justify-center">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 7v10a2 2 0 002 2h14a2 2 0 002-2V9a2 2 0 00-2-2h-6l-2-2H5a2 2 0 00-2 2z"/>
            </svg>
          </div>
        </div>
        <div class="mt-4 w-full bg-slate-100 rounded-full h-1.5 overflow-hidden">
          <div 
            class="bg-blue-600 h-1.5 rounded-full transition-all duration-500" 
            :style="{ width: `${stats.activePercent}%` }"
          ></div>
        </div>
      </div>

      <!-- 3. Total Received / Disbursed -->
      <div class="bg-white rounded-2xl p-5 border border-slate-100 shadow-xs flex flex-col justify-between hover:shadow-md transition">
        <div class="flex items-start justify-between">
          <div>
            <span class="text-[11px] font-bold uppercase tracking-wider text-slate-400">Total Disbursed</span>
            <div class="text-2xl font-black text-slate-900 mt-1 tracking-tight">₹{{ stats.totalReceivedFormatted }}</div>
            <div class="text-xs text-slate-400 font-medium mt-1">Funds disbursed to projects</div>
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
            :style="{ width: `${stats.disbursedPercent}%` }"
          ></div>
        </div>
      </div>

      <!-- 4. Completed Grants -->
      <div class="bg-white rounded-2xl p-5 border border-slate-100 shadow-xs flex flex-col justify-between hover:shadow-md transition">
        <div class="flex items-start justify-between">
          <div>
            <span class="text-[11px] font-bold uppercase tracking-wider text-slate-400">Completed Grants</span>
            <div class="text-2xl font-black text-slate-900 mt-1 tracking-tight">{{ stats.completedCount }}</div>
            <div class="text-xs text-slate-400 font-medium mt-1">Successfully closed</div>
          </div>
          <div class="w-10 h-10 rounded-xl bg-purple-50 text-purple-600 flex items-center justify-center">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>
            </svg>
          </div>
        </div>
        <div class="mt-4 w-full bg-slate-100 rounded-full h-1.5 overflow-hidden">
          <div 
            class="bg-purple-500 h-1.5 rounded-full transition-all duration-500" 
            :style="{ width: `${stats.completedPercent}%` }"
          ></div>
        </div>
      </div>
    </div>

    <!-- Filters & Search Bar -->
    <div class="bg-white rounded-2xl p-4 border border-slate-100 shadow-xs flex flex-col xl:flex-row items-center justify-between gap-3">
      <div class="flex flex-col sm:flex-row items-center gap-3 w-full xl:w-auto flex-1">
        <!-- Search Input -->
        <div class="relative w-full sm:w-80">
          <svg class="w-4 h-4 absolute left-3.5 top-1/2 -translate-y-1/2 text-slate-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/>
          </svg>
          <input 
            type="text" 
            v-model="searchQuery" 
            placeholder="Search by grant name, project or reference..." 
            class="w-full pl-10 pr-4 py-2 text-xs rounded-xl border border-slate-200 focus:outline-none focus:ring-2 focus:ring-emerald-500/20 focus:border-emerald-500 bg-slate-50/50"
          />
        </div>

        <!-- Dropdowns -->
        <div class="flex flex-wrap items-center gap-2 w-full sm:w-auto">
          <select 
            v-model="selectedStatus" 
            class="px-3 py-2 text-xs rounded-xl border border-slate-200 focus:outline-none focus:ring-2 focus:ring-emerald-500/20 bg-white text-slate-700"
          >
            <option value="">All Status</option>
            <option v-for="st in uniqueStatuses" :key="st" :value="st">{{ st }}</option>
          </select>

          <select 
            v-model="selectedSector" 
            class="px-3 py-2 text-xs rounded-xl border border-slate-200 focus:outline-none focus:ring-2 focus:ring-emerald-500/20 bg-white text-slate-700"
          >
            <option value="">All Sectors</option>
            <option v-for="sec in uniqueSectors" :key="sec" :value="sec">{{ sec }}</option>
          </select>
        </div>
      </div>

      <!-- Right Buttons -->
      <div class="flex items-center space-x-3 w-full xl:w-auto justify-end">
        <button 
          type="button" 
          @click="clearFilters"
          class="text-xs font-semibold text-slate-500 hover:text-slate-800 transition"
        >
          Clear Filters
        </button>
      </div>
    </div>

    <!-- Main Table Card -->
    <div class="bg-white rounded-2xl border border-slate-100 shadow-xs overflow-hidden">
      <!-- Loading State -->
      <div v-if="loading" class="py-16 text-center text-slate-400 text-xs font-medium">
        Loading grants...
      </div>

      <!-- Empty State -->
      <div v-else-if="filteredGrants.length === 0" class="py-16 text-center text-slate-400">
        <svg class="w-10 h-10 mx-auto mb-2 text-slate-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/>
        </svg>
        <p class="text-sm font-semibold text-slate-600">No grants found</p>
        <p class="text-xs text-slate-400 mt-1">There are no grants linked to your donor profile matching this filter.</p>
      </div>

      <div v-else class="overflow-x-auto">
        <table class="w-full text-left text-xs">
          <thead class="bg-slate-50/75 border-b border-slate-100 text-[11px] font-bold text-slate-500 uppercase tracking-wider">
            <tr>
              <th class="py-3.5 px-4">#</th>
              <th class="py-3.5 px-4">Grant Name</th>
              <th class="py-3.5 px-4">Project / Initiative</th>
              <th class="py-3.5 px-3">Sector</th>
              <th class="py-3.5 px-4">Grant Amount</th>
              <th class="py-3.5 px-4">Disbursed Amount</th>
              <th class="py-3.5 px-3">Status</th>
              <th class="py-3.5 px-4">Progress</th>
              <th class="py-3.5 px-3">Start Date</th>
              <th class="py-3.5 px-3">End Date</th>
              <th class="py-3.5 px-4 text-right">Actions</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-slate-100 text-slate-700">
            <tr 
              v-for="(grant, idx) in filteredGrants" 
              :key="grant.name"
              class="hover:bg-slate-50/60 transition group"
            >
              <td class="py-3.5 px-4 text-slate-400 font-medium">{{ idx + 1 }}</td>
              <td class="py-3.5 px-4">
                <div class="font-semibold text-slate-900">{{ grant.grant_title || grant.grant_id || grant.name }}</div>
                <div class="text-[11px] text-slate-400 font-mono">{{ grant.grant_id || grant.name }}</div>
              </td>
              <td class="py-3.5 px-4 text-slate-600 font-medium">{{ grant.linked_project || 'General Support' }}</td>
              <td class="py-3.5 px-3">
                <span 
                  class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-[11px] font-medium"
                  :class="getSectorClass(grant.sector)"
                >
                  <component :is="getSectorIcon(grant.sector)" class="w-3 h-3" />
                  {{ grant.sector || 'General' }}
                </span>
              </td>
              <td class="py-3.5 px-4 font-semibold text-slate-900">{{ formatRupee(grant.total_amount) }}</td>
              <td class="py-3.5 px-4 font-semibold text-slate-900">{{ formatRupee(grant.received || grant.spent) }}</td>
              <td class="py-3.5 px-3">
                <span 
                  class="inline-block px-2.5 py-0.5 rounded-full text-[11px] font-semibold"
                  :class="{
                    'bg-emerald-50 text-emerald-700 border border-emerald-100': grant.status === 'Active',
                    'bg-amber-50 text-amber-700 border border-amber-200': grant.status === 'Pending Approval' || grant.status === 'Draft',
                    'bg-purple-50 text-purple-700 border border-purple-200': grant.status === 'Completed'
                  }"
                >
                  {{ grant.status || 'Active' }}
                </span>
              </td>
              <td class="py-3.5 px-4">
                <div class="flex items-center space-x-2">
                  <span class="text-xs font-semibold text-slate-700 w-8">{{ Math.round(grant.utilization_percent || 0) }}%</span>
                  <div class="w-20 bg-slate-100 rounded-full h-1.5 overflow-hidden">
                    <div 
                      class="h-1.5 rounded-full"
                      :class="(grant.utilization_percent || 0) >= 100 ? 'bg-emerald-500' : 'bg-teal-500'"
                      :style="{ width: `${Math.min(100, grant.utilization_percent || 0)}%` }"
                    ></div>
                  </div>
                </div>
              </td>
              <td class="py-3.5 px-3 text-slate-500 whitespace-nowrap">{{ grant.valid_from || '-' }}</td>
              <td class="py-3.5 px-3 text-slate-500 whitespace-nowrap">{{ grant.valid_to || '-' }}</td>
              <td class="py-3.5 px-4 text-right">
                <div class="flex items-center justify-end space-x-1.5">
                  <router-link 
                    :to="`/donor-portal/grants/${grant.name || grant.grant_id}`"
                    class="p-1 rounded-lg hover:bg-slate-100 text-slate-400 hover:text-emerald-600 transition"
                    title="View Details"
                  >
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/>
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"/>
                    </svg>
                  </router-link>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- Pagination / Footer Info -->
      <div v-if="filteredGrants.length > 0" class="p-4 border-t border-slate-100 flex items-center justify-between text-xs text-slate-500">
        <div>
          Showing {{ filteredGrants.length }} grant(s)
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
const selectedStatus = ref("")
const selectedSector = ref("")

const grants = ref([])

onMounted(async () => {
  try {
    const res = await donorApi.getGrants()
    if (Array.isArray(res)) {
      grants.value = res
    }
  } catch (err) {
    console.error("Failed to fetch grants:", err)
  } finally {
    loading.value = false
  }
})

// Unique sectors & statuses for filter dropdowns
const uniqueSectors = computed(() => {
  const set = new Set()
  grants.value.forEach(g => {
    if (g.sector) set.add(g.sector)
  })
  return Array.from(set)
})

const uniqueStatuses = computed(() => {
  const set = new Set()
  grants.value.forEach(g => {
    if (g.status) set.add(g.status)
  })
  return Array.from(set)
})

// KPI Stats
const stats = computed(() => {
  const total = grants.value.length
  let totalAmount = 0
  let totalReceived = 0
  let active = 0
  let completed = 0

  grants.value.forEach(g => {
    totalAmount += Number(g.total_amount || 0)
    totalReceived += Number(g.received || g.spent || 0)
    if (g.status === "Active") active++
    if (g.status === "Completed") completed++
  })

  return {
    totalCount: total,
    totalAmountFormatted: formatLakhCr(totalAmount),
    totalReceivedFormatted: formatLakhCr(totalReceived),
    activeCount: active,
    activePercent: total > 0 ? Math.round((active / total) * 100) : 0,
    disbursedPercent: totalAmount > 0 ? Math.min(100, Math.round((totalReceived / totalAmount) * 100)) : 0,
    completedCount: completed,
    completedPercent: total > 0 ? Math.round((completed / total) * 100) : 0,
  }
})

function formatLakhCr(val) {
  if (!val || val === 0) return "0.00"
  if (val >= 10000000) {
    return `${(val / 10000000).toFixed(2)} Cr`
  }
  return `${(val / 100000).toFixed(2)} L`
}

function formatRupee(val) {
  if (!val && val !== 0) return "₹0"
  return "₹" + Number(val).toLocaleString("en-IN", { maximumFractionDigits: 0 })
}

// Sector icons & styles
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

// Clear filters
function clearFilters() {
  searchQuery.value = ""
  selectedStatus.value = ""
  selectedSector.value = ""
}

// Filtered grants
const filteredGrants = computed(() => {
  return grants.value.filter(grant => {
    const title = (grant.grant_title || grant.grant_id || grant.name || "").toLowerCase()
    const code = (grant.grant_id || grant.name || "").toLowerCase()
    const proj = (grant.linked_project || "").toLowerCase()
    const q = searchQuery.value.toLowerCase().trim()

    const matchesSearch = !q || title.includes(q) || code.includes(q) || proj.includes(q)
    const matchesStatus = !selectedStatus.value || grant.status === selectedStatus.value
    const matchesSector = !selectedSector.value || grant.sector === selectedSector.value

    return matchesSearch && matchesStatus && matchesSector
  })
})
</script>
