<template>
  <div class="space-y-6">
    <!-- Top Stat Cards (5 Cards) -->
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-4">
      <!-- 1. Total Projects -->
      <div class="bg-white rounded-2xl p-5 border border-slate-100 shadow-xs flex flex-col justify-between hover:shadow-md transition">
        <div class="flex items-start justify-between">
          <div>
            <span class="text-[11px] font-bold uppercase tracking-wider text-slate-400">Total Projects</span>
            <div class="text-2xl font-black text-slate-900 mt-1 tracking-tight">10</div>
            <div class="text-xs text-slate-400 font-medium mt-1">Active projects under your grants</div>
          </div>
          <div class="w-10 h-10 rounded-xl bg-emerald-50 text-emerald-600 flex items-center justify-center">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"/>
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
            <div class="text-2xl font-black text-slate-900 mt-1 tracking-tight">7</div>
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
            <div class="bg-blue-600 h-1.5 rounded-full w-[70%]"></div>
          </div>
          <span class="text-[10px] font-semibold text-slate-400 ml-2">70%</span>
        </div>
      </div>

      <!-- 3. At Risk -->
      <div class="bg-white rounded-2xl p-5 border border-slate-100 shadow-xs flex flex-col justify-between hover:shadow-md transition">
        <div class="flex items-start justify-between">
          <div>
            <span class="text-[11px] font-bold uppercase tracking-wider text-slate-400">At Risk</span>
            <div class="text-2xl font-black text-slate-900 mt-1 tracking-tight">2</div>
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
            <div class="bg-amber-400 h-1.5 rounded-full w-[20%]"></div>
          </div>
          <span class="text-[10px] font-semibold text-slate-400 ml-2">20%</span>
        </div>
      </div>

      <!-- 4. Delayed -->
      <div class="bg-white rounded-2xl p-5 border border-slate-100 shadow-xs flex flex-col justify-between hover:shadow-md transition">
        <div class="flex items-start justify-between">
          <div>
            <span class="text-[11px] font-bold uppercase tracking-wider text-slate-400">Delayed</span>
            <div class="text-2xl font-black text-slate-900 mt-1 tracking-tight">1</div>
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
            <div class="bg-rose-500 h-1.5 rounded-full w-[10%]"></div>
          </div>
          <span class="text-[10px] font-semibold text-slate-400 ml-2">10%</span>
        </div>
      </div>

      <!-- 5. Completed -->
      <div class="bg-white rounded-2xl p-5 border border-slate-100 shadow-xs flex flex-col justify-between hover:shadow-md transition">
        <div class="flex items-start justify-between">
          <div>
            <span class="text-[11px] font-bold uppercase tracking-wider text-slate-400">Completed</span>
            <div class="text-2xl font-black text-slate-900 mt-1 tracking-tight">0</div>
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
            <div class="bg-purple-500 h-1.5 rounded-full w-0"></div>
          </div>
          <span class="text-[10px] font-semibold text-slate-400 ml-2">0%</span>
        </div>
      </div>
    </div>

    <!-- Middle Section: 3 Cards in a row -->
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-6">
      <!-- Card 1: Project Progress Overview (5 cols) -->
      <div class="lg:col-span-5 bg-white rounded-2xl p-5 border border-slate-100 shadow-xs flex flex-col justify-between">
        <div>
          <div class="flex items-center space-x-2 mb-4">
            <div class="w-2.5 h-2.5 rounded-full bg-emerald-500"></div>
            <h3 class="text-sm font-bold text-slate-900 tracking-tight">Project Progress Overview</h3>
          </div>

          <div class="space-y-4 pt-1">
            <div v-for="item in overviewProjects" :key="item.name" class="space-y-1.5">
              <div class="flex items-center justify-between text-xs">
                <span class="font-medium text-slate-700 truncate pr-2">{{ item.name }}</span>
                <span class="font-bold text-slate-900">{{ item.progress }}%</span>
              </div>
              <!-- Segmented Progress Bar -->
              <div class="w-full bg-slate-100 rounded-full h-2.5 overflow-hidden flex">
                <div 
                  class="h-full bg-emerald-500" 
                  :style="{ width: `${item.completed}%` }"
                ></div>
                <div 
                  class="h-full bg-teal-400" 
                  :style="{ width: `${item.inProgress}%` }"
                ></div>
                <div 
                  v-if="item.atRisk"
                  class="h-full bg-amber-400" 
                  :style="{ width: `${item.atRisk}%` }"
                ></div>
                <div 
                  v-if="item.delayed"
                  class="h-full bg-rose-500" 
                  :style="{ width: `${item.delayed}%` }"
                ></div>
              </div>
            </div>
          </div>
        </div>

        <!-- Legend at bottom -->
        <div class="pt-4 mt-4 border-t border-slate-100 flex flex-wrap items-center gap-3 text-[11px] text-slate-500">
          <span class="flex items-center gap-1.5"><span class="w-2 h-2 rounded-full bg-emerald-500"></span> Completed</span>
          <span class="flex items-center gap-1.5"><span class="w-2 h-2 rounded-full bg-teal-400"></span> In Progress</span>
          <span class="flex items-center gap-1.5"><span class="w-2 h-2 rounded-full bg-rose-500"></span> Delayed</span>
          <span class="flex items-center gap-1.5"><span class="w-2 h-2 rounded-full bg-amber-400"></span> At Risk</span>
          <span class="flex items-center gap-1.5"><span class="w-2 h-2 rounded-full bg-slate-200"></span> Not Started</span>
        </div>
      </div>

      <!-- Card 2: Project Progress by Sector (3.5 cols) -->
      <div class="lg:col-span-3.5 bg-white rounded-2xl p-5 border border-slate-100 shadow-xs flex flex-col justify-between">
        <div>
          <div class="flex items-center space-x-2 mb-4">
            <div class="w-2.5 h-2.5 rounded-full bg-emerald-500"></div>
            <h3 class="text-sm font-bold text-slate-900 tracking-tight">Project Progress by Sector</h3>
          </div>

          <div class="flex items-center justify-center my-3">
            <!-- Donut -->
            <div class="relative w-32 h-32 flex items-center justify-center">
              <svg class="w-full h-full transform -rotate-90" viewBox="0 0 36 36">
                <circle cx="18" cy="18" r="14" fill="none" stroke="#3B82F6" stroke-width="4.5" stroke-dasharray="30 70" stroke-dashoffset="0" />
                <circle cx="18" cy="18" r="14" fill="none" stroke="#059669" stroke-width="4.5" stroke-dasharray="20 80" stroke-dashoffset="-30" />
                <circle cx="18" cy="18" r="14" fill="none" stroke="#F59E0B" stroke-width="4.5" stroke-dasharray="20 80" stroke-dashoffset="-50" />
                <circle cx="18" cy="18" r="14" fill="none" stroke="#8B5CF6" stroke-width="4.5" stroke-dasharray="10 90" stroke-dashoffset="-70" />
                <circle cx="18" cy="18" r="14" fill="none" stroke="#06B6D4" stroke-width="4.5" stroke-dasharray="10 90" stroke-dashoffset="-80" />
                <circle cx="18" cy="18" r="14" fill="none" stroke="#EF4444" stroke-width="4.5" stroke-dasharray="10 90" stroke-dashoffset="-90" />
              </svg>
              <div class="absolute inset-0 flex flex-col items-center justify-center text-center">
                <span class="text-base font-black text-slate-900 leading-tight">10</span>
                <span class="text-[9px] text-slate-400 font-medium">Projects</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Legend list -->
        <div class="space-y-1.5 text-xs text-slate-600">
          <div class="flex items-center justify-between">
            <span class="flex items-center gap-1.5"><span class="w-2 h-2 rounded-full bg-blue-600"></span> Health</span>
            <span class="font-semibold text-slate-900">3 (30%)</span>
          </div>
          <div class="flex items-center justify-between">
            <span class="flex items-center gap-1.5"><span class="w-2 h-2 rounded-full bg-emerald-600"></span> Education</span>
            <span class="font-semibold text-slate-900">2 (20%)</span>
          </div>
          <div class="flex items-center justify-between">
            <span class="flex items-center gap-1.5"><span class="w-2 h-2 rounded-full bg-amber-500"></span> WASH</span>
            <span class="font-semibold text-slate-900">2 (20%)</span>
          </div>
          <div class="flex items-center justify-between">
            <span class="flex items-center gap-1.5"><span class="w-2 h-2 rounded-full bg-purple-600"></span> Livelihoods</span>
            <span class="font-semibold text-slate-900">1 (10%)</span>
          </div>
          <div class="flex items-center justify-between">
            <span class="flex items-center gap-1.5"><span class="w-2 h-2 rounded-full bg-teal-500"></span> Disaster Relief</span>
            <span class="font-semibold text-slate-900">1 (10%)</span>
          </div>
          <div class="flex items-center justify-between">
            <span class="flex items-center gap-1.5"><span class="w-2 h-2 rounded-full bg-rose-500"></span> Governance</span>
            <span class="font-semibold text-slate-900">1 (10%)</span>
          </div>
        </div>
      </div>

      <!-- Card 3: Project Status (3.5 cols) -->
      <div class="lg:col-span-3.5 bg-white rounded-2xl p-5 border border-slate-100 shadow-xs flex flex-col justify-between">
        <div>
          <div class="flex items-center space-x-2 mb-4">
            <div class="w-2.5 h-2.5 rounded-full bg-emerald-500"></div>
            <h3 class="text-sm font-bold text-slate-900 tracking-tight">Project Status</h3>
          </div>

          <div class="flex items-center gap-4 my-2">
            <!-- Radial Progress Ring -->
            <div class="relative w-28 h-28 flex items-center justify-center shrink-0">
              <svg class="w-full h-full transform -rotate-90" viewBox="0 0 36 36">
                <circle cx="18" cy="18" r="14" fill="none" stroke="#E2E8F0" stroke-width="4.5" />
                <circle cx="18" cy="18" r="14" fill="none" stroke="#00875A" stroke-width="4.5" stroke-dasharray="70 30" stroke-dashoffset="0" stroke-linecap="round" />
              </svg>
              <div class="absolute inset-0 flex flex-col items-center justify-center text-center">
                <span class="text-base font-black text-slate-900 leading-tight">70%</span>
                <span class="text-[9px] text-emerald-600 font-semibold">On Track</span>
              </div>
            </div>

            <!-- Legend Status Counts -->
            <div class="space-y-1.5 flex-1 text-xs">
              <div class="flex items-center justify-between text-slate-600">
                <span class="flex items-center gap-1.5"><span class="w-2 h-2 rounded-full bg-emerald-500"></span> On Track</span>
                <span class="font-semibold text-slate-900">7</span>
              </div>
              <div class="flex items-center justify-between text-slate-600">
                <span class="flex items-center gap-1.5"><span class="w-2 h-2 rounded-full bg-amber-400"></span> At Risk</span>
                <span class="font-semibold text-slate-900">2</span>
              </div>
              <div class="flex items-center justify-between text-slate-600">
                <span class="flex items-center gap-1.5"><span class="w-2 h-2 rounded-full bg-rose-500"></span> Delayed</span>
                <span class="font-semibold text-slate-900">1</span>
              </div>
              <div class="flex items-center justify-between text-slate-600">
                <span class="flex items-center gap-1.5"><span class="w-2 h-2 rounded-full bg-purple-500"></span> Completed</span>
                <span class="font-semibold text-slate-900">0</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Alert Banner Callout -->
        <div class="mt-4 p-3 rounded-xl bg-emerald-50/80 border border-emerald-100/80 flex items-start space-x-2 text-xs text-emerald-900">
          <svg class="w-4 h-4 text-emerald-600 shrink-0 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>
          </svg>
          <span class="font-medium leading-tight">Your projects are making good progress. Keep it up!</span>
        </div>
      </div>
    </div>

    <!-- Bottom Section: Project Progress Details Table -->
    <div class="bg-white rounded-2xl border border-slate-100 shadow-xs overflow-hidden">
      <div class="p-4 border-b border-slate-100 flex flex-col md:flex-row md:items-center justify-between gap-3">
        <div class="flex items-center space-x-2">
          <div class="w-2.5 h-2.5 rounded-full bg-emerald-500"></div>
          <h3 class="text-sm font-bold text-slate-900 tracking-tight">Project Progress Details</h3>
        </div>

        <!-- Filters -->
        <div class="flex flex-wrap items-center gap-2">
          <select v-model="selectedSector" class="px-3 py-1.5 text-xs rounded-xl border border-slate-200 bg-white text-slate-700">
            <option value="">All Sectors</option>
            <option value="WASH">WASH</option>
            <option value="Education">Education</option>
            <option value="Health">Health</option>
            <option value="Livelihoods">Livelihoods</option>
            <option value="Disaster Relief">Disaster Relief</option>
          </select>

          <select v-model="selectedGeography" class="px-3 py-1.5 text-xs rounded-xl border border-slate-200 bg-white text-slate-700">
            <option value="">All Geographies</option>
            <option value="Bihar">Bihar</option>
            <option value="Uttar Pradesh">Uttar Pradesh</option>
            <option value="Tamil Nadu">Tamil Nadu</option>
            <option value="Odisha">Odisha</option>
            <option value="Assam">Assam</option>
          </select>

          <select v-model="selectedStatus" class="px-3 py-1.5 text-xs rounded-xl border border-slate-200 bg-white text-slate-700">
            <option value="">All Status</option>
            <option value="On Track">On Track</option>
            <option value="At Risk">At Risk</option>
            <option value="Delayed">Delayed</option>
          </select>

          <div class="relative">
            <input 
              type="text" 
              v-model="searchQuery" 
              placeholder="Search project by name..." 
              class="pl-8 pr-3 py-1.5 text-xs rounded-xl border border-slate-200 bg-slate-50/50 focus:outline-none focus:ring-2 focus:ring-emerald-500/20"
            />
            <svg class="w-3.5 h-3.5 absolute left-2.5 top-1/2 -translate-y-1/2 text-slate-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/>
            </svg>
          </div>
        </div>
      </div>

      <div class="overflow-x-auto">
        <table class="w-full text-left text-xs">
          <thead class="bg-slate-50/75 border-b border-slate-100 text-[11px] font-bold text-slate-500 uppercase tracking-wider">
            <tr>
              <th class="py-3.5 px-4">#</th>
              <th class="py-3.5 px-4">Project Name</th>
              <th class="py-3.5 px-3">Sector</th>
              <th class="py-3.5 px-3">Geography</th>
              <th class="py-3.5 px-3">Start Date</th>
              <th class="py-3.5 px-3">End Date</th>
              <th class="py-3.5 px-4">Progress</th>
              <th class="py-3.5 px-3">Status</th>
              <th class="py-3.5 px-4 text-right">Actions</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-slate-100 text-slate-700">
            <tr 
              v-for="(proj, idx) in paginatedProjects" 
              :key="proj.code"
              class="hover:bg-slate-50/60 transition group"
            >
              <td class="py-3.5 px-4 text-slate-400 font-medium">{{ (currentPage - 1) * pageSize + idx + 1 }}</td>
              <td class="py-3.5 px-4">
                <div class="flex items-center space-x-3">
                  <!-- Thumbnail Image -->
                  <div class="w-10 h-10 rounded-xl bg-slate-100 overflow-hidden shrink-0 border border-slate-200/80">
                    <img :src="proj.thumbnail" alt="thumbnail" class="w-full h-full object-cover" />
                  </div>
                  <div>
                    <div class="font-semibold text-slate-900">{{ proj.name }}</div>
                    <div class="text-[11px] text-slate-400 font-mono">{{ proj.code }}</div>
                  </div>
                </div>
              </td>
              <td class="py-3.5 px-3">
                <span 
                  class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-[11px] font-medium"
                  :class="getSectorClass(proj.sector)"
                >
                  <component :is="getSectorIcon(proj.sector)" class="w-3 h-3" />
                  {{ proj.sector }}
                </span>
              </td>
              <td class="py-3.5 px-3 text-slate-600">{{ proj.geography }}</td>
              <td class="py-3.5 px-3 text-slate-500 whitespace-nowrap">{{ proj.startDate }}</td>
              <td class="py-3.5 px-3 text-slate-500 whitespace-nowrap">{{ proj.endDate }}</td>
              <td class="py-3.5 px-4">
                <div class="flex items-center space-x-2">
                  <span class="text-xs font-semibold text-slate-700 w-8">{{ proj.progress }}%</span>
                  <div class="w-16 bg-slate-100 rounded-full h-1.5 overflow-hidden">
                    <div 
                      class="h-1.5 rounded-full"
                      :class="proj.status === 'On Track' ? 'bg-emerald-500' : proj.status === 'At Risk' ? 'bg-amber-400' : 'bg-rose-500'"
                      :style="{ width: `${proj.progress}%` }"
                    ></div>
                  </div>
                </div>
              </td>
              <td class="py-3.5 px-3">
                <span 
                  class="inline-block px-2.5 py-0.5 rounded-full text-[11px] font-semibold"
                  :class="{
                    'bg-emerald-50 text-emerald-700 border border-emerald-100': proj.status === 'On Track',
                    'bg-amber-50 text-amber-700 border border-amber-200': proj.status === 'At Risk',
                    'bg-rose-50 text-rose-700 border border-rose-200': proj.status === 'Delayed'
                  }"
                >
                  {{ proj.status }}
                </span>
              </td>
              <td class="py-3.5 px-4 text-right">
                <div class="flex items-center justify-end space-x-2">
                  <button type="button" class="text-xs font-semibold text-slate-700 hover:text-emerald-600 transition">
                    View
                  </button>
                  <button type="button" class="p-1 rounded-lg hover:bg-slate-100 text-slate-400 hover:text-slate-600">
                    <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20">
                      <path d="M10 6a2 2 0 110-4 2 2 0 010 4zM10 12a2 2 0 110-4 2 2 0 010 4zM10 18a2 2 0 110-4 2 2 0 010 4z" />
                    </svg>
                  </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- Pagination -->
      <div class="px-5 py-3.5 border-t border-slate-100 flex items-center justify-between text-xs text-slate-500">
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
  </div>
