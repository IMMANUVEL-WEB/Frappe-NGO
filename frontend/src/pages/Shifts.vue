<template>
  <VolunteerLayout>
    <div class="max-w-7xl mx-auto space-y-6 pb-16">
      <!-- Top Breadcrumb & Header -->
      <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div>
          <!-- Breadcrumb -->
          <nav class="flex items-center gap-1.5 text-xs text-black-400 font-medium mb-1">
            <router-link to="/" class="hover:text-emerald-700 transition-colors flex items-center gap-1">
              <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path>
                <polyline points="9 22 9 12 15 12 15 22"></polyline>
              </svg>
            </router-link>
            <span>&rsaquo;</span>
            <span class="text-black-600">My Shifts</span>
          </nav>

          <h1 class="text-2xl sm:text-3xl font-extrabold text-black-900 tracking-tight">
            My Shifts
          </h1>
          <p class="text-black-500 text-sm mt-0.5">
            Your scheduled and past volunteering shifts.
          </p>
        </div>

        <!-- Segmented Toggle (Upcoming | Past) -->
        <div class="bg-black-100 p-1 rounded-xl inline-flex self-start sm:self-auto border border-black-200/60 shadow-inner">
          <button
            @click="activeView = 'upcoming'"
            class="px-5 py-2 text-xs font-bold rounded-lg transition-all"
            :class="[
              activeView === 'upcoming'
                ? 'bg-[#064e3b] text-white shadow-sm'
                : 'text-black-600 hover:text-black-900',
            ]"
          >
            Upcoming ({{ upcomingShiftsList.length }})
          </button>
          <button
            @click="activeView = 'past'"
            class="px-5 py-2 text-xs font-bold rounded-lg transition-all"
            :class="[
              activeView === 'past'
                ? 'bg-[#064e3b] text-white shadow-sm'
                : 'text-black-600 hover:text-black-900',
            ]"
          >
            Past ({{ pastShiftsList.length }})
          </button>
        </div>
      </div>

      <!-- 4 Stat Summary Cards (Real Volunteer Data) -->
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        <!-- Total Shifts -->
        <div class="bg-white rounded-2xl p-5 border border-black-100 shadow-sm hover:shadow-md transition-shadow relative overflow-hidden flex items-start justify-between">
          <div class="flex items-start gap-4">
            <div class="w-12 h-12 rounded-xl bg-emerald-50 text-emerald-600 flex items-center justify-center flex-shrink-0 border border-emerald-100/60">
              <svg class="w-6 h-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect>
                <line x1="16" y1="2" x2="16" y2="6"></line>
                <line x1="8" y1="2" x2="8" y2="6"></line>
                <line x1="3" y1="10" x2="21" y2="10"></line>
              </svg>
            </div>
            <div>
              <p class="text-xs font-semibold text-black-500 uppercase tracking-wider">Total Shifts</p>
              <h3 class="text-2xl font-black text-black-900 mt-0.5">
                {{ totalShiftsCount }}
              </h3>
              <p class="text-xs text-black-400 mt-0.5">All time shifts</p>
            </div>
          </div>
          <div class="text-emerald-500 opacity-60">
            <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M18 20V10M12 20V4M6 20v-6" />
            </svg>
          </div>
        </div>

        <!-- Upcoming Shifts -->
        <div class="bg-white rounded-2xl p-5 border border-black-100 shadow-sm hover:shadow-md transition-shadow relative overflow-hidden flex items-start justify-between">
          <div class="flex items-start gap-4">
            <div class="w-12 h-12 rounded-xl bg-blue-50 text-blue-600 flex items-center justify-center flex-shrink-0 border border-blue-100/60">
              <svg class="w-6 h-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <circle cx="12" cy="12" r="10"></circle>
                <polyline points="12 6 12 12 16 14"></polyline>
              </svg>
            </div>
            <div>
              <p class="text-xs font-semibold text-black-500 uppercase tracking-wider">Upcoming Shifts</p>
              <h3 class="text-2xl font-black text-black-900 mt-0.5">
                {{ upcomingShiftsList.length }}
              </h3>
              <p class="text-xs text-black-400 mt-0.5">Scheduled</p>
            </div>
          </div>
          <div class="text-blue-500 opacity-60">
            <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M18 20V10M12 20V4M6 20v-6" />
            </svg>
          </div>
        </div>

        <!-- Completed Shifts -->
        <div class="bg-white rounded-2xl p-5 border border-black-100 shadow-sm hover:shadow-md transition-shadow relative overflow-hidden flex items-start justify-between">
          <div class="flex items-start gap-4">
            <div class="w-12 h-12 rounded-xl bg-amber-50 text-amber-600 flex items-center justify-center flex-shrink-0 border border-amber-100/60">
              <svg class="w-6 h-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
                <polyline points="22 4 12 14.01 9 11.01"></polyline>
              </svg>
            </div>
            <div>
              <p class="text-xs font-semibold text-black-500 uppercase tracking-wider">Completed Shifts</p>
              <h3 class="text-2xl font-black text-black-900 mt-0.5">
                {{ completedShiftsCount }}
              </h3>
              <p class="text-xs text-black-400 mt-0.5">Successfully completed</p>
            </div>
          </div>
          <div class="text-amber-500 opacity-60">
            <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M18 20V10M12 20V4M6 20v-6" />
            </svg>
          </div>
        </div>

        <!-- Total Hours -->
        <div class="bg-white rounded-2xl p-5 border border-black-100 shadow-sm hover:shadow-md transition-shadow relative overflow-hidden flex items-start justify-between">
          <div class="flex items-start gap-4">
            <div class="w-12 h-12 rounded-xl bg-purple-50 text-purple-600 flex items-center justify-center flex-shrink-0 border border-purple-100/60">
              <svg class="w-6 h-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M5 22h14"></path>
                <path d="M5 2h14"></path>
                <path d="M17 22v-4.172a2 2 0 0 0-.586-1.414L12 12l-4.414 4.414A2 2 0 0 0 7 17.828V22"></path>
                <path d="M7 2v4.172a2 2 0 0 0 .586 1.414L12 12l4.414-4.414A2 2 0 0 0 17 6.172V2"></path>
              </svg>
            </div>
            <div>
              <p class="text-xs font-semibold text-black-500 uppercase tracking-wider">Total Hours</p>
              <h3 class="text-2xl font-black text-black-900 mt-0.5">
                {{ totalShiftsHours }} hrs
              </h3>
              <p class="text-xs text-black-400 mt-0.5">Across shifts</p>
            </div>
          </div>
          <div class="text-purple-500 opacity-60">
            <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M18 20V10M12 20V4M6 20v-6" />
            </svg>
          </div>
        </div>
      </div>

      <!-- SECTION 1: Upcoming Shifts -->
      <div v-if="activeView === 'upcoming' || activeView === 'all'" class="space-y-4">
        <!-- Section Header -->
        <div class="flex items-center justify-between">
          <div class="flex items-center gap-2">
            <svg class="w-5 h-5 text-black-700" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect>
              <line x1="16" y1="2" x2="16" y2="6"></line>
              <line x1="8" y1="2" x2="8" y2="6"></line>
              <line x1="3" y1="10" x2="21" y2="10"></line>
            </svg>
            <h2 class="text-lg font-bold text-black-900">Upcoming Shifts</h2>
          </div>
        </div>

        <!-- Empty state when no upcoming shifts -->
        <div
          v-if="upcomingShiftsList.length === 0"
          class="bg-white rounded-2xl p-10 text-center border border-black-100 shadow-sm"
        >
          <div class="w-14 h-14 bg-black-50 text-black-400 rounded-full flex items-center justify-center mx-auto mb-3">
            <svg class="w-7 h-7" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect>
              <line x1="16" y1="2" x2="16" y2="6"></line>
              <line x1="8" y1="2" x2="8" y2="6"></line>
              <line x1="3" y1="10" x2="21" y2="10"></line>
            </svg>
          </div>
          <h3 class="text-base font-bold text-black-900 mb-1">No upcoming shifts scheduled</h3>
          <p class="text-xs text-black-500 max-w-sm mx-auto">
            You do not have any upcoming volunteer shifts. Join available opportunities to schedule a shift.
          </p>
          <div class="mt-4">
            <router-link
              to="/opportunities"
              class="inline-flex items-center gap-1.5 px-4 py-2 bg-[#064e3b] text-white text-xs font-semibold rounded-xl hover:bg-[#043226] transition-all"
            >
              Browse Open Opportunities &rarr;
            </router-link>
          </div>
        </div>

        <!-- Upcoming Shift Cards -->
        <div v-else class="space-y-4">
          <div
            v-for="shift in upcomingShiftsList"
            :key="shift.name"
            class="bg-white rounded-2xl border border-black-100 p-5 shadow-sm hover:shadow-md transition-all flex flex-col lg:flex-row items-stretch lg:items-center justify-between gap-6"
          >
            <!-- Left: Date Box & Details -->
            <div class="flex flex-col sm:flex-row items-start sm:items-center gap-4 flex-1">
              <!-- Date Box -->
              <div class="w-20 h-24 rounded-2xl bg-[#043226] text-white flex flex-col items-center justify-center p-2 text-center flex-shrink-0 shadow-sm border border-emerald-800">
                <span class="text-[11px] font-extrabold tracking-wider text-emerald-300 uppercase leading-none">
                  {{ getMonthName(shift.shift_date) }}
                </span>
                <span class="text-2xl font-black text-white leading-tight my-0.5">
                  {{ getDayNumber(shift.shift_date) }}
                </span>
                <span class="text-[10px] font-bold tracking-wider text-emerald-200/80 uppercase leading-none">
                  {{ getWeekday(shift.shift_date) }}
                </span>
              </div>

              <!-- Thumbnail -->
              <img
                :src="shift.image || volunteerTutoring"
                :alt="shift.opportunity_title"
                class="w-full sm:w-36 h-24 rounded-xl object-cover shadow-inner flex-shrink-0"
                @error="handleImgError"
              />

              <!-- Center Info -->
              <div class="space-y-1.5 flex-1 min-w-0">
                <h3 class="text-base sm:text-lg font-bold text-black-900 leading-snug line-clamp-1">
                  {{ shift.opportunity_title }}
                </h3>

                <!-- Project Name -->
                <div class="flex items-center gap-1.5 text-xs font-semibold text-blue-600">
                  <svg class="w-3.5 h-3.5 flex-shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"></path>
                  </svg>
                  <span class="truncate">{{ shift.project_name || shift.project || 'General Project' }}</span>
                </div>

                <!-- Location -->
                <div v-if="shift.location" class="flex items-center gap-1.5 text-xs text-black-500 font-medium">
                  <svg class="w-3.5 h-3.5 text-black-400 flex-shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path>
                    <circle cx="12" cy="10" r="3"></circle>
                  </svg>
                  <span class="truncate">{{ shift.location }}</span>
                </div>

                <!-- Time -->
                <div class="flex flex-wrap items-center gap-x-4 gap-y-1 text-xs text-black-500 font-medium pt-0.5">
                  <div class="flex items-center gap-1">
                    <svg class="w-3.5 h-3.5 text-black-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                      <circle cx="12" cy="12" r="10"></circle>
                      <polyline points="12 6 12 12 16 14"></polyline>
                    </svg>
                    <span>{{ formatTimeRange(shift.start_time, shift.end_time) }}</span>
                  </div>
                </div>
              </div>
            </div>

            <!-- Right: Status & Actions -->
            <div class="flex flex-col sm:flex-row lg:flex-row items-start sm:items-center gap-4 self-end lg:self-center">
              <span
                class="inline-flex items-center gap-1 px-3 py-1 rounded-full text-xs font-bold"
                :class="[
                  shift.participant_status === 'Confirmed' || shift.status === 'Confirmed'
                    ? 'bg-emerald-100 text-emerald-800'
                    : 'bg-blue-100 text-blue-800',
                ]"
              >
                <span>{{ shift.participant_status || shift.status || "Scheduled" }}</span>
              </span>

              <!-- Buttons -->
              <div class="flex items-center gap-2">
                <button
                  @click="openShiftDetails(shift)"
                  class="px-4 py-2.5 bg-[#064e3b] hover:bg-[#043226] text-white text-xs font-bold rounded-xl transition-all shadow-sm flex items-center gap-1.5 whitespace-nowrap"
                >
                  <span>View Details</span>
                  <span class="text-emerald-300">&rarr;</span>
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- SECTION 2: Past Shifts -->
      <div v-if="activeView === 'past' || activeView === 'all'" class="space-y-4 pt-4">
        <!-- Section Header -->
        <div class="flex items-center justify-between">
          <div class="flex items-center gap-2">
            <svg class="w-5 h-5 text-black-700" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <circle cx="12" cy="12" r="10"></circle>
              <polyline points="12 6 12 12 16 14"></polyline>
            </svg>
            <h2 class="text-lg font-bold text-black-900">Past Shifts</h2>
          </div>
        </div>

        <!-- Empty state when no past shifts -->
        <div
          v-if="pastShiftsList.length === 0"
          class="bg-white rounded-2xl p-10 text-center border border-black-100 shadow-sm"
        >
          <div class="w-14 h-14 bg-black-50 text-black-400 rounded-full flex items-center justify-center mx-auto mb-3">
            <svg class="w-7 h-7" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <circle cx="12" cy="12" r="10"></circle>
              <polyline points="12 6 12 12 16 14"></polyline>
            </svg>
          </div>
          <h3 class="text-base font-bold text-black-900 mb-1">No past shifts recorded</h3>
          <p class="text-xs text-black-500 max-w-sm mx-auto">
            Your completed shifts will appear here once attended.
          </p>
        </div>

        <!-- Past Shift Cards -->
        <div v-else class="space-y-4">
          <div
            v-for="shift in pastShiftsList"
            :key="shift.name"
            class="bg-white rounded-2xl border border-black-100 p-5 shadow-sm hover:shadow-md transition-all flex flex-col lg:flex-row items-stretch lg:items-center justify-between gap-6"
          >
            <!-- Left: Date Box & Details -->
            <div class="flex flex-col sm:flex-row items-start sm:items-center gap-4 flex-1">
              <div class="w-20 h-24 rounded-2xl bg-black-100 text-black-800 flex flex-col items-center justify-center p-2 text-center flex-shrink-0 shadow-inner border border-black-200">
                <span class="text-[11px] font-extrabold tracking-wider text-black-500 uppercase leading-none">
                  {{ getMonthName(shift.shift_date) }}
                </span>
                <span class="text-2xl font-black text-black-900 leading-tight my-0.5">
                  {{ getDayNumber(shift.shift_date) }}
                </span>
                <span class="text-[10px] font-bold tracking-wider text-black-400 uppercase leading-none">
                  {{ getWeekday(shift.shift_date) }}
                </span>
              </div>

              <img
                :src="shift.image || volunteersPlanting"
                :alt="shift.opportunity_title"
                class="w-full sm:w-36 h-24 rounded-xl object-cover shadow-inner flex-shrink-0"
              />

              <!-- Center Info -->
              <div class="space-y-1.5 flex-1 min-w-0">
                <h3 class="text-base sm:text-lg font-bold text-black-900 leading-snug line-clamp-1">
                  {{ shift.opportunity_title }}
                </h3>

                <!-- Project Name -->
                <div class="flex items-center gap-1.5 text-xs font-semibold text-blue-600">
                  <svg class="w-3.5 h-3.5 flex-shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"></path>
                  </svg>
                  <span class="truncate">{{ shift.project_name || shift.project || 'General Project' }}</span>
                </div>

                <!-- Location -->
                <div v-if="shift.location" class="flex items-center gap-1.5 text-xs text-black-500 font-medium">
                  <svg class="w-3.5 h-3.5 text-black-400 flex-shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path>
                    <circle cx="12" cy="10" r="3"></circle>
                  </svg>
                  <span class="truncate">{{ shift.location }}</span>
                </div>

                <!-- Time -->
                <div class="flex items-center gap-1 text-xs text-black-500 font-medium pt-0.5">
                  <svg class="w-3.5 h-3.5 text-black-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <circle cx="12" cy="12" r="10"></circle>
                    <polyline points="12 6 12 12 16 14"></polyline>
                  </svg>
                  <span>{{ formatTimeRange(shift.start_time, shift.end_time) }}</span>
                </div>
              </div>
            </div>

            <!-- Right: Status -->
            <div class="flex items-center self-end lg:self-center">
              <span class="inline-flex items-center gap-1 px-3 py-1 bg-emerald-100 text-emerald-800 rounded-full text-xs font-bold">
                <span>✓</span>
                <span>{{ shift.participant_status || shift.status || 'Completed' }}</span>
              </span>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Shift Details Modal -->
    <div
      v-if="selectedShift"
      class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/60 backdrop-blur-sm animate-fade-in"
    >
      <div class="bg-white rounded-3xl max-w-lg w-full p-6 sm:p-8 shadow-2xl relative">
        <button
          @click="selectedShift = null"
          class="absolute top-5 right-5 text-black-400 hover:text-black-600 p-1.5 rounded-full hover:bg-black-100"
        >
          <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <line x1="18" y1="6" x2="6" y2="18"></line>
            <line x1="6" y1="6" x2="18" y2="18"></line>
          </svg>
        </button>

        <span class="px-2.5 py-0.5 rounded-full text-xs font-bold bg-emerald-100 text-emerald-800 inline-block mb-3">
          {{ selectedShift.participant_status || selectedShift.status || "Scheduled" }}
        </span>

        <h3 class="text-xl font-bold text-black-900 mb-2">
          {{ selectedShift.opportunity_title }}
        </h3>
        <p class="text-xs font-semibold text-blue-600 mb-4 flex items-center gap-1">
          📁 {{ selectedShift.project_name || selectedShift.project }}
        </p>

        <div class="space-y-3 text-sm text-black-600 bg-black-50/80 p-4 rounded-2xl mb-6">
          <div class="flex justify-between">
            <span class="font-medium text-black-500">Date:</span>
            <span class="font-bold text-black-800">{{ formatDate(selectedShift.shift_date) }}</span>
          </div>
          <div class="flex justify-between">
            <span class="font-medium text-black-500">Time:</span>
            <span class="font-bold text-black-800">{{ formatTimeRange(selectedShift.start_time, selectedShift.end_time) }}</span>
          </div>
          <div v-if="selectedShift.location" class="flex justify-between">
            <span class="font-medium text-black-500">Location:</span>
            <span class="font-bold text-black-800">{{ selectedShift.location }}</span>
          </div>
        </div>

        <div class="flex justify-end gap-2">
          <button
            @click="selectedShift = null"
            class="px-5 py-2 bg-[#064e3b] text-white rounded-xl font-bold text-sm hover:bg-[#043226]"
          >
            Close
          </button>
        </div>
      </div>
    </div>
  </VolunteerLayout>
