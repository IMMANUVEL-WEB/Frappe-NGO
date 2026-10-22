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
              :style="{ width: `${Math.min(kpis.percent_given_committed, 100)}%` }"
            ></div>
          </div>
          <div class="text-right text-[11px] text-slate-400 font-medium">
            {{ kpis.percent_given_committed }}% committed
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
            {{ kpis.percent_spent_given }}% of funds received
          </div>
        </div>
        <div class="mt-4 pt-3 border-t border-slate-50">
          <div class="w-full bg-slate-100 rounded-full h-1.5 overflow-hidden mb-1.5">
            <div 
              class="bg-blue-600 h-1.5 rounded-full transition-all duration-700"
              :style="{ width: `${Math.min(kpis.percent_spent_given, 100)}%` }"
            ></div>
          </div>
          <div class="text-right text-[11px] text-slate-400 font-medium">
            {{ kpis.percent_spent_given }}% utilized
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
              class="bg-amber-400 h-1.5 rounded-full transition-all duration-700 w-[40%]"
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
                {{ kpis.active_grants_count }}
              </div>
            </div>
          </div>
          <div class="text-xs text-slate-400 font-medium">
            {{ kpis.expiring_soon_count }} expiring within 90 days
          </div>
        </div>
        <div class="mt-4 pt-3 border-t border-slate-50">
          <div class="flex items-center text-[11px] text-purple-700 font-medium bg-purple-50 px-2 py-1 rounded-lg">
            <svg class="w-3.5 h-3.5 mr-1 text-purple-500 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/>
            </svg>
            <span>{{ kpis.expiring_soon_count }} expiring within 90 days</span>
          </div>
        </div>
      </div>

      <!-- 5. Total Purchase Amount -->
      <div class="bg-white rounded-2xl p-5 border border-slate-100 shadow-xs flex flex-col justify-between hover:shadow-md transition">
        <div>
          <div class="flex items-center space-x-3 mb-2.5">
            <div class="w-10 h-10 rounded-xl bg-teal-50 text-teal-600 flex items-center justify-center border border-teal-100/60">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z"/>
              </svg>
            </div>
            <div>
              <span class="text-[11px] font-bold uppercase tracking-wider text-slate-400">Total Purchase Amount</span>
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
      <div class="lg:col-span-7 bg-white rounded-2xl p-5 border border-slate-100 shadow-xs flex flex-col justify-between">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 mb-6">
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
        <div class="h-60 relative flex flex-col justify-end">
          <!-- Background Grid Lines -->
          <div class="absolute inset-x-6 inset-y-2 flex flex-col justify-between pointer-events-none text-[10px] text-slate-400 font-medium">
            <div class="border-b border-slate-100 pb-1">50</div>
            <div class="border-b border-slate-100 pb-1">40</div>
            <div class="border-b border-slate-100 pb-1">30</div>
            <div class="border-b border-slate-100 pb-1">20</div>
            <div class="border-b border-slate-100 pb-1">10</div>
            <div class="border-b border-slate-200 pb-1">0</div>
          </div>

          <!-- Bars Container -->
          <div class="relative h-full mx-10 flex items-end justify-between z-10">
            <div 
              v-for="(item, idx) in monthlySeries" 
              :key="idx" 
              class="flex flex-col items-center flex-1"
            >
              <!-- Dual stacked or side-by-side bars -->
              <div class="relative w-7 bg-blue-500 rounded-t-sm transition-all duration-500 hover:brightness-105 flex flex-col justify-end"
                   :style="{ height: `${(item.given / 50) * 100}%` }">
                <!-- Spent portion inside or bottom bar -->
                <div class="w-full bg-amber-400 rounded-t-sm"
                     :style="{ height: `${(item.spent / item.given) * 100}%` }"></div>
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
            <div class="bg-cyan-500 h-full w-[32%]" title="CapEx"></div>
            <div class="bg-emerald-500 h-full w-[55%]" title="OpEx"></div>
            <div class="bg-amber-400 h-full w-[13%]" title="Admin"></div>
          </div>

          <!-- Category Legend -->
          <div class="flex flex-wrap items-center gap-x-3.5 gap-y-1 text-xs text-slate-600">
            <div class="flex items-center space-x-1.5">
              <span class="w-2.5 h-2.5 rounded-sm bg-cyan-500"></span>
              <span>CapEx 32% (₹36.00 L)</span>
            </div>
            <div class="flex items-center space-x-1.5">
              <span class="w-2.5 h-2.5 rounded-sm bg-emerald-500"></span>
              <span>OpEx 55% (₹62.00 L)</span>
            </div>
            <div class="flex items-center space-x-1.5">
              <span class="w-2.5 h-2.5 rounded-sm bg-amber-400"></span>
              <span>Admin 13% (₹14.40 L)</span>
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

          <div class="space-y-3">
            <div v-for="(p, idx) in projectSpendList" :key="idx" class="text-xs">
              <div class="flex justify-between items-center mb-1">
                <span class="font-medium text-slate-700 truncate pr-2">{{ p.name }}</span>
                <span class="font-bold text-slate-900 shrink-0">₹{{ p.amount }} L</span>
              </div>
              <div class="w-full bg-slate-100 rounded-full h-1.5 overflow-hidden">
                <div 
                  class="h-1.5 rounded-full transition-all duration-500"
                  :class="p.barColor"
                  :style="{ width: `${p.percent}%` }"
                ></div>
              </div>
            </div>
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

      <!-- Proposal Card Matching Image 1 -->
      <div class="border border-slate-100 rounded-2xl p-4 flex flex-col md:flex-row items-start md:items-center justify-between gap-4 bg-slate-50/50 hover:bg-white hover:shadow-sm transition">
        <!-- Left Thumbnail & Details -->
        <div class="flex items-center space-x-4">
          <div class="w-20 h-16 rounded-xl overflow-hidden shrink-0 bg-slate-200 border border-slate-200/80">
            <img 
              src="https://images.unsplash.com/photo-1541252260730-0412e8e2108e?w=200&auto=format&fit=crop&q=60" 
              alt="Safe Drinking Water" 
              class="w-full h-full object-cover"
            />
          </div>
          <div>
            <h3 class="text-sm font-bold text-slate-900">Safe Drinking Water, Phase 2</h3>
            <div class="text-[11px] text-slate-500 font-medium mt-0.5">
              PP-2026-016 &middot; WASH &middot; Bihar
            </div>
            <div class="text-[11px] text-slate-500 mt-0.5">
              CapEx ₹18.00 L &middot; OpEx ₹13.00 L &middot; Admin ₹4.00 L
            </div>
            <!-- Action Buttons -->
            <div class="flex items-center space-x-2 mt-2">
              <button 
                type="button" 
                @click="handleDecision('Approved')"
                class="flex items-center space-x-1 px-3 py-1 bg-[#00875A] hover:bg-[#00744D] text-white rounded-lg text-xs font-semibold shadow-xs transition"
              >
                <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
                </svg>
                <span>Approve</span>
              </button>
              <button 
                type="button" 
                @click="handleDecision('Rejected')"
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
            ₹35.00 L
          </div>
          <div class="text-xs text-slate-400 font-medium">
            12 months
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue"

