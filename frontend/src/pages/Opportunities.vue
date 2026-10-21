<template>
  <VolunteerLayout>
    <div class="max-w-7xl mx-auto pb-16 md:pb-8">
      
      <!-- Breadcrumb Navigation -->
      <div class="flex items-center gap-2 text-xs text-gray-500 mb-3">
        <router-link to="/" class="hover:text-emerald-700 transition flex items-center gap-1">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="text-gray-400">
            <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path>
            <polyline points="9 22 9 12 15 12 15 22"></polyline>
          </svg>
        </router-link>
        <span class="text-gray-300">›</span>
        <span class="text-gray-600 font-medium">Opportunities</span>
      </div>

      <!-- Page Title & Motivational Quote -->
      <div class="flex flex-col md:flex-row md:items-end justify-between gap-4 mb-6">
        <div>
          <h1 class="text-2xl sm:text-3xl font-extrabold text-gray-900 tracking-tight">Volunteer Opportunities</h1>
          <p class="text-xs sm:text-sm text-gray-500 mt-1">Find meaningful ways to make a difference in your community.</p>
        </div>
        <div class="text-right hidden md:block">
          <p class="text-xs text-gray-500 italic max-w-xs leading-relaxed">
            “Communities thrive when people give their time.”
          </p>
        </div>
      </div>
      
      <!-- Hero Banner with Planting Volunteers Photo and Script Calligraphy -->
      <div class="rounded-3xl bg-gradient-to-r from-[#032e23] via-[#054032] to-[#075341] text-white relative overflow-hidden shadow-xl mb-6">
        
        <!-- Subtle Pattern Overlay -->
        <div class="absolute inset-0 opacity-10 bg-[radial-gradient(#ffffff_1px,transparent_1px)] [background-size:16px_16px] pointer-events-none"></div>

        <!-- Right Side Image with Soft Gradient Masking -->
        <div class="absolute right-0 top-0 bottom-0 w-full md:w-1/2 lg:w-[48%] pointer-events-none overflow-hidden">
          <img 
            src="/volunteers_planting.jpg" 
            alt="Volunteers planting trees in the community" 
            class="w-full h-full object-cover object-center transform scale-105"
          />
          <div class="absolute inset-0 bg-gradient-to-r from-[#054032] via-[#054032]/60 to-transparent"></div>
          
          <!-- Script Calligraphy on Image -->
          <div class="absolute bottom-5 left-6 lg:left-10 z-10 select-none">
            <span class="font-script text-2xl lg:text-3xl text-emerald-100/95 -rotate-6 block drop-shadow-[0_2px_6px_rgba(0,0,0,0.85)]">
              Communities Thrive Together
            </span>
          </div>
        </div>

        <!-- Left Content -->
        <div class="relative z-10 p-6 sm:p-8 lg:p-10 max-w-xl md:max-w-md lg:max-w-xl">
          <!-- Orange/Amber Badge -->
          <div class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-amber-600/90 text-amber-100 text-[10px] font-bold tracking-widest uppercase mb-3.5 shadow-sm">
            MAKE A BIGGER IMPACT
          </div>

          <!-- Headline -->
          <h2 class="text-2xl sm:text-3xl font-extrabold text-white tracking-tight leading-tight mb-3">
            Your time can create lasting change.
          </h2>

          <!-- Subtitle -->
          <p class="text-xs sm:text-sm text-emerald-100/90 leading-relaxed font-normal mb-6">
            Discover open roles and projects where your skills can make a real difference in the community through education, health, environment and more.
          </p>

          <!-- Buttons -->
          <div class="flex flex-wrap items-center gap-3">
            <button 
              @click="scrollToGrid"
              class="inline-flex items-center gap-2 px-5 py-2.5 rounded-xl bg-amber-600 hover:bg-amber-700 text-white font-bold text-xs shadow-md transition-all active:scale-[0.98]"
            >
              <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
              <span>Browse Opportunities</span>
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
            </button>

            <router-link 
              to="/shifts"
              class="inline-flex items-center gap-2 px-5 py-2.5 rounded-xl bg-white/10 hover:bg-white/20 border border-white/25 text-white font-semibold text-xs backdrop-blur-sm transition-all"
            >
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>
              <span>View My Schedule</span>
            </router-link>
          </div>
        </div>

      </div>

      <!-- Filter & Search Bar Row -->
      <div id="opportunities-filter" class="bg-white rounded-2xl border border-gray-100 p-3 shadow-sm mb-6 flex flex-col md:flex-row items-stretch md:items-center gap-3">
        
        <!-- Search Input -->
        <div class="relative flex-1">
          <svg class="absolute left-3.5 top-1/2 -translate-y-1/2 text-gray-400" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
          <input 
            v-model="searchQuery" 
            type="text" 
            placeholder="Search by title, skill or keyword..." 
            class="w-full pl-9 pr-4 py-2 bg-gray-50/70 border border-gray-200/80 rounded-xl text-xs text-gray-800 placeholder:text-gray-400 focus:bg-white focus:outline-none focus:ring-2 focus:ring-emerald-600/15 focus:border-emerald-600 transition"
          />
        </div>

        <!-- Location Dropdown -->
        <div class="relative min-w-[170px]">
          <svg class="absolute left-3 top-1/2 -translate-y-1/2 text-gray-400" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
          <select 
            v-model="selectedLocation" 
            class="w-full pl-8 pr-8 py-2 bg-gray-50/70 border border-gray-200/80 rounded-xl text-xs text-gray-700 focus:bg-white focus:outline-none focus:ring-2 focus:ring-emerald-600/15 focus:border-emerald-600 appearance-none font-medium transition cursor-pointer"
          >
            <option value="">All Locations</option>
            <option v-for="loc in uniqueLocations" :key="loc" :value="loc">{{ loc }}</option>
          </select>
          <svg class="absolute right-3 top-1/2 -translate-y-1/2 text-gray-400 pointer-events-none" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
        </div>

        <!-- Skill Dropdown -->
        <div class="relative min-w-[170px]">
          <svg class="absolute left-3 top-1/2 -translate-y-1/2 text-gray-400" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/></svg>
          <select 
            v-model="selectedSkill" 
            class="w-full pl-8 pr-8 py-2 bg-gray-50/70 border border-gray-200/80 rounded-xl text-xs text-gray-700 focus:bg-white focus:outline-none focus:ring-2 focus:ring-emerald-600/15 focus:border-emerald-600 appearance-none font-medium transition cursor-pointer"
          >
            <option value="">All Skills</option>
            <option v-for="skill in uniqueSkills" :key="skill" :value="skill">{{ skill }}</option>
          </select>
          <svg class="absolute right-3 top-1/2 -translate-y-1/2 text-gray-400 pointer-events-none" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
        </div>

        <!-- Sort Dropdown -->
        <div class="relative min-w-[160px]">
          <svg class="absolute left-3 top-1/2 -translate-y-1/2 text-gray-400" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M11 5h10M11 9h7M11 13h4M3 17l3 3 3-3M6 18V4"/></svg>
          <select 
            v-model="sortBy" 
            class="w-full pl-8 pr-8 py-2 bg-gray-50/70 border border-gray-200/80 rounded-xl text-xs text-gray-700 focus:bg-white focus:outline-none focus:ring-2 focus:ring-emerald-600/15 focus:border-emerald-600 appearance-none font-medium transition cursor-pointer"
          >
            <option value="newest">Newest First</option>
            <option value="endingSoon">Apply Deadline</option>
            <option value="vacancies">Most Slots</option>
            <option value="title">Title (A-Z)</option>
          </select>
          <svg class="absolute right-3 top-1/2 -translate-y-1/2 text-gray-400 pointer-events-none" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
        </div>

        <!-- Counter Indicator -->
        <div class="px-2 text-xs font-semibold text-gray-500 whitespace-nowrap self-center">
          {{ filteredOpportunities.length }} {{ filteredOpportunities.length === 1 ? 'opportunity' : 'opportunities' }} found
        </div>
      </div>
      
      <!-- Loading State -->
      <div v-if="opportunities.loading" class="flex justify-center py-20">
        <LoadingText>Loading opportunities...</LoadingText>
      </div>
      
      <!-- Error State -->
      <div v-else-if="opportunities.error" class="bg-red-50 text-red-600 p-4 rounded-xl shadow-sm border border-red-100">
        {{ opportunities.error.message || opportunities.error }}
      </div>
      
      <!-- Opportunities Content (Exactly 3 cards per page with pagination) -->
      <div v-else id="opportunities-grid">
        
        <!-- Empty State -->
        <div v-if="filteredOpportunities.length === 0" class="flex flex-col items-center justify-center bg-white rounded-2xl border border-gray-100 p-16 shadow-sm">
          <div class="w-16 h-16 bg-emerald-50 rounded-full flex items-center justify-center mb-4 text-emerald-800">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
          </div>
          <p class="text-gray-800 font-bold text-base">No matching opportunities found</p>
          <p class="text-gray-400 text-xs mt-1">Try adjusting your search criteria or clearing active filters.</p>
          <button 
            @click="clearFilters" 
            class="mt-4 px-4 py-2 text-xs font-semibold text-emerald-800 bg-emerald-50 hover:bg-emerald-100 rounded-xl transition"
          >
            Clear Filters
          </button>
        </div>
        
        <!-- 3-Cards Grid -->
        <div v-else>
          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            <div 
              v-for="opp in paginatedOpportunities" 
              :key="opp.name"
              class="bg-white rounded-2xl border-t-4 border-t-[#043d30] border-x border-b border-gray-200/80 shadow-sm hover:shadow-xl transition-all duration-300 transform hover:-translate-y-1 flex flex-col justify-between overflow-hidden relative group"
            >
              <div class="p-6 flex flex-col flex-1">
                
                <!-- Card Header: Badges Row -->
                <div class="flex items-center justify-between gap-2 mb-4">
                  <!-- Open Role Badge -->
                  <div class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-bold bg-emerald-50 text-emerald-800 border border-emerald-200/70">
                    <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M11 5L6 9H2v6h4l5 4V5z"/><path d="M19.07 4.93a10 10 0 0 1 0 14.14M15.54 8.46a5 5 0 0 1 0 7.07"/></svg>
                    <span>Open Role</span>
                  </div>

                  <!-- Slots Badge -->
                  <div class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-xs font-semibold bg-gray-100 text-gray-600">
                    <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
                    <span>{{ opp.vacancies || 1 }} slots</span>
                  </div>
                </div>
                
                <!-- Opportunity Title -->
                <h3 class="text-lg font-bold text-gray-900 mb-2.5 leading-snug group-hover:text-emerald-900 transition-colors line-clamp-2">
                  {{ opp.title }}
                </h3>
                
                <!-- Project Name Tag -->
                <div class="flex items-center gap-2 text-xs font-bold text-blue-600 mb-2 min-w-0" :title="opp.project_name || opp.project">
                  <svg class="flex-shrink-0" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"/></svg>
                  <span class="truncate">{{ opp.project_name || opp.project }}</span>
                </div>
                
                <!-- Location -->
                <div class="flex items-center gap-2 text-xs text-gray-600 font-medium mb-2">
                  <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="text-gray-400 flex-shrink-0"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
                  <span class="truncate">{{ opp.location || 'Community Hub' }}</span>
                </div>
                
                <!-- Deadline -->
                <div class="flex items-center gap-2 text-xs text-gray-600 font-medium mb-4">
                  <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="text-gray-400 flex-shrink-0"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>
                  <span>Apply by {{ formatDate(opp.application_deadline || opp.end_date) }}</span>
                </div>
                
                <!-- Description -->
                <div class="text-xs text-gray-500 leading-relaxed mb-6 flex-1 line-clamp-3" v-html="opp.description"></div>
                
                <!-- Required Skills Section -->
                <div class="mt-auto pt-4 border-t border-gray-100">
                  <p class="text-[10px] font-bold text-gray-400 uppercase tracking-wider mb-2.5">REQUIRED SKILLS</p>
                  <div class="flex flex-wrap gap-1.5 min-h-[32px]">
                    <span 
                      v-for="skill in getSkillsList(opp)" 
                      :key="skill"
                      class="inline-flex items-center px-2.5 py-1 rounded-md text-[11px] font-semibold bg-emerald-50 text-emerald-900 border border-emerald-200/70"
                    >
                      {{ skill }}
                    </span>
                    <span v-if="getSkillsList(opp).length === 0" class="text-xs text-gray-400 italic">
                      Open to all volunteers
                    </span>
                  </div>
                </div>

                <!-- Action Button -->
                <div class="pt-4 mt-2">
                  <button 
                    v-if="!opp.has_interest"
                    @click="submitInterest(opp)"
                    :disabled="submitting === opp.name"
                    class="w-full py-2.5 px-4 rounded-xl text-xs font-bold text-white bg-[#043d30] hover:bg-[#064e3b] active:scale-[0.99] transition-all flex items-center justify-center gap-2 shadow-sm disabled:opacity-50"
                  >
                    <span v-if="submitting === opp.name" class="flex items-center gap-2">
                      <svg class="animate-spin h-3.5 w-3.5 text-white" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8v8H4z"></path></svg>
                      Applying...
                    </span>
                    <span v-else class="flex items-center justify-center gap-2">
                      Apply Now
                      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                    </span>
                  </button>

                  <div 
                    v-else 
                    class="w-full py-2.5 px-4 rounded-xl text-xs font-bold text-emerald-800 bg-emerald-50 border border-emerald-200 flex items-center justify-center gap-2 shadow-sm"
                  >
                    <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg>
                    Application Submitted
                  </div>
                </div>

              </div>
            </div>
          </div>

          <!-- Pagination Bar (Showing 3 cards per page) -->
          <div v-if="totalPages > 1" class="flex flex-col sm:flex-row items-center justify-between gap-4 mt-9 pt-6 border-t border-gray-200">
            <!-- Counter Information -->
            <div class="text-xs text-gray-500 font-medium">
              Showing <span class="font-bold text-gray-800">{{ (currentPage - 1) * pageSize + 1 }}</span>
              to <span class="font-bold text-gray-800">{{ Math.min(currentPage * pageSize, filteredOpportunities.length) }}</span>
              of <span class="font-bold text-gray-800">{{ filteredOpportunities.length }}</span> opportunities
            </div>

            <!-- Page Navigation Controls -->
            <div class="flex items-center gap-1.5">
              <!-- Previous Button -->
              <button 
                @click="goToPage(currentPage - 1)" 
                :disabled="currentPage === 1"
                class="px-3.5 py-2 rounded-xl text-xs font-semibold text-gray-700 bg-white border border-gray-200 hover:bg-gray-50 disabled:opacity-40 disabled:cursor-not-allowed transition flex items-center gap-1 shadow-sm"
              >
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="15 18 9 12 15 6"/></svg>
                Previous
              </button>

              <!-- Page Number Buttons -->
              <button 
                v-for="p in totalPages" 
                :key="p"
                @click="goToPage(p)"
                :class="[
                  'w-8 h-8 rounded-xl text-xs font-bold transition flex items-center justify-center shadow-sm',
                  currentPage === p 
                    ? 'bg-[#043d30] text-white shadow-emerald-900/20' 
                    : 'bg-white text-gray-700 border border-gray-200 hover:bg-gray-50'
                ]"
              >
                {{ p }}
              </button>

              <!-- Next Button -->
              <button 
                @click="goToPage(currentPage + 1)" 
                :disabled="currentPage === totalPages"
                class="px-3.5 py-2 rounded-xl text-xs font-semibold text-gray-700 bg-white border border-gray-200 hover:bg-gray-50 disabled:opacity-40 disabled:cursor-not-allowed transition flex items-center gap-1 shadow-sm"
              >
                Next
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 18 15 12 9 6"/></svg>
              </button>
            </div>
          </div>

        </div>

      </div>

    </div>
  </VolunteerLayout>
