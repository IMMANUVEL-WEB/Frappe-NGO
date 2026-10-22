<template>
  <div class="min-h-screen bg-[#f8fafc] flex flex-col md:flex-row font-sans text-gray-800 antialiased">
    
    <!-- Mobile Top Header -->
    <div class="md:hidden bg-[#043226] text-white px-4 py-3.5 flex justify-between items-center shadow-md sticky top-0 z-30">
      <div class="flex items-center gap-2.5 min-w-0">
        <!-- Dynamic Logo from Portal Settings -->
        <template v-if="portalSettings.login_logo">
          <img 
            :src="portalSettings.login_logo" 
            alt="Logo" 
            class="h-8 w-auto max-w-[100px] object-contain rounded flex-shrink-0" 
          />
        </template>
        <template v-else>
          <div class="w-8 h-8 rounded-lg bg-emerald-900/60 flex items-center justify-center border border-emerald-500/30 flex-shrink-0">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none">
              <path d="M12 22V12" stroke="#10b981" stroke-width="2.2" stroke-linecap="round"/>
              <path d="M12 12C12 7.02944 16.0294 3 21 3C21 7.97056 16.9706 12 12 12Z" fill="#f59e0b" fill-opacity="0.9"/>
              <path d="M12 14C12 9.02944 7.97056 5 3 5C3 9.97056 7.02944 14 12 14Z" fill="#10b981"/>
            </svg>
          </div>
        </template>
        <div class="min-w-0">
          <span class="font-extrabold text-base tracking-tight text-white block leading-tight truncate">
            {{ portalSettings.login_portal_title || 'Kindred' }}
          </span>
          <span class="block text-[9px] text-emerald-300 tracking-wider uppercase font-medium truncate">
            {{ portalSettings.login_portal_subtitle || 'Volunteer Impact' }}
          </span>
        </div>
      </div>
      <button 
        @click="mobileMenuOpen = !mobileMenuOpen" 
        class="text-emerald-200 hover:text-white p-1 rounded-lg focus:outline-none flex-shrink-0 ml-2"
        aria-label="Toggle Navigation"
      >
        <svg v-if="!mobileMenuOpen" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>
        <svg v-else xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
      </button>
    </div>

    <!-- Left Sidebar (Desktop + Mobile Drawer) -->
    <aside 
      :class="[
        'fixed md:sticky top-0 h-screen inset-y-0 left-0 flex flex-col w-64 bg-[#043226] text-white z-40 transition-transform duration-300 ease-in-out shadow-2xl md:shadow-none select-none overflow-hidden',
        mobileMenuOpen ? 'translate-x-0' : '-translate-x-full md:translate-x-0'
      ]"
    >
      <!-- Subtle Decorative Botanical Leaf Watermark at bottom left -->
      <div class="absolute -bottom-8 -left-10 w-48 h-48 opacity-[0.09] pointer-events-none text-emerald-300">
        <svg viewBox="0 0 200 200" fill="currentColor">
          <path d="M40,160 C20,100 60,30 160,20 C170,120 100,180 40,160 Z" />
          <path d="M40,160 C70,130 120,90 160,20" stroke="#a7f3d0" stroke-width="6" fill="none" />
          <path d="M80,135 C100,120 120,125 130,120" stroke="#a7f3d0" stroke-width="4" fill="none" />
          <path d="M110,105 C130,90 145,95 155,90" stroke="#a7f3d0" stroke-width="4" fill="none" />
        </svg>
      </div>

      <!-- Brand Header with Dynamic Portal Settings Logo -->
      <div class="px-6 pt-7 pb-6 flex items-center gap-3 border-b border-emerald-900/40">
        <template v-if="portalSettings.login_logo">
          <img 
            :src="portalSettings.login_logo" 
            alt="Logo" 
            class="h-9 w-auto max-w-[120px] object-contain rounded-lg flex-shrink-0"
          />
        </template>
        <template v-else>
          <div class="w-9 h-9 rounded-xl bg-emerald-900/60 flex items-center justify-center border border-emerald-500/30 shadow-inner flex-shrink-0">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none">
              <path d="M12 22V12" stroke="#34d399" stroke-width="2.2" stroke-linecap="round"/>
              <path d="M12 12C12 7.02944 16.0294 3 21 3C21 7.97056 16.9706 12 12 12Z" fill="#f59e0b" fill-opacity="0.95"/>
              <path d="M12 14C12 9.02944 7.97056 5 3 5C3 9.97056 7.02944 14 12 14Z" fill="#10b981"/>
            </svg>
          </div>
        </template>
        <div class="min-w-0">
          <h1 class="font-bold text-lg text-white tracking-tight leading-snug truncate">
            {{ portalSettings.login_portal_title || 'Kindred' }}
          </h1>
          <p class="text-[10px] text-emerald-300/80 font-medium tracking-wide uppercase truncate mt-0.5">
            {{ portalSettings.login_portal_subtitle || 'Volunteer Impact' }}
          </p>
        </div>
      </div>
      
      <!-- Navigation Links -->
      <nav class="flex-1 px-3.5 py-5 space-y-1 overflow-y-auto z-10">
        <router-link 
          v-for="item in navItems" 
          :key="item.path" 
          :to="item.path"
          class="flex items-center gap-3.5 px-3.5 py-2.5 text-sm font-medium rounded-xl transition-all duration-200 group relative"
          :class="[
            isCurrentRoute(item.path) 
              ? 'bg-[#124d3e] text-white shadow-sm font-semibold' 
              : 'text-emerald-100/70 hover:bg-[#083d30] hover:text-white'
          ]"
          @click="mobileMenuOpen = false"
        >
          <span 
            class="transition-colors flex-shrink-0"
            :class="isCurrentRoute(item.path) ? 'text-white' : 'text-emerald-200/60 group-hover:text-emerald-100'"
            v-html="item.icon"
          ></span>
          <span class="truncate">{{ item.label }}</span>
        </router-link>
      </nav>

      <!-- Bottom Profile & Sign Out Section -->
      <div class="p-4 border-t border-emerald-900/40 z-10 bg-[#042d22]/40 backdrop-blur-sm">
        <!-- User Pill Card with Dynamic Volunteer Avatar -->
        <router-link 
          to="/profile" 
          class="flex items-center justify-between p-2 rounded-xl hover:bg-[#083d30]/60 transition-colors group cursor-pointer"
        >
          <div class="flex items-center gap-3 min-w-0">
            <div class="w-9 h-9 rounded-full bg-[#a7f3d0] text-[#043226] font-bold text-xs flex items-center justify-center flex-shrink-0 shadow-sm uppercase overflow-hidden border border-emerald-500/20">
              <img v-if="userImage" :src="userImage" :alt="displayName" class="w-full h-full object-cover" />
              <span v-else>{{ userInitials }}</span>
            </div>
            <div class="min-w-0">
              <p class="text-sm font-semibold text-white truncate leading-tight group-hover:text-emerald-200 transition-colors">{{ displayName }}</p>
              <p class="text-[11px] text-emerald-300/70 font-medium">Volunteer</p>
            </div>
          </div>
          <svg class="text-emerald-300/40 group-hover:text-emerald-200 group-hover:translate-x-0.5 transition-all flex-shrink-0" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"></polyline></svg>
        </router-link>

        <!-- Sign Out Link -->
        <button 
          @click="showLogoutDialog = true" 
          class="w-full mt-3 flex items-center gap-2.5 px-3 py-2 text-xs font-medium text-emerald-200/70 hover:text-white hover:bg-[#083d30]/50 rounded-lg transition-all"
        >
          <svg xmlns="http://www.w3.org/2000/svg" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"></path><polyline points="16 17 21 12 16 7"></polyline><line x1="21" y1="12" x2="9" y2="12"></line></svg>
          Sign Out
        </button>
      </div>
    </aside>
    
    <!-- Mobile Backdrop Overlay -->
    <div 
      v-if="mobileMenuOpen" 
      @click="mobileMenuOpen = false"
      class="fixed inset-0 bg-gray-950/60 backdrop-blur-sm z-30 md:hidden"
    ></div>

    <!-- Main Content Area with Top Header -->
    <div class="flex-1 flex flex-col min-w-0 overflow-y-auto">
      
      <!-- Top Header Bar: Rich, Aesthetic, Interactive Navbar -->
      <header class="bg-white/95 backdrop-blur-md border-b border-gray-200/70 px-4 sm:px-6 lg:px-8 py-2.5 flex items-center justify-between sticky top-0 z-20 shadow-[0_1px_3px_rgba(0,0,0,0.02)] transition-all">
        
        <!-- Left: Current Page Indicator + Quick Global Search -->
        <div class="flex items-center gap-3 lg:gap-4 min-w-0">
          <!-- Mobile Sidebar Hamburger (visible on small screens) -->
          <button 
            @click="mobileMenuOpen = !mobileMenuOpen" 
            class="md:hidden text-gray-600 hover:text-emerald-800 p-1.5 -ml-1 rounded-xl hover:bg-gray-100 transition-colors focus:outline-none"
            aria-label="Toggle Navigation"
          >
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24" stroke-width="2">
              <line x1="3" y1="12" x2="21" y2="12"></line>
              <line x1="3" y1="6" x2="21" y2="6"></line>
              <line x1="3" y1="18" x2="21" y2="18"></line>
            </svg>
          </button>

          <!-- Current Page Title with Live Indicator -->
          <div class="flex items-center gap-2.5">
            <span class="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span>
            <div class="min-w-0">
              <h2 class="text-sm font-bold text-gray-900 leading-tight truncate">
                {{ currentPageInfo.title }}
              </h2>
              <p class="hidden sm:block text-[10px] text-gray-400 font-medium truncate">
                {{ currentPageInfo.subtitle }}
              </p>
            </div>
          </div>

          <!-- Divider -->
          <div class="hidden sm:block h-6 w-px bg-gray-200/80 mx-1"></div>

          <!-- Global Quick Search -->
          <div class="hidden sm:flex items-center relative">
            <svg class="w-3.5 h-3.5 text-gray-400 absolute left-3 pointer-events-none" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <circle cx="11" cy="11" r="8"></circle>
              <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
            </svg>
            <input 
              type="text" 
              v-model="globalSearch" 
              @keydown.enter="handleSearch"
              placeholder="Search opportunities, causes..." 
              class="w-44 lg:w-64 pl-8 pr-7 py-1.5 text-xs bg-gray-50 hover:bg-gray-100 focus:bg-white border border-gray-200 focus:border-emerald-600 rounded-xl focus:outline-none focus:ring-2 focus:ring-emerald-600/10 transition-all text-gray-700 placeholder-gray-400"
            />
            <button 
              v-if="globalSearch" 
              @click="globalSearch = ''" 
              class="absolute right-2 text-gray-400 hover:text-gray-600 text-xs p-0.5"
            >
              &times;
            </button>
            <span v-else class="absolute right-2 px-1 py-0.2 text-[9px] font-semibold text-gray-400 bg-white border border-gray-200 rounded shadow-2xs">?</span>
          </div>
        </div>

        <!-- Center: Date & Live Status Pill (on wide screens) -->
        <div class="hidden xl:flex items-center gap-2 px-3 py-1 bg-emerald-50/80 border border-emerald-100/90 rounded-full text-xs text-emerald-800 shadow-2xs">
          <svg class="w-3.5 h-3.5 text-emerald-600" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect>
            <line x1="16" y1="2" x2="16" y2="6"></line>
            <line x1="8" y1="2" x2="8" y2="6"></line>
            <line x1="3" y1="10" x2="21" y2="10"></line>
          </svg>
          <span class="font-medium text-emerald-950">{{ formattedTodayDate }}</span>
          <span class="text-emerald-300 font-semibold">?</span>
          <span class="font-bold text-emerald-700">Active Volunteer</span>
        </div>

        <!-- Right Side: Quick Action + Notifications + Profile Pill -->
        <div class="flex items-center gap-2.5 sm:gap-3 flex-shrink-0">
          
          <!-- Quick Action: Explore Causes -->
          <router-link 
            to="/opportunities" 
            class="hidden md:inline-flex items-center gap-1.5 px-3 py-1.5 text-xs font-bold text-emerald-800 bg-emerald-50/80 hover:bg-emerald-100 border border-emerald-200/80 rounded-xl transition-all shadow-2xs hover:shadow-xs group"
          >
            <svg class="w-3.5 h-3.5 text-emerald-600 group-hover:rotate-45 transition-transform duration-200" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <circle cx="12" cy="12" r="10"></circle>
              <polygon points="12 8 8 12 12 16 12 8"></polygon>
            </svg>
            <span>Explore Causes</span>
          </router-link>

          <!-- Notifications Bell Dropdown -->
          <div class="relative" ref="notificationsRef">
            <button 
              @click="toggleNotifications" 
              class="relative p-2 rounded-xl text-gray-500 hover:text-emerald-800 hover:bg-emerald-50/70 border border-transparent hover:border-emerald-100 transition-all focus:outline-none"
              :class="{ 'bg-emerald-50/70 text-emerald-800 border-emerald-100': notificationsOpen }"
              aria-label="View notifications"
            >
              <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"></path>
                <path d="M13.73 21a2 2 0 0 1-3.46 0"></path>
              </svg>
              <!-- Unread badge dot -->
              <span v-if="unreadCount > 0" class="absolute top-1.5 right-1.5 w-2 h-2 rounded-full bg-emerald-500 ring-2 ring-white"></span>
            </button>

            <!-- Notifications Flyout -->
            <div 
              v-if="notificationsOpen"
              class="absolute right-0 mt-2 w-80 sm:w-96 bg-white rounded-2xl shadow-xl border border-gray-100 z-50 overflow-hidden transform transition-all"
            >
              <div class="px-4 py-3 bg-gray-50/80 border-b border-gray-100 flex items-center justify-between">
                <div class="flex items-center gap-2">
                  <span class="text-xs font-bold text-gray-900">Notifications</span>
                  <span v-if="unreadCount > 0" class="px-1.5 py-0.5 rounded-full text-[10px] font-bold bg-emerald-100 text-emerald-800">
                    {{ unreadCount }} new
                  </span>
                </div>
                <button 
                  v-if="unreadCount > 0"
                  @click="unreadCount = 0"
                  class="text-[11px] font-semibold text-emerald-700 hover:text-emerald-900 transition-colors"
                >
                  Mark read
                </button>
              </div>

              <div class="divide-y divide-gray-50 max-h-80 overflow-y-auto">
                <div 
                  v-for="(n, idx) in notificationsList" 
                  :key="idx"
                  class="p-3.5 hover:bg-gray-50/80 transition-colors flex items-start gap-3"
                >
                  <div 
                    class="w-7 h-7 rounded-lg flex items-center justify-center flex-shrink-0 mt-0.5"
                    :class="n.iconBg"
                  >
                    <span v-html="n.icon"></span>
                  </div>
                  <div class="flex-1 min-w-0">
                    <p class="text-xs font-semibold text-gray-800 leading-snug">{{ n.title }}</p>
                    <p class="text-[11px] text-gray-500 mt-0.5 leading-relaxed">{{ n.desc }}</p>
                    <span class="text-[10px] text-gray-400 font-medium block mt-1">{{ n.time }}</span>
                  </div>
                </div>
              </div>

              <div class="p-2.5 bg-gray-50/50 border-t border-gray-100 text-center">
                <router-link 
                  to="/shifts" 
                  @click="notificationsOpen = false"
                  class="text-xs font-bold text-emerald-700 hover:text-emerald-900 transition-colors"
                >
                  View All Shifts & Schedules &rarr;
                </router-link>
              </div>
            </div>
          </div>

          <!-- Vertical separator -->
          <div class="h-6 w-px bg-gray-200/80"></div>

          <!-- Profile User Pill + Dropdown -->
          <div class="relative" ref="profileMenuRef">
            <button 
              @click="toggleProfileMenu" 
              class="flex items-center gap-2 p-1 pl-1.5 sm:pr-2.5 rounded-xl hover:bg-gray-100/80 border border-transparent hover:border-gray-200/60 transition-all focus:outline-none"
              :class="{ 'bg-gray-100/90 border-gray-200/70': profileMenuOpen }"
              aria-label="User profile menu"
            >
              <!-- Avatar Circle with online ring -->
              <div class="relative flex-shrink-0">
                <div class="w-8 h-8 rounded-full bg-[#043226] text-white font-bold text-xs flex items-center justify-center shadow-xs uppercase overflow-hidden border border-emerald-700/20">
                  <img v-if="userImage" :src="userImage" :alt="displayName" class="w-full h-full object-cover" />
                  <span v-else>{{ userInitials }}</span>
                </div>
                <span class="absolute -bottom-0.5 -right-0.5 w-2.5 h-2.5 bg-emerald-500 border-2 border-white rounded-full"></span>
              </div>

              <!-- Name and Role (hidden on tiny screens) -->
              <div class="hidden sm:block text-left min-w-0 max-w-[120px]">
                <p class="text-xs font-bold text-gray-900 truncate leading-tight">{{ displayName }}</p>
                <p class="text-[10px] text-emerald-700 font-medium leading-none">Volunteer</p>
              </div>

              <!-- Chevron Down -->
              <svg 
                class="w-3.5 h-3.5 text-gray-400 transition-transform duration-200 hidden sm:block" 
                :class="{ 'rotate-180': profileMenuOpen }" 
                viewBox="0 0 24 24" 
                fill="none" 
                stroke="currentColor" 
                stroke-width="2.5"
              >
                <polyline points="6 9 12 15 18 9"></polyline>
              </svg>
            </button>

            <!-- Profile Dropdown Menu -->
            <div 
              v-if="profileMenuOpen"
              class="absolute right-0 mt-2 w-60 bg-white rounded-2xl shadow-xl border border-gray-100 z-50 py-1.5 overflow-hidden transform transition-all"
            >
              <!-- User Summary Header -->
              <div class="px-4 py-3 border-b border-gray-100 bg-gray-50/60">
                <p class="text-xs font-bold text-gray-900 truncate">{{ displayName }}</p>
                <p class="text-[11px] text-gray-400 truncate mt-0.5">{{ userEmail || 'volunteer@impactsphere.org' }}</p>
                <span class="inline-flex items-center gap-1 mt-2 px-2 py-0.5 rounded-full text-[10px] font-bold bg-emerald-50 text-emerald-700 border border-emerald-200/60">
                  <span class="w-1.5 h-1.5 rounded-full bg-emerald-500"></span> Verified Volunteer
                </span>
              </div>

              <!-- Links -->
              <div class="py-1">
                <router-link 
                  to="/profile" 
                  @click="profileMenuOpen = false" 
                  class="flex items-center gap-2.5 px-4 py-2 text-xs font-medium text-gray-700 hover:bg-emerald-50/60 hover:text-emerald-900 transition-colors"
                >
                  <svg class="w-4 h-4 text-gray-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
                    <circle cx="12" cy="7" r="4"></circle>
                  </svg>
                  Profile Settings
                </router-link>

                <router-link 
                  to="/assignments" 
                  @click="profileMenuOpen = false" 
                  class="flex items-center gap-2.5 px-4 py-2 text-xs font-medium text-gray-700 hover:bg-emerald-50/60 hover:text-emerald-900 transition-colors"
                >
                  <svg class="w-4 h-4 text-gray-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
                    <polyline points="14 2 14 8 20 8"></polyline>
                  </svg>
                  My Assignments
                </router-link>

                <router-link 
                  to="/shifts" 
                  @click="profileMenuOpen = false" 
                  class="flex items-center gap-2.5 px-4 py-2 text-xs font-medium text-gray-700 hover:bg-emerald-50/60 hover:text-emerald-900 transition-colors"
                >
                  <svg class="w-4 h-4 text-gray-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect>
                    <line x1="16" y1="2" x2="16" y2="6"></line>
                    <line x1="8" y1="2" x2="8" y2="6"></line>
                  </svg>
                  My Shifts
                </router-link>

                <router-link 
                  to="/attendance" 
                  @click="profileMenuOpen = false" 
                  class="flex items-center gap-2.5 px-4 py-2 text-xs font-medium text-gray-700 hover:bg-emerald-50/60 hover:text-emerald-900 transition-colors"
                >
                  <svg class="w-4 h-4 text-gray-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <circle cx="12" cy="12" r="10"></circle>
                    <polyline points="9 12 11 14 15 10"></polyline>
                  </svg>
                  Attendance Record
                </router-link>
              </div>

              <!-- Sign Out Item -->
              <div class="pt-1 border-t border-gray-100">
                <button 
                  @click="profileMenuOpen = false; showLogoutDialog = true" 
                  class="w-full flex items-center gap-2.5 px-4 py-2 text-xs font-semibold text-rose-600 hover:bg-rose-50/70 transition-colors"
                >
                  <svg class="w-4 h-4 text-rose-500" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"></path>
                    <polyline points="16 17 21 12 16 7"></polyline>
                    <line x1="21" y1="12" x2="9" y2="12"></line>
                  </svg>
                  Sign Out
                </button>
              </div>
            </div>
          </div>

        </div>

      </header>

      <!-- Main Slot Content -->
      <main class="flex-1 p-5 md:p-8 max-w-7xl mx-auto w-full">
        <slot />
      </main>

    </div>

    <!-- Solid, Perfectly Aligned Sign Out Modal -->
    <Teleport to="body">
      <Transition
        enter-active-class="transition duration-200 ease-out"
        enter-from-class="opacity-0"
        enter-to-class="opacity-100"
        leave-active-class="transition duration-150 ease-in"
        leave-from-class="opacity-100"
        leave-to-class="opacity-0"
      >
        <div 
          v-if="showLogoutDialog" 
          class="fixed inset-0 z-[999] overflow-y-auto bg-black/60 backdrop-blur-sm flex items-center justify-center p-4"
          @click.self="showLogoutDialog = false"
        >
          <div 
            class="relative bg-white rounded-2xl max-w-md w-full p-6 shadow-2xl border border-gray-100 transform transition-all text-left"
          >
            <!-- Header with Close Icon -->
            <div class="flex items-start justify-between mb-4">
              <div class="flex items-center gap-3">
                <div class="w-10 h-10 rounded-full bg-red-50 text-red-600 flex items-center justify-center flex-shrink-0">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"></path>
                    <polyline points="16 17 21 12 16 7"></polyline>
                    <line x1="21" y1="12" x2="9" y2="12"></line>
                  </svg>
                </div>
                <div>
                  <h3 class="text-lg font-bold text-gray-900 leading-snug">Sign Out</h3>
                  <p class="text-xs text-gray-400">Volunteer Portal</p>
                </div>
              </div>
              
              <button 
                @click="showLogoutDialog = false"
                class="text-gray-400 hover:text-gray-600 p-1.5 rounded-lg hover:bg-gray-100 transition-colors"
                aria-label="Close"
              >
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
              </button>
            </div>

            <!-- Body Text -->
            <p class="text-sm text-gray-600 mb-6 leading-relaxed">
              Are you sure you want to sign out of the Volunteer Portal? You will need to enter your credentials to log back in.
            </p>

            <!-- Action Buttons: Clean horizontal layout with Cancel and Red Sign Out -->
            <div class="flex items-center justify-end gap-3 pt-3 border-t border-gray-100">
              <button 
                @click="showLogoutDialog = false"
                class="px-4 py-2 text-xs font-semibold text-gray-700 bg-white hover:bg-gray-50 border border-gray-200 rounded-xl transition-all shadow-sm"
              >
                Cancel
              </button>
              <button 
                @click="logout"
                :disabled="loggingOut"
                class="inline-flex items-center gap-2 px-5 py-2 text-xs font-semibold text-white bg-red-600 hover:bg-red-700 rounded-xl shadow-sm transition-all disabled:opacity-50"
              >
                <svg v-if="loggingOut" class="animate-spin -ml-0.5 mr-1 h-3.5 w-3.5 text-white" fill="none" viewBox="0 0 24 24">
                  <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                  <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8v8H4z"></path>
                </svg>
                <span>{{ loggingOut ? 'Signing out...' : 'Sign Out' }}</span>
              </button>
            </div>
          </div>
        </div>
      </Transition>
    </Teleport>

  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'

