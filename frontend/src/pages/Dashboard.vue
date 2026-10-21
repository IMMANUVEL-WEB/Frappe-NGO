<template>
  <VolunteerLayout>
    <div class="space-y-6">
      <!-- Top Welcome Bar -->
      <div
        class="flex flex-col md:flex-row md:items-center justify-between gap-2"
      >
        <div>
          <h1
            class="text-2xl md:text-3xl font-extrabold text-gray-900 tracking-tight flex items-center gap-2"
          >
            Welcome back{{ userName ? ", " + userName : "" }}!
            <span class="inline-block animate-wave origin-[70%_70%]">👋</span>
          </h1>
          <p class="text-xs md:text-sm text-gray-500 font-normal mt-0.5">
            Your time makes a difference in the community.
          </p>
        </div>

        <div class="hidden md:block text-right">
          <p class="text-xs md:text-sm font-semibold text-gray-700">
            {{ currentDate }}
          </p>
          <p class="text-xs italic text-gray-400 mt-0.5 font-serif">
            "People helping people creates a stronger tomorrow."
          </p>
        </div>
      </div>

      <!-- Hero Mission Banner -->
      <div
        class="relative overflow-hidden rounded-2xl bg-[#032e23] text-white shadow-md border border-emerald-900/30"
      >
        <div class="flex flex-col lg:flex-row items-stretch min-h-[220px]">
          <!-- Banner Text & CTAs (Left ~60%) -->
          <div
            class="p-6 md:p-8 lg:p-9 flex-1 flex flex-col justify-between z-10 space-y-4"
          >
            <div class="space-y-2.5">
              <!-- Our Mission Badge -->
              <span
                class="inline-flex items-center px-2.5 py-1 rounded-md text-[10px] font-bold tracking-widest uppercase bg-emerald-900/80 text-emerald-300 border border-emerald-500/30"
              >
                OUR MISSION
              </span>

              <h2
                class="text-2xl md:text-3xl font-extrabold text-white tracking-tight leading-tight"
              >
                Together, we create lasting impact.
              </h2>

              <p
                class="text-xs md:text-sm text-emerald-100/85 max-w-xl leading-relaxed"
              >
                Join hands in building stronger, healthier and more inclusive
                communities through education, environment, and humanitarian
                support.
              </p>
            </div>

            <!-- Action Buttons -->
            <div class="flex flex-wrap items-center gap-3 pt-1">
              <router-link
                to="/opportunities"
                class="inline-flex items-center gap-2 px-5 py-2.5 bg-[#d97706] hover:bg-[#b45309] text-white text-xs md:text-sm font-semibold rounded-xl shadow-sm transition-all duration-200 hover:shadow-md"
              >
                <!-- Binoculars icon -->
                <svg
                  width="17"
                  height="17"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  stroke-width="2"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                >
                  <path d="M10 10m-7 0a7 7 0 1 0 14 0a7 7 0 1 0 -14 0"></path>
                  <path d="M21 21l-6 -6"></path>
                </svg>
                Browse Opportunities →
              </router-link>

              <router-link
                to="/shifts"
                class="inline-flex items-center gap-2 px-5 py-2.5 bg-emerald-950/40 hover:bg-emerald-900/60 border border-emerald-500/40 text-white text-xs md:text-sm font-semibold rounded-xl transition-all duration-200"
              >
                <svg
                  width="16"
                  height="16"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  stroke-width="2"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                >
                  <rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect>
                  <line x1="16" y1="2" x2="16" y2="6"></line>
                  <line x1="8" y1="2" x2="8" y2="6"></line>
                  <line x1="3" y1="10" x2="21" y2="10"></line>
                </svg>
                View My Schedule
              </router-link>
            </div>
          </div>

          <!-- Banner Right Side (Photo + Script Calligraphy) -->
          <div
            class="relative lg:w-5/12 overflow-hidden flex items-center justify-end min-h-[200px] lg:min-h-full"
          >
            <!-- Cursive Floating Watermark -->
            <div
              class="absolute left-4 lg:left-2 bottom-6 z-20 pointer-events-none transform -rotate-6 select-none"
            >
              <span
                class="font-script text-2xl md:text-3xl text-white/95 drop-shadow-[0_2px_6px_rgba(0,0,0,0.6)] whitespace-nowrap"
              >
                Communities Thrive Together
              </span>
            </div>

            <!-- Soft Edge Mask -->
            <img
              src="/volunteers_planting.jpg"
              alt="Volunteers planting saplings"
              class="w-full h-full object-cover object-center min-h-[200px] [mask-image:linear-gradient(to_right,transparent_0%,black_18%)] [-webkit-mask-image:linear-gradient(to_right,transparent_0%,black_18%)]"
            />
          </div>
        </div>
      </div>

      <!-- 3 Key Metric Cards (Evenly Spaced Across the Row) -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-5 md:gap-6">
        <!-- Card 1: Total Impact -->
        <div
          class="bg-white rounded-2xl p-5 border border-gray-100/90 shadow-sm hover:shadow-md transition-all flex flex-col justify-between"
        >
          <div class="flex items-start justify-between">
            <div
              class="w-10 h-10 rounded-xl bg-emerald-50 text-emerald-600 flex items-center justify-center flex-shrink-0"
            >
              <svg
                width="20"
                height="20"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
                stroke-linecap="round"
                stroke-linejoin="round"
              >
                <circle cx="12" cy="12" r="10"></circle>
                <polyline points="12 6 12 12 16 14"></polyline>
              </svg>
            </div>
            <div class="text-right">
              <p
                class="text-[11px] uppercase tracking-wider font-bold text-gray-500"
              >
                Total Impact
              </p>
              <svg
                class="text-gray-300 ml-auto mt-1"
                width="14"
                height="14"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
              >
                <path d="M18 20V10M12 20V4M6 20v-6"></path>
              </svg>
            </div>
          </div>

          <div class="my-3">
            <div
              class="text-2xl md:text-3xl font-black text-gray-900 tracking-tight"
            >
              {{ metrics.total_hours }} hrs
            </div>
          </div>

          <div class="flex items-center justify-between text-xs">
            <span
              class="inline-flex items-center gap-1 font-semibold text-emerald-600"
            >
              <svg
                width="12"
                height="12"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2.5"
              >
                <polyline points="23 6 13.5 15.5 8.5 10.5 1 18"></polyline>
                <polyline points="17 6 23 6 23 12"></polyline>
              </svg>
              Verified Hours
            </span>
            <!-- Mini Sparkline in Green -->
            <svg
              class="w-16 h-5 text-emerald-500"
              viewBox="0 0 60 20"
              fill="none"
            >
              <path
                d="M2,18 Q15,16 25,10 T45,12 T58,3"
                stroke="currentColor"
                stroke-width="2"
                stroke-linecap="round"
                fill="none"
              />
            </svg>
          </div>
        </div>

        <!-- Card 2: This Month -->
        <div
          class="bg-white rounded-2xl p-5 border border-gray-100/90 shadow-sm hover:shadow-md transition-all flex flex-col justify-between"
        >
          <div class="flex items-start justify-between">
            <div
              class="w-10 h-10 rounded-xl bg-amber-50 text-amber-600 flex items-center justify-center flex-shrink-0"
            >
              <svg
                width="20"
                height="20"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
                stroke-linecap="round"
                stroke-linejoin="round"
              >
                <rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect>
                <line x1="16" y1="2" x2="16" y2="6"></line>
                <line x1="8" y1="2" x2="8" y2="6"></line>
                <line x1="3" y1="10" x2="21" y2="10"></line>
              </svg>
            </div>
            <div class="text-right">
              <p
                class="text-[11px] uppercase tracking-wider font-bold text-gray-500"
              >
                This Month
              </p>
              <svg
                class="text-gray-300 ml-auto mt-1"
                width="14"
                height="14"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
              >
                <path d="M18 20V10M12 20V4M6 20v-6"></path>
              </svg>
            </div>
          </div>

          <div class="my-3">
            <div
              class="text-2xl md:text-3xl font-black text-gray-900 tracking-tight"
            >
              {{ metrics.hours_this_month }} hrs
            </div>
          </div>

          <div class="flex items-center justify-between text-xs">
            <span
              class="inline-flex items-center gap-1 font-semibold text-amber-600"
            >
              <svg
                width="12"
                height="12"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2.5"
              >
                <polyline points="23 6 13.5 15.5 8.5 10.5 1 18"></polyline>
                <polyline points="17 6 23 6 23 12"></polyline>
              </svg>
              Current Period
            </span>
            <!-- Mini Sparkline in Amber -->
            <svg
              class="w-16 h-5 text-amber-500"
              viewBox="0 0 60 20"
              fill="none"
            >
              <path
                d="M2,16 Q18,17 30,11 T45,8 T58,4"
                stroke="currentColor"
                stroke-width="2"
                stroke-linecap="round"
                fill="none"
              />
            </svg>
          </div>
        </div>

        <!-- Card 3: Active Assignments -->
        <div
          class="bg-white rounded-2xl p-5 border border-gray-100/90 shadow-sm hover:shadow-md transition-all flex flex-col justify-between"
        >
          <div class="flex items-start justify-between">
            <div
              class="w-10 h-10 rounded-xl bg-purple-50 text-purple-600 flex items-center justify-center flex-shrink-0"
            >
              <svg
                width="20"
                height="20"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
                stroke-linecap="round"
                stroke-linejoin="round"
              >
                <path
                  d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"
                ></path>
                <polyline points="14 2 14 8 20 8"></polyline>
                <line x1="16" y1="13" x2="8" y2="13"></line>
                <line x1="16" y1="17" x2="8" y2="17"></line>
              </svg>
            </div>
            <div class="text-right">
              <p
                class="text-[11px] uppercase tracking-wider font-bold text-gray-500"
              >
                Active Assignments
              </p>
              <svg
                class="text-purple-400 ml-auto mt-1"
                width="16"
                height="16"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
              >
                <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path>
                <circle cx="9" cy="7" r="4"></circle>
                <path d="M23 21v-2a4 4 0 0 0-3-3.87"></path>
                <path d="M16 3.13a4 4 0 0 1 0 7.75"></path>
              </svg>
            </div>
          </div>

          <div class="my-3">
            <div
              class="text-2xl md:text-3xl font-black text-gray-900 tracking-tight"
            >
              {{ metrics.active_assignments }}
              {{ metrics.active_assignments === 1 ? "campaign" : "campaigns" }}
            </div>
          </div>

          <p class="text-xs text-gray-400 font-medium">
            {{
              metrics.active_assignments > 0
                ? `You are assigned to ${
                    metrics.active_assignments
                  } active campaign${
                    metrics.active_assignments > 1 ? "s" : ""
                  }.`
                : "No active assignments yet."
            }}
          </p>
        </div>
      </div>

      <!-- Middle Two-Column Section -->
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-6">
        <!-- Left Column: Next Upcoming Shift (7 Cols) -->
        <div
          class="lg:col-span-7 bg-white rounded-2xl p-6 border border-gray-100 shadow-sm flex flex-col justify-between"
        >
          <!-- Header -->
          <div
            class="flex items-center justify-between pb-4 border-b border-gray-100/80"
          >
            <h3
              class="text-base md:text-lg font-bold text-gray-900 flex items-center gap-2.5"
            >
              <svg
                class="text-emerald-700"
                width="19"
                height="19"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
                stroke-linecap="round"
                stroke-linejoin="round"
              >
                <rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect>
                <line x1="16" y1="2" x2="16" y2="6"></line>
                <line x1="8" y1="2" x2="8" y2="6"></line>
                <line x1="3" y1="10" x2="21" y2="10"></line>
              </svg>
              Next Upcoming Shift
            </h3>
            <router-link
              to="/shifts"
              class="text-xs font-semibold text-emerald-700 hover:text-emerald-800 transition-colors"
            >
              View All Shifts →
            </router-link>
          </div>

          <!-- Shift Card Content -->
          <div
            v-if="nextShift"
            class="grid grid-cols-1 md:grid-cols-12 gap-5 mt-5 items-center"
          >
            <!-- Classroom Tutoring Image (5 cols) -->
            <div
              class="md:col-span-5 h-44 rounded-xl overflow-hidden shadow-sm border border-gray-100 relative group"
            >
              <img
                src="/volunteer_tutoring.jpg"
                alt="Volunteer tutoring children"
                class="w-full h-full object-cover object-center group-hover:scale-105 transition-transform duration-300"
              />
            </div>

            <!-- Shift Details (7 cols) -->
            <div class="md:col-span-7 space-y-3">
              <!-- Status Pill -->
              <span
                class="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full text-xs font-semibold bg-emerald-50 text-emerald-700 border border-emerald-200"
              >
                <span class="w-1.5 h-1.5 rounded-full bg-emerald-600"></span>
                Confirmed
              </span>

              <h4 class="text-base font-extrabold text-gray-950 leading-snug">
                {{ nextShift.opportunity_title }}
              </h4>

              <!-- Meta List -->
              <div class="space-y-1.5 text-xs text-gray-600 font-medium">
                <div
                  v-if="nextShift.date_label"
                  class="flex items-center gap-2"
                >
                  <svg
                    class="text-gray-400 flex-shrink-0"
                    width="14"
                    height="14"
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
                  <span>{{ nextShift.date_label }}</span>
                </div>

                <div
                  v-if="nextShift.time_label"
                  class="flex items-center gap-2"
                >
                  <svg
                    class="text-gray-400 flex-shrink-0"
                    width="14"
                    height="14"
                    viewBox="0 0 24 24"
                    fill="none"
                    stroke="currentColor"
                    stroke-width="2"
                  >
                    <circle cx="12" cy="12" r="10"></circle>
                    <polyline points="12 6 12 12 16 14"></polyline>
                  </svg>
                  <span>{{ nextShift.time_label }}</span>
                </div>

                <div v-if="nextShift.location" class="flex items-center gap-2">
                  <svg
                    class="text-gray-400 flex-shrink-0"
                    width="14"
                    height="14"
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
                  <span>{{ nextShift.location }}</span>
                </div>

                <div v-if="nextShift.project" class="flex items-center gap-2">
                  <svg
                    class="text-gray-400 flex-shrink-0"
                    width="14"
                    height="14"
                    viewBox="0 0 24 24"
                    fill="none"
                    stroke="currentColor"
                    stroke-width="2"
                  >
                    <path d="M22 10v6M2 10l10-5 10 5-10 5z"></path>
                    <path d="M6 12v5c3 3 9 3 12 0v-5"></path>
                  </svg>
                  <span>{{ nextShift.project }}</span>
                </div>
              </div>

              <!-- View Shift Details CTA Button -->
              <div class="pt-1">
                <router-link
                  to="/shifts"
                  class="inline-flex items-center justify-center gap-1.5 px-4 py-2 bg-[#d97706] hover:bg-[#b45309] text-white text-xs font-semibold rounded-xl shadow-sm transition-all"
                >
                  View Shift Details →
                </router-link>
              </div>
            </div>
          </div>

          <!-- Empty State when no upcoming shifts -->
          <div
            v-else
            class="flex flex-col items-center justify-center p-8 my-auto text-center"
          >
            <div
              class="w-12 h-12 rounded-2xl bg-emerald-50 text-emerald-700 flex items-center justify-center mb-3"
            >
              <svg
                width="24"
                height="24"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
                stroke-linecap="round"
                stroke-linejoin="round"
              >
                <rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect>
                <line x1="16" y1="2" x2="16" y2="6"></line>
                <line x1="8" y1="2" x2="8" y2="6"></line>
                <line x1="3" y1="10" x2="21" y2="10"></line>
              </svg>
            </div>
            <h4 class="text-sm font-bold text-gray-800">
              No upcoming shifts scheduled
            </h4>
            <p class="text-xs text-gray-500 max-w-sm mt-1">
              Explore open volunteer opportunities to register for your next
              shift.
            </p>
            <router-link
              to="/opportunities"
              class="mt-4 inline-flex items-center gap-1.5 px-4 py-2 bg-emerald-800 hover:bg-emerald-900 text-black text-xs font-semibold rounded-xl transition-all shadow-sm"
            >
              Browse Opportunities →
            </router-link>
          </div>
        </div>

        <!-- Right Column: 2 Stacked Cards (5 Cols) -->
        <div class="lg:col-span-5 space-y-6">
          <!-- Card 1: Annual Impact Goal -->
          <div
            class="bg-white rounded-2xl p-6 border border-gray-100 shadow-sm"
          >
            <div
              class="flex items-center justify-between pb-3 border-b border-gray-100/80"
            >
              <h3
                class="text-sm md:text-base font-bold text-gray-900 flex items-center gap-2"
              >
                <svg
                  class="text-emerald-700"
                  width="18"
                  height="18"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  stroke-width="2"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                >
                  <circle cx="12" cy="12" r="10"></circle>
                  <circle cx="12" cy="6" r="6"></circle>
                  <circle cx="12" cy="2" r="2"></circle>
                </svg>
                Annual Impact Goal
              </h3>
              <router-link
                to="/attendance"
                class="text-xs font-semibold text-emerald-700 hover:text-emerald-800"
              >
                View Progress →
              </router-link>
            </div>

            <div class="flex items-center gap-5 mt-4">
              <!-- Circular Progress Gauge -->
              <div
                class="relative w-20 h-20 flex-shrink-0 flex items-center justify-center"
              >
                <svg class="w-full h-full -rotate-90" viewBox="0 0 36 36">
                  <!-- Background Trail -->
                  <path
                    class="text-gray-100"
                    stroke-width="3.5"
                    stroke="currentColor"
                    fill="none"
                    d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831"
                  />
                  <!-- Active Ring -->
                  <path
                    class="text-emerald-600 transition-all duration-500"
                    :stroke-dasharray="`${goalPercentage}, 100`"
                    stroke-width="3.5"
                    stroke-linecap="round"
                    stroke="currentColor"
                    fill="none"
                    d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831"
                  />
                </svg>
                <div class="absolute inset-0 flex items-center justify-center">
                  <span class="text-base font-black text-gray-900"
                    >{{ goalPercentage }}%</span
                  >
                </div>
              </div>

              <!-- Gauge Details -->
              <div class="flex-1 space-y-1.5 min-w-0">
                <div class="text-base font-black text-gray-900 leading-tight">
                  {{ metrics.total_hours }} of {{ targetGoalHours }} hours
                </div>
                <p class="text-xs text-gray-500 font-medium">
                  Next milestone: {{ targetGoalHours }} hours
                </p>

                <!-- Linear Progress -->
                <div
                  class="w-full bg-gray-100 rounded-full h-2 overflow-hidden"
                >
                  <div
                    class="bg-emerald-600 h-2 rounded-full transition-all duration-500"
                    :style="{ width: `${goalPercentage}%` }"
                  ></div>
                </div>

                <div class="pt-0.5">
                  <span
                    class="inline-flex items-center gap-1.5 text-[11px] font-semibold text-emerald-800 bg-emerald-50 px-2.5 py-0.5 rounded-lg border border-emerald-200/60"
                  >
                    {{
                      goalPercentage > 0
                        ? "🌱 You're on track! Keep going!"
                        : "🌱 Complete shifts to reach your goal!"
                    }}
                  </span>
                </div>
              </div>
            </div>
          </div>

          <!-- Card 2: Volunteer Resources -->
          <div
            class="bg-white rounded-2xl p-6 border border-gray-100 shadow-sm"
          >
            <div
              class="flex items-center justify-between pb-3 border-b border-gray-100/80"
            >
              <h3
                class="text-sm md:text-base font-bold text-gray-900 flex items-center gap-2"
              >
                <svg
                  class="text-emerald-700"
                  width="18"
                  height="18"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  stroke-width="2"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                >
                  <path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path>
                  <path
                    d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"
                  ></path>
                </svg>
                Volunteer Resources
              </h3>
              <router-link
                to="/profile"
                class="text-xs font-semibold text-emerald-700 hover:text-emerald-800"
              >
                View All →
              </router-link>
            </div>

            <div class="space-y-3 mt-4">
              <!-- Resource Item 1 -->
              <router-link
                to="/profile"
                class="flex items-center justify-between p-3 rounded-xl hover:bg-gray-50 border border-gray-100 transition-all group"
              >
                <div class="flex items-center gap-3">
                  <div
                    class="w-9 h-9 rounded-lg bg-amber-50 text-amber-600 flex items-center justify-center flex-shrink-0"
                  >
                    <svg
                      width="18"
                      height="18"
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
                  <div>
                    <h5
                      class="text-xs font-bold text-gray-900 group-hover:text-emerald-800 transition-colors"
                    >
                      Guidelines & Handbook
                    </h5>
                    <p class="text-[11px] text-gray-500 font-medium">
                      Learn about policies and best practices
                    </p>
                  </div>
                </div>
                <svg
                  class="text-gray-400 group-hover:text-gray-600 group-hover:translate-x-0.5 transition-all"
                  width="14"
                  height="14"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  stroke-width="2.5"
                >
                  <polyline points="9 18 15 12 9 6"></polyline>
                </svg>
              </router-link>

              <!-- Resource Item 2 -->
              <router-link
                to="/opportunities"
                class="flex items-center justify-between p-3 rounded-xl hover:bg-gray-50 border border-gray-100 transition-all group"
              >
                <div class="flex items-center gap-3">
                  <div
                    class="w-9 h-9 rounded-lg bg-teal-50 text-teal-600 flex items-center justify-center flex-shrink-0"
                  >
                    <svg
                      width="18"
                      height="18"
                      viewBox="0 0 24 24"
                      fill="none"
                      stroke="currentColor"
                      stroke-width="2"
                    >
                      <path
                        d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"
                      ></path>
                      <circle cx="9" cy="7" r="4"></circle>
                      <path d="M23 21v-2a4 4 0 0 0-3-3.87"></path>
                      <path d="M16 3.13a4 4 0 0 1 0 7.75"></path>
                    </svg>
                  </div>
                  <div>
                    <h5
                      class="text-xs font-bold text-gray-900 group-hover:text-emerald-800 transition-colors"
                    >
                      Training Materials
                    </h5>
                    <p class="text-[11px] text-gray-500 font-medium">
                      Build your skills as a volunteer
                    </p>
                  </div>
                </div>
                <svg
                  class="text-gray-400 group-hover:text-gray-600 group-hover:translate-x-0.5 transition-all"
                  width="14"
                  height="14"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  stroke-width="2.5"
                >
                  <polyline points="9 18 15 12 9 6"></polyline>
                </svg>
              </router-link>
            </div>
          </div>
        </div>
      </div>

      <!-- Bottom Section: Recent Attendance Table -->
      <div
        class="bg-white rounded-2xl p-6 border border-gray-100 shadow-sm overflow-hidden"
      >
        <!-- Table Header -->
        <div
          class="flex items-center justify-between pb-4 border-b border-gray-100/80 mb-2"
        >
          <h3
            class="text-base md:text-lg font-bold text-gray-900 flex items-center gap-2.5"
          >
            <svg
              class="text-emerald-700"
              width="19"
              height="19"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              stroke-width="2"
              stroke-linecap="round"
              stroke-linejoin="round"
            >
              <circle cx="12" cy="12" r="10"></circle>
              <polyline points="12 6 12 12 16 14"></polyline>
            </svg>
            Recent Attendance
          </h3>
          <router-link
            to="/attendance"
            class="text-xs font-semibold text-emerald-700 hover:text-emerald-800 transition-colors"
          >
            View All Attendance →
          </router-link>
        </div>

        <!-- Attendance Data Table -->
        <div class="overflow-x-auto">
          <table class="w-full text-left text-xs">
            <thead>
              <tr
                class="text-[11px] uppercase tracking-wider text-gray-400 font-bold border-b border-gray-100"
              >
                <th class="py-3 px-3 w-10">#</th>
                <th class="py-3 px-3">Activity / Assignment</th>
                <th class="py-3 px-3">Date</th>
                <th class="py-3 px-3">Hours</th>
                <th class="py-3 px-3">Location</th>
                <th class="py-3 px-3">Status</th>
                <th class="py-3 px-3 text-right w-10"></th>
              </tr>
            </thead>
            <tbody
              v-if="attendanceRows && attendanceRows.length > 0"
              class="divide-y divide-gray-50"
            >
              <tr
                v-for="(row, idx) in attendanceRows"
                :key="idx"
                class="hover:bg-gray-50/70 transition-colors group"
              >
                <!-- # -->
                <td class="py-3.5 px-3 font-semibold text-gray-400">
                  {{ idx + 1 }}
                </td>

                <!-- Activity / Assignment -->
                <td class="py-3.5 px-3 font-semibold text-gray-900">
                  {{ row.activity }}
                </td>

                <!-- Date -->
                <td class="py-3.5 px-3 text-gray-600">
                  {{ formatDate(row.date) }}
                </td>

                <!-- Hours -->
                <td class="py-3.5 px-3 font-semibold text-gray-800">
                  {{ row.hours }}
                </td>

                <!-- Location -->
                <td class="py-3.5 px-3 text-gray-600">
                  {{ row.location || "-" }}
                </td>

                <!-- Status Badge -->
                <td class="py-3.5 px-3">
                  <span
                    v-if="row.status === 'Approved'"
                    class="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full text-[11px] font-semibold bg-emerald-50 text-emerald-700 border border-emerald-200"
                  >
                    <svg
                      width="10"
                      height="10"
                      viewBox="0 0 24 24"
                      fill="none"
                      stroke="currentColor"
                      stroke-width="3.5"
                    >
                      <polyline points="20 6 9 17 4 12"></polyline>
                    </svg>
                    Approved
                  </span>
                  <span
                    v-else
                    class="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full text-[11px] font-semibold bg-amber-50 text-amber-700 border border-amber-200"
                  >
                    <span class="w-1.5 h-1.5 rounded-full bg-amber-500"></span>
                    {{ row.status || "In Review" }}
                  </span>
                </td>

                <!-- Action Menu -->
                <td class="py-3.5 px-3 text-right">
                  <router-link
                    to="/attendance"
                    class="text-gray-400 hover:text-emerald-700 p-1 rounded-md hover:bg-gray-100 transition-colors inline-block"
                  >
                    <svg
                      width="14"
                      height="14"
                      viewBox="0 0 24 24"
                      fill="none"
                      stroke="currentColor"
                      stroke-width="2"
                    >
                      <polyline points="9 18 15 12 9 6"></polyline>
                    </svg>
                  </router-link>
                </td>
              </tr>
            </tbody>

            <!-- Empty Attendance State -->
            <tbody v-else>
              <tr>
                <td colspan="7" class="py-10 text-center text-gray-400">
                  <p class="font-medium text-xs text-gray-500">
                    No attendance records found yet
                  </p>
                  <p class="text-[11px] text-gray-400 mt-1">
                    Your approved shifts and logged volunteer hours will appear
                    here once submitted.
                  </p>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </VolunteerLayout>
