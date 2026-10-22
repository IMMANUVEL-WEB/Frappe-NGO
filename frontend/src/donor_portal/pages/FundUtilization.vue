<template>
  <div class="space-y-6">
    <!-- Top Stat Cards (5 Cards) -->
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-4">
      <!-- 1. Total Funds Received -->
      <div class="bg-white rounded-2xl p-5 border border-slate-100 shadow-xs flex flex-col justify-between hover:shadow-md transition">
        <div class="flex items-start justify-between">
          <div>
            <span class="text-[11px] font-bold uppercase tracking-wider text-slate-400">Total Funds Received</span>
            <div class="text-2xl font-black text-slate-900 mt-1 tracking-tight">₹72.60 L</div>
            <div class="text-xs text-slate-400 font-medium mt-1">Across all grants</div>
          </div>
          <div class="w-10 h-10 rounded-xl bg-emerald-50 text-emerald-600 flex items-center justify-center">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 9V7a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2m2 4h10a2 2 0 002-2v-6a2 2 0 00-2-2H9a2 2 0 00-2 2v6a2 2 0 002 2zm7-5a2 2 0 11-4 0 2 2 0 014 0z"/>
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

      <!-- 2. Total Utilized -->
      <div class="bg-white rounded-2xl p-5 border border-slate-100 shadow-xs flex flex-col justify-between hover:shadow-md transition">
        <div class="flex items-start justify-between">
          <div>
            <span class="text-[11px] font-bold uppercase tracking-wider text-slate-400">Total Utilized</span>
            <div class="text-2xl font-black text-slate-900 mt-1 tracking-tight">₹48.32 L</div>
            <div class="text-xs text-slate-400 font-medium mt-1">66.5% of total received</div>
          </div>
          <div class="w-10 h-10 rounded-xl bg-blue-50 text-blue-600 flex items-center justify-center">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 10h18M7 15h1m4 0h1m-7 4h12a3 3 0 003-3V8a3 3 0 00-3-3H6a3 3 0 00-3 3v8a3 3 0 003 3z"/>
            </svg>
          </div>
        </div>
        <div class="mt-4 flex items-center justify-between">
          <div class="w-full bg-slate-100 rounded-full h-1.5 overflow-hidden">
            <div class="bg-blue-600 h-1.5 rounded-full w-[66.5%]"></div>
          </div>
          <span class="text-[10px] font-semibold text-slate-400 ml-2">66.5%</span>
        </div>
      </div>

      <!-- 3. Remaining Balance -->
      <div class="bg-white rounded-2xl p-5 border border-slate-100 shadow-xs flex flex-col justify-between hover:shadow-md transition">
        <div class="flex items-start justify-between">
          <div>
            <span class="text-[11px] font-bold uppercase tracking-wider text-slate-400">Remaining Balance</span>
            <div class="text-2xl font-black text-slate-900 mt-1 tracking-tight">₹24.28 L</div>
            <div class="text-xs text-slate-400 font-medium mt-1">33.5% of total received</div>
          </div>
          <div class="w-10 h-10 rounded-xl bg-amber-50 text-amber-500 flex items-center justify-center">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/>
            </svg>
          </div>
        </div>
        <div class="mt-4 flex items-center justify-between">
          <div class="w-full bg-slate-100 rounded-full h-1.5 overflow-hidden">
            <div class="bg-amber-400 h-1.5 rounded-full w-[33.5%]"></div>
          </div>
          <span class="text-[10px] font-semibold text-slate-400 ml-2">33.5%</span>
        </div>
      </div>

      <!-- 4. Active Grants -->
      <div class="bg-white rounded-2xl p-5 border border-slate-100 shadow-xs flex flex-col justify-between hover:shadow-md transition">
        <div class="flex items-start justify-between">
          <div>
            <span class="text-[11px] font-bold uppercase tracking-wider text-slate-400">Active Grants</span>
            <div class="text-2xl font-black text-slate-900 mt-1 tracking-tight">3</div>
            <div class="text-xs text-slate-400 font-medium mt-1">Out of 6 total grants</div>
          </div>
          <div class="w-10 h-10 rounded-xl bg-purple-50 text-purple-600 flex items-center justify-center">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/>
            </svg>
          </div>
        </div>
        <div class="mt-4 flex items-center justify-between">
          <div class="w-full bg-slate-100 rounded-full h-1.5 overflow-hidden">
            <div class="bg-purple-500 h-1.5 rounded-full w-[50%]"></div>
          </div>
          <span class="text-[10px] font-semibold text-slate-400 ml-2">50%</span>
        </div>
      </div>

      <!-- 5. Avg. Utilization Time -->
      <div class="bg-white rounded-2xl p-5 border border-slate-100 shadow-xs flex flex-col justify-between hover:shadow-md transition">
        <div class="flex items-start justify-between">
          <div>
            <span class="text-[11px] font-bold uppercase tracking-wider text-slate-400">Avg. Utilization Time</span>
            <div class="text-2xl font-black text-slate-900 mt-1 tracking-tight">8.5 months</div>
            <div class="text-xs text-slate-400 font-medium mt-1">From start date</div>
          </div>
          <div class="w-10 h-10 rounded-xl bg-teal-50 text-teal-600 flex items-center justify-center">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/>
            </svg>
          </div>
        </div>
        <div class="mt-4 flex items-center justify-between">
          <div class="w-full bg-slate-100 rounded-full h-1.5 overflow-hidden">
            <div class="bg-teal-500 h-1.5 rounded-full w-[85%]"></div>
          </div>
          <span class="text-[10px] font-semibold text-slate-400 ml-2">85%</span>
        </div>
      </div>
    </div>

    <!-- Middle Charts Row (2 Cards) -->
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-6">
      <!-- Left Card: Fund Utilization Trend (7 cols) -->
      <div class="lg:col-span-7 bg-white rounded-2xl p-5 border border-slate-100 shadow-xs">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 mb-6">
          <div class="flex items-center space-x-2">
            <div class="w-2.5 h-2.5 rounded-full bg-emerald-500"></div>
            <h3 class="text-sm font-bold text-slate-900 tracking-tight">Fund Utilization Trend</h3>
          </div>

          <div class="flex items-center space-x-3 text-xs">
            <div class="flex items-center space-x-3">
              <span class="flex items-center gap-1.5 text-slate-600">
                <span class="w-2.5 h-2.5 rounded bg-blue-600"></span> Funds Received
              </span>
              <span class="flex items-center gap-1.5 text-slate-600">
                <span class="w-2.5 h-2.5 rounded bg-emerald-500"></span> Funds Utilized
              </span>
              <span class="flex items-center gap-1.5 text-slate-600">
                <span class="w-2 h-2 rounded-full bg-amber-400"></span> Utilization %
              </span>
            </div>

            <select class="px-2.5 py-1 text-xs rounded-lg border border-slate-200 bg-white text-slate-700 font-medium">
              <option>Apr 2026 - Oct 2026</option>
              <option>Q1 2026 - Q2 2026</option>
              <option>Year 2026</option>
            </select>
          </div>
        </div>

        <!-- Custom Visual Dual-Axis Chart -->
        <div class="relative h-64 pt-4 pb-2">
          <!-- Background Grid Lines & Left Labels -->
          <div class="absolute inset-x-8 inset-y-4 flex flex-col justify-between pointer-events-none text-[10px] text-slate-400 font-medium">
            <div class="border-b border-slate-100 pb-1 flex justify-between"><span>50L</span><span>100%</span></div>
            <div class="border-b border-slate-100 pb-1 flex justify-between"><span>40L</span><span>80%</span></div>
            <div class="border-b border-slate-100 pb-1 flex justify-between"><span>30L</span><span>60%</span></div>
            <div class="border-b border-slate-100 pb-1 flex justify-between"><span>20L</span><span>40%</span></div>
            <div class="border-b border-slate-100 pb-1 flex justify-between"><span>10L</span><span>20%</span></div>
            <div class="border-b border-slate-200 pb-1 flex justify-between"><span>0L</span><span>0%</span></div>
          </div>

          <!-- Bars and Line Container -->
          <div class="relative h-full mx-10 flex items-end justify-between z-10">
            <!-- SVG Line for Utilization % Overlay -->
            <svg class="absolute inset-0 w-full h-full pointer-events-none overflow-visible">
              <polyline
                fill="none"
                stroke="#F59E0B"
                stroke-width="2.5"
                points="25,120 75,135 125,115 175,90 225,80 275,70 325,75"
              />
              <circle cx="25" cy="120" r="4" fill="#F59E0B" />
              <circle cx="75" cy="135" r="4" fill="#F59E0B" />
              <circle cx="125" cy="115" r="4" fill="#F59E0B" />
              <circle cx="175" cy="90" r="4" fill="#F59E0B" />
              <circle cx="225" cy="80" r="4" fill="#F59E0B" />
              <circle cx="275" cy="70" r="4" fill="#F59E0B" />
              <circle cx="325" cy="75" r="4" fill="#F59E0B" />
            </svg>

            <!-- Month 1: Apr -->
            <div class="flex flex-col items-center">
              <div class="flex items-end space-x-1.5 h-48">
                <div class="w-3.5 bg-blue-600 rounded-t-sm h-[40%] transition-all"></div>
                <div class="w-3.5 bg-emerald-500 rounded-t-sm h-[46%] transition-all"></div>
              </div>
              <span class="text-[11px] text-slate-500 font-medium mt-2">Apr</span>
            </div>

            <!-- Month 2: May -->
            <div class="flex flex-col items-center">
              <div class="flex items-end space-x-1.5 h-48">
                <div class="w-3.5 bg-blue-600 rounded-t-sm h-[52%] transition-all"></div>
                <div class="w-3.5 bg-emerald-500 rounded-t-sm h-[56%] transition-all"></div>
              </div>
              <span class="text-[11px] text-slate-500 font-medium mt-2">May</span>
            </div>

            <!-- Month 3: Jun -->
            <div class="flex flex-col items-center">
              <div class="flex items-end space-x-1.5 h-48">
                <div class="w-3.5 bg-blue-600 rounded-t-sm h-[68%] transition-all"></div>
                <div class="w-3.5 bg-emerald-500 rounded-t-sm h-[60%] transition-all"></div>
              </div>
              <span class="text-[11px] text-slate-500 font-medium mt-2">Jun</span>
            </div>

            <!-- Month 4: Jul -->
            <div class="flex flex-col items-center">
              <div class="flex items-end space-x-1.5 h-48">
                <div class="w-3.5 bg-blue-600 rounded-t-sm h-[78%] transition-all"></div>
                <div class="w-3.5 bg-emerald-500 rounded-t-sm h-[70%] transition-all"></div>
              </div>
              <span class="text-[11px] text-slate-500 font-medium mt-2">Jul</span>
            </div>

            <!-- Month 5: Aug -->
            <div class="flex flex-col items-center">
              <div class="flex items-end space-x-1.5 h-48">
                <div class="w-3.5 bg-blue-600 rounded-t-sm h-[82%] transition-all"></div>
                <div class="w-3.5 bg-emerald-500 rounded-t-sm h-[78%] transition-all"></div>
              </div>
              <span class="text-[11px] text-slate-500 font-medium mt-2">Aug</span>
            </div>

            <!-- Month 6: Sep -->
            <div class="flex flex-col items-center">
              <div class="flex items-end space-x-1.5 h-48">
                <div class="w-3.5 bg-blue-600 rounded-t-sm h-[90%] transition-all"></div>
                <div class="w-3.5 bg-emerald-500 rounded-t-sm h-[86%] transition-all"></div>
              </div>
              <span class="text-[11px] text-slate-500 font-medium mt-2">Sep</span>
            </div>

            <!-- Month 7: Oct -->
            <div class="flex flex-col items-center">
              <div class="flex items-end space-x-1.5 h-48">
                <div class="w-3.5 bg-blue-600 rounded-t-sm h-[96%] transition-all"></div>
                <div class="w-3.5 bg-emerald-500 rounded-t-sm h-[92%] transition-all"></div>
              </div>
              <span class="text-[11px] text-slate-500 font-medium mt-2">Oct</span>
            </div>
          </div>
        </div>
      </div>

      <!-- Right Card: Utilization by Project (5 cols) -->
      <div class="lg:col-span-5 bg-white rounded-2xl p-5 border border-slate-100 shadow-xs flex flex-col justify-between">
        <div>
          <div class="flex items-center space-x-2 mb-4">
            <div class="w-2.5 h-2.5 rounded-full bg-emerald-500"></div>
            <h3 class="text-sm font-bold text-slate-900 tracking-tight">Utilization by Project</h3>
          </div>

          <div class="flex items-center justify-center my-2">
            <!-- Donut Chart -->
            <div class="relative w-36 h-36 flex items-center justify-center">
              <svg class="w-full h-full transform -rotate-90" viewBox="0 0 36 36">
                <circle cx="18" cy="18" r="14" fill="none" stroke="#2563EB" stroke-width="5" stroke-dasharray="32 68" stroke-dashoffset="0" />
                <circle cx="18" cy="18" r="14" fill="none" stroke="#059669" stroke-width="5" stroke-dasharray="24 76" stroke-dashoffset="-32" />
                <circle cx="18" cy="18" r="14" fill="none" stroke="#F59E0B" stroke-width="5" stroke-dasharray="18 82" stroke-dashoffset="-56" />
                <circle cx="18" cy="18" r="14" fill="none" stroke="#8B5CF6" stroke-width="5" stroke-dasharray="14 86" stroke-dashoffset="-74" />
                <circle cx="18" cy="18" r="14" fill="none" stroke="#10B981" stroke-width="5" stroke-dasharray="12 88" stroke-dashoffset="-88" />
              </svg>
              <div class="absolute inset-0 flex flex-col items-center justify-center text-center">
                <span class="text-xs font-black text-slate-900 leading-tight">₹48.32 L</span>
                <span class="text-[9px] text-slate-400 font-medium">Utilized</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Legend Table -->
        <div class="space-y-2 mt-4 text-xs">
          <div class="flex items-center justify-between text-slate-700">
            <span class="flex items-center gap-2"><span class="w-2.5 h-2.5 rounded-full bg-blue-600"></span> Clean Water Access Initiative</span>
            <span class="font-semibold text-slate-900">₹15.40 L <span class="text-slate-400 font-normal">32%</span></span>
          </div>
          <div class="flex items-center justify-between text-slate-700">
            <span class="flex items-center gap-2"><span class="w-2.5 h-2.5 rounded-full bg-emerald-600"></span> Education for Rural Children</span>
            <span class="font-semibold text-slate-900">₹11.58 L <span class="text-slate-400 font-normal">24%</span></span>
          </div>
          <div class="flex items-center justify-between text-slate-700">
            <span class="flex items-center gap-2"><span class="w-2.5 h-2.5 rounded-full bg-amber-500"></span> Health & Wellness Program</span>
            <span class="font-semibold text-slate-900">₹8.69 L <span class="text-slate-400 font-normal">18%</span></span>
          </div>
          <div class="flex items-center justify-between text-slate-700">
            <span class="flex items-center gap-2"><span class="w-2.5 h-2.5 rounded-full bg-purple-500"></span> Livelihood Support for Women</span>
            <span class="font-semibold text-slate-900">₹6.76 L <span class="text-slate-400 font-normal">14%</span></span>
          </div>
          <div class="flex items-center justify-between text-slate-700">
            <span class="flex items-center gap-2"><span class="w-2.5 h-2.5 rounded-full bg-teal-500"></span> Disaster Relief Response</span>
            <span class="font-semibold text-slate-900">₹5.89 L <span class="text-slate-400 font-normal">12%</span></span>
          </div>
        </div>
      </div>
    </div>

    <!-- Bottom Section: Fund Utilization Details Table -->
    <div class="bg-white rounded-2xl border border-slate-100 shadow-xs overflow-hidden">
      <div class="p-4 border-b border-slate-100 flex flex-col md:flex-row md:items-center justify-between gap-3">
        <div class="flex items-center space-x-2">
          <div class="w-2.5 h-2.5 rounded-full bg-emerald-500"></div>
          <h3 class="text-sm font-bold text-slate-900 tracking-tight">Fund Utilization Details</h3>
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

          <select class="px-3 py-1.5 text-xs rounded-xl border border-slate-200 bg-white text-slate-700">
            <option>All Grants</option>
          </select>

          <div class="relative">
            <input 
              type="text" 
              v-model="searchQuery" 
              placeholder="Search project or grant..." 
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
              <th class="py-3.5 px-4">Grant Name</th>
              <th class="py-3.5 px-4">Project / Initiative</th>
              <th class="py-3.5 px-3">Sector</th>
              <th class="py-3.5 px-3">Geography</th>
              <th class="py-3.5 px-4">Total Grant Amount</th>
              <th class="py-3.5 px-4">Utilized Amount</th>
              <th class="py-3.5 px-4">Remaining Balance</th>
              <th class="py-3.5 px-4">Utilization %</th>
              <th class="py-3.5 px-3">Status</th>
              <th class="py-3.5 px-4 text-right">Actions</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-slate-100 text-slate-700">
            <tr 
              v-for="(row, idx) in filteredRows" 
              :key="row.code"
              class="hover:bg-slate-50/60 transition group"
            >
              <td class="py-3.5 px-4 text-slate-400 font-medium">{{ idx + 1 }}</td>
              <td class="py-3.5 px-4">
                <div class="font-semibold text-slate-900">{{ row.name }}</div>
                <div class="text-[11px] text-slate-400 font-mono">{{ row.code }}</div>
              </td>
              <td class="py-3.5 px-4 text-slate-600 font-medium">{{ row.project }}</td>
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
              <td class="py-3.5 px-4 font-semibold text-slate-900">{{ row.totalAmount }}</td>
              <td class="py-3.5 px-4 font-semibold text-slate-900">{{ row.utilizedAmount }}</td>
              <td class="py-3.5 px-4 font-semibold text-slate-900">{{ row.balance }}</td>
              <td class="py-3.5 px-4">
                <div class="flex items-center space-x-2">
                  <span class="text-xs font-semibold text-slate-700 w-8">{{ row.utilizationPercent }}%</span>
                  <div class="w-16 bg-slate-100 rounded-full h-1.5 overflow-hidden">
                    <div 
                      class="bg-emerald-500 h-1.5 rounded-full"
                      :style="{ width: `${row.utilizationPercent}%` }"
                    ></div>
                  </div>
                </div>
              </td>
              <td class="py-3.5 px-3">
                <span 
                  class="inline-block px-2.5 py-0.5 rounded-full text-[11px] font-semibold"
                  :class="row.status === 'Active' ? 'bg-emerald-50 text-emerald-700 border border-emerald-100' : 'bg-amber-50 text-amber-700 border border-amber-200'"
                >
                  {{ row.status }}
                </span>
              </td>
              <td class="py-3.5 px-4 text-right">
                <div class="flex items-center justify-end space-x-1.5">
                  <button type="button" class="p-1 rounded-lg hover:bg-slate-100 text-slate-400 hover:text-emerald-600">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/>
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"/>
                    </svg>
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
          Showing 1 - {{ filteredRows.length }} of {{ filteredRows.length }} grants
        </div>
        <div class="flex items-center space-x-1.5">
          <button class="w-7 h-7 rounded-lg border border-slate-200 flex items-center justify-center opacity-40 cursor-not-allowed">&lt;</button>
          <button class="w-7 h-7 rounded-lg bg-[#00875A] text-white flex items-center justify-center font-semibold">1</button>
          <button class="w-7 h-7 rounded-lg border border-slate-200 flex items-center justify-center opacity-40 cursor-not-allowed">&gt;</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, h } from "vue"

