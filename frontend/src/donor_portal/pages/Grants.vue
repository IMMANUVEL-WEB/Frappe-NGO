<template>
  <div class="space-y-6">
    <!-- Top Stat Cards (4 Cards) -->
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
      <!-- 1. Total Grants -->
      <div class="bg-white rounded-2xl p-5 border border-slate-100 shadow-xs flex flex-col justify-between hover:shadow-md transition">
        <div class="flex items-start justify-between">
          <div>
            <span class="text-[11px] font-bold uppercase tracking-wider text-slate-400">Total Grants</span>
            <div class="text-2xl font-black text-slate-900 mt-1 tracking-tight">₹1.25 Cr</div>
            <div class="text-xs text-slate-400 font-medium mt-1">Value of active grants</div>
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
            <div class="text-2xl font-black text-slate-900 mt-1 tracking-tight">6</div>
            <div class="text-xs text-slate-400 font-medium mt-1">Ongoing grants</div>
          </div>
          <div class="w-10 h-10 rounded-xl bg-blue-50 text-blue-600 flex items-center justify-center">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 7v10a2 2 0 002 2h14a2 2 0 002-2V9a2 2 0 00-2-2h-6l-2-2H5a2 2 0 00-2 2z"/>
            </svg>
          </div>
        </div>
        <div class="mt-4 w-full bg-slate-100 rounded-full h-1.5 overflow-hidden">
          <div class="bg-blue-600 h-1.5 rounded-full w-[60%]"></div>
        </div>
      </div>

      <!-- 3. Pending Approval -->
      <div class="bg-white rounded-2xl p-5 border border-slate-100 shadow-xs flex flex-col justify-between hover:shadow-md transition">
        <div class="flex items-start justify-between">
          <div>
            <span class="text-[11px] font-bold uppercase tracking-wider text-slate-400">Pending Approval</span>
            <div class="text-2xl font-black text-slate-900 mt-1 tracking-tight">1</div>
            <div class="text-xs text-slate-400 font-medium mt-1">Awaiting confirmation</div>
          </div>
          <div class="w-10 h-10 rounded-xl bg-amber-50 text-amber-500 flex items-center justify-center">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/>
            </svg>
          </div>
        </div>
        <div class="mt-4 w-full bg-slate-100 rounded-full h-1.5 overflow-hidden">
          <div class="bg-amber-400 h-1.5 rounded-full w-[35%]"></div>
        </div>
      </div>

      <!-- 4. Completed Grants -->
      <div class="bg-white rounded-2xl p-5 border border-slate-100 shadow-xs flex flex-col justify-between hover:shadow-md transition">
        <div class="flex items-start justify-between">
          <div>
            <span class="text-[11px] font-bold uppercase tracking-wider text-slate-400">Completed Grants</span>
            <div class="text-2xl font-black text-slate-900 mt-1 tracking-tight">2</div>
            <div class="text-xs text-slate-400 font-medium mt-1">Successfully closed</div>
          </div>
          <div class="w-10 h-10 rounded-xl bg-purple-50 text-purple-600 flex items-center justify-center">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>
            </svg>
          </div>
        </div>
        <div class="mt-4 w-full bg-slate-100 rounded-full h-1.5 overflow-hidden">
          <div class="bg-purple-500 h-1.5 rounded-full w-full"></div>
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
            placeholder="Search by grant name, project, sector or reference number..." 
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
            <option value="Active">Active</option>
            <option value="Pending Approval">Pending Approval</option>
            <option value="Completed">Completed</option>
          </select>

          <select 
            v-model="selectedSector" 
            class="px-3 py-2 text-xs rounded-xl border border-slate-200 focus:outline-none focus:ring-2 focus:ring-emerald-500/20 bg-white text-slate-700"
          >
            <option value="">All Sectors</option>
            <option value="WASH">WASH</option>
            <option value="Education">Education</option>
            <option value="Health">Health</option>
            <option value="Disaster Relief">Disaster Relief</option>
            <option value="Livelihoods">Livelihoods</option>
            <option value="Governance">Governance</option>
          </select>

          <select 
            v-model="selectedGeography" 
            class="px-3 py-2 text-xs rounded-xl border border-slate-200 focus:outline-none focus:ring-2 focus:ring-emerald-500/20 bg-white text-slate-700"
          >
            <option value="">All Geographies</option>
            <option value="Bihar">Bihar</option>
            <option value="Uttar Pradesh">Uttar Pradesh</option>
            <option value="Tamil Nadu">Tamil Nadu</option>
            <option value="Assam">Assam</option>
            <option value="Odisha">Odisha</option>
            <option value="Maharashtra">Maharashtra</option>
          </select>

          <!-- Date Range Picker Badge -->
          <div class="flex items-center space-x-1 px-3 py-1.5 rounded-xl border border-slate-200 bg-white text-xs text-slate-600">
            <svg class="w-3.5 h-3.5 text-slate-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/>
            </svg>
            <span class="text-slate-500">Select Date Range</span>
            <button type="button" class="text-slate-400 hover:text-slate-600 ml-1">&times;</button>
          </div>
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

        <button 
          type="button" 
          class="flex items-center space-x-1.5 px-3 py-2 rounded-xl border border-slate-200 text-xs font-semibold text-slate-700 hover:bg-slate-50 transition"
        >
          <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"/>
          </svg>
          <span>Export</span>
          <svg class="w-3 h-3 text-slate-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
          </svg>
        </button>
      </div>
    </div>

    <!-- Main Table Card -->
    <div class="bg-white rounded-2xl border border-slate-100 shadow-xs overflow-hidden">
      <div class="overflow-x-auto">
        <table class="w-full text-left text-xs">
          <thead class="bg-slate-50/75 border-b border-slate-100 text-[11px] font-bold text-slate-500 uppercase tracking-wider">
            <tr>
              <th class="py-3.5 px-4">#</th>
              <th class="py-3.5 px-4">Grant Name</th>
              <th class="py-3.5 px-4">Project / Initiative</th>
              <th class="py-3.5 px-3">Sector</th>
              <th class="py-3.5 px-3">Geography</th>
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
              :key="grant.code"
              class="hover:bg-slate-50/60 transition group"
            >
              <td class="py-3.5 px-4 text-slate-400 font-medium">{{ idx + 1 }}</td>
              <td class="py-3.5 px-4">
                <div class="font-semibold text-slate-900">{{ grant.name }}</div>
                <div class="text-[11px] text-slate-400 font-mono">{{ grant.code }}</div>
              </td>
              <td class="py-3.5 px-4 text-slate-600 font-medium">{{ grant.project }}</td>
              <td class="py-3.5 px-3">
                <span 
                  class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-[11px] font-medium"
                  :class="getSectorClass(grant.sector)"
                >
                  <component :is="getSectorIcon(grant.sector)" class="w-3 h-3" />
                  {{ grant.sector }}
                </span>
              </td>
              <td class="py-3.5 px-3 text-slate-600">{{ grant.geography }}</td>
              <td class="py-3.5 px-4 font-semibold text-slate-900">{{ grant.grantAmount }}</td>
              <td class="py-3.5 px-4 font-semibold text-slate-900">{{ grant.disbursedAmount }}</td>
              <td class="py-3.5 px-3">
                <span 
                  class="inline-block px-2.5 py-0.5 rounded-full text-[11px] font-semibold"
                  :class="{
                    'bg-emerald-50 text-emerald-700 border border-emerald-100': grant.status === 'Active',
                    'bg-amber-50 text-amber-700 border border-amber-200': grant.status === 'Pending Approval',
                    'bg-purple-50 text-purple-700 border border-purple-200': grant.status === 'Completed'
                  }"
                >
                  {{ grant.status }}
                </span>
              </td>
              <td class="py-3.5 px-4">
                <div class="flex items-center space-x-2">
                  <span class="text-xs font-semibold text-slate-700 w-8">{{ grant.progress }}%</span>
                  <div class="w-20 bg-slate-100 rounded-full h-1.5 overflow-hidden">
                    <div 
                      class="h-1.5 rounded-full"
                      :class="grant.progress === 100 ? 'bg-emerald-500' : 'bg-teal-500'"
                      :style="{ width: `${grant.progress}%` }"
                    ></div>
                  </div>
                </div>
              </td>
              <td class="py-3.5 px-3 text-slate-500 whitespace-nowrap">{{ grant.startDate }}</td>
              <td class="py-3.5 px-3 text-slate-500 whitespace-nowrap">{{ grant.endDate }}</td>
              <td class="py-3.5 px-4 text-right">
                <div class="flex items-center justify-end space-x-1.5">
                  <router-link 
                    :to="`/donor-portal/grants/${grant.code}`"
                    class="p-1 rounded-lg hover:bg-slate-100 text-slate-400 hover:text-emerald-600 transition"
                    title="View Details"
                  >
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/>
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"/>
                    </svg>
                  </router-link>
                  <button 
                    type="button" 
                    class="p-1 rounded-lg hover:bg-slate-100 text-slate-400 hover:text-slate-600"
                  >
                    <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20">
                      <path d="M10 6a2 2 0 110-4 2 2 0 010 4zM10 12a2 2 0 110-4 2 2 0 010 4zM10 18a2 2 0 110-4 2 2 0 010 4z" />
                    </svg>
                  </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- Pagination -->
      <div class="px-5 py-3.5 border-t border-slate-100 flex items-center justify-between text-xs text-slate-500">
        <div>
          Showing 1 - {{ filteredGrants.length }} of {{ filteredGrants.length }} grants
        </div>
        <div class="flex items-center space-x-1.5">
          <button class="w-7 h-7 rounded-lg border border-slate-200 flex items-center justify-center opacity-40 cursor-not-allowed">
            &lt;
          </button>
          <button class="w-7 h-7 rounded-lg bg-[#00875A] text-white flex items-center justify-center font-semibold">
            1
          </button>
          <button class="w-7 h-7 rounded-lg border border-slate-200 flex items-center justify-center opacity-40 cursor-not-allowed">
            &gt;
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, h } from "vue"