</template>

<script setup>
import volunteerTutoring from "@/assets/volunteer_tutoring.jpg"
import volunteersPlanting from "@/assets/volunteers_planting.jpg"

const handleImgError = (e) => {
	e.target.onerror = null
	e.target.src = volunteersPlanting
}

import { createResource } from "frappe-ui"
import { computed, ref } from "vue"
import VolunteerLayout from "../components/VolunteerLayout.vue"

const activeView = ref("all")
const selectedShift = ref(null)

// Real backend upcoming shifts
const upcomingResource = createResource({
	url: "ngo.api.volunteer.my_shifts",
	params: { period: "upcoming" },
	auto: true,
})

// Real backend past shifts
const pastResource = createResource({
	url: "ngo.api.volunteer.my_shifts",
	params: { period: "past" },
	auto: true,
})

// Real upcoming shifts list
const upcomingShiftsList = computed(() => {
	if (upcomingResource.data && Array.isArray(upcomingResource.data)) {
		return upcomingResource.data.map((s) => ({
			...s,
			image: volunteerTutoring,
		}))
	}
	return []
})

// Real past shifts list
const pastShiftsList = computed(() => {
	if (pastResource.data && Array.isArray(pastResource.data)) {
		return pastResource.data.map((s) => ({
			...s,
			image: volunteersPlanting,
		}))
	}
	return []
})