const searchQuery = ref("")
const selectedSector = ref("")
const selectedGeography = ref("")

const utilizationRows = ref([
  {
    name: "Clean Water Access Initiative",
    code: "GI-2026-001",
    project: "Clean Water Access Initiative",
    sector: "WASH",
    geography: "Bihar",
    totalAmount: "₹22,00,000",
    utilizedAmount: "₹15,40,000",
    balance: "₹6,60,000",
    utilizationPercent: 70,
    status: "Active"
  },
  {
    name: "Education for Rural Children",
    code: "GI-2026-002",
    project: "Quality Education for Rural Children",
    sector: "Education",
    geography: "Uttar Pradesh",
    totalAmount: "₹18,00,000",
    utilizedAmount: "₹11,58,000",
    balance: "₹6,42,000",
    utilizationPercent: 64,
    status: "Active"
  },
  {
    name: "Health & Wellness Program",
    code: "GI-2026-003",
    project: "Community Health & Wellness Program",
    sector: "Health",
    geography: "Tamil Nadu",
    totalAmount: "₹25,00,000",
    utilizedAmount: "₹8,69,000",
    balance: "₹16,31,000",
    utilizationPercent: 35,
    status: "Active"
  },
  {
    name: "Livelihood Support for Women",
    code: "GI-2026-004",
    project: "Livelihood Support for Women",
    sector: "Livelihoods",
    geography: "Odisha",
    totalAmount: "₹12,00,000",
    utilizedAmount: "₹6,76,000",
    balance: "₹5,24,000",
    utilizationPercent: 56,
    status: "Pending"
  },
  {
    name: "Disaster Relief Response",
    code: "GI-2026-005",
    project: "Disaster Relief Response",
    sector: "Disaster Relief",
    geography: "Assam",
    totalAmount: "₹15,00,000",
    utilizedAmount: "₹5,89,000",
    balance: "₹9,11,000",
    utilizationPercent: 39,
    status: "Active"
  }
])