const searchQuery = ref("")
const selectedStatus = ref("")
const selectedSector = ref("")
const selectedGeography = ref("")

const grants = ref([
  {
    name: "Clean Water Access Initiative",
    code: "GI-2026-001",
    project: "Clean Water Access Initiative",
    sector: "WASH",
    geography: "Bihar",
    grantAmount: "₹22,00,000",
    disbursedAmount: "₹15,40,000",
    status: "Active",
    progress: 70,
    startDate: "05 Oct 2026",
    endDate: "30 Jun 2027"
  },
  {
    name: "Education for Rural Children",
    code: "GI-2026-002",
    project: "Quality Education for Rural Children",
    sector: "Education",
    geography: "Uttar Pradesh",
    grantAmount: "₹18,00,000",
    disbursedAmount: "₹9,00,000",
    status: "Active",
    progress: 50,
    startDate: "12 Sep 2026",
    endDate: "31 Mar 2027"
  },
  {
    name: "Health & Wellness Program",
    code: "GI-2026-003",
    project: "Community Health & Wellness Program",
    sector: "Health",
    geography: "Tamil Nadu",
    grantAmount: "₹25,00,000",
    disbursedAmount: "₹12,50,000",
    status: "Active",
    progress: 50,
    startDate: "12 Oct 2026",
    endDate: "30 Sep 2027"
  },
  {
    name: "Disaster Relief Support",
    code: "GI-2026-004",
    project: "Disaster Relief Response",
    sector: "Disaster Relief",
    geography: "Assam",
    grantAmount: "₹15,00,000",
    disbursedAmount: "₹7,50,000",
    status: "Pending Approval",
    progress: 50,
    startDate: "20 Sep 2026",
    endDate: "31 Dec 2026"
  },
  {
    name: "Livelihood Support Program",
    code: "GI-2026-005",
    project: "Livelihood Support for Women",
    sector: "Livelihoods",
    geography: "Odisha",
    grantAmount: "₹12,00,000",
    disbursedAmount: "₹6,00,000",
    status: "Active",
    progress: 60,
    startDate: "28 Sep 2026",
    endDate: "31 Mar 2027"
  },
  {
    name: "Governance & Participation",
    code: "GI-2026-006",
    project: "Governance & Community Participation",
    sector: "Governance",
    geography: "Maharashtra",
    grantAmount: "₹10,00,000",
    disbursedAmount: "₹5,00,000",
    status: "Completed",
    progress: 100,
    startDate: "15 Sep 2026",
    endDate: "15 Dec 2026"
  }
])

