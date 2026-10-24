<template>
  <div class="space-y-6">
    <!-- Top Stat Cards (5 Cards) -->
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-4">
      <!-- 1. Total Funds Received -->
      <div class="bg-white rounded-2xl p-5 border border-slate-100 shadow-xs flex flex-col justify-between hover:shadow-md transition">
        <div class="flex items-start justify-between">
          <div>
            <span class="text-[11px] font-bold uppercase tracking-wider text-slate-400">Total Funds Received</span>
            <div class="text-2xl font-black text-slate-900 mt-1 tracking-tight">₹{{ stats.totalReceivedFormatted }}</div>
            <div class="text-xs text-slate-400 font-medium mt-1">Across all grants</div>
          </div>
          <div class="w-10 h-10 rounded-xl bg-emerald-50 text-emerald-600 flex items-center justify-center">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 9V7a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2m2 4h10a2 2 0 002-2v-6a2 2 0 00-2-2H9a2 2 0 00-2 2v6a2 2 0 002 2zm7-5a2 2 0 11-4 0 2 2 0 014 0z"/>
            </svg>
          </div>
        </div>
        <div class="mt-4 flex items-center justify-between">
          <div class="w-full bg-slate-100 rounded-full h-1.5 overflow-hidden">
            <div class="bg-emerald-500 h-1.5 rounded-full w-full"></div>
          </div>
          <span class="text-[10px] font-semibold text-slate-400 ml-2">100%</span>
        </div>
      </div>

      <!-- 2. Total Utilized -->
      <div class="bg-white rounded-2xl p-5 border border-slate-100 shadow-xs flex flex-col justify-between hover:shadow-md transition">
        <div class="flex items-start justify-between">
          <div>
            <span class="text-[11px] font-bold uppercase tracking-wider text-slate-400">Total Utilized</span>
            <div class="text-2xl font-black text-slate-900 mt-1 tracking-tight">₹{{ stats.totalSpentFormatted }}</div>
            <div class="text-xs text-slate-400 font-medium mt-1">{{ stats.utilizationPercent }}% of total received</div>
          </div>
          <div class="w-10 h-10 rounded-xl bg-blue-50 text-blue-600 flex items-center justify-center">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 10h18M7 15h1m4 0h1m-7 4h12a3 3 0 003-3V8a3 3 0 00-3-3H6a3 3 0 00-3 3v8a3 3 0 003 3z"/>
            </svg>
          </div>
        </div>
        <div class="mt-4 flex items-center justify-between">
          <div class="w-full bg-slate-100 rounded-full h-1.5 overflow-hidden">
            <div 
              class="bg-blue-600 h-1.5 rounded-full transition-all duration-500" 
              :style="{ width: `${stats.utilizationPercent}%` }"
            ></div>
          </div>
          <span class="text-[10px] font-semibold text-slate-400 ml-2">{{ stats.utilizationPercent }}%</span>
        </div>
      </div>

      <!-- 3. Remaining Balance -->
      <div class="bg-white rounded-2xl p-5 border border-slate-100 shadow-xs flex flex-col justify-between hover:shadow-md transition">
        <div class="flex items-start justify-between">
          <div>
            <span class="text-[11px] font-bold uppercase tracking-wider text-slate-400">Remaining Balance</span>
            <div class="text-2xl font-black text-slate-900 mt-1 tracking-tight">₹{{ stats.remainingBalanceFormatted }}</div>
            <div class="text-xs text-slate-400 font-medium mt-1">{{ stats.balancePercent }}% liquid unspent</div>
          </div>
          <div class="w-10 h-10 rounded-xl bg-amber-50 text-amber-500 flex items-center justify-center">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/>
            </svg>
          </div>
        </div>
        <div class="mt-4 flex items-center justify-between">
          <div class="w-full bg-slate-100 rounded-full h-1.5 overflow-hidden">
            <div 
              class="bg-amber-400 h-1.5 rounded-full transition-all duration-500" 
              :style="{ width: `${stats.balancePercent}%` }"
            ></div>
          </div>
          <span class="text-[10px] font-semibold text-slate-400 ml-2">{{ stats.balancePercent }}%</span>
        </div>
      </div>

      <!-- 4. Active Grants -->
      <div class="bg-white rounded-2xl p-5 border border-slate-100 shadow-xs flex flex-col justify-between hover:shadow-md transition">
        <div class="flex items-start justify-between">
          <div>
            <span class="text-[11px] font-bold uppercase tracking-wider text-slate-400">Active Grants</span>
            <div class="text-2xl font-black text-slate-900 mt-1 tracking-tight">{{ stats.activeCount }}</div>
            <div class="text-xs text-slate-400 font-medium mt-1">Out of {{ grants.length }} total grants</div>
          </div>
          <div class="w-10 h-10 rounded-xl bg-purple-50 text-purple-600 flex items-center justify-center">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/>
            </svg>
          </div>
        </div>
        <div class="mt-4 flex items-center justify-between">
          <div class="w-full bg-slate-100 rounded-full h-1.5 overflow-hidden">
            <div 
              class="bg-purple-500 h-1.5 rounded-full transition-all duration-500" 
              :style="{ width: `${stats.activePercent}%` }"
            ></div>
          </div>
          <span class="text-[10px] font-semibold text-slate-400 ml-2">{{ stats.activePercent }}%</span>
        </div>
      </div>

      <!-- 5. Committed Budget -->
      <div class="bg-white rounded-2xl p-5 border border-slate-100 shadow-xs flex flex-col justify-between hover:shadow-md transition">
        <div class="flex items-start justify-between">
          <div>
            <span class="text-[11px] font-bold uppercase tracking-wider text-slate-400">Committed Budget</span>
            <div class="text-2xl font-black text-slate-900 mt-1 tracking-tight">₹{{ stats.totalAmountFormatted }}</div>
            <div class="text-xs text-slate-400 font-medium mt-1">Total grant sanctioned</div>
          </div>
          <div class="w-10 h-10 rounded-xl bg-teal-50 text-teal-600 flex items-center justify-center">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/>
            </svg>
          </div>
        </div>
        <div class="mt-4 flex items-center justify-between">
          <div class="w-full bg-slate-100 rounded-full h-1.5 overflow-hidden">
            <div class="bg-teal-500 h-1.5 rounded-full w-full"></div>
          </div>
          <span class="text-[10px] font-semibold text-slate-400 ml-2">100%</span>
        </div>
      </div>
    </div>

    <!-- Middle Charts Row (2 Cards) -->
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-6">
      <!-- Left Card: Monthly Trend (7 cols) -->
      <div class="lg:col-span-7 bg-white rounded-2xl p-6 border border-slate-100 shadow-xs flex flex-col justify-between min-h-[350px]">
        <!-- Header -->
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pb-4 border-b border-slate-100">
          <div class="flex items-center space-x-3">
            <div class="w-9 h-9 rounded-xl bg-emerald-50 text-emerald-600 flex items-center justify-center border border-emerald-100/60">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6" />
              </svg>
            </div>
            <div>
              <h3 class="text-sm font-bold text-slate-900 tracking-tight">Fund Utilization Trend (Lakh)</h3>
              <p class="text-[11px] text-slate-400 font-medium">Monthly grant receipts vs project execution disbursements</p>
            </div>
          </div>

          <!-- Legend Pills -->
          <div class="flex items-center gap-2">
            <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-lg text-xs font-semibold bg-blue-50/80 text-blue-700 border border-blue-100">
              <span class="w-2 h-2 rounded-full bg-blue-600"></span>
              Given
            </span>
            <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-lg text-xs font-semibold bg-amber-50/80 text-amber-700 border border-amber-100">
              <span class="w-2 h-2 rounded-full bg-amber-500"></span>
              Spent
            </span>
          </div>
        </div>

        <!-- Monthly Dynamic Bars -->
        <div class="relative pt-6 pb-2 min-h-[250px] flex flex-col justify-end">
          <!-- Background Grid Lines -->
          <div class="absolute inset-x-0 inset-y-4 flex flex-col justify-between pointer-events-none text-[10px] text-slate-400 font-medium">
            <div v-for="tick in chartTicks" :key="tick" class="border-b border-slate-100/90 pb-0.5 flex justify-between">
              <span class="font-mono text-slate-400 text-[10px]">?{{ tick }}L</span>
            </div>
          </div>

          <!-- Bars Container with background pillar tracks -->
          <div class="relative h-48 ml-10 mr-2 flex items-end justify-between z-10 gap-2 sm:gap-3">
            <div 
              v-for="(item, idx) in monthlyChartData" 
              :key="idx" 
              class="flex flex-col items-center flex-1 h-full justify-end relative cursor-pointer group"
              @mouseenter="hoveredTrendIndex = idx"
              @mouseleave="hoveredTrendIndex = null"
            >
              <!-- Floating Tooltip on Hover -->
              <transition
                enter-active-class="transition duration-150 ease-out"
                enter-from-class="opacity-0 translate-y-1"
                enter-to-class="opacity-100 translate-y-0"
                leave-active-class="transition duration-100 ease-in"
                leave-from-class="opacity-100 translate-y-0"
                leave-to-class="opacity-0 translate-y-1"
              >
                <div
                  v-if="hoveredTrendIndex === idx"
                  class="absolute -top-16 left-1/2 -translate-x-1/2 bg-slate-900/95 backdrop-blur-xs text-white text-[11px] rounded-xl py-2 px-3 shadow-xl border border-slate-800 whitespace-nowrap z-30 pointer-events-none"
                >
                  <div class="font-bold text-slate-300 border-b border-slate-700/60 pb-1 mb-1 text-[10px] uppercase tracking-wider text-center">
                    {{ item.month_year || item.month }}
                  </div>
                  <div class="flex items-center gap-2.5">
                    <span class="flex items-center gap-1 font-semibold text-blue-300">
                      <span class="w-1.5 h-1.5 rounded-full bg-blue-400"></span>
                      Given: ?{{ item.given }} L
                    </span>
                    <span class="text-slate-600">|</span>
                    <span class="flex items-center gap-1 font-semibold text-amber-300">
                      <span class="w-1.5 h-1.5 rounded-full bg-amber-400"></span>
                      Spent: ?{{ item.spent }} L
                    </span>
                  </div>
                </div>
              </transition>

              <!-- Pillar Slot -->
              <div 
                class="w-full max-w-[44px] h-40 rounded-xl bg-slate-50/80 border border-slate-100 flex items-end justify-center gap-1 sm:gap-1.5 p-1 transition-all duration-200"
                :class="hoveredTrendIndex === idx ? 'bg-slate-100 ring-2 ring-emerald-500/20' : ''"
              >
                <!-- Given Bar (Blue gradient) -->
                <div class="w-2.5 sm:w-3 h-full flex items-end justify-center">
                  <div 
                    class="w-full bg-gradient-to-t from-blue-600 to-sky-400 rounded-t-md transition-all duration-500 shadow-xs"
                    :style="{ height: getBarHeight(item.given) }"
                  ></div>
                </div>
                <!-- Spent Bar (Amber gradient) -->
                <div class="w-2.5 sm:w-3 h-full flex items-end justify-center">
                  <div 
                    class="w-full bg-gradient-to-t from-amber-500 to-amber-300 rounded-t-md transition-all duration-500 shadow-xs"
                    :style="{ height: getBarHeight(item.spent) }"
                  ></div>
                </div>
              </div>

              <!-- Month Label -->
              <span 
                class="text-[11px] font-semibold mt-2 transition"
                :class="item.given > 0 || item.spent > 0 ? 'text-slate-900 font-bold' : 'text-slate-400'"
              >
                {{ item.month }}
              </span>
            </div>
          </div>
        </div>
      </div>

      <!-- Right Card: Spend by Category / Breakdown (5 cols) -->
      <div class="lg:col-span-5 bg-white rounded-2xl p-5 border border-slate-100 shadow-xs flex flex-col justify-between">
        <div>
          <div class="flex items-center space-x-2 mb-4">
            <div class="w-2.5 h-2.5 rounded-full bg-emerald-500"></div>
            <h3 class="text-sm font-bold text-slate-900 tracking-tight">Expenditure Breakdown</h3>
          </div>

          <!-- Total Center Box -->
          <div class="p-4 rounded-xl bg-slate-50 text-center my-3 border border-slate-100">
            <span class="text-xs text-slate-500 font-medium">Total Expenditure Recorded</span>
            <div class="text-2xl font-black text-slate-900 mt-1">₹{{ stats.totalSpentFormatted }}</div>
          </div>
        </div>

        <!-- Category Items -->
        <div class="space-y-3 mt-2 text-xs">
          <div v-for="cat in spendCategories" :key="cat.label" class="space-y-1">
            <div class="flex items-center justify-between text-slate-700">
              <span class="flex items-center gap-2">
                <span class="w-2.5 h-2.5 rounded-full" :class="cat.dotColor"></span>
                <span class="font-medium text-slate-800">{{ cat.label }}</span>
              </span>
              <span class="font-semibold text-slate-900">
                ₹{{ formatRupee(cat.amount) }}
                <span class="text-slate-400 font-normal ml-1">({{ cat.percent }}%)</span>
              </span>
            </div>
            <div class="w-full bg-slate-100 rounded-full h-1.5 overflow-hidden">
              <div 
                class="h-1.5 rounded-full transition-all duration-500" 
                :class="cat.barColor" 
                :style="{ width: `${cat.percent}%` }"
              ></div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Bottom Section: Fund Utilization Details Table -->
    <div class="bg-white rounded-2xl border border-slate-100 shadow-xs overflow-hidden">
      <div class="p-4 border-b border-slate-100 flex flex-col md:flex-row md:items-center justify-between gap-3">
        <div class="flex items-center space-x-2">
          <div class="w-2.5 h-2.5 rounded-full bg-emerald-500"></div>
          <h3 class="text-sm font-bold text-slate-900 tracking-tight">Fund Utilization by Grant</h3>
        </div>

        <!-- Filters -->
        <div class="flex flex-wrap items-center gap-2">
          <select v-model="selectedSector" class="px-3 py-1.5 text-xs rounded-xl border border-slate-200 bg-white text-slate-700">
            <option value="">All Sectors</option>
            <option v-for="sec in uniqueSectors" :key="sec" :value="sec">{{ sec }}</option>
          </select>

          <div class="relative">
            <input 
              type="text" 
              v-model="searchQuery" 
              placeholder="Search project or grant..." 
              class="pl-8 pr-3 py-1.5 text-xs rounded-xl border border-slate-200 bg-slate-50/50 focus:outline-none focus:ring-2 focus:ring-emerald-500/20"
            />
            <svg class="w-3.5 h-3.5 absolute left-2.5 top-1/2 -translate-y-1/2 text-slate-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/>
            </svg>
          </div>
        </div>
      </div>

      <!-- Loading State -->
      <div v-if="loading" class="py-16 text-center text-slate-400 text-xs font-medium">
        Loading utilization data...
      </div>

      <!-- Empty State -->
      <div v-else-if="filteredGrants.length === 0" class="py-16 text-center text-slate-400">
        <svg class="w-10 h-10 mx-auto mb-2 text-slate-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/>
        </svg>
        <p class="text-sm font-semibold text-slate-600">No grant records found</p>
        <p class="text-xs text-slate-400 mt-1">No utilization records matching the filter criteria.</p>
      </div>

      <div v-else class="overflow-x-auto">
        <table class="w-full text-left text-xs">
          <thead class="bg-slate-50/75 border-b border-slate-100 text-[11px] font-bold text-slate-500 uppercase tracking-wider">
            <tr>
              <th class="py-3.5 px-4">#</th>
              <th class="py-3.5 px-4">Grant Name</th>
              <th class="py-3.5 px-4">Project / Initiative</th>
              <th class="py-3.5 px-3">Sector</th>
              <th class="py-3.5 px-4">Total Sanctioned</th>
              <th class="py-3.5 px-4">Disbursed</th>
              <th class="py-3.5 px-4">Utilized</th>
              <th class="py-3.5 px-4">Remaining Balance</th>
              <th class="py-3.5 px-4">Utilization %</th>
              <th class="py-3.5 px-3">Status</th>
              <th class="py-3.5 px-4 text-right">Actions</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-slate-100 text-slate-700">
            <tr 
              v-for="(row, idx) in filteredGrants" 
              :key="row.name"
              class="hover:bg-slate-50/60 transition group"
            >
              <td class="py-3.5 px-4 text-slate-400 font-medium">{{ idx + 1 }}</td>
              <td class="py-3.5 px-4">
                <div class="font-semibold text-slate-900">{{ row.grant_title || row.grant_id || row.name }}</div>
                <div class="text-[11px] text-slate-400 font-mono">{{ row.grant_id || row.name }}</div>
              </td>
              <td class="py-3.5 px-4 text-slate-600 font-medium">{{ row.linked_project || 'General Support' }}</td>
              <td class="py-3.5 px-3">
                <span class="inline-block px-2.5 py-0.5 rounded-full text-[11px] font-medium bg-slate-100 text-slate-700">
                  {{ row.sector || 'General' }}
                </span>
              </td>
              <td class="py-3.5 px-4 font-semibold text-slate-900">{{ formatRupee(row.total_amount) }}</td>
              <td class="py-3.5 px-4 font-semibold text-slate-900">{{ formatRupee(row.received) }}</td>
              <td class="py-3.5 px-4 font-semibold text-slate-900">{{ formatRupee(row.spent) }}</td>
              <td class="py-3.5 px-4 font-semibold text-emerald-600">{{ formatRupee(row.balance) }}</td>
              <td class="py-3.5 px-4">
                <div class="flex items-center space-x-2">
                  <span class="text-xs font-semibold text-slate-700 w-8">{{ Math.round(row.utilization_percent || 0) }}%</span>
                  <div class="w-16 bg-slate-100 rounded-full h-1.5 overflow-hidden">
                    <div 
                      class="h-1.5 rounded-full"
                      :class="(row.utilization_percent || 0) >= 100 ? 'bg-emerald-500' : 'bg-blue-600'"
                      :style="{ width: `${Math.min(100, row.utilization_percent || 0)}%` }"
                    ></div>
                  </div>
                </div>
              </td>
              <td class="py-3.5 px-3">
                <span 
                  class="inline-block px-2.5 py-0.5 rounded-full text-[11px] font-semibold"
                  :class="{
                    'bg-emerald-50 text-emerald-700 border border-emerald-100': row.status === 'Active',
                    'bg-amber-50 text-amber-700 border border-amber-200': row.status === 'Pending Approval' || row.status === 'Draft',
                    'bg-purple-50 text-purple-700 border border-purple-200': row.status === 'Completed'
                  }"
                >
                  {{ row.status || 'Active' }}
                </span>
              </td>
              <td class="py-3.5 px-4 text-right">
                <router-link 
                  :to="`/donor-portal/grants/${row.name || row.grant_id}`"
                  class="inline-flex items-center gap-1 text-xs font-medium text-emerald-600 hover:text-emerald-700"
                >
                  View Details
                </router-link>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed, onMounted, ref } from "vue"