const route = useRoute()
const router = useRouter()
const portalSettings = ref({})
const userEmail = ref('')
const displayName = ref('Volunteer')
const userInitials = ref('V')
const userImage = ref('')
const mobileMenuOpen = ref(false)
const showLogoutDialog = ref(false)
const loggingOut = ref(false)

const globalSearch = ref('')
const notificationsOpen = ref(false)
const profileMenuOpen = ref(false)
const unreadCount = ref(2)
const notificationsRef = ref(null)
const profileMenuRef = ref(null)

const formattedTodayDate = computed(() => {
  const options = { weekday: 'short', month: 'short', day: 'numeric', year: 'numeric' }
  return new Date().toLocaleDateString('en-US', options)
})

const currentPageInfo = computed(() => {
  const path = route.path
  if (path === '/') return { title: 'Dashboard', subtitle: 'Overview & metrics' }
  if (path.startsWith('/opportunities')) return { title: 'Opportunities', subtitle: 'Browse community causes' }
  if (path.startsWith('/assignments')) return { title: 'My Assignments', subtitle: 'Active & completed roles' }
  if (path.startsWith('/shifts')) return { title: 'My Shifts', subtitle: 'Upcoming & past schedules' }
  if (path.startsWith('/attendance')) return { title: 'Attendance Record', subtitle: 'Service hours log' }
  if (path.startsWith('/profile')) return { title: 'Profile Settings', subtitle: 'Manage your volunteer info' }
  return { title: 'Volunteer Portal', subtitle: 'ImpactSphere' }
})