const kpis = ref({
  total_given: 18500000,
  total_committed: 35000000,
  percent_given_committed: 53,
  total_spent: 11200000,
  percent_spent_given: 61,
  balance_available: 7260000,
  committed_balance: 13800000,
  active_grants_count: 3,
  expiring_soon_count: 1,
  total_purchase_amount: 4350000
})

const monthlySeries = ref([
  { month: "Apr", given: 46, spent: 14 },
  { month: "May", given: 36, spent: 23 },
  { month: "Jun", given: 42, spent: 16 },
  { month: "Jul", given: 41, spent: 19 },
  { month: "Aug", given: 39, spent: 17 },
  { month: "Sep", given: 41, spent: 18 },
  { month: "Oct", given: 38, spent: 16 }
])

const projectSpendList = ref([
  { name: "Flood Relief Assam", amount: "48.00", percent: 90, barColor: "bg-blue-600" },
  { name: "School Kits Odisha", amount: "33.00", percent: 65, barColor: "bg-teal-500" },
  { name: "Livelihood Tamil Nadu", amount: "22.00", percent: 45, barColor: "bg-amber-400" },
  { name: "Clean Water Bihar", amount: "9.40", percent: 20, barColor: "bg-purple-600" }
])

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

function handleDecision(type) {
  alert(`Proposal decision recorded: ${type}`)
}
</script>