import { donorApi } from "../api"

const loading = ref(true)
const searchQuery = ref("")
const selectedSector = ref("")

const grants = ref([])
const spendBreakdown = ref(null)
const monthlyChartData = ref([])
const hoveredTrendIndex = ref(null)

onMounted(async () => {
  try {
    const [grantsRes, spendRes, dashRes] = await Promise.all([
      donorApi.getGrants(),
      donorApi.getSpendBreakdown(),
      donorApi.getDashboard().catch(() => null)
    ])

    if (Array.isArray(grantsRes)) {
      grants.value = grantsRes
    }

    if (spendRes) {
      spendBreakdown.value = spendRes
    }

    if (dashRes && dashRes.charts && Array.isArray(dashRes.charts.given_vs_spent)) {
      monthlyChartData.value = dashRes.charts.given_vs_spent
    } else {
      // Default 6 months
      monthlyChartData.value = [
        { month: "May", given: 0, spent: 0 },
        { month: "Jun", given: 0, spent: 0 },
        { month: "Jul", given: 0, spent: 0 },
        { month: "Aug", given: 0, spent: 0 },
        { month: "Sep", given: 0, spent: 0 },
        { month: "Oct", given: 0, spent: 0 },
      ]
    }
  } catch (err) {
    console.error("Failed to fetch fund utilization data:", err)
  } finally {
    loading.value = false
  }
})