const notificationsList = ref([
  {
    title: 'Attendance Verified',
    desc: '5.0 hours verified for Emergency Blood Donation Camp Support.',
    time: 'Today',
    iconBg: 'bg-emerald-100 text-emerald-700',
    icon: '<svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>'
  },
  {
    title: 'Shift Assignment Ready',
    desc: 'You are enrolled in Volunteer Opportunities.',
    time: 'Oct 21',
    iconBg: 'bg-blue-100 text-blue-700',
    icon: '<svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line></svg>'
  },
  {
    title: 'Welcome to Volunteer Portal',
    desc: 'Thank you for contributing to your community with ImpactSphere.',
    time: 'Oct 20',
    iconBg: 'bg-amber-100 text-amber-700',
    icon: '<svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"></path></svg>'
  }
])

function toggleNotifications() {
  notificationsOpen.value = !notificationsOpen.value
  if (notificationsOpen.value) profileMenuOpen.value = false
}

function toggleProfileMenu() {
  profileMenuOpen.value = !profileMenuOpen.value
  if (profileMenuOpen.value) notificationsOpen.value = false
}

function handleSearch() {
  if (globalSearch.value.trim()) {
    router.push({ path: '/opportunities', query: { search: globalSearch.value.trim() } })
  }
}

