<template>
  <div class="space-y-6">
    <!-- Top Stat Cards (4 Cards) -->
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
      <!-- 1. Total Proposals -->
      <div class="bg-white rounded-2xl p-5 border border-slate-100 shadow-xs flex flex-col justify-between hover:shadow-md transition">
        <div class="flex items-start justify-between">
          <div>
            <span class="text-[11px] font-bold uppercase tracking-wider text-slate-400">Total Proposals</span>
            <div class="text-2xl font-black text-slate-900 mt-1 tracking-tight">14</div>
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
            <div class="text-2xl font-black text-slate-900 mt-1 tracking-tight">10</div>
            <div class="text-xs text-slate-400 font-medium mt-1">71% of total proposals</div>
          </div>
          <div class="w-10 h-10 rounded-xl bg-blue-50 text-blue-600 flex items-center justify-center">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>
            </svg>
          </div>
        </div>
        <div class="mt-4 w-full bg-slate-100 rounded-full h-1.5 overflow-hidden">
          <div class="bg-blue-600 h-1.5 rounded-full w-[71%]"></div>
        </div>
      </div>

      <!-- 3. Pending -->
      <div class="bg-white rounded-2xl p-5 border border-slate-100 shadow-xs flex flex-col justify-between hover:shadow-md transition">
        <div class="flex items-start justify-between">
          <div>
            <span class="text-[11px] font-bold uppercase tracking-wider text-slate-400">Pending</span>
            <div class="text-2xl font-black text-slate-900 mt-1 tracking-tight">3</div>
            <div class="text-xs text-slate-400 font-medium mt-1">Under review</div>
          </div>
          <div class="w-10 h-10 rounded-xl bg-amber-50 text-amber-500 flex items-center justify-center">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/>
            </svg>
          </div>
        </div>
        <div class="mt-4 w-full bg-slate-100 rounded-full h-1.5 overflow-hidden">
          <div class="bg-amber-400 h-1.5 rounded-full w-[21%]"></div>
        </div>
      </div>

      <!-- 4. Rejected -->
      <div class="bg-white rounded-2xl p-5 border border-slate-100 shadow-xs flex flex-col justify-between hover:shadow-md transition">
        <div class="flex items-start justify-between">
          <div>
            <span class="text-[11px] font-bold uppercase tracking-wider text-slate-400">Rejected</span>
            <div class="text-2xl font-black text-slate-900 mt-1 tracking-tight">1</div>
            <div class="text-xs text-slate-400 font-medium mt-1">Needs revision / not approved</div>
          </div>
          <div class="w-10 h-10 rounded-xl bg-purple-50 text-purple-600 flex items-center justify-center">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z"/>
            </svg>
          </div>
        </div>
        <div class="mt-4 w-full bg-slate-100 rounded-full h-1.5 overflow-hidden">
          <div class="bg-purple-500 h-1.5 rounded-full w-[8%]"></div>
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
            <option value="Health">Health</option>
            <option value="Education">Education</option>
            <option value="WASH">WASH</option>
            <option value="Livelihoods">Livelihoods</option>
            <option value="Disaster Relief">Disaster Relief</option>
            <option value="Governance">Governance</option>
          </select>

          <select 
            v-model="selectedStatus" 
            class="px-3 py-2 text-xs rounded-xl border border-slate-200 focus:outline-none focus:ring-2 focus:ring-emerald-500/20 bg-white text-slate-700"
          >
            <option value="">All Status</option>
            <option value="Approved">Approved</option>
            <option value="Under Review">Under Review</option>
            <option value="Rejected">Rejected</option>
          </select>

          <select 
            v-model="selectedGeography" 
            class="px-3 py-2 text-xs rounded-xl border border-slate-200 focus:outline-none focus:ring-2 focus:ring-emerald-500/20 bg-white text-slate-700"
          >
            <option value="">All Geographies</option>
            <option value="Tamil Nadu">Tamil Nadu</option>
            <option value="Bihar">Bihar</option>
            <option value="Odisha">Odisha</option>
            <option value="Assam">Assam</option>
            <option value="Maharashtra">Maharashtra</option>
            <option value="Karnataka">Karnataka</option>
            <option value="Jharkhand">Jharkhand</option>
          </select>
        </div>
      </div>

      <!-- Action Button -->
      <div class="w-full lg:w-auto flex justify-end">
        <button 
          type="button" 
          @click="showNewProposalModal = true"
          class="flex items-center space-x-1.5 px-4 py-2 bg-[#00875A] hover:bg-[#00744D] text-white rounded-xl text-xs font-semibold shadow-sm transition"
        >
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"/>
          </svg>
          <span>New Proposal</span>
        </button>
      </div>
    </div>

    <!-- Main Content: Two Columns -->
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-6">
      <!-- Left Column: Proposals Table (8 cols) -->
      <div class="lg:col-span-8 bg-white rounded-2xl border border-slate-100 shadow-xs overflow-hidden flex flex-col justify-between">
        <div class="overflow-x-auto">
          <table class="w-full text-left text-xs">
            <thead class="bg-slate-50/75 border-b border-slate-100 text-[11px] font-bold text-slate-500 uppercase tracking-wider">
              <tr>
                <th class="py-3 px-4">#</th>
                <th class="py-3 px-4">Proposal Title</th>
                <th class="py-3 px-3">Code</th>
                <th class="py-3 px-3">Sector</th>
                <th class="py-3 px-3">Geography</th>
                <th class="py-3 px-3">Status</th>
                <th class="py-3 px-3">Submitted On</th>
                <th class="py-3 px-3 text-right">Actions</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-slate-100 text-slate-700">
              <tr 
                v-for="(row, idx) in paginatedProposals" 
                :key="row.code"
                class="hover:bg-slate-50/60 transition group"
              >
                <td class="py-3.5 px-4 text-slate-400 font-medium">{{ (currentPage - 1) * pageSize + idx + 1 }}</td>
                <td class="py-3.5 px-4 font-semibold text-slate-900 max-w-xs truncate">
                  {{ row.title }}
                </td>
                <td class="py-3.5 px-3 font-mono text-[11px] text-slate-500">{{ row.code }}</td>
                <td class="py-3.5 px-3">
                  <span 
                    class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-[11px] font-medium"
                    :class="getSectorClass(row.sector)"
                  >
                    <component :is="getSectorIcon(row.sector)" class="w-3 h-3" />
                    {{ row.sector }}
                  </span>
                </td>
                <td class="py-3.5 px-3 text-slate-600">{{ row.geography }}</td>
                <td class="py-3.5 px-3">
                  <span 
                    class="inline-block px-2.5 py-0.5 rounded-full text-[11px] font-semibold"
                    :class="{
                      'bg-emerald-50 text-emerald-700 border border-emerald-100': row.status === 'Approved',
                      'bg-amber-50 text-amber-700 border border-amber-200': row.status === 'Under Review',
                      'bg-rose-50 text-rose-700 border border-rose-200': row.status === 'Rejected'
                    }"
                  >
                    {{ row.status }}
                  </span>
                </td>
                <td class="py-3.5 px-3 text-slate-500">{{ row.submittedOn }}</td>
                <td class="py-3.5 px-3 text-right relative">
                  <button 
                    type="button" 
                    @click="activeActionRow = activeActionRow === row.code ? null : row.code"
                    class="p-1 rounded-lg hover:bg-slate-100 text-slate-400 hover:text-slate-600"
                  >
                    <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20">
                      <path d="M10 6a2 2 0 110-4 2 2 0 010 4zM10 12a2 2 0 110-4 2 2 0 010 4zM10 18a2 2 0 110-4 2 2 0 010 4z" />
                    </svg>
                  </button>

                  <!-- Dropdown Menu -->
                  <div 
                    v-if="activeActionRow === row.code" 
                    class="absolute right-3 mt-1 w-36 bg-white rounded-xl shadow-lg border border-slate-100 py-1.5 z-20 text-left"
                  >
                    <button 
                      @click="viewDetails(row)"
                      class="w-full px-3 py-1.5 text-xs text-slate-700 hover:bg-slate-50 flex items-center gap-2"
                    >
                      View Details
                    </button>
                    <button 
                      v-if="row.status === 'Under Review'"
                      @click="quickDecision(row, 'Approve')"
                      class="w-full px-3 py-1.5 text-xs text-emerald-600 hover:bg-emerald-50 flex items-center gap-2 font-medium"
                    >
                      Approve
                    </button>
                    <button 
                      v-if="row.status === 'Under Review'"
                      @click="quickDecision(row, 'Reject')"
                      class="w-full px-3 py-1.5 text-xs text-rose-600 hover:bg-rose-50 flex items-center gap-2 font-medium"
                    >
                      Reject
                    </button>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>

        <!-- Pagination Footer -->
        <div class="px-5 py-3.5 border-t border-slate-100 flex items-center justify-between text-xs text-slate-500">
          <div>
            Showing {{ (currentPage - 1) * pageSize + 1 }} - {{ Math.min(currentPage * pageSize, filteredProposals.length) }} of {{ filteredProposals.length }} proposals
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
        <!-- 1. Proposals by Sector (Donut) -->
        <div class="bg-white rounded-2xl p-5 border border-slate-100 shadow-xs">
          <div class="flex items-center space-x-2 mb-4">
            <div class="w-2.5 h-2.5 rounded-full bg-emerald-500"></div>
            <h3 class="text-sm font-bold text-slate-900 tracking-tight">Proposals by Sector</h3>
          </div>

          <div class="flex items-center gap-4">
            <!-- Donut Visual -->
            <div class="relative w-28 h-28 shrink-0 flex items-center justify-center">
              <svg class="w-full h-full transform -rotate-90" viewBox="0 0 36 36">
                <!-- Slices calculated for 14 total -->
                <circle cx="18" cy="18" r="14" fill="none" stroke="#00875A" stroke-width="4.5" stroke-dasharray="29 71" stroke-dashoffset="0" />
                <circle cx="18" cy="18" r="14" fill="none" stroke="#3B82F6" stroke-width="4.5" stroke-dasharray="21 79" stroke-dashoffset="-29" />
                <circle cx="18" cy="18" r="14" fill="none" stroke="#06B6D4" stroke-width="4.5" stroke-dasharray="14 86" stroke-dashoffset="-50" />
                <circle cx="18" cy="18" r="14" fill="none" stroke="#10B981" stroke-width="4.5" stroke-dasharray="14 86" stroke-dashoffset="-64" />
                <circle cx="18" cy="18" r="14" fill="none" stroke="#F59E0B" stroke-width="4.5" stroke-dasharray="14 86" stroke-dashoffset="-78" />
                <circle cx="18" cy="18" r="14" fill="none" stroke="#8B5CF6" stroke-width="4.5" stroke-dasharray="7 93" stroke-dashoffset="-92" />
              </svg>
              <div class="absolute inset-0 flex flex-col items-center justify-center text-center">
                <span class="text-base font-black text-slate-900 leading-none">14</span>
                <span class="text-[9px] text-slate-400 font-medium">Total</span>
              </div>
            </div>

            <!-- Legend List -->
            <div class="space-y-1.5 flex-1 text-xs">
              <div class="flex items-center justify-between text-slate-600">
                <span class="flex items-center gap-1.5"><span class="w-2 h-2 rounded-full bg-[#00875A]"></span> Health</span>
                <span class="font-semibold text-slate-900">4 (29%)</span>
              </div>
              <div class="flex items-center justify-between text-slate-600">
                <span class="flex items-center gap-1.5"><span class="w-2 h-2 rounded-full bg-[#3B82F6]"></span> Education</span>
                <span class="font-semibold text-slate-900">3 (21%)</span>
              </div>
              <div class="flex items-center justify-between text-slate-600">
                <span class="flex items-center gap-1.5"><span class="w-2 h-2 rounded-full bg-[#06B6D4]"></span> WASH</span>
                <span class="font-semibold text-slate-900">2 (14%)</span>
              </div>
              <div class="flex items-center justify-between text-slate-600">
                <span class="flex items-center gap-1.5"><span class="w-2 h-2 rounded-full bg-[#10B981]"></span> Livelihoods</span>
                <span class="font-semibold text-slate-900">2 (14%)</span>
              </div>
              <div class="flex items-center justify-between text-slate-600">
                <span class="flex items-center gap-1.5"><span class="w-2 h-2 rounded-full bg-[#F59E0B]"></span> Disaster Relief</span>
                <span class="font-semibold text-slate-900">2 (14%)</span>
              </div>
              <div class="flex items-center justify-between text-slate-600">
                <span class="flex items-center gap-1.5"><span class="w-2 h-2 rounded-full bg-[#8B5CF6]"></span> Governance</span>
                <span class="font-semibold text-slate-900">1 (7%)</span>
              </div>
            </div>
          </div>
        </div>

        <!-- 2. Recent Activity -->
        <div class="bg-white rounded-2xl p-5 border border-slate-100 shadow-xs">
          <div class="flex items-center justify-between mb-4">
            <div class="flex items-center space-x-2">
              <div class="w-2.5 h-2.5 rounded-full bg-emerald-500"></div>
              <h3 class="text-sm font-bold text-slate-900 tracking-tight">Recent Activity</h3>
            </div>
            <button type="button" class="text-xs font-semibold text-emerald-600 hover:text-emerald-700">
              View All
            </button>
          </div>

          <div class="space-y-4">
            <!-- Item 1 -->
            <div class="flex items-start space-x-3 text-xs">
              <div class="w-7 h-7 rounded-full bg-emerald-50 text-emerald-600 flex items-center justify-center shrink-0 mt-0.5">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
                </svg>
              </div>
              <div class="flex-1 min-w-0">
                <div class="font-semibold text-slate-900">Proposal CP-0014 approved</div>
                <div class="text-[11px] text-slate-500 truncate">Community Health & Wellness Program</div>
              </div>
              <div class="text-[10px] text-slate-400 whitespace-nowrap">12 Oct 2026</div>
            </div>

            <!-- Item 2 -->
            <div class="flex items-start space-x-3 text-xs">
              <div class="w-7 h-7 rounded-full bg-amber-50 text-amber-500 flex items-center justify-center shrink-0 mt-0.5">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/>
                </svg>
              </div>
              <div class="flex-1 min-w-0">
                <div class="font-semibold text-slate-900">Proposal CP-0012 under review</div>
                <div class="text-[11px] text-slate-500 truncate">Clean Water Access Initiative</div>
              </div>
              <div class="text-[10px] text-slate-400 whitespace-nowrap">05 Oct 2026</div>
            </div>

            <!-- Item 3 -->
            <div class="flex items-start space-x-3 text-xs">
              <div class="w-7 h-7 rounded-full bg-rose-50 text-rose-600 flex items-center justify-center shrink-0 mt-0.5">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
                </svg>
              </div>
              <div class="flex-1 min-w-0">
                <div class="font-semibold text-slate-900">Proposal CP-0009 rejected</div>
                <div class="text-[11px] text-slate-500 truncate">Governance & Community Participation</div>
              </div>
              <div class="text-[10px] text-slate-400 whitespace-nowrap">15 Sep 2026</div>
            </div>

            <!-- Item 4 -->
            <div class="flex items-start space-x-3 text-xs">
              <div class="w-7 h-7 rounded-full bg-blue-50 text-blue-600 flex items-center justify-center shrink-0 mt-0.5">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/>
                </svg>
              </div>
              <div class="flex-1 min-w-0">
                <div class="font-semibold text-slate-900">New proposal submitted</div>
                <div class="text-[11px] text-slate-500 truncate">School Infrastructure Development</div>
              </div>
              <div class="text-[10px] text-slate-400 whitespace-nowrap">02 Sep 2026</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed, h, ref } from "vue"