</template>

<script setup>
import { ref, computed, onMounted } from "vue";
import VolunteerLayout from "../components/VolunteerLayout.vue";

const userName = ref("");
const currentDate = ref("");
const targetGoalHours = ref(100);

const metrics = ref({
  total_hours: 0,
  hours_this_month: 0,
  active_assignments: 0,
});

const nextShift = ref(null);
const attendanceRows = ref([]);

const goalPercentage = computed(() => {
  const hrs = Number(metrics.value.total_hours) || 0;
  const target = Number(targetGoalHours.value) || 100;
  return Math.min(100, Math.round((hrs / target) * 100));
});

function formatDate(dateStr) {
  if (!dateStr || dateStr === "-") return "-";
  try {
    return new Date(dateStr).toLocaleDateString("en-US", {
      month: "short",
      day: "numeric",
      year: "numeric",
    });
  } catch (e) {
    return dateStr;
  }
}

onMounted(async () => {
  // Current Date
  try {
    const now = new Date();
    currentDate.value = now.toLocaleDateString("en-US", {
      weekday: "long",
      year: "numeric",
      month: "long",
      day: "numeric",
    });
  } catch (e) {}

  // Fetch Real Dashboard Data for Current Volunteer
  try {
    const res = await fetch("/api/method/ngo.api.volunteer.my_dashboard");
    const json = await res.json();
    if (json.message) {
      const d = json.message;

      // User Name
      if (d.first_name || d.volunteer_name) {
        userName.value = d.first_name || d.volunteer_name;
      }

      // Real Metrics
      metrics.value.total_hours = d.total_hours ?? 0;
      metrics.value.hours_this_month = d.hours_this_month ?? 0;
      metrics.value.active_assignments = d.active_assignments ?? 0;

      if (d.annual_goal) {
        targetGoalHours.value = d.annual_goal;
      }

      // Real Next Shift
      if (d.next_shift && d.next_shift.opportunity_title) {
        const s = d.next_shift;
        let dateLabel = "";
        if (s.date) {
          try {
            dateLabel = new Date(s.date).toLocaleDateString("en-US", {
              weekday: "short",
              month: "short",
              day: "numeric",
              year: "numeric",
            });
          } catch (e) {
            dateLabel = s.date;
          }
        }

        let timeLabel = "";
        if (s.start_time && s.end_time) {
          const st = s.start_time.slice(0, 5);
          const et = s.end_time.slice(0, 5);
          timeLabel = `${st} - ${et}`;
        }

        nextShift.value = {
          opportunity_title: s.opportunity_title,
          date_label: dateLabel,
          time_label: timeLabel,
          location: s.location || "",
          project: s.project || "",
        };
      } else {
        nextShift.value = null;
      }

      // Real Attendance
      if (Array.isArray(d.recent_attendances)) {
        attendanceRows.value = d.recent_attendances;
      }
    }
  } catch (err) {
    console.error("Error fetching volunteer dashboard data:", err);
  }
});
</script>

<style scoped>
@keyframes wave {
  0% {
    transform: rotate(0deg);
  }
  20% {
    transform: rotate(14deg);
  }
  40% {
    transform: rotate(-8deg);
  }
  60% {
    transform: rotate(14deg);
  }
  80% {
    transform: rotate(-4deg);
  }
  100% {
    transform: rotate(10deg);
  }
}
.animate-wave {
  animation: wave 2.2s infinite ease-in-out;
}
</style>