function handleDocumentClick(e) {
  if (profileMenuRef.value && !profileMenuRef.value.contains(e.target)) {
    profileMenuOpen.value = false
  }
  if (notificationsRef.value && !notificationsRef.value.contains(e.target)) {
    notificationsOpen.value = false
  }
}

const navItems = [
  { 
    path: '/', 
    label: 'Dashboard', 
    icon: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline></svg>' 
  },
  { 
    path: '/opportunities', 
    label: 'Opportunities', 
    icon: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"></path><path d="M13.73 21a2 2 0 0 1-3.46 0"></path><line x1="2" y1="2" x2="22" y2="22"></line></svg>' 
  },
  { 
    path: '/assignments', 
    label: 'My Assignments', 
    icon: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>' 
  },
  { 
    path: '/shifts', 
    label: 'My Shifts', 
    icon: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>' 
  },
  { 
    path: '/attendance', 
    label: 'Attendance', 
    icon: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><polyline points="9 12 11 14 15 10"></polyline></svg>' 
  },
  { 
    path: '/profile', 
    label: 'Profile Settings', 
    icon: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>' 
  },
]

function isCurrentRoute(path) {
  if (path === '/') return route.path === '/'
  return route.path.startsWith(path)
}

function handleProfileImageUpdated(e) {
  if (e?.detail?.image) {
    userImage.value = e.detail.image
  }
}

