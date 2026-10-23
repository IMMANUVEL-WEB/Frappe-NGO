<template>
  <VolunteerLayout>
    <div class="max-w-7xl mx-auto space-y-6 pb-16">
      <!-- Top Breadcrumb & Header -->
      <div
        class="flex flex-col lg:flex-row lg:items-center justify-between gap-4"
      >
        <div>
          <!-- Breadcrumb -->
          <nav
            class="flex items-center gap-1.5 text-xs text-black-400 font-medium mb-1"
          >
            <router-link
              to="/"
              class="hover:text-emerald-700 transition-colors flex items-center gap-1"
            >
              <svg
                class="w-3.5 h-3.5"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
              >
                <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path>
                <polyline points="9 22 9 12 15 12 15 22"></polyline>
              </svg>
            </router-link>
            <span>&rsaquo;</span>
            <span class="text-black-600">My Assignments</span>
          </nav>

          <h1
            class="text-2xl sm:text-3xl font-extrabold text-black-900 tracking-tight"
          >
            My Assignments
          </h1>
          <p class="text-black-500 text-sm mt-0.5">
            View and manage your active and past assignments.
          </p>
        </div>

        <!-- Inspirational Quote -->
        <div class="hidden lg:block text-right">
          <p
            class="text-xs sm:text-sm text-black-400 italic font-serif leading-relaxed"
          >
            “Every assignment is a step towards a stronger community.”
          </p>
        </div>
      </div>

      <!-- 4 Stat Summary Cards (Real Volunteer Data) -->
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        <!-- Total Assignments -->
        <div
          class="bg-white rounded-2xl p-5 border border-black-100 shadow-sm hover:shadow-md transition-shadow relative overflow-hidden flex items-start justify-between"
        >
          <div class="flex items-start gap-4">
            <div
              class="w-12 h-12 rounded-xl bg-emerald-50 text-emerald-600 flex items-center justify-center flex-shrink-0 border border-emerald-100/60"
            >
              <svg
                class="w-6 h-6"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
              >
                <path
                  d="M9 5H7a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V7a2 2 0 0 0-2-2h-2"
                ></path>
                <rect x="9" y="3" width="6" height="4" rx="1"></rect>
                <path d="M9 14l2 2 4-4"></path>
              </svg>
            </div>
            <div>
              <p
                class="text-xs font-semibold text-black-500 uppercase tracking-wider"
              >
                Total Assignments
              </p>
              <h3 class="text-2xl font-black text-black-900 mt-0.5">
                {{ totalStats.total }}
              </h3>
              <p class="text-xs text-black-400 mt-0.5">All time assignments</p>
            </div>
          </div>
          <div class="text-emerald-500 opacity-60">
            <svg
              class="w-4 h-4"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              stroke-width="2"
            >
              <path d="M18 20V10M12 20V4M6 20v-6" />
            </svg>
          </div>
        </div>

        <!-- Active Assignments -->
        <div
          class="bg-white rounded-2xl p-5 border border-black-100 shadow-sm hover:shadow-md transition-shadow relative overflow-hidden flex items-start justify-between"
        >
          <div class="flex items-start gap-4">
            <div
              class="w-12 h-12 rounded-xl bg-blue-50 text-blue-600 flex items-center justify-center flex-shrink-0 border border-blue-100/60"
            >
              <svg
                class="w-6 h-6"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
              >
                <circle cx="12" cy="12" r="10"></circle>
                <polyline points="12 6 12 12 16 14"></polyline>
              </svg>
            </div>
            <div>
              <p
                class="text-xs font-semibold text-black-500 uppercase tracking-wider"
              >
                Active Assignments
              </p>
              <h3 class="text-2xl font-black text-black-900 mt-0.5">
                {{ totalStats.active }}
              </h3>
              <p class="text-xs text-black-400 mt-0.5">Currently in progress</p>
            </div>
          </div>
          <div class="text-blue-500 opacity-60">
            <svg
              class="w-4 h-4"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              stroke-width="2"
            >
              <path d="M18 20V10M12 20V4M6 20v-6" />
            </svg>
          </div>
        </div>

        <!-- Completed Assignments -->
        <div
          class="bg-white rounded-2xl p-5 border border-black-100 shadow-sm hover:shadow-md transition-shadow relative overflow-hidden flex items-start justify-between"
        >
          <div class="flex items-start gap-4">
            <div
              class="w-12 h-12 rounded-xl bg-amber-50 text-amber-600 flex items-center justify-center flex-shrink-0 border border-amber-100/60"
            >
              <svg
                class="w-6 h-6"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
              >
                <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
                <polyline points="22 4 12 14.01 9 11.01"></polyline>
              </svg>
            </div>
            <div>
              <p
                class="text-xs font-semibold text-black-500 uppercase tracking-wider"
              >
                Completed Assignments
              </p>
              <h3 class="text-2xl font-black text-black-900 mt-0.5">
                {{ totalStats.completed }}
              </h3>
              <p class="text-xs text-black-400 mt-0.5">
                Successfully completed
              </p>
            </div>
          </div>
          <div class="text-amber-500 opacity-60">
            <svg
              class="w-4 h-4"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              stroke-width="2"
            >
              <path d="M18 20V10M12 20V4M6 20v-6" />
            </svg>
          </div>
        </div>

        <!-- Withdrawn Assignments -->
        <div
          class="bg-white rounded-2xl p-5 border border-black-100 shadow-sm hover:shadow-md transition-shadow relative overflow-hidden flex items-start justify-between"
        >
          <div class="flex items-start gap-4">
            <div
              class="w-12 h-12 rounded-xl bg-rose-50 text-rose-600 flex items-center justify-center flex-shrink-0 border border-rose-100/60"
            >
              <svg
                class="w-6 h-6"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
              >
                <circle cx="12" cy="12" r="10"></circle>
                <line x1="15" y1="9" x2="9" y2="15"></line>
                <line x1="9" y1="9" x2="15" y2="15"></line>
              </svg>
            </div>
            <div>
              <p
                class="text-xs font-semibold text-black-500 uppercase tracking-wider"
              >
                Withdrawn
              </p>
              <h3 class="text-2xl font-black text-black-900 mt-0.5">
                {{ totalStats.withdrawn }}
              </h3>
              <p class="text-xs text-black-400 mt-0.5">Withdrawn assignments</p>
            </div>
          </div>
          <div class="text-rose-500 opacity-60">
            <svg
              class="w-4 h-4"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              stroke-width="2"
            >
              <path d="M18 20V10M12 20V4M6 20v-6" />
            </svg>
          </div>
        </div>
      </div>

      <!-- Filter Tabs & Controls Bar -->
      <div
        class="flex flex-col md:flex-row md:items-center justify-between gap-4 border-b border-black-200 pb-3"
      >
        <!-- Status Tabs -->
        <div
          class="flex items-center gap-2 overflow-x-auto pb-1 md:pb-0 scrollbar-none"
        >
          <button
            v-for="tab in filterTabs"
            :key="tab.id"
            @click="activeFilter = tab.id"
            class="flex items-center gap-2 px-3 py-2 text-sm font-semibold transition-all relative whitespace-nowrap"
            :class="[
              activeFilter === tab.id
                ? 'text-[#064e3b] font-bold after:content-[\'\'] after:absolute after:bottom-[-13px] after:left-0 after:right-0 after:h-0.5 after:bg-[#064e3b]'
                : 'text-black-500 hover:text-black-800',
            ]"
          >
            <span>{{ tab.label }}</span>
            <span
              class="px-2 py-0.5 text-xs rounded-full font-bold"
              :class="[
                activeFilter === tab.id
                  ? 'bg-[#064e3b] text-white'
                  : 'bg-black-100 text-black-600',
              ]"
            >
              {{ tab.count }}
            </span>
          </button>
        </div>

        <!-- Sort and Date Dropdowns -->
        <div class="flex items-center gap-3 self-end md:self-auto">
          <!-- Sort Dropdown -->
          <div class="relative inline-block text-left">
            <select
              v-model="sortBy"
              class="appearance-none bg-white border border-black-200 rounded-xl px-3.5 py-2 pr-8 text-xs font-semibold text-black-700 shadow-sm focus:outline-none focus:ring-2 focus:ring-emerald-600 cursor-pointer"
            >
              <option value="newest">⇅ Newest First</option>
              <option value="oldest">⇅ Oldest First</option>
            </select>
            <div
              class="pointer-events-none absolute inset-y-0 right-0 flex items-center px-2 text-black-500"
            >
              <svg class="w-3.5 h-3.5" viewBox="0 0 20 20" fill="currentColor">
                <path
                  fill-rule="evenodd"
                  d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z"
                  clip-rule="evenodd"
                />
              </svg>
            </div>
          </div>
        </div>
      </div>

      <!-- Assignments List -->
      <div v-if="assignmentsResource.loading" class="flex justify-center py-16">
        <div class="flex flex-col items-center gap-3">
          <div
            class="w-10 h-10 border-4 border-emerald-200 border-t-emerald-600 rounded-full animate-spin"
          ></div>
          <p class="text-sm font-medium text-black-500">
            Loading assignments...
          </p>
        </div>
      </div>

      <div
        v-else-if="filteredAssignments.length === 0"
        class="bg-white rounded-2xl p-12 text-center border border-black-100 shadow-sm"
      >
        <div
          class="w-16 h-16 bg-black-50 text-black-400 rounded-full flex items-center justify-center mx-auto mb-4"
        >
          <svg
            class="w-8 h-8"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            stroke-width="2"
          >
            <path
              d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"
            ></path>
            <polyline points="14 2 14 8 20 8"></polyline>
          </svg>
        </div>
        <h3 class="text-lg font-bold text-black-900 mb-1">
          No assignments found
        </h3>
        <p class="text-sm text-black-500 max-w-sm mx-auto">
          You currently have no assignments registered matching this filter.
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

      <div v-else class="space-y-4">
        <div
          v-for="item in filteredAssignments"
          :key="item.name"
          class="bg-white rounded-2xl border border-black-100 p-5 shadow-sm hover:shadow-md transition-all flex flex-col lg:flex-row items-stretch lg:items-center justify-between gap-6"
        >
          <!-- Left: Thumbnail Image & Info -->
          <div
            class="flex flex-col sm:flex-row items-start sm:items-center gap-4 flex-1"
          >
            <img
              :src="item.image || volunteerTutoring"
              :alt="item.opportunity_title"
              class="w-full sm:w-44 h-32 rounded-xl object-cover shadow-inner flex-shrink-0"
              @error="handleImgError"
            />

            <!-- Middle Info Column -->
            <div class="space-y-2 flex-1 min-w-0">
              <div class="flex items-center gap-2">
                <span
                  class="px-2.5 py-0.5 rounded-full text-xs font-bold"
                  :class="getStatusBadgeClass(item.status)"
                >
                  {{ item.status }}
                </span>
              </div>

              <!-- Title -->
              <h2
                class="text-lg font-bold text-black-900 hover:text-emerald-800 transition-colors leading-snug line-clamp-1"
              >
                {{ item.opportunity_title }}
              </h2>

              <!-- Project Name (Human Readable) -->
              <div
                class="flex items-center gap-1.5 text-xs font-semibold text-blue-600 hover:text-blue-700"
              >
                <svg
                  class="w-3.5 h-3.5 flex-shrink-0"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  stroke-width="2"
                >
                  <path
                    d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"
                  ></path>
                </svg>
                <span class="truncate">{{
                  item.project_name || item.project || "General Project"
                }}</span>
              </div>

              <!-- Meta: Location & Dates -->
              <div
                class="flex flex-wrap items-center gap-x-4 gap-y-1 text-xs text-black-500 font-medium"
              >
                <div v-if="item.location" class="flex items-center gap-1">
                  <svg
                    class="w-3.5 h-3.5 text-black-400"
                    viewBox="0 0 24 24"
                    fill="none"
                    stroke="currentColor"
                    stroke-width="2"
                  >
                    <path
                      d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"
                    ></path>
                    <circle cx="12" cy="10" r="3"></circle>
                  </svg>
                  <span>{{ item.location }}</span>
                </div>
                <div class="flex items-center gap-1">
                  <svg
                    class="w-3.5 h-3.5 text-black-400"
                    viewBox="0 0 24 24"
                    fill="none"
                    stroke="currentColor"
                    stroke-width="2"
                  >
                    <rect
                      x="3"
                      y="4"
                      width="18"
                      height="18"
                      rx="2"
                      ry="2"
                    ></rect>
                    <line x1="16" y1="2" x2="16" y2="6"></line>
                    <line x1="8" y1="2" x2="8" y2="6"></line>
                    <line x1="3" y1="10" x2="21" y2="10"></line>
                  </svg>
                  <span
                    >{{ formatDate(item.from_date) }} –
                    {{ formatDate(item.to_date) }}</span
                  >
                </div>
              </div>
            </div>
          </div>

          <!-- Middle-Right: Progress & Skills -->
          <div
            class="lg:w-80 flex flex-col justify-center space-y-3 lg:border-l lg:border-black-100 lg:pl-6"
          >
            <!-- Active Assignment Progress -->
            <div v-if="item.status === 'Active'" class="space-y-1.5">
              <div
                class="flex justify-between items-center text-xs font-semibold"
              >
                <span class="text-black-500">Progress</span>
                <span class="text-black-900 font-bold"
                  >{{ item.progress_pct }}%</span
                >
              </div>
              <div class="w-full h-2 bg-black-100 rounded-full overflow-hidden">
                <div
                  class="h-full bg-emerald-700 rounded-full transition-all duration-500"
                  :style="{ width: `${item.progress_pct}%` }"
                ></div>
              </div>
              <p class="text-xs text-black-500 font-medium">
                {{ Number(item.hours_done || 0).toFixed(1) }} hours completed
              </p>
            </div>

            <!-- Completed Assignment -->
            <div v-else-if="item.status === 'Completed'" class="space-y-1.5">
              <span class="text-xs font-semibold text-black-500 block"
                >Hours Completed</span
              >
              <div
                class="flex items-center gap-1.5 text-xs font-bold text-black-900"
              >
                <svg
                  class="w-3.5 h-3.5 text-emerald-600"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  stroke-width="2.5"
                >
                  <circle cx="12" cy="12" r="10"></circle>
                  <polyline points="12 6 12 12 16 14"></polyline>
                </svg>
                <span>{{ Number(item.hours_done || 0).toFixed(1) }} hrs</span>
              </div>
              <div class="w-full h-2 bg-emerald-600 rounded-full"></div>
            </div>

            <!-- Skill Tags -->
            <div
              v-if="item.tags && item.tags.length > 0"
              class="flex flex-wrap gap-1.5"
            >
              <span
                v-for="(skill, idx) in item.tags"
                :key="idx"
                class="px-2.5 py-1 bg-emerald-50 text-emerald-800 border border-emerald-100 rounded-md text-[11px] font-semibold"
              >
                {{ skill }}
              </span>
            </div>
          </div>

          <!-- Far Right: Action Buttons -->
          <div class="flex items-center gap-2 self-end lg:self-center">
            <button
              v-if="item.status === 'Completed'"
              @click="openCertificateModal(item)"
              class="px-4 py-2 bg-white border border-black-300 hover:bg-black-50 text-black-800 text-xs font-bold rounded-xl transition-all shadow-sm whitespace-nowrap"
            >
              View Certificate
            </button>
            <button
              v-else
              @click="openDetailsModal(item)"
              class="px-4 py-2 bg-[#064e3b] hover:bg-[#043226] text-white text-xs font-bold rounded-xl transition-all shadow-sm flex items-center gap-1.5 whitespace-nowrap"
            >
              <span>View Details</span>
              <span class="text-emerald-300">&rarr;</span>
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- Details Modal -->
    <div
      v-if="selectedItem"
      class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/60 backdrop-blur-sm animate-fade-in"
    >
      <div
        class="bg-white rounded-3xl max-w-xl w-full p-6 sm:p-8 shadow-2xl relative"
      >
        <button
          @click="selectedItem = null"
          class="absolute top-5 right-5 text-black-400 hover:text-black-600 p-1.5 rounded-full hover:bg-black-100"
        >
          <svg
            class="w-5 h-5"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            stroke-width="2"
          >
            <line x1="18" y1="6" x2="6" y2="18"></line>
            <line x1="6" y1="6" x2="18" y2="18"></line>
          </svg>
        </button>

        <div class="flex items-center gap-2 mb-3">
          <span
            :class="getStatusBadgeClass(selectedItem.status)"
            class="px-2.5 py-0.5 rounded-full text-xs font-bold"
          >
            {{ selectedItem.status }}
          </span>
          <span class="text-xs text-black-400 font-semibold">{{
            selectedItem.name
          }}</span>
        </div>

        <h3 class="text-xl font-bold text-black-900 mb-2">
          {{ selectedItem.opportunity_title }}
        </h3>
        <p
          class="text-xs font-semibold text-blue-600 mb-4 flex items-center gap-1"
        >
          📁 {{ selectedItem.project_name || selectedItem.project }}
        </p>

        <div
          class="space-y-3 text-sm text-black-600 bg-black-50/80 p-4 rounded-2xl mb-6"
        >
          <div v-if="selectedItem.location" class="flex justify-between">
            <span class="font-medium text-black-500">Location:</span>
            <span class="font-bold text-black-800">{{
              selectedItem.location
            }}</span>
          </div>
          <div class="flex justify-between">
            <span class="font-medium text-black-500">Role:</span>
            <span class="font-bold text-black-800">{{
              selectedItem.role || "Volunteer"
            }}</span>
          </div>
          <div class="flex justify-between">
            <span class="font-medium text-black-500">Duration:</span>
            <span class="font-bold text-black-800">
              {{ formatDate(selectedItem.from_date) }} –
              {{ formatDate(selectedItem.to_date) }}
            </span>
          </div>
          <div class="flex justify-between">
            <span class="font-medium text-black-500">Hours Completed:</span>
            <span class="font-bold text-emerald-800"
              >{{ Number(selectedItem.hours_done || 0).toFixed(1) }} hrs</span
            >
          </div>
        </div>

        <div class="flex justify-end">
          <button
            @click="selectedItem = null"
            class="px-5 py-2.5 bg-[#064e3b] text-white rounded-xl font-bold text-sm hover:bg-[#043226]"
          >
            Close
          </button>
        </div>
      </div>
    </div>

    <!-- Certificate Modal -->
    <div
      v-if="certItem"
      class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/60 backdrop-blur-sm animate-fade-in"
    >
      <div
        class="bg-white rounded-3xl max-w-2xl w-full p-8 shadow-2xl relative border-8 border-emerald-900/10 text-center"
      >
        <button
          @click="certItem = null"
          class="absolute top-5 right-5 text-black-400 hover:text-black-600 p-1.5 rounded-full hover:bg-black-100"
        >
          <svg
            class="w-5 h-5"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            stroke-width="2"
          >
            <line x1="18" y1="6" x2="6" y2="18"></line>
            <line x1="6" y1="6" x2="18" y2="18"></line>
          </svg>
        </button>

        <div
          class="w-16 h-16 bg-emerald-50 text-emerald-700 rounded-full flex items-center justify-center mx-auto mb-3"
        >
          <svg
            class="w-8 h-8"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            stroke-width="2"
          >
            <circle cx="12" cy="8" r="7"></circle>
            <polyline
              points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"
            ></polyline>
          </svg>
        </div>

        <h4
          class="text-xs uppercase tracking-widest font-black text-emerald-800 mb-1"
        >
          Volunteer Recognition
        </h4>
        <h2 class="text-2xl font-serif font-black text-black-900 mb-2">
          Certificate of Completion
        </h2>
        <p class="text-xs text-black-500 mb-6">
          This certificate is awarded in recognition of dedicated volunteer
          service.
        </p>

        <div
          class="bg-emerald-50/50 p-6 rounded-2xl border border-emerald-100/80 mb-6"
        >
          <p class="text-xs text-black-500 max-w-md mx-auto">
            for successfully completing assignment on
            <span class="font-bold text-black-800"
              >"{{ certItem.opportunity_title }}"</span
            >
            under
            <span class="font-bold text-black-800">{{
              certItem.project_name || certItem.project
            }}</span
            >.
          </p>
        </div>

        <div class="flex justify-center gap-3">
          <button
            @click="certItem = null"
            class="px-5 py-2.5 bg-[#064e3b] text-white rounded-xl font-bold text-sm hover:bg-[#043226]"
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

