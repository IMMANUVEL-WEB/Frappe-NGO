<template>
  <div class="space-y-6">
    <!-- Top Stat Cards (5 Cards) -->
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-4">
      <!-- 1. Total Projects -->
      <div class="bg-white rounded-2xl p-5 border border-slate-100 shadow-xs flex flex-col justify-between hover:shadow-md transition">
        <div class="flex items-start justify-between">
          <div>
            <span class="text-[11px] font-bold uppercase tracking-wider text-slate-400">Total Projects</span>
            <div class="text-2xl font-black text-slate-900 mt-1 tracking-tight">{{ stats.total }}</div>
            <div class="text-xs text-slate-400 font-medium mt-1">Active projects under your grants</div>
          </div>
          <div class="w-10 h-10 rounded-xl bg-slate-50 text-slate-600 flex items-center justify-center">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"/>
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

      <!-- 2. On Track -->
      <div class="bg-white rounded-2xl p-5 border border-slate-100 shadow-xs flex flex-col justify-between hover:shadow-md transition">
        <div class="flex items-start justify-between">
          <div>
            <span class="text-[11px] font-bold uppercase tracking-wider text-slate-400">On Track</span>
            <div class="text-2xl font-black text-slate-900 mt-1 tracking-tight">{{ stats.onTrack }}</div>
            <div class="text-xs text-slate-400 font-medium mt-1">Projects progressing as planned</div>
          </div>
          <div class="w-10 h-10 rounded-xl bg-blue-50 text-blue-600 flex items-center justify-center">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14.752 11.168l-3.197-2.132A1 1 0 0010 9.87v4.263a1 1 0 001.555.832l3.197-2.132a1 1 0 000-1.664z"/>
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
            </svg>
          </div>
        </div>
        <div class="mt-4 flex items-center justify-between">
          <div class="w-full bg-slate-100 rounded-full h-1.5 overflow-hidden">
            <div 
              class="bg-blue-600 h-1.5 rounded-full transition-all duration-500"
              :style="{ width: `${stats.total > 0 ? (stats.onTrack / stats.total) * 100 : 0}%` }"
            ></div>
          </div>
          <span class="text-[10px] font-semibold text-slate-400 ml-2">
            {{ stats.total > 0 ? Math.round((stats.onTrack / stats.total) * 100) : 0 }}%
          </span>
        </div>
      </div>

      <!-- 3. At Risk -->
      <div class="bg-white rounded-2xl p-5 border border-slate-100 shadow-xs flex flex-col justify-between hover:shadow-md transition">
        <div class="flex items-start justify-between">
          <div>
            <span class="text-[11px] font-bold uppercase tracking-wider text-slate-400">At Risk</span>
            <div class="text-2xl font-black text-slate-900 mt-1 tracking-tight">{{ stats.atRisk }}</div>
            <div class="text-xs text-slate-400 font-medium mt-1">Need attention / delayed</div>
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
              :style="{ width: `${stats.total > 0 ? (stats.atRisk / stats.total) * 100 : 0}%` }"
            ></div>
          </div>
          <span class="text-[10px] font-semibold text-slate-400 ml-2">
            {{ stats.total > 0 ? Math.round((stats.atRisk / stats.total) * 100) : 0 }}%
          </span>
        </div>
      </div>

      <!-- 4. Delayed -->
      <div class="bg-white rounded-2xl p-5 border border-slate-100 shadow-xs flex flex-col justify-between hover:shadow-md transition">
        <div class="flex items-start justify-between">
          <div>
            <span class="text-[11px] font-bold uppercase tracking-wider text-slate-400">Delayed</span>
            <div class="text-2xl font-black text-slate-900 mt-1 tracking-tight">{{ stats.delayed }}</div>
            <div class="text-xs text-slate-400 font-medium mt-1">Behind schedule</div>
          </div>
          <div class="w-10 h-10 rounded-xl bg-rose-50 text-rose-600 flex items-center justify-center">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/>
            </svg>
          </div>
        </div>
        <div class="mt-4 flex items-center justify-between">
          <div class="w-full bg-slate-100 rounded-full h-1.5 overflow-hidden">
            <div 
              class="bg-rose-500 h-1.5 rounded-full transition-all duration-500"
              :style="{ width: `${stats.total > 0 ? (stats.delayed / stats.total) * 100 : 0}%` }"
            ></div>
          </div>
          <span class="text-[10px] font-semibold text-slate-400 ml-2">
            {{ stats.total > 0 ? Math.round((stats.delayed / stats.total) * 100) : 0 }}%
          </span>
        </div>
      </div>

      <!-- 5. Completed -->
      <div class="bg-white rounded-2xl p-5 border border-slate-100 shadow-xs flex flex-col justify-between hover:shadow-md transition">
        <div class="flex items-start justify-between">
          <div>
            <span class="text-[11px] font-bold uppercase tracking-wider text-slate-400">Completed</span>
            <div class="text-2xl font-black text-slate-900 mt-1 tracking-tight">{{ stats.completed }}</div>
            <div class="text-xs text-slate-400 font-medium mt-1">Completed this period</div>
          </div>
          <div class="w-10 h-10 rounded-xl bg-purple-50 text-purple-600 flex items-center justify-center">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 21v-4m0 0V5a2 2 0 012-2h6.5l1 1H21l-3 6 3 6h-8.5l-1-1H5a2 2 0 00-2 2zm9-13.5V9"/>
            </svg>
          </div>
        </div>
        <div class="mt-4 flex items-center justify-between">
          <div class="w-full bg-slate-100 rounded-full h-1.5 overflow-hidden">
            <div 
              class="bg-purple-500 h-1.5 rounded-full transition-all duration-500"
              :style="{ width: `${stats.total > 0 ? (stats.completed / stats.total) * 100 : 0}%` }"
            ></div>
          </div>
          <span class="text-[10px] font-semibold text-slate-400 ml-2">
            {{ stats.total > 0 ? Math.round((stats.completed / stats.total) * 100) : 0 }}%
          </span>
        </div>
      </div>
    </div>

    <!-- Middle Section: 3 Cards in a row with proper, non-squished column widths -->
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-stretch">
      <!-- Card 1: Project Progress Overview (6 cols) -->
      <div class="lg:col-span-6 bg-white rounded-2xl p-5 border border-slate-100 shadow-xs flex flex-col justify-between">
        <div>
          <div class="flex items-center space-x-2 mb-4">
            <div class="w-2.5 h-2.5 rounded-full bg-emerald-500"></div>
            <h3 class="text-sm font-bold text-slate-900 tracking-tight">Project Progress Overview</h3>
          </div>

          <div v-if="projectsList.length" class="space-y-4 pt-1">
            <div v-for="item in projectsList.slice(0, 5)" :key="item.name" class="space-y-1.5">
              <div class="flex items-center justify-between text-xs">
                <span class="font-medium text-slate-700 truncate pr-2">{{ item.project_name || item.name }}</span>
                <span class="font-bold text-slate-900">{{ item.percent_complete }}%</span>
              </div>
              <!-- Progress Bar -->
              <div class="w-full bg-slate-100 rounded-full h-2.5 overflow-hidden flex">
                <div 
                  class="h-full rounded-full transition-all duration-500"
                  :class="item.status === 'Completed' ? 'bg-purple-500' : item.status === 'At Risk' ? 'bg-amber-400' : item.status === 'Delayed' ? 'bg-rose-500' : 'bg-emerald-500'" 
                  :style="{ width: `${Math.min(item.percent_complete, 100)}%` }"
                ></div>
              </div>
            </div>
          </div>
          <div v-else class="py-12 text-center text-xs text-slate-400 font-medium">
            No active projects found under your grants.
          </div>
        </div>

        <!-- Legend at bottom -->
        <div class="pt-4 mt-4 border-t border-slate-100 flex flex-wrap items-center gap-3 text-[11px] text-slate-500">
          <span class="flex items-center gap-1.5"><span class="w-2 h-2 rounded-full bg-emerald-500"></span> On Track</span>
          <span class="flex items-center gap-1.5"><span class="w-2 h-2 rounded-full bg-amber-400"></span> At Risk</span>
          <span class="flex items-center gap-1.5"><span class="w-2 h-2 rounded-full bg-rose-500"></span> Delayed</span>
          <span class="flex items-center gap-1.5"><span class="w-2 h-2 rounded-full bg-purple-500"></span> Completed</span>
        </div>
      </div>

      <!-- Card 2: Project Progress by Sector (3 cols) -->
      <div class="lg:col-span-3 bg-white rounded-2xl p-5 border border-slate-100 shadow-xs flex flex-col justify-between">
        <div>
          <div class="flex items-center space-x-2 mb-4">
            <div class="w-2.5 h-2.5 rounded-full bg-blue-500"></div>
            <h3 class="text-sm font-bold text-slate-900 tracking-tight">Projects by Sector</h3>
          </div>

          <div class="flex items-center justify-center my-3">
            <!-- Donut -->
            <div class="relative w-28 h-28 flex items-center justify-center">
              <svg class="w-full h-full transform -rotate-90" viewBox="0 0 36 36">
                <circle cx="18" cy="18" r="14" fill="none" stroke="#e2e8f0" stroke-width="4.5" />
                <circle 
                  v-for="(sec, sIdx) in sectorBreakdown" 
                  :key="sIdx"
                  cx="18" cy="18" r="14" fill="none" 
                  :stroke="sec.color" 
                  stroke-width="4.5" 
                  :stroke-dasharray="`${sec.percent} ${100 - sec.percent}`" 
                  :stroke-dashoffset="sec.offset" 
                />
              </svg>
              <div class="absolute inset-0 flex flex-col items-center justify-center text-center">
                <span class="text-base font-black text-slate-900 leading-tight">{{ projectsList.length }}</span>
                <span class="text-[9px] text-slate-400 font-medium">Projects</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Legend list -->
        <div v-if="sectorBreakdown.length" class="space-y-2 text-xs text-slate-600 mt-2">
          <div v-for="(sec, sIdx) in sectorBreakdown" :key="sIdx" class="flex items-center justify-between">
            <span class="flex items-center gap-1.5 truncate pr-2">
              <span class="w-2 h-2 rounded-full shrink-0" :style="{ backgroundColor: sec.color }"></span>
              <span class="truncate">{{ sec.sector }}</span>
            </span>
            <span class="font-semibold text-slate-900 shrink-0">{{ sec.count }} ({{ sec.percent }}%)</span>
          </div>
        </div>
        <div v-else class="text-center text-xs text-slate-400 py-3">
          No sectors available.
        </div>
      </div>

      <!-- Card 3: Project Status (3 cols) -->
      <div class="lg:col-span-3 bg-white rounded-2xl p-5 border border-slate-100 shadow-xs flex flex-col justify-between">
        <div>
          <div class="flex items-center space-x-2 mb-4">
            <div class="w-2.5 h-2.5 rounded-full bg-emerald-500"></div>
            <h3 class="text-sm font-bold text-slate-900 tracking-tight">Project Status</h3>
          </div>

          <div class="flex items-center justify-center my-3">
            <!-- Status Donut -->
            <div class="relative w-28 h-28 flex items-center justify-center">
              <svg class="w-full h-full transform -rotate-90" viewBox="0 0 36 36">
                <circle cx="18" cy="18" r="14" fill="none" stroke="#e2e8f0" stroke-width="4.5" />
                <circle 
                  cx="18" cy="18" r="14" fill="none" 
                  stroke="#10b981" 
                  stroke-width="4.5" 
                  :stroke-dasharray="`${stats.total > 0 ? Math.round((stats.onTrack / stats.total) * 100) : 0} 100`" 
                  stroke-dashoffset="0" 
                />
              </svg>
              <div class="absolute inset-0 flex flex-col items-center justify-center text-center">
                <span class="text-base font-black text-slate-900 leading-tight">
                  {{ stats.total > 0 ? Math.round((stats.onTrack / stats.total) * 100) : 0 }}%
                </span>
                <span class="text-[9px] text-slate-400 font-medium">On Track</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Status Legend list -->
        <div class="space-y-2 text-xs text-slate-600 mt-2">
          <div class="flex items-center justify-between">
            <span class="flex items-center gap-1.5"><span class="w-2 h-2 rounded-full bg-emerald-500"></span> On Track</span>
            <span class="font-semibold text-slate-900">{{ stats.onTrack }}</span>
          </div>
          <div class="flex items-center justify-between">
            <span class="flex items-center gap-1.5"><span class="w-2 h-2 rounded-full bg-amber-400"></span> At Risk</span>
            <span class="font-semibold text-slate-900">{{ stats.atRisk }}</span>
          </div>
          <div class="flex items-center justify-between">
            <span class="flex items-center gap-1.5"><span class="w-2 h-2 rounded-full bg-rose-500"></span> Delayed</span>
            <span class="font-semibold text-slate-900">{{ stats.delayed }}</span>
          </div>
          <div class="flex items-center justify-between">
            <span class="flex items-center gap-1.5"><span class="w-2 h-2 rounded-full bg-purple-500"></span> Completed</span>
            <span class="font-semibold text-slate-900">{{ stats.completed }}</span>
          </div>
        </div>
      </div>
    </div>

    <!-- Bottom Section: Project Progress Details (Table) -->
    <div class="bg-white rounded-2xl border border-slate-100 shadow-xs overflow-hidden">
      <!-- Table Header & Controls -->
      <div class="p-5 border-b border-slate-100 flex flex-col lg:flex-row lg:items-center justify-between gap-4">
        <h3 class="text-sm font-bold text-slate-900 tracking-tight">Project Progress Details</h3>

        <!-- Filter Controls -->
        <div class="flex flex-wrap items-center gap-2.5">
          <!-- Sector Filter -->
          <select 
            v-model="selectedSector"
            class="text-xs bg-slate-50 border border-slate-200 rounded-xl px-3 py-1.5 focus:outline-none focus:ring-2 focus:ring-emerald-500 text-slate-700"
          >
            <option value="">All Sectors</option>
            <option v-for="sec in availableSectors" :key="sec" :value="sec">{{ sec }}</option>
          </select>

          <!-- Status Filter -->
          <select 
            v-model="selectedStatus"
            class="text-xs bg-slate-50 border border-slate-200 rounded-xl px-3 py-1.5 focus:outline-none focus:ring-2 focus:ring-emerald-500 text-slate-700"
          >
            <option value="">All Status</option>
            <option value="Open">Open</option>
            <option value="On Track">On Track</option>
            <option value="At Risk">At Risk</option>
            <option value="Delayed">Delayed</option>
            <option value="Completed">Completed</option>
          </select>

          <!-- Search Input -->
          <div class="relative">
            <input 
              type="text" 
              v-model="searchQuery"
              placeholder="Search project by name..." 
              class="text-xs bg-slate-50 border border-slate-200 rounded-xl pl-8 pr-3 py-1.5 focus:outline-none focus:ring-2 focus:ring-emerald-500 text-slate-700 w-48 sm:w-56"
            />
            <svg class="w-3.5 h-3.5 text-slate-400 absolute left-2.5 top-2.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/>
            </svg>
          </div>
        </div>
      </div>

      <!-- Projects Table -->
      <div class="overflow-x-auto">
        <table class="w-full text-left border-collapse text-xs">
          <thead>
            <tr class="border-b border-slate-100 bg-slate-50/50 text-[10px] font-bold uppercase tracking-wider text-slate-400">
              <th class="py-3 px-4">#</th>
              <th class="py-3 px-4">Project Name</th>
              <th class="py-3 px-3">Sector</th>
              <th class="py-3 px-3">Geography</th>
              <th class="py-3 px-3">Start Date</th>
              <th class="py-3 px-3">End Date</th>
              <th class="py-3 px-4">Progress</th>
              <th class="py-3 px-3">Status</th>
              <th class="py-3 px-4 text-right">Actions</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-slate-100 text-slate-700">
            <tr 
              v-for="(proj, idx) in paginatedProjects" 
              :key="proj.name"
              class="hover:bg-slate-50/80 transition"
            >
              <td class="py-3.5 px-4 text-slate-400 font-mono">{{ (currentPage - 1) * pageSize + idx + 1 }}</td>
              <td class="py-3.5 px-4 font-semibold text-slate-900">
                <div class="flex items-center space-x-3">
                  <div class="w-8 h-8 rounded-lg bg-emerald-100 text-emerald-800 font-bold flex items-center justify-center shrink-0 text-xs">
                    {{ (proj.sector || 'P').substring(0, 1).toUpperCase() }}
                  </div>
                  <div>
                    <div class="font-semibold text-slate-900">{{ proj.project_name || proj.name }}</div>
                    <div class="text-[11px] text-slate-400 font-mono">{{ proj.name }}</div>
                  </div>
                </div>
              </td>
              <td class="py-3.5 px-3">
                <span class="inline-block px-2.5 py-0.5 rounded-full text-[11px] font-medium bg-emerald-50 text-emerald-700 border border-emerald-100">
                  {{ proj.sector || 'General' }}
                </span>
              </td>
              <td class="py-3.5 px-3 text-slate-600">{{ formatGeography(proj.geography) }}</td>
              <td class="py-3.5 px-3 text-slate-500 whitespace-nowrap">{{ proj.expected_start_date || '—' }}</td>
              <td class="py-3.5 px-3 text-slate-500 whitespace-nowrap">{{ proj.expected_end_date || '—' }}</td>
              <td class="py-3.5 px-4">
                <div class="flex items-center space-x-2">
                  <span class="text-xs font-semibold text-slate-700 w-8">{{ proj.percent_complete || 0 }}%</span>
                  <div class="w-16 bg-slate-100 rounded-full h-1.5 overflow-hidden">
                    <div 
                      class="h-1.5 rounded-full bg-emerald-500 transition-all duration-500"
                      :style="{ width: `${Math.min(proj.percent_complete || 0, 100)}%` }"
                    ></div>
                  </div>
                </div>
              </td>
              <td class="py-3.5 px-3">
                <span 
                  class="inline-block px-2.5 py-0.5 rounded-full text-[11px] font-semibold"
                  :class="{
                    'bg-emerald-50 text-emerald-700 border border-emerald-100': proj.status === 'On Track' || proj.status === 'Open',
                    'bg-amber-50 text-amber-700 border border-amber-200': proj.status === 'At Risk',
                    'bg-rose-50 text-rose-700 border border-rose-200': proj.status === 'Delayed',
                    'bg-purple-50 text-purple-700 border border-purple-200': proj.status === 'Completed'
                  }"
                >
                  {{ proj.status || 'Open' }}
                </span>
              </td>
              <td class="py-3.5 px-4 text-right">
                <router-link 
                  to="/donor-portal/grants"
                  class="text-xs font-semibold text-emerald-600 hover:text-emerald-700 transition"
                >
                  View Details
                </router-link>
              </td>
            </tr>
            <tr v-if="!filteredProjects.length">
              <td colspan="9" class="py-8 text-center text-xs text-slate-400">
                No matching projects found.
              </td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- Pagination -->
      <div v-if="filteredProjects.length > pageSize" class="px-5 py-3.5 border-t border-slate-100 flex items-center justify-between text-xs text-slate-500">
        <div>
          Showing {{ (currentPage - 1) * pageSize + 1 }} - {{ Math.min(currentPage * pageSize, filteredProjects.length) }} of {{ filteredProjects.length }} projects
        </div>
        <div class="flex items-center space-x-1.5">
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
            class="w-7 h-7 rounded-lg border flex items-center justify-center font-bold"
            :class="currentPage === p ? 'bg-emerald-600 text-white border-emerald-600' : 'border-slate-200 hover:bg-slate-50 text-slate-700'"
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
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from "vue"
import { donorApi } from "../api"