const filteredGrants = computed(() => {
  return grants.value.filter(g => {
    const matchSearch = !searchQuery.value || 
      g.name.toLowerCase().includes(searchQuery.value.toLowerCase()) || 
      g.code.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
      g.project.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
      g.sector.toLowerCase().includes(searchQuery.value.toLowerCase())
    const matchStatus = !selectedStatus.value || g.status === selectedStatus.value
    const matchSector = !selectedSector.value || g.sector === selectedSector.value
    const matchGeo = !selectedGeography.value || g.geography === selectedGeography.value
    return matchSearch && matchStatus && matchSector && matchGeo
  })
})

function clearFilters() {
  searchQuery.value = ""
  selectedStatus.value = ""
  selectedSector.value = ""
  selectedGeography.value = ""
}

function getSectorClass(sector) {
  switch (sector) {
    case 'Health': return 'bg-rose-50 text-rose-600'
    case 'Education': return 'bg-purple-50 text-purple-600'
    case 'WASH': return 'bg-sky-50 text-sky-600'
    case 'Livelihoods': return 'bg-emerald-50 text-emerald-600'
    case 'Disaster Relief': return 'bg-amber-50 text-amber-700'
    case 'Governance': return 'bg-indigo-50 text-indigo-600'
    default: return 'bg-slate-100 text-slate-700'
  }
}