// Stats calculation
const stats = computed(() => {
  let totalSanctioned = 0
  let totalReceived = 0
  let totalSpent = 0
  let active = 0

  grants.value.forEach(g => {
    totalSanctioned += Number(g.total_amount || 0)
    totalReceived += Number(g.received || 0)
    totalSpent += Number(g.spent || 0)
    if (g.status === "Active") active++
  })

  // Fallback to spendBreakdown if available
  if (spendBreakdown.value && spendBreakdown.value.total_spent > totalSpent) {
    totalSpent = spendBreakdown.value.total_spent
  }

  const remaining = Math.max(0, totalReceived - totalSpent)
  const utilPercent = totalReceived > 0 ? Math.min(100, Math.round((totalSpent / totalReceived) * 100)) : 0
  const balPercent = totalReceived > 0 ? Math.max(0, 100 - utilPercent) : 0

  return {
    totalAmountFormatted: formatLakhCr(totalSanctioned),
    totalReceivedFormatted: formatLakhCr(totalReceived),
    totalSpentFormatted: formatLakhCr(totalSpent),
    remainingBalanceFormatted: formatLakhCr(remaining),
    utilizationPercent: utilPercent,
    balancePercent: balPercent,
    activeCount: active,
    activePercent: grants.value.length > 0 ? Math.round((active / grants.value.length) * 100) : 0
  }
})