const loading = ref(true)
const searchQuery = ref("")
const selectedSector = ref("")
const selectedStatus = ref("")
const currentPage = ref(1)
const pageSize = 5

const projectsList = ref([])

const stats = computed(() => {
	const list = projectsList.value || []
	const total = list.length
	let onTrack = 0
	let atRisk = 0
	let delayed = 0
	let completed = 0

	for (const p of list) {
		const s = p.status || "Open"
		if (s === "On Track" || s === "Open") onTrack++
		else if (s === "At Risk") atRisk++
		else if (s === "Delayed") delayed++
		else if (s === "Completed") completed++
		else onTrack++
	}

	return { total, onTrack, atRisk, delayed, completed }
})

const sectorColors = ["#3B82F6", "#059669", "#F59E0B", "#8B5CF6", "#06B6D4", "#EF4444"]

const sectorBreakdown = computed(() => {
	const list = projectsList.value || []
	if (!list.length) return []

	const counts = {}
	for (const p of list) {
		const s = p.sector || "General"
		counts[s] = (counts[s] || 0) + 1
	}

	const total = list.length
	let offset = 0
	return Object.entries(counts).map(([sec, count], idx) => {
		const percent = Math.round((count / total) * 100)
		const currentOffset = offset
		offset -= percent
		return {
			sector: sec,
			count,
			percent,
			color: sectorColors[idx % sectorColors.length],
			offset: currentOffset,
		}
	})
})