const filteredRows = computed(() => {
  return utilizationRows.value.filter(r => {
    const matchSearch = !searchQuery.value || 
      r.name.toLowerCase().includes(searchQuery.value.toLowerCase()) || 
      r.code.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
      r.project.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
      r.sector.toLowerCase().includes(searchQuery.value.toLowerCase())
    const matchSector = !selectedSector.value || r.sector === selectedSector.value
    const matchGeo = !selectedGeography.value || r.geography === selectedGeography.value
    return matchSearch && matchSector && matchGeo
  })
})

function getSectorClass(sector) {
  switch (sector) {
    case 'Health': return 'bg-rose-50 text-rose-600'
    case 'Education': return 'bg-purple-50 text-purple-600'
    case 'WASH': return 'bg-sky-50 text-sky-600'
    case 'Livelihoods': return 'bg-emerald-50 text-emerald-600'
    case 'Disaster Relief': return 'bg-amber-50 text-amber-700'
    default: return 'bg-slate-100 text-slate-700'
  }
}

function getSectorIcon(sector) {
  return {
    render() {
      if (sector === 'Health') {
        return h('svg', { fill: 'currentColor', viewBox: '0 0 20 20' }, [
          h('path', { 'fill-rule': 'evenodd', d: 'M3.172 5.172a4 4 0 015.656 0L10 6.343l1.172-1.171a4 4 0 115.656 5.656L10 17.657l-6.828-6.829a4 4 0 010-5.656z', 'clip-rule': 'evenodd' })
        ])
      }
      if (sector === 'Education') {
        return h('svg', { fill: 'none', stroke: 'currentColor', 'stroke-width': '2', viewBox: '0 0 24 24' }, [
          h('path', { 'stroke-linecap': 'round', 'stroke-linejoin': 'round', d: 'M12 14l9-5-9-5-9 5 9 5z' }),
          h('path', { 'stroke-linecap': 'round', 'stroke-linejoin': 'round', d: 'M12 14l6.16-3.422a12.083 12.083 0 01.665 6.479A11.952 11.952 0 0012 20.055a11.952 11.952 0 00-6.824-2.998 12.078 12.078 0 01.665-6.479L12 14z' })
        ])
      }
      if (sector === 'WASH') {
        return h('svg', { fill: 'currentColor', viewBox: '0 0 20 20' }, [
          h('path', { 'fill-rule': 'evenodd', d: 'M10 2a1 1 0 01.832.445l4.83 7.245A6 6 0 114.338 9.69L9.168 2.445A1 1 0 0110 2z', 'clip-rule': 'evenodd' })
        ])
      }
      if (sector === 'Livelihoods') {
        return h('svg', { fill: 'none', stroke: 'currentColor', 'stroke-width': '2', viewBox: '0 0 24 24' }, [
          h('path', { 'stroke-linecap': 'round', 'stroke-linejoin': 'round', d: 'M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z' })
        ])
      }
      if (sector === 'Disaster Relief') {
        return h('svg', { fill: 'currentColor', viewBox: '0 0 20 20' }, [
          h('path', { 'fill-rule': 'evenodd', d: 'M8.257 3.099c.765-1.36 2.722-1.36 3.486 0l5.58 9.92c.75 1.334-.213 2.98-1.742 2.98H4.42c-1.53 0-2.493-1.646-1.743-2.98l5.58-9.92zM11 13a1 1 0 11-2 0 1 1 0 012 0zm-1-8a1 1 0 00-1 1v3a1 1 0 002 0V6a1 1 0 00-1-1z', 'clip-rule': 'evenodd' })
        ])
      }
      return h('svg', { fill: 'currentColor', viewBox: '0 0 20 20' }, [
        h('path', { d: 'M4 4a2 2 0 00-2 2v1h16V6a2 2 0 00-2-2H4z' }),
        h('path', { 'fill-rule': 'evenodd', d: 'M18 9H2v5a2 2 0 002 2h12a2 2 0 002-2V9z' })
      ])
    }
  }
}
</script>