const totalShiftsCount = computed(() => {
	return upcomingShiftsList.value.length + pastShiftsList.value.length
})

const completedShiftsCount = computed(() => {
	return pastShiftsList.value.filter(
		(s) => s.participant_status === "Present" || s.status === "Completed",
	).length
})

const totalShiftsHours = computed(() => {
	// Approximate duration or sum from past records
	return completedShiftsCount.value * 3
})

function getMonthName(dateStr) {
	if (!dateStr) return "DATE"
	const d = new Date(dateStr)
	return d.toLocaleDateString("en-US", { month: "short" }).toUpperCase()
}

function getDayNumber(dateStr) {
	if (!dateStr) return "-"
	const d = new Date(dateStr)
	return d.getDate()
}

function getWeekday(dateStr) {
	if (!dateStr) return "-"
	const d = new Date(dateStr)
	return d.toLocaleDateString("en-US", { weekday: "short" }).toUpperCase()
}

function formatDate(dateStr) {
	if (!dateStr) return "-"
	const d = new Date(dateStr)
	return d.toLocaleDateString("en-US", {
		weekday: "short",
		month: "short",
		day: "numeric",
		year: "numeric",
	})
}

function formatTimeRange(start, end) {
	if (!start && !end) return "Time TBA"
	return `${start || ""} – ${end || ""}`
}

function openShiftDetails(shift) {
	selectedShift.value = shift
}
</script>