const availableSectors = computed(() => {
	const sectors = new Set((projectsList.value || []).map((p) => p.sector || "General"))
	return Array.from(sectors)
})

function formatGeography(geo) {
	if (!geo) return "India"
	if (typeof geo === "string" && geo.startsWith("{")) {
		try {
			const parsed = JSON.parse(geo)
			if (parsed.features?.[0]?.geometry?.coordinates) {
				const [lng, lat] = parsed.features[0].geometry.coordinates
				return `${lat.toFixed(2)}°N, ${lng.toFixed(2)}°E`
			}
		} catch (e) {
			// fallback
		}
	}
	return typeof geo === "string" ? geo : "India"
}

const filteredProjects = computed(() => {
	return (projectsList.value || []).filter((p) => {
		const matchesSearch =
			!searchQuery.value ||
			(p.project_name || "").toLowerCase().includes(searchQuery.value.toLowerCase()) ||
			(p.name || "").toLowerCase().includes(searchQuery.value.toLowerCase()) ||
			(p.sector || "").toLowerCase().includes(searchQuery.value.toLowerCase())

		const matchesSector = !selectedSector.value || (p.sector || "General") === selectedSector.value
		const matchesStatus = !selectedStatus.value || p.status === selectedStatus.value

		return matchesSearch && matchesSector && matchesStatus
	})
})

const totalPages = computed(() => {
	return Math.max(1, Math.ceil(filteredProjects.value.length / pageSize))
})

const paginatedProjects = computed(() => {
	const start = (currentPage.value - 1) * pageSize
	return filteredProjects.value.slice(start, start + pageSize)
})

async function loadProjects() {
	loading.value = true
	try {
		const res = await donorApi.getProjects()
		if (Array.isArray(res)) {
			projectsList.value = res
		}
	} catch (e) {
		console.error("Failed to load projects:", e)
	} finally {
		loading.value = false
	}
}

onMounted(() => {
	loadProjects()
})
</script>