const activeFilter = ref("all")
const sortBy = ref("newest")
const selectedItem = ref(null)
const certItem = ref(null)

// Real backend resource for assignments
const assignmentsResource = createResource({
	url: "ngo.api.volunteer.my_assignments",
	method: "GET",
	auto: true,
})

// Unified assignments list strictly based on real API data
const assignmentsList = computed(() => {
	if (assignmentsResource.data && Array.isArray(assignmentsResource.data)) {
		return assignmentsResource.data.map((item) => {
			const hoursDone = Number(item.hours_done) || 0
			const isCompleted = item.status === "Completed"
			return {
				...item,
				progress_pct: isCompleted
					? 100
					: hoursDone > 0
						? Math.min(100, Math.round((hoursDone / 20) * 100))
						: 0,
				hours_done: hoursDone,
				tags: Array.isArray(item.skills) ? item.skills : [],
				image: item.image || volunteerTutoring,
			}
		})
	}
	return []
})

// Filter tabs with dynamic counts strictly from real assignments
const filterTabs = computed(() => {
	const all = assignmentsList.value
	return [
		{ id: "all", label: "All", count: all.length },
		{
			id: "Assigned",
			label: "Assigned",
			count: all.filter(
				(a) => a.status === "Assigned" || a.status === "Upcoming",
			).length,
		},
		{
			id: "Active",
			label: "Active",
			count: all.filter((a) => a.status === "Active").length,
		},
		{
			id: "Completed",
			label: "Completed",
			count: all.filter((a) => a.status === "Completed").length,
		},
		{
			id: "Withdrawn",
			label: "Withdrawn",
			count: all.filter(
				(a) => a.status === "Withdrawn" || a.status === "Cancelled",
			).length,
		},
	]
})