</template>

<script setup>
import { computed, h, ref } from "vue"

const searchQuery = ref("")
const selectedSector = ref("")
const selectedGeography = ref("")
const selectedStatus = ref("")
const currentPage = ref(1)
const pageSize = 5

const overviewProjects = ref([
	{
		name: "Clean Water Access Initiative",
		progress: 70,
		completed: 50,
		inProgress: 20,
	},
	{
		name: "Education for Rural Children",
		progress: 64,
		completed: 45,
		inProgress: 19,
	},
	{
		name: "Health & Wellness Program",
		progress: 35,
		completed: 20,
		inProgress: 15,
		atRisk: 10,
	},
	{
		name: "Livelihood Support for Women",
		progress: 56,
		completed: 35,
		inProgress: 21,
	},
	{
		name: "Disaster Relief Response",
		progress: 39,
		completed: 20,
		inProgress: 19,
		delayed: 15,
	},
])

const projectsList = ref([
	{
		name: "Clean Water Access Initiative",
		code: "GI-2026-001",
		sector: "WASH",
		geography: "Bihar",
		startDate: "05 Oct 2026",
		endDate: "30 Jun 2027",
		progress: 70,
		status: "On Track",
		thumbnail:
			"https://images.unsplash.com/photo-1541252260730-0412e8e2108e?w=100&auto=format&fit=crop&q=60",
	},
	{
		name: "Education for Rural Children",
		code: "GI-2026-002",
		sector: "Education",
		geography: "Uttar Pradesh",
		startDate: "12 Sep 2026",
		endDate: "31 Mar 2027",
		progress: 64,
		status: "On Track",
		thumbnail:
			"https://images.unsplash.com/photo-1497633762265-9d179a990aa6?w=100&auto=format&fit=crop&q=60",
	},
	{
		name: "Health & Wellness Program",
		code: "GI-2026-003",
		sector: "Health",
		geography: "Tamil Nadu",
		startDate: "12 Oct 2026",
		endDate: "30 Sep 2027",
		progress: 35,
		status: "At Risk",
		thumbnail:
			"https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?w=100&auto=format&fit=crop&q=60",
	},
	{
		name: "Livelihood Support for Women",
		code: "GI-2026-004",
		sector: "Livelihoods",
		geography: "Odisha",
		startDate: "28 Sep 2026",
		endDate: "31 Mar 2027",
		progress: 56,
		status: "On Track",
		thumbnail:
			"https://images.unsplash.com/photo-1593113598332-cd288d649433?w=100&auto=format&fit=crop&q=60",
	},
	{
		name: "Disaster Relief Response",
		code: "GI-2026-005",
		sector: "Disaster Relief",
		geography: "Assam",
		startDate: "20 Sep 2026",
		endDate: "31 Dec 2026",
		progress: 39,
		status: "Delayed",
		thumbnail:
			"https://images.unsplash.com/photo-1547471080-7cc2caa01a7e?w=100&auto=format&fit=crop&q=60",
	},
	{
		name: "School Digital Infrastructure",
		code: "GI-2026-006",
		sector: "Education",
		geography: "Jharkhand",
		startDate: "01 Sep 2026",
		endDate: "28 Feb 2027",
		progress: 80,
		status: "On Track",
		thumbnail:
			"https://images.unsplash.com/photo-1509062522246-3755977927d7?w=100&auto=format&fit=crop&q=60",
	},
	{
		name: "Community Sanitation Drive",
		code: "GI-2026-007",
		sector: "WASH",
		geography: "Bihar",
		startDate: "15 Aug 2026",
		endDate: "15 Jan 2027",
		progress: 75,
		status: "On Track",
		thumbnail:
			"https://images.unsplash.com/photo-1541252260730-0412e8e2108e?w=100&auto=format&fit=crop&q=60",
	},
	{
		name: "Maternal Health Support",
		code: "GI-2026-008",
		sector: "Health",
		geography: "Karnataka",
		startDate: "01 Aug 2026",
		endDate: "31 Dec 2026",
		progress: 60,
		status: "On Track",
		thumbnail:
			"https://images.unsplash.com/photo-1584515979956-d9f6e5d09982?w=100&auto=format&fit=crop&q=60",
	},
	{
		name: "Artisan Empowerment Unit",
		code: "GI-2026-009",
		sector: "Livelihoods",
		geography: "Odisha",
		startDate: "10 Jul 2026",
		endDate: "30 Dec 2026",
		progress: 40,
		status: "At Risk",
		thumbnail:
			"https://images.unsplash.com/photo-1593113598332-cd288d649433?w=100&auto=format&fit=crop&q=60",
	},
	{
		name: "Civic Awareness Seminars",
		code: "GI-2026-010",
		sector: "Governance",
		geography: "Maharashtra",
		startDate: "01 Jun 2026",
		endDate: "30 Nov 2026",
		progress: 90,
		status: "On Track",
		thumbnail:
			"https://images.unsplash.com/photo-1577495508048-b635879837f1?w=100&auto=format&fit=crop&q=60",
	},
])

const filteredProjects = computed(() => {
	return projectsList.value.filter((p) => {
		const matchSearch =
			!searchQuery.value ||
			p.name.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
			p.code.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
			p.sector.toLowerCase().includes(searchQuery.value.toLowerCase())
		const matchSector =
			!selectedSector.value || p.sector === selectedSector.value
		const matchGeo =
			!selectedGeography.value || p.geography === selectedGeography.value
		const matchStatus =
			!selectedStatus.value || p.status === selectedStatus.value
		return matchSearch && matchSector && matchGeo && matchStatus
	})
})

const totalPages = computed(
	() => Math.ceil(filteredProjects.value.length / pageSize) || 1,
)

const paginatedProjects = computed(() => {
	const start = (currentPage.value - 1) * pageSize
	return filteredProjects.value.slice(start, start + pageSize)
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
			return h("svg", { fill: "currentColor", viewBox: "0 0 20 20" }, [
				h("path", { d: "M4 4a2 2 0 00-2 2v1h16V6a2 2 0 00-2-2H4z" }),
				h("path", {
					"fill-rule": "evenodd",
					d: "M18 9H2v5a2 2 0 002 2h12a2 2 0 002-2V9z",
				}),
			])
		},
	}
}
</script>
