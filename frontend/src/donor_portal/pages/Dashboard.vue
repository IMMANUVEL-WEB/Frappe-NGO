<template>
  <div class="space-y-6">
    <!-- ROW 1: 5 KPI CARDS -->
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-4">
      <!-- 1. Total Given -->
      <div class="bg-white rounded-2xl p-5 border border-slate-100 shadow-xs flex flex-col justify-between hover:shadow-md transition">
        <div>
          <div class="flex items-center space-x-3 mb-2.5">
            <div class="w-10 h-10 rounded-xl bg-emerald-50 text-emerald-600 flex items-center justify-center text-lg font-black border border-emerald-100/60">
              ₹
            </div>
            <div>
              <span class="text-[11px] font-bold uppercase tracking-wider text-slate-400">Total Given</span>
              <div class="text-xl md:text-2xl font-black text-slate-900 tracking-tight">
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
              :style="{ width: `${Math.min(kpis.percent_given_committed || 0, 100)}%` }"
            ></div>
          </div>
          <div class="text-right text-[11px] text-slate-400 font-medium">
            {{ kpis.percent_given_committed || 0 }}% committed
          </div>
        </div>
      </div>

      <!-- 2. Total Spend -->
      <div class="bg-white rounded-2xl p-5 border border-slate-100 shadow-xs flex flex-col justify-between hover:shadow-md transition">
        <div>
          <div class="flex items-center space-x-3 mb-2.5">
            <div class="w-10 h-10 rounded-xl bg-blue-50 text-blue-600 flex items-center justify-center border border-blue-100/60">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 10h18M7 15h1m4 0h1m-7 4h12a3 3 0 003-3V8a3 3 0 00-3-3H6a3 3 0 00-3 3v8a3 3 0 003 3z"/>
              </svg>
            </div>
            <div>
              <span class="text-[11px] font-bold uppercase tracking-wider text-slate-400">Total Spend</span>
              <div class="text-xl md:text-2xl font-black text-slate-900 tracking-tight">
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
              :style="{ width: `${Math.min(kpis.percent_spent_given || 0, 100)}%` }"
            ></div>
          </div>
          <div class="text-right text-[11px] text-slate-400 font-medium">
            {{ kpis.percent_spent_given || 0 }}% utilized
          </div>
        </div>
      </div>

      <!-- 3. Balance Available -->
      <div class="bg-white rounded-2xl p-5 border border-slate-100 shadow-xs flex flex-col justify-between hover:shadow-md transition">
        <div>
          <div class="flex items-center space-x-3 mb-2.5">
            <div class="w-10 h-10 rounded-xl bg-amber-50 text-amber-500 flex items-center justify-center border border-amber-100/60">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
              </svg>
            </div>
            <div>
              <span class="text-[11px] font-bold uppercase tracking-wider text-slate-400">Balance Available</span>
              <div class="text-xl md:text-2xl font-black text-slate-900 tracking-tight">
                {{ formatCurrencyDisplay(kpis.balance_available) }}
              </div>
            </div>
          </div>
          <div class="text-xs text-slate-400 font-medium">
            Committed balance {{ formatCurrencyDisplay(kpis.committed_balance) }}
          </div>
        </div>
        <div class="mt-4 pt-3 border-t border-slate-50">
          <div class="w-full bg-slate-100 rounded-full h-1.5 overflow-hidden mb-1.5">
            <div 
              class="bg-amber-400 h-1.5 rounded-full transition-all duration-700"
              :style="{ width: `${kpis.total_committed > 0 ? Math.min((kpis.balance_available / kpis.total_committed) * 100, 100) : 0}%` }"
            ></div>
          </div>
          <div class="text-right text-[11px] text-slate-400 font-medium">
            Liquid reserves
          </div>
        </div>
      </div>

      <!-- 4. Active Grants -->
      <div class="bg-white rounded-2xl p-5 border border-slate-100 shadow-xs flex flex-col justify-between hover:shadow-md transition">
        <div>
          <div class="flex items-center space-x-3 mb-2.5">
            <div class="w-10 h-10 rounded-xl bg-purple-50 text-purple-600 flex items-center justify-center border border-purple-100/60">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/>
              </svg>
            </div>
            <div>
              <span class="text-[11px] font-bold uppercase tracking-wider text-slate-400">Active Grants</span>
              <div class="text-xl md:text-2xl font-black text-slate-900 tracking-tight">
                {{ kpis.active_grants_count || 0 }}
              </div>
            </div>
          </div>
          <div class="text-xs text-slate-400 font-medium">
            {{ kpis.expiring_soon_count || 0 }} expiring within 90 days
          </div>
        </div>
        <div class="mt-4 pt-3 border-t border-slate-50">
          <div class="text-[11px] text-purple-700 font-medium flex items-center space-x-1.5">
            <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/>
            </svg>
            <span>{{ kpis.expiring_soon_count || 0 }} expiring within 90 days</span>
          </div>
        </div>
      </div>

      <!-- 5. Total Purchase Amount -->
      <div class="bg-white rounded-2xl p-5 border border-slate-100 shadow-xs flex flex-col justify-between hover:shadow-md transition">
        <div>
          <div class="flex items-center space-x-3 mb-2.5">
            <div class="w-10 h-10 rounded-xl bg-teal-50 text-teal-600 flex items-center justify-center border border-teal-100/60">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z"/>
              </svg>
            </div>
            <div>
              <span class="text-[11px] font-bold uppercase tracking-wider text-slate-400">Total Purchase</span>
              <div class="text-xl md:text-2xl font-black text-slate-900 tracking-tight">
                {{ formatCurrencyDisplay(kpis.total_purchase_amount) }}
              </div>
            </div>
          </div>
          <div class="text-xs text-slate-400 font-medium">
            Goods and services bought
          </div>
        </div>
        <div class="mt-4 pt-3 border-t border-slate-50">
          <div class="text-[11px] text-teal-700 font-semibold flex items-center justify-between">
            <span>Verified Invoices</span>
            <span>100% Tax Compliant</span>
          </div>
        </div>
      </div>
    </div>

    <!-- ROW 2: VISUALIZATIONS -->
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-6">
      <!-- Given vs Spent by Month (Lakh) (7 cols) -->
      <div class="lg:col-span-7 bg-white rounded-2xl p-5 border border-slate-100 shadow-xs flex flex-col justify-between min-h-[340px]">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 mb-3">
          <div class="flex items-center space-x-2">
            <svg class="w-4 h-4 text-emerald-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"/>
            </svg>
            <h2 class="text-sm font-bold text-slate-900 tracking-tight">Given vs Spent by Month (Lakh)</h2>
          </div>
          <!-- Legend -->
          <div class="flex items-center space-x-4 text-xs font-medium text-slate-600">
            <div class="flex items-center space-x-1.5">
              <span class="w-2.5 h-2.5 rounded-sm bg-blue-500 inline-block"></span>
              <span>Given</span>
            </div>
            <div class="flex items-center space-x-1.5">
              <span class="w-2.5 h-2.5 rounded-sm bg-amber-400 inline-block"></span>
              <span>Spent</span>
            </div>
          </div>
        </div>

        <!-- Custom Visual Vertical Bar Chart -->
        <div class="h-64 relative flex flex-col justify-end pt-6">
          <!-- Background Grid Lines with Dynamic Y-Axis scale -->
          <div class="absolute inset-x-8 inset-y-4 flex flex-col justify-between pointer-events-none text-[10px] text-slate-400 font-medium">
            <div v-for="tick in yAxisTicks" :key="tick" class="border-b border-slate-100 pb-1">
              {{ tick }}
            </div>
          </div>

          <!-- Bars Container (Side-by-side grouped bars) -->
          <div class="relative h-48 ml-8 mr-4 flex items-end justify-between z-10 gap-1.5 sm:gap-3">
            <div 
              v-for="(item, idx) in monthlySeries" 
              :key="idx" 
              class="flex flex-col items-center flex-1 h-full justify-end group relative"
            >
              <!-- Hover Tooltip -->
              <div class="absolute -top-12 left-1/2 -translate-x-1/2 bg-slate-900 text-white text-[10px] rounded-lg py-1 px-2.5 pointer-events-none opacity-0 group-hover:opacity-100 transition shadow-xl whitespace-nowrap z-30">
                <span class="font-bold text-blue-300">Given: ₹{{ item.given }} L</span>
                <span class="mx-1.5 text-slate-500">|</span>
                <span class="font-bold text-amber-300">Spent: ₹{{ item.spent }} L</span>
              </div>

              <!-- Pair of Bars -->
              <div class="flex items-end gap-1 sm:gap-1.5 h-full w-full justify-center">
                <!-- Bar 1: Given (Blue) -->
                <div 
                  class="w-2.5 sm:w-3.5 bg-blue-500 rounded-t transition-all duration-500 hover:brightness-110 shadow-xs"
                  :style="{ height: `${getBarHeight(item.given)}%` }"
                  :title="`Given: ₹${item.given} Lakh`"
                ></div>

                <!-- Bar 2: Spent (Amber) -->
                <div 
                  class="w-2.5 sm:w-3.5 bg-amber-400 rounded-t transition-all duration-500 hover:brightness-110 shadow-xs"
                  :style="{ height: `${getBarHeight(item.spent)}%` }"
                  :title="`Spent: ₹${item.spent} Lakh`"
                ></div>
              </div>

              <span class="text-[11px] text-slate-500 font-medium mt-2">{{ item.month }}</span>
            </div>
          </div>
        </div>
      </div>

      <!-- Spend by category & Spend by project (5 cols) -->
      <div class="lg:col-span-5 bg-white rounded-2xl p-5 border border-slate-100 shadow-xs flex flex-col justify-between space-y-5">
        <!-- Spend by category -->
        <div>
          <div class="flex items-center space-x-2 mb-3">
            <svg class="w-4 h-4 text-teal-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 3.055A9.001 9.001 0 1020.945 13H11V3.055z"/>
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.488 9H15V3.512A9.025 9.025 0 0120.488 9z"/>
            </svg>
            <h2 class="text-sm font-bold text-slate-900 tracking-tight">Spend by category</h2>
          </div>

          <!-- Horizontal Stacked Progress Bar -->
          <div class="w-full h-3.5 bg-slate-100 rounded-full overflow-hidden flex mb-2.5">
            <div 
              class="bg-cyan-500 h-full transition-all duration-500" 
              :style="{ width: `${spendByCategory.capex?.percent || 0}%` }"
              :title="`CapEx: ${spendByCategory.capex?.percent || 0}%`"
            ></div>
            <div 
              class="bg-emerald-500 h-full transition-all duration-500" 
              :style="{ width: `${spendByCategory.opex?.percent || 0}%` }"
              :title="`OpEx: ${spendByCategory.opex?.percent || 0}%`"
            ></div>
            <div 
              class="bg-amber-400 h-full transition-all duration-500" 
              :style="{ width: `${spendByCategory.admin?.percent || 0}%` }"
              :title="`Admin: ${spendByCategory.admin?.percent || 0}%`"
            ></div>
          </div>

          <!-- Category Legend -->
          <div class="flex flex-wrap items-center gap-x-3.5 gap-y-1 text-xs text-slate-600">
            <div class="flex items-center space-x-1.5">
              <span class="w-2.5 h-2.5 rounded-sm bg-cyan-500"></span>
              <span>CapEx {{ spendByCategory.capex?.percent || 0 }}% (₹{{ spendByCategory.capex?.amount || 0 }} L)</span>
            </div>
            <div class="flex items-center space-x-1.5">
              <span class="w-2.5 h-2.5 rounded-sm bg-emerald-500"></span>
              <span>OpEx {{ spendByCategory.opex?.percent || 0 }}% (₹{{ spendByCategory.opex?.amount || 0 }} L)</span>
            </div>
            <div class="flex items-center space-x-1.5">
              <span class="w-2.5 h-2.5 rounded-sm bg-amber-400"></span>
              <span>Admin {{ spendByCategory.admin?.percent || 0 }}% (₹{{ spendByCategory.admin?.amount || 0 }} L)</span>
            </div>
          </div>
        </div>

        <!-- Spend by project -->
        <div class="border-t border-slate-100 pt-4">
          <div class="flex items-center space-x-2 mb-3">
            <svg class="w-4 h-4 text-indigo-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"/>
            </svg>
            <h2 class="text-sm font-bold text-slate-900 tracking-tight">Spend by project</h2>
          </div>

          <div v-if="projectSpendList.length" class="space-y-3">
            <div v-for="(p, idx) in projectSpendList" :key="idx" class="text-xs">
              <div class="flex justify-between items-center mb-1">
                <span class="font-medium text-slate-700 truncate pr-2">{{ p.project_name || p.project_id || p.name }}</span>
                <span class="font-bold text-slate-900 shrink-0">₹{{ p.amount_lakh || p.amount }} L</span>
              </div>
              <div class="w-full bg-slate-100 rounded-full h-1.5 overflow-hidden">
                <div 
                  class="h-1.5 rounded-full transition-all duration-500"
                  :class="getBarColor(idx)"
                  :style="{ width: `${Math.min(p.percent || 0, 100)}%` }"
                ></div>
              </div>
            </div>
          </div>
          <div v-else class="text-xs text-slate-400 py-3 text-center">
            No project spend recorded yet.
          </div>
        </div>
      </div>
    </div>

    <!-- ROW 3: PROJECT PROPOSALS AWAITING YOUR DECISION -->
    <div class="bg-white rounded-2xl p-5 border border-slate-100 shadow-xs">
      <div class="flex items-center justify-between mb-4">
        <div class="flex items-center space-x-2">
          <svg class="w-4 h-4 text-emerald-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/>
          </svg>
          <h2 class="text-sm font-bold text-slate-900 tracking-tight">Project proposals awaiting your decision</h2>
        </div>
        <router-link to="/donor-portal/proposals" class="text-xs font-semibold text-emerald-600 hover:text-emerald-700 flex items-center">
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
            <div class="w-12 h-12 rounded-xl bg-emerald-100/70 text-emerald-800 flex items-center justify-center font-bold text-sm shrink-0 border border-emerald-200/60">
              {{ (prop.sector || 'P').substring(0, 2).toUpperCase() }}
            </div>
            <div>
              <div class="flex items-center space-x-2">
                <span class="text-xs font-mono text-slate-400 font-semibold">{{ prop.code }}</span>
                <span class="px-2 py-0.5 rounded-full text-[10px] font-bold bg-amber-100 text-amber-800 border border-amber-200">
                  {{ prop.state || 'Pending Review' }}
                </span>
              </div>
              <h3 class="text-sm font-bold text-slate-900 mt-0.5">
                {{ prop.title }}
              </h3>
              <p class="text-xs text-slate-500 mt-0.5">
                Sector: {{ prop.sector }} &bull; CapEx: ₹{{ prop.capex_lakh }} L &bull; OpEx: ₹{{ prop.opex_lakh }} L &bull; Admin: ₹{{ prop.admin_lakh }} L
              </p>
              <div class="flex items-center space-x-3 mt-3">
                <button 
                  type="button" 
                  @click="handleDecision(prop.name, 'approve')"
                  class="flex items-center space-x-1 px-3 py-1 bg-emerald-600 hover:bg-emerald-700 text-white rounded-lg text-xs font-semibold shadow-xs transition"
                >
                  <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
                  </svg>
                  <span>Approve</span>
                </button>
                <button 
                  type="button" 
                  @click="handleDecision(prop.name, 'reject')"
                  class="flex items-center space-x-1 px-3 py-1 border border-rose-300 text-rose-600 hover:bg-rose-50 rounded-lg text-xs font-semibold transition"
                >
                  <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
                  </svg>
                  <span>Reject</span>
                </button>
              </div>
            </div>
          </div>

          <!-- Right Budget Info Badge -->
          <div class="text-left md:text-right shrink-0 bg-white md:bg-transparent p-3 md:p-0 rounded-xl border md:border-0 border-slate-100">
            <div class="text-lg font-black text-slate-900">
              ₹{{ prop.total_budget_lakh }} L
            </div>
            <div class="text-xs text-slate-400 font-medium">
              {{ prop.duration_months }} months
            </div>
          </div>
        </div>
      </div>

      <div v-else class="text-center py-8 text-xs text-slate-400 font-medium bg-slate-50/50 rounded-2xl border border-slate-100">
        No project proposals currently awaiting decision.
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from "vue"
import { donorApi } from "../api"

