<template>
  <div class="space-y-6">
    <!-- Back Button -->
    <div class="flex items-center space-x-2">
      <router-link to="/donor-portal/grants" class="text-xs font-bold text-slate-500 hover:text-slate-800 flex items-center">
        <span class="mr-1">&larr;</span> Back to Grants
      </router-link>
    </div>

    <!-- Loading Skeleton -->
    <div v-if="loading" class="h-64 bg-white rounded-2xl border border-slate-200 animate-pulse"></div>

    <div v-else-if="grantData" class="space-y-6">
      <!-- Grant Summary Header Card -->
      <div class="bg-white rounded-2xl p-6 border border-slate-200/90 shadow-xs">
        <div class="flex flex-col md:flex-row md:items-center justify-between gap-4 pb-5 border-b border-slate-100">
          <div>
            <div class="flex items-center space-x-2.5 mb-2">
              <span class="text-xs font-bold px-2.5 py-0.5 rounded-full bg-emerald-100 text-emerald-800">
                {{ grantData.grant.status }}
              </span>
              <span class="text-xs font-semibold px-2 py-0.5 rounded-md bg-slate-100 text-slate-700">
                {{ grantData.grant.compliance_tag }}
              </span>
              <span class="text-xs font-mono text-slate-400">{{ grantData.grant.grant_id }}</span>
            </div>
            <h1 class="text-xl md:text-2xl font-extrabold text-slate-900 tracking-tight">{{ grantData.grant.grant_title }}</h1>
            <p class="text-xs text-slate-500 font-medium mt-1">
              Project: <span class="text-slate-800 font-semibold">{{ grantData.grant.linked_project }}</span> &middot; 
              Cost Center: <span class="text-slate-800 font-semibold">{{ grantData.grant.cost_center }}</span>
            </p>
          </div>
          <div class="text-left md:text-right">
            <span class="text-xs text-slate-400 uppercase font-bold tracking-wider block">Total Commitment</span>
            <span class="text-2xl font-black text-slate-900">₹{{ (grantData.grant.total_amount / 100000).toFixed(2) }} L</span>
            <span class="text-xs text-slate-500 block">INR Equivalent</span>
          </div>
        </div>

        <!-- Agreement Metadata -->
        <div class="grid grid-cols-2 sm:grid-cols-4 gap-4 pt-4 text-xs">
          <div>
            <span class="text-slate-400 font-medium block">Valid From</span>
            <span class="font-bold text-slate-800">{{ grantData.grant.valid_from }}</span>
          </div>
          <div>
            <span class="text-slate-400 font-medium block">Valid To</span>
            <span class="font-bold text-slate-800">{{ grantData.grant.valid_to || 'Ongoing' }}</span>
          </div>
          <div>
            <span class="text-slate-400 font-medium block">Funding Type</span>
            <span class="font-bold text-slate-800">{{ grantData.grant.funding_type }}</span>
          </div>
          <div>
            <span class="text-slate-400 font-medium block">Currency</span>
            <span class="font-bold text-slate-800">{{ grantData.grant.currency }}</span>
          </div>
        </div>
      </div>

      <!-- Budget vs Actual Table with Variance -->
      <div class="bg-white rounded-2xl p-6 border border-slate-200/90 shadow-xs">
        <h2 class="text-base font-bold text-slate-900 mb-4 flex items-center space-x-2">
          <svg class="w-5 h-5 text-emerald-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"/>
          </svg>
          <span>Budget vs Actual Variance</span>
        </h2>

        <div class="overflow-x-auto">
          <table class="w-full text-left text-xs">
            <thead>
              <tr class="border-b border-slate-200 text-slate-400 font-bold uppercase tracking-wider">
                <th class="py-3 px-3">Account</th>
                <th class="py-3 px-3">Category</th>
                <th class="py-3 px-3 text-right">Budget (₹)</th>
                <th class="py-3 px-3 text-right">Actual Spent (₹)</th>
                <th class="py-3 px-3 text-right">Variance (Unspent)</th>
                <th class="py-3 px-3 text-center">Utilization</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-slate-100">
              <tr v-for="(b, idx) in grantData.budget_vs_actual" :key="idx" class="hover:bg-slate-50">
                <td class="py-3.5 px-3 font-semibold text-slate-900">{{ b.account }}</td>
                <td class="py-3.5 px-3">
                  <span 
                    class="px-2 py-0.5 rounded-md font-semibold text-[11px]"
                    :class="{
                      'bg-cyan-100 text-cyan-800': b.category === 'CapEx',
                      'bg-emerald-100 text-emerald-800': b.category === 'OpEx',
                      'bg-amber-100 text-amber-800': b.category === 'Admin'
                    }"
                  >
                    {{ b.category }}
                  </span>
                </td>
                <td class="py-3.5 px-3 text-right font-medium text-slate-700">₹{{ Number(b.budget_amount).toLocaleString('en-IN') }}</td>
                <td class="py-3.5 px-3 text-right font-medium text-blue-600">₹{{ Number(b.actual_spent).toLocaleString('en-IN') }}</td>
                <td class="py-3.5 px-3 text-right font-bold text-emerald-600">₹{{ Number(b.variance).toLocaleString('en-IN') }}</td>
                <td class="py-3.5 px-3 text-center">
                  <div class="w-24 bg-slate-100 rounded-full h-2 inline-block overflow-hidden mr-2">
                    <div 
                      class="bg-blue-600 h-2 rounded-full"
                      :style="{ width: `${Math.min(b.utilization_percent, 100)}%` }"
                    ></div>
                  </div>
                  <span class="font-bold text-slate-700">{{ b.utilization_percent }}%</span>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- Fund Flow Timeline -->
      <div class="bg-white rounded-2xl p-6 border border-slate-200/90 shadow-xs">
        <h2 class="text-base font-bold text-slate-900 mb-6 flex items-center space-x-2">
          <svg class="w-5 h-5 text-indigo-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/>
          </svg>
          <span>Fund Flow Lifecycle</span>
        </h2>

        <div class="relative pl-6 space-y-6 before:absolute before:left-2 before:top-2 before:bottom-2 before:w-0.5 before:bg-slate-200">
          <div v-for="(t, idx) in grantData.timeline" :key="idx" class="relative">
            <div 
              class="absolute -left-[27px] top-0 w-3.5 h-3.5 rounded-full border-2 bg-white"
              :class="t.status === 'Completed' ? 'border-emerald-600 bg-emerald-600' : 'border-blue-600 bg-blue-600'"
            ></div>
            <div class="text-xs">
              <span class="font-bold text-slate-900 text-sm block">{{ t.stage }}</span>
              <span class="text-slate-500 font-medium">₹{{ Number(t.amount).toLocaleString('en-IN') }} &middot; Status: {{ t.status }}</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue"
import { useRoute } from "vue-router"
import { donorApi } from "../api"

const route = useRoute()
const loading = ref(true)
const grantData = ref(null)

onMounted(async () => {
  const grantId = route.params.id
  try {
    const res = await donorApi.getGrantDetail(grantId)
    if (res) grantData.value = res
  } catch (e) {
    console.error("Failed to load grant details:", e)
  } finally {
    loading.value = false
  }
})
</script>