function handleProfileUpdated(e) {
  if (e?.detail?.full_name) {
    displayName.value = e.detail.full_name
    const parts = e.detail.full_name.trim().split(/\s+/)
    if (parts.length >= 2) {
      userInitials.value = `${parts[0].charAt(0)}${parts[parts.length - 1].charAt(0)}`.toUpperCase()
    } else {
      userInitials.value = parts[0].slice(0, 2).toUpperCase()
    }
  }
}

onMounted(async () => {
  document.addEventListener('click', handleDocumentClick)
  window.addEventListener('volunteer-image-updated', handleProfileImageUpdated)
  window.addEventListener('volunteer-profile-updated', handleProfileUpdated)

  // 1. Fetch portal settings for dynamic branding logo and title
  try {
    const settingsRes = await fetch('/api/method/ngo.api.volunteer.get_portal_settings')
    const settingsData = await settingsRes.json()
    if (settingsData.message) {
      portalSettings.value = settingsData.message
    }
  } catch (e) {
    console.error('Failed to load portal settings:', e)
  }

  // 2. Fetch logged user details
  try {
    const res = await fetch('/api/method/frappe.auth.get_logged_user')
    const data = await res.json()
    if (data.message && data.message !== 'Guest') {
      userEmail.value = data.message

      // 2a. Fetch volunteer profile to get volunteer's image and full name
      try {
        const profRes = await fetch('/api/method/ngo.api.volunteer.my_profile')
        const profData = await profRes.json()
        if (profData.message) {
          const p = profData.message
          if (p.full_name) displayName.value = p.full_name
          if (p.image) userImage.value = p.image
        }
      } catch (err) {
        console.error('Volunteer profile fetch notice:', err)
      }
      
      // 2b. Fetch User details for fallback initials or user_image
      const userRes = await fetch(`/api/method/frappe.client.get?doctype=User&name=${encodeURIComponent(data.message)}`)
      const userData = await userRes.json()
      if (userData.message) {
        const u = userData.message
        if (!userImage.value && u.user_image) {
          userImage.value = u.user_image
        }
        const first = u.first_name || ''
        const last = u.last_name || ''
        const full = (first || last) ? `${first} ${last}`.trim() : (u.full_name || data.message)
        if (!displayName.value || displayName.value === 'Volunteer') {
          displayName.value = full
        }
        
        if (first && last) {
          userInitials.value = `${first.charAt(0)}${last.charAt(0)}`.toUpperCase()
        } else if (first) {
          userInitials.value = first.slice(0, 2).toUpperCase()
        } else if (displayName.value && displayName.value !== 'Volunteer') {
          const parts = displayName.value.trim().split(/\s+/)
          if (parts.length >= 2) {
            userInitials.value = `${parts[0].charAt(0)}${parts[parts.length - 1].charAt(0)}`.toUpperCase()
          } else {
            userInitials.value = parts[0].slice(0, 2).toUpperCase()
          }
        } else {
          userInitials.value = data.message.slice(0, 2).toUpperCase()
        }
      }
    }
  } catch (e) {
    console.error(e)
  }
})

onUnmounted(() => {
  document.removeEventListener('click', handleDocumentClick)
  window.removeEventListener('volunteer-image-updated', handleProfileImageUpdated)
  window.removeEventListener('volunteer-profile-updated', handleProfileUpdated)
})

async function logout() {
  loggingOut.value = true
  try {
    await fetch('/api/method/logout', { 
      method: 'POST', 
      headers: { ...(window.csrf_token && { 'X-Frappe-CSRF-Token': window.csrf_token }) } 
    })
    window.location.href = '/frontend/account/login'
  } catch (e) {
    console.error(e)
    loggingOut.value = false
    showLogoutDialog.value = false
  }
}
</script>