// Stats totals for top cards strictly from real data
const totalStats = computed(() => {
	const all = assignmentsList.value
	const active = all.filter((a) => a.status === "Active").length
	const completed = all.filter((a) => a.status === "Completed").length
	const withdrawn = all.filter(
		(a) => a.status === "Withdrawn" || a.status === "Cancelled",
	).length
	const hours = all.reduce(
		(acc, curr) => acc + (Number(curr.hours_done) || 0),
		0,
	)
	return {
		total: all.length,
		active,
		completed,
		withdrawn,
		hours: hours,
	}
})

// Filtered assignments
const filteredAssignments = computed(() => {
	let list = [...assignmentsList.value]
	if (activeFilter.value !== "all") {
		if (activeFilter.value === "Withdrawn") {
			list = list.filter(
				(a) => a.status === "Withdrawn" || a.status === "Cancelled",
			)
		} else if (activeFilter.value === "Assigned") {
			list = list.filter(
				(a) => a.status === "Assigned" || a.status === "Upcoming",
			)
		} else {
			list = list.filter((a) => a.status === activeFilter.value)
		}
	}

	if (sortBy.value === "oldest") {
		list.sort((a, b) => new Date(a.from_date || 0) - new Date(b.from_date || 0))
	} else {
		list.sort((a, b) => new Date(b.from_date || 0) - new Date(a.from_date || 0))
	}

	return list
})

function getStatusBadgeClass(status) {
	if (status === "Assigned" || status === "Upcoming")
		return "bg-blue-100 text-blue-800 border border-blue-200"
	if (status === "Active")
		return "bg-emerald-100 text-emerald-800 border border-emerald-200"
	if (status === "Completed")
		return "bg-purple-100 text-purple-800 border border-purple-200"
	if (status === "Withdrawn" || status === "Cancelled")
		return "bg-rose-100 text-rose-800 border border-rose-200"
	return "bg-black-100 text-black-700"
}

function formatDate(dateStr) {
	if (!dateStr) return "Ongoing"
	const d = new Date(dateStr)
	return d.toLocaleDateString("en-US", {
		month: "short",
		day: "numeric",
		year: "numeric",
	})
}

function openDetailsModal(item) {
	selectedItem.value = item
}

function openCertificateModal(item) {
	certItem.value = item
}
</script>