const loading = ref(true)

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
})

const monthlySeries = ref([
	{ month: "Apr", given: 0, spent: 0 },
	{ month: "May", given: 0, spent: 0 },
	{ month: "Jun", given: 0, spent: 0 },
	{ month: "Jul", given: 0, spent: 0 },
	{ month: "Aug", given: 0, spent: 0 },
	{ month: "Sep", given: 0, spent: 0 },
	{ month: "Oct", given: 0, spent: 0 },
])

const spendByCategory = ref({
	capex: { amount: 0, percent: 0 },
	opex: { amount: 0, percent: 0 },
	admin: { amount: 0, percent: 0 },
})

const projectSpendList = ref([])
const pendingProposals = ref([])

const barColors = ["bg-blue-600", "bg-teal-500", "bg-amber-400", "bg-purple-600", "bg-rose-500"]
function getBarColor(idx) {
	return barColors[idx % barColors.length]
}

const maxChartVal = computed(() => {
	const vals = (monthlySeries.value || []).flatMap((m) => [
		Number(m.given) || 0,
		Number(m.spent) || 0,
	])
	const max = Math.max(...vals, 0)
	if (max <= 0) return 10
	if (max <= 10) return 10
	if (max <= 25) return 25
	if (max <= 50) return 50
	return Math.ceil(max * 1.15)
})