const searchQuery = ref("")
const selectedSector = ref("")
const selectedStatus = ref("")
const selectedGeography = ref("")
const activeActionRow = ref(null)
const currentPage = ref(1)
const pageSize = 8

const proposalsData = ref([
	{
		title: "Community Health & Wellness Program",
		code: "CP-0014",
		sector: "Health",
		geography: "Tamil Nadu",
		status: "Approved",
		submittedOn: "12 Oct 2026",
	},
	{
		title: "Quality Education for Rural Children",
		code: "CP-0013",
		sector: "Education",
		geography: "Rural Areas",
		status: "Approved",
		submittedOn: "08 Oct 2026",
	},
	{
		title: "Clean Water Access Initiative",
		code: "CP-0012",
		sector: "WASH",
		geography: "Bihar",
		status: "Under Review",
		submittedOn: "05 Oct 2026",
	},
	{
		title: "Livelihood Support for Women",
		code: "CP-0011",
		sector: "Livelihoods",
		geography: "Odisha",
		status: "Approved",
		submittedOn: "28 Sep 2026",
	},
	{
		title: "Disaster Relief Response",
		code: "CP-0010",
		sector: "Disaster Relief",
		geography: "Assam",
		status: "Under Review",
		submittedOn: "20 Sep 2026",
	},
	{
		title: "Governance & Community Participation",
		code: "CP-0009",
		sector: "Governance",
		geography: "Maharashtra",
		status: "Rejected",
		submittedOn: "15 Sep 2026",
	},
	{
		title: "Healthcare Infrastructure Support",
		code: "CP-0008",
		sector: "Health",
		geography: "Karnataka",
		status: "Approved",
		submittedOn: "10 Sep 2026",
	},
	{
		title: "School Infrastructure Development",
		code: "CP-0007",
		sector: "Education",
		geography: "Jharkhand",
		status: "Approved",
		submittedOn: "02 Sep 2026",
	},
	{
		title: "Emergency Flood Relief Phase 1",
		code: "CP-0006",
		sector: "Disaster Relief",
		geography: "Assam",
		status: "Approved",
		submittedOn: "20 Aug 2026",
	},
	{
		title: "Rural Sanitation Facility",
		code: "CP-0005",
		sector: "WASH",
		geography: "Bihar",
		status: "Approved",
		submittedOn: "14 Aug 2026",
	},
	{
		title: "Tribal Youth Skill Center",
		code: "CP-0004",
		sector: "Livelihoods",
		geography: "Odisha",
		status: "Approved",
		submittedOn: "01 Aug 2026",
	},
	{
		title: "Mobile Clinic Outreach",
		code: "CP-0003",
		sector: "Health",
		geography: "Tamil Nadu",
		status: "Approved",
		submittedOn: "18 Jul 2026",
	},
	{
		title: "Girl Child Digital Literacy",
		code: "CP-0002",
		sector: "Education",
		geography: "Uttar Pradesh",
		status: "Under Review",
		submittedOn: "10 Jul 2026",
	},
	{
		title: "Panchayat Civic Training",
		code: "CP-0001",
		sector: "Governance",
		geography: "Maharashtra",
		status: "Approved",
		submittedOn: "25 Jun 2026",
	},
])