</template>

<script setup>
import { createResource, LoadingText } from "frappe-ui"
import { ref, computed, watch } from "vue"
import VolunteerLayout from "../components/VolunteerLayout.vue"

const submitting = ref(null)
const searchQuery = ref("")
const selectedLocation = ref("")
const selectedSkill = ref("")
const sortBy = ref("newest")

// Pagination configuration: exactly 3 cards per page
const currentPage = ref(1)
const pageSize = 3

const opportunities = createResource({
  url: "ngo.api.volunteer.open_opportunities",
  method: "GET",
  auto: true
})

// Unique locations for filter dropdown
const uniqueLocations = computed(() => {
  const locs = new Set()
  for (const opp of (opportunities.data || [])) {
    if (opp.location) locs.add(opp.location.trim())
  }
  return Array.from(locs).sort()
})

// Unique skills for filter dropdown
const uniqueSkills = computed(() => {
  const skills = new Set()
  for (const opp of (opportunities.data || [])) {
    if (opp.required_skills) {
      opp.required_skills.split(',').forEach(s => {
        const trimmed = s.trim()
        if (trimmed) skills.add(trimmed)
      })
    }
  }
  return Array.from(skills).sort()
})

// Filtered and sorted opportunities list
const filteredOpportunities = computed(() => {
  let list = (opportunities.data || []).slice()

  if (searchQuery.value.trim()) {
    const q = searchQuery.value.toLowerCase().trim()
    list = list.filter(opp => 
      (opp.title && opp.title.toLowerCase().includes(q)) ||
      (opp.project_name && opp.project_name.toLowerCase().includes(q)) ||
      (opp.project && opp.project.toLowerCase().includes(q)) ||
      (opp.location && opp.location.toLowerCase().includes(q)) ||
      (opp.description && opp.description.toLowerCase().includes(q)) ||
      (opp.required_skills && opp.required_skills.toLowerCase().includes(q))
    )
  }

  if (selectedLocation.value) {
    list = list.filter(opp => opp.location === selectedLocation.value)
  }

  if (selectedSkill.value) {
    list = list.filter(opp => opp.required_skills && opp.required_skills.includes(selectedSkill.value))
  }

  if (sortBy.value === 'newest') {
    list.sort((a, b) => (b.name > a.name ? 1 : -1))
  } else if (sortBy.value === 'endingSoon') {
    list.sort((a, b) => {
      const da = a.end_date || a.application_deadline || '9999-99-99'
      const db = b.end_date || b.application_deadline || '9999-99-99'
      return String(da).localeCompare(String(db))
    })
  } else if (sortBy.value === 'vacancies') {
    list.sort((a, b) => (b.vacancies || 0) - (a.vacancies || 0))
  } else if (sortBy.value === 'title') {
    list.sort((a, b) => (a.title || '').localeCompare(b.title || ''))
  }

  return list
})