const yAxisTicks = computed(() => {
	const max = maxChartVal.value
	return [
		max,
		Math.round(max * 0.75),
		Math.round(max * 0.5),
		Math.round(max * 0.25),
		0,
	]
})

function getBarHeight(val) {
	const num = Number(val) || 0
	if (num <= 0) return 0
	const max = maxChartVal.value
	const pct = (num / max) * 100
	return Math.max(Math.min(pct, 100), 2)
}

function formatCurrencyDisplay(val) {
	if (!val || val === 0) return "₹0"
	if (val >= 10000000) {
		return `₹${(val / 10000000).toFixed(2)} Cr`
	}
	if (val >= 100000) {
		return `₹${(val / 100000).toFixed(2)} L`
	}
	return `₹${Number(val).toLocaleString("en-IN")}`
}

async function loadDashboard() {
	loading.value = true
	try {
		const res = await donorApi.getDashboard()
		if (res) {
			if (res.kpis) kpis.value = res.kpis
			if (res.charts?.monthly_series?.length) {
				monthlySeries.value = res.charts.monthly_series
			}
			if (res.charts?.spend_by_category) {
				spendByCategory.value = res.charts.spend_by_category
			}
			if (res.charts?.spend_by_project) {
				projectSpendList.value = res.charts.spend_by_project
			}
			if (res.pending_proposals) {
				pendingProposals.value = res.pending_proposals
			}
		}
	} catch (err) {
		console.error("Failed to load dashboard data:", err)
	} finally {
		loading.value = false
	}
}

async function handleDecision(proposalName, action) {
	try {
		if (action === "approve") {
			await donorApi.approveProposal(proposalName)
			alert("Proposal approved successfully.")
		} else {
			const reason = prompt("Enter rejection reason (optional):")
			await donorApi.rejectProposal(proposalName, reason)
			alert("Proposal rejected.")
		}
		await loadDashboard()
	} catch (e) {
		alert(e?.message || `Failed to ${action} proposal.`)
	}
}

onMounted(() => {
	loadDashboard()
})
</script>