const filteredProposals = computed(() => {
	return proposalsData.value.filter((p) => {
		const matchSearch =
			!searchQuery.value ||
			p.title.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
			p.code.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
			p.sector.toLowerCase().includes(searchQuery.value.toLowerCase())
		const matchSector =
			!selectedSector.value || p.sector === selectedSector.value
		const matchStatus =
			!selectedStatus.value || p.status === selectedStatus.value
		const matchGeo =
			!selectedGeography.value || p.geography === selectedGeography.value
		return matchSearch && matchSector && matchStatus && matchGeo
	})
})

const totalPages = computed(
	() => Math.ceil(filteredProposals.value.length / pageSize) || 1,
)

const paginatedProposals = computed(() => {
	const start = (currentPage.value - 1) * pageSize
	return filteredProposals.value.slice(start, start + pageSize)
})

function getSectorClass(sector) {
	switch (sector) {
		case "Health":
			return "bg-rose-50 text-rose-600"
		case "Education":
			return "bg-purple-50 text-purple-600"
		case "WASH":
			return "bg-sky-50 text-sky-600"
		case "Livelihoods":
			return "bg-emerald-50 text-emerald-600"
		case "Disaster Relief":
			return "bg-amber-50 text-amber-700"
		case "Governance":
			return "bg-indigo-50 text-indigo-600"
		default:
			return "bg-slate-100 text-slate-700"
	}
}