function getSectorIcon(sector) {
  return {
    render() {
      if (sector === 'Health') {
        return h('svg', { fill: 'currentColor', viewBox: '0 0 20 20' }, [
          h('path', { 'fill-rule': 'evenodd', d: 'M3.172 5.172a4 4 0 015.656 0L10 6.343l1.172-1.171a4 4 0 115.656 5.656L10 17.657l-6.828-6.829a4 4 0 010-5.656z', 'clip-rule': 'evenodd' })
        ])
      }
      if (sector === 'Education') {
        return h('svg', { fill: 'none', stroke: 'currentColor', 'stroke-width': '2', viewBox: '0 0 24 24' }, [
          h('path', { 'stroke-linecap': 'round', 'stroke-linejoin': 'round', d: 'M12 14l9-5-9-5-9 5 9 5z' }),
          h('path', { 'stroke-linecap': 'round', 'stroke-linejoin': 'round', d: 'M12 14l6.16-3.422a12.083 12.083 0 01.665 6.479A11.952 11.952 0 0012 20.055a11.952 11.952 0 00-6.824-2.998 12.078 12.078 0 01.665-6.479L12 14z' })
        ])
      }
      if (sector === 'WASH') {
        return h('svg', { fill: 'currentColor', viewBox: '0 0 20 20' }, [
          h('path', { 'fill-rule': 'evenodd', d: 'M10 2a1 1 0 01.832.445l4.83 7.245A6 6 0 114.338 9.69L9.168 2.445A1 1 0 0110 2z', 'clip-rule': 'evenodd' })
        ])
      }
      if (sector === 'Livelihoods') {
        return h('svg', { fill: 'none', stroke: 'currentColor', 'stroke-width': '2', viewBox: '0 0 24 24' }, [
          h('path', { 'stroke-linecap': 'round', 'stroke-linejoin': 'round', d: 'M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z' })
        ])
      }
      if (sector === 'Disaster Relief') {
        return h('svg', { fill: 'currentColor', viewBox: '0 0 20 20' }, [
          h('path', { 'fill-rule': 'evenodd', d: 'M8.257 3.099c.765-1.36 2.722-1.36 3.486 0l5.58 9.92c.75 1.334-.213 2.98-1.742 2.98H4.42c-1.53 0-2.493-1.646-1.743-2.98l5.58-9.92zM11 13a1 1 0 11-2 0 1 1 0 012 0zm-1-8a1 1 0 00-1 1v3a1 1 0 002 0V6a1 1 0 00-1-1z', 'clip-rule': 'evenodd' })
        ])
      }
      return h('svg', { fill: 'currentColor', viewBox: '0 0 20 20' }, [
        h('path', { d: 'M4 4a2 2 0 00-2 2v1h16V6a2 2 0 00-2-2H4z' }),
        h('path', { 'fill-rule': 'evenodd', d: 'M18 9H2v5a2 2 0 002 2h12a2 2 0 002-2V9zM4 13a1 1 0 011-1h1a1 1 0 110 2H5a1 1 0 01-1-1zm5-1a1 1 0 100 2h1a1 1 0 100-2H9z', 'clip-rule': 'evenodd' })
      ])
    }
  }
}
</script>
