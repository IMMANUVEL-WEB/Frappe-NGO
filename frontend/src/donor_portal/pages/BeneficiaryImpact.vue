<template>
  <div class="space-y-6">
    <!-- Top Stat Cards (4 Cards) -->
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
      <!-- 1. Total Beneficiaries -->
      <div class="bg-white rounded-2xl p-5 border border-slate-100 shadow-xs flex flex-col justify-between hover:shadow-md transition">
        <div class="flex items-start justify-between">
          <div>
            <span class="text-[11px] font-bold uppercase tracking-wider text-slate-400">Total Beneficiaries</span>
            <div class="text-2xl font-black text-slate-900 mt-1 tracking-tight">28,450</div>
            <div class="text-xs text-slate-400 font-medium mt-1">Direct community impact</div>
          </div>
          <div class="w-10 h-10 rounded-xl bg-emerald-50 text-emerald-600 flex items-center justify-center">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z"/>
            </svg>
          </div>
        </div>
        <div class="mt-4 w-full bg-slate-100 rounded-full h-1.5 overflow-hidden">
          <div class="bg-emerald-500 h-1.5 rounded-full w-full"></div>
        </div>
      </div>

      <!-- 2. Services Delivered -->
      <div class="bg-white rounded-2xl p-5 border border-slate-100 shadow-xs flex flex-col justify-between hover:shadow-md transition">
        <div class="flex items-start justify-between">
          <div>
            <span class="text-[11px] font-bold uppercase tracking-wider text-slate-400">Services Delivered</span>
            <div class="text-2xl font-black text-slate-900 mt-1 tracking-tight">41,200</div>
            <div class="text-xs text-slate-400 font-medium mt-1">Medical, food, educational aid</div>
          </div>
          <div class="w-10 h-10 rounded-xl bg-blue-50 text-blue-600 flex items-center justify-center">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>
            </svg>
          </div>
        </div>
        <div class="mt-4 w-full bg-slate-100 rounded-full h-1.5 overflow-hidden">
          <div class="bg-blue-600 h-1.5 rounded-full w-[85%]"></div>
        </div>
      </div>

      <!-- 3. Active Districts -->
      <div class="bg-white rounded-2xl p-5 border border-slate-100 shadow-xs flex flex-col justify-between hover:shadow-md transition">
        <div class="flex items-start justify-between">
          <div>
            <span class="text-[11px] font-bold uppercase tracking-wider text-slate-400">Active Districts</span>
            <div class="text-2xl font-black text-slate-900 mt-1 tracking-tight">18</div>
            <div class="text-xs text-slate-400 font-medium mt-1">Across 6 states</div>
          </div>
          <div class="w-10 h-10 rounded-xl bg-amber-50 text-amber-500 flex items-center justify-center">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3.055 11H5a2 2 0 012 2v1a2 2 0 002 2 2 2 0 012 2v2.945M8 3.935V5.5A2.5 2.5 0 0010.5 8h.5a2 2 0 012 2 2 2 0 104 0 2 2 0 012-2h1.064M15 20.488V18a2 2 0 012-2h3.064M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
            </svg>
          </div>
        </div>
        <div class="mt-4 w-full bg-slate-100 rounded-full h-1.5 overflow-hidden">
          <div class="bg-amber-400 h-1.5 rounded-full w-[60%]"></div>
        </div>
      </div>

      <!-- 4. Verification Rate -->
      <div class="bg-white rounded-2xl p-5 border border-slate-100 shadow-xs flex flex-col justify-between hover:shadow-md transition">
        <div class="flex items-start justify-between">
          <div>
            <span class="text-[11px] font-bold uppercase tracking-wider text-slate-400">Audit Verification</span>
            <div class="text-2xl font-black text-slate-900 mt-1 tracking-tight">100%</div>
            <div class="text-xs text-slate-400 font-medium mt-1">Zero PII Leakage Compliant</div>
          </div>
          <div class="w-10 h-10 rounded-xl bg-purple-50 text-purple-600 flex items-center justify-center">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"/>
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
      <!-- Sector Impact Distribution (7 cols) -->
      <div class="lg:col-span-7 bg-white rounded-2xl p-5 border border-slate-100 shadow-xs">
        <div class="flex items-center space-x-2 mb-4">
          <div class="w-2.5 h-2.5 rounded-full bg-emerald-500"></div>
          <h3 class="text-sm font-bold text-slate-900 tracking-tight">Impact Reach by Sector</h3>
        </div>

        <div class="space-y-3.5">
          <div v-for="item in sectorImpact" :key="item.sector" class="space-y-1 text-xs">
            <div class="flex justify-between items-center">
              <span class="font-semibold text-slate-800">{{ item.sector }}</span>
              <span class="font-bold text-slate-900">{{ item.count.toLocaleString() }} beneficiaries <span class="text-slate-400 font-normal">({{ item.percent }}%)</span></span>
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
      <div class="lg:col-span-5 bg-white rounded-2xl p-5 border border-slate-100 shadow-xs flex flex-col justify-between">
        <div>
          <div class="flex items-center space-x-2 mb-4">
            <div class="w-2.5 h-2.5 rounded-full bg-emerald-500"></div>
            <h3 class="text-sm font-bold text-slate-900 tracking-tight">Territory Outreach</h3>
          </div>

          <div class="space-y-2.5 text-xs">
            <div 
              v-for="dist in districtImpact" 
              :key="dist.name"
              class="p-2.5 rounded-xl bg-slate-50 flex items-center justify-between"
            >
              <div class="flex items-center space-x-2.5">
                <span class="w-2 h-2 rounded-full" :class="dist.dotColor"></span>
                <span class="font-semibold text-slate-800">{{ dist.name }}</span>
              </div>
              <span class="font-bold text-slate-900">{{ dist.count.toLocaleString() }} reach</span>
            </div>
          </div>
        </div>

        <div class="mt-4 pt-3 border-t border-slate-100 text-[11px] text-slate-400 flex items-center justify-between">
          <span>State Centroid Verified</span>
          <span>Demographics Aggregated</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue"

const sectorImpact = ref([
  { sector: "Health & Nutrition", count: 9800, percent: 34, barColor: "bg-rose-500" },
  { sector: "Education & Youth Empowerment", count: 7200, percent: 25, barColor: "bg-purple-600" },
  { sector: "WASH (Water, Sanitation & Hygiene)", count: 5400, percent: 19, barColor: "bg-blue-600" },
  { sector: "Livelihood & Women Self Help", count: 3800, percent: 14, barColor: "bg-emerald-500" },
  { sector: "Disaster Emergency Relief", count: 2250, percent: 8, barColor: "bg-amber-400" }
])

const districtImpact = ref([
  { name: "Patna & Gaya (Bihar)", count: 7850, dotColor: "bg-blue-500" },
  { name: "Varanasi (Uttar Pradesh)", count: 6200, dotColor: "bg-emerald-500" },
  { name: "Madurai & Chennai (Tamil Nadu)", count: 5400, dotColor: "bg-rose-500" },
  { name: "Koraput (Odisha)", count: 4600, dotColor: "bg-purple-500" },
  { name: "Guwahati & Cachar (Assam)", count: 4400, dotColor: "bg-amber-500" }
])
</script>