function getSectorIcon(sector) {
	// SVG Icon definitions
	return {
		render() {
			if (sector === "Health") {
				return h("svg", { fill: "currentColor", viewBox: "0 0 20 20" }, [
					h("path", {
						"fill-rule": "evenodd",
						d: "M3.172 5.172a4 4 0 015.656 0L10 6.343l1.172-1.171a4 4 0 115.656 5.656L10 17.657l-6.828-6.829a4 4 0 010-5.656z",
						"clip-rule": "evenodd",
					}),
				])
			}
			if (sector === "Education") {
				return h(
					"svg",
					{
						fill: "none",
						stroke: "currentColor",
						"stroke-width": "2",
						viewBox: "0 0 24 24",
					},
					[
						h("path", {
							"stroke-linecap": "round",
							"stroke-linejoin": "round",
							d: "M12 14l9-5-9-5-9 5 9 5z",
						}),
						h("path", {
							"stroke-linecap": "round",
							"stroke-linejoin": "round",
							d: "M12 14l6.16-3.422a12.083 12.083 0 01.665 6.479A11.952 11.952 0 0012 20.055a11.952 11.952 0 00-6.824-2.998 12.078 12.078 0 01.665-6.479L12 14z",
						}),
					],
				)
			}
			if (sector === "WASH") {
				return h("svg", { fill: "currentColor", viewBox: "0 0 20 20" }, [
					h("path", {
						"fill-rule": "evenodd",
						d: "M10 2a1 1 0 01.832.445l4.83 7.245A6 6 0 114.338 9.69L9.168 2.445A1 1 0 0110 2z",
						"clip-rule": "evenodd",
					}),
				])
			}
			if (sector === "Livelihoods") {
				return h(
					"svg",
					{
						fill: "none",
						stroke: "currentColor",
						"stroke-width": "2",
						viewBox: "0 0 24 24",
					},
					[
						h("path", {
							"stroke-linecap": "round",
							"stroke-linejoin": "round",
							d: "M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z",
						}),
					],
				)
			}
			if (sector === "Disaster Relief") {
				return h("svg", { fill: "currentColor", viewBox: "0 0 20 20" }, [
					h("path", {
						"fill-rule": "evenodd",
						d: "M8.257 3.099c.765-1.36 2.722-1.36 3.486 0l5.58 9.92c.75 1.334-.213 2.98-1.742 2.98H4.42c-1.53 0-2.493-1.646-1.743-2.98l5.58-9.92zM11 13a1 1 0 11-2 0 1 1 0 012 0zm-1-8a1 1 0 00-1 1v3a1 1 0 002 0V6a1 1 0 00-1-1z",
						"clip-rule": "evenodd",
					}),
				])
			}
			// Governance
			return h("svg", { fill: "currentColor", viewBox: "0 0 20 20" }, [
				h("path", { d: "M4 4a2 2 0 00-2 2v1h16V6a2 2 0 00-2-2H4z" }),
				h("path", {
					"fill-rule": "evenodd",
					d: "M18 9H2v5a2 2 0 002 2h12a2 2 0 002-2V9zM4 13a1 1 0 011-1h1a1 1 0 110 2H5a1 1 0 01-1-1zm5-1a1 1 0 100 2h1a1 1 0 100-2H9z",
					"clip-rule": "evenodd",
				}),
			])
		},
	}
}

function viewDetails(row) {
	alert(
		`Proposal Details for ${row.code} - ${row.title}\nStatus: ${row.status}\nGeography: ${row.geography}`,
	)
	activeActionRow.value = null
}

function quickDecision(row, action) {
	row.status = action === "Approve" ? "Approved" : "Rejected"
	activeActionRow.value = null
}
</script>