// Total pages calculation based on pageSize = 3
const totalPages = computed(() => {
  return Math.ceil(filteredOpportunities.value.length / pageSize) || 1
})

// Exactly 3 cards for the active page
const paginatedOpportunities = computed(() => {
  const start = (currentPage.value - 1) * pageSize
  return filteredOpportunities.value.slice(start, start + pageSize)
})

// Reset to page 1 whenever any filter changes
watch([searchQuery, selectedLocation, selectedSkill, sortBy], () => {
  currentPage.value = 1
})

function goToPage(page) {
  if (page >= 1 && page <= totalPages.value) {
    currentPage.value = page
    scrollToGrid()
  }
}

function clearFilters() {
  searchQuery.value = ""
  selectedLocation.value = ""
  selectedSkill.value = ""
  sortBy.value = "newest"
  currentPage.value = 1
}

function scrollToGrid() {
  const el = document.getElementById('opportunities-filter')
  if (el) {
    el.scrollIntoView({ behavior: 'smooth', block: 'start' })
  }
}

function getSkillsList(opp) {
  if (!opp.required_skills) return []
  return opp.required_skills
    .split(',')
    .map(s => s.trim())
    .filter(Boolean)
}

async function submitInterest(opp) {
  submitting.value = opp.name
  try {
    const res = await fetch('/api/method/ngo.api.volunteer.submit_interest', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        ...(window.csrf_token && { 'X-Frappe-CSRF-Token': window.csrf_token }),
      },
      body: JSON.stringify({
        opportunity: opp.name
      })
    })
    
    if (res.ok) {
      opp.has_interest = true
    } else {
      const err = await res.json()
      alert(err.message || "Failed to submit interest")
    }
  } catch (error) {
    alert("An error occurred")
  } finally {
    submitting.value = null
  }
}

function formatDate(dateStr) {
  if (!dateStr) return "Ongoing"
  return new Date(dateStr).toLocaleDateString("en-GB", {
    day: "numeric", month: "short", year: "numeric"
  })
}
</script>

<style scoped>
.line-clamp-2 {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;  
  overflow: hidden;
}
.line-clamp-3 {
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;  
  overflow: hidden;
}
</style>