// Spend Categories Breakdown
const spendCategories = computed(() => {
  const sb = spendBreakdown.value || {}
  const goods = Number(sb.goods || 0)
  const services = Number(sb.services_salaries || 0)
  const cash = Number(sb.cash_assistance || 0)
  const admin = Number(sb.admin || 0)
  const total = goods + services + cash + admin

  const calcPercent = (val) => total > 0 ? Math.round((val / total) * 100) : 0

  return [
    { label: "Goods & Direct Relief Kits", amount: goods, percent: calcPercent(goods), dotColor: "bg-blue-600", barColor: "bg-blue-600" },
    { label: "Services & Field Operations", amount: services, percent: calcPercent(services), dotColor: "bg-emerald-500", barColor: "bg-emerald-500" },
    { label: "Direct Cash / Beneficiary Aid", amount: cash, percent: calcPercent(cash), dotColor: "bg-purple-600", barColor: "bg-purple-600" },
    { label: "Admin & Statutory Audits", amount: admin, percent: calcPercent(admin), dotColor: "bg-amber-400", barColor: "bg-amber-400" },
  ]
})

// Chart Ticks & Scale
const maxChartValue = computed(() => {
  let max = 10
  monthlyChartData.value.forEach(item => {
    if (item.given > max) max = item.given
    if (item.spent > max) max = item.spent
  })
  return Math.ceil(max / 10) * 10
})

const chartTicks = computed(() => {
  const max = maxChartValue.value
  const step = max / 4
  return [max, Math.round(step * 3), Math.round(step * 2), Math.round(step), 0]
})

function getBarHeight(val) {
  const num = Number(val || 0)
  if (num <= 0) return "4px"
  const pct = Math.min(100, Math.max(6, Math.round((num / maxChartValue.value) * 100)))
  return `${pct}%`
}

// Formatting helpers
function formatLakhCr(val) {
  if (!val || val === 0) return "0.00"
  if (val >= 10000000) {
    return `${(val / 10000000).toFixed(2)} Cr`
  }
  return `${(val / 100000).toFixed(2)} L`
}

function formatRupee(val) {
  if (!val && val !== 0) return "0"
  return Number(val).toLocaleString("en-IN", { maximumFractionDigits: 0 })
}

// Unique sectors for filter dropdown
const uniqueSectors = computed(() => {
  const set = new Set()
  grants.value.forEach(g => {
    if (g.sector) set.add(g.sector)
  })
  return Array.from(set)
})

// Filtered grants
const filteredGrants = computed(() => {
  return grants.value.filter(g => {
    const title = (g.grant_title || g.grant_id || g.name || "").toLowerCase()
    const code = (g.grant_id || g.name || "").toLowerCase()
    const proj = (g.linked_project || "").toLowerCase()
    const q = searchQuery.value.toLowerCase().trim()

    const matchesSearch = !q || title.includes(q) || code.includes(q) || proj.includes(q)
    const matchesSector = !selectedSector.value || g.sector === selectedSector.value

    return matchesSearch && matchesSector
  })
})
</script>
