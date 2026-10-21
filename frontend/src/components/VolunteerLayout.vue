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
      
      <!-- Top Header Bar: Cleaned (Network selector, search bar, and notification bell removed) -->
      <header class="bg-white border-b border-gray-100 px-6 lg:px-8 py-3.5 flex items-center justify-end sticky top-0 z-20 shadow-[0_1px_3px_rgba(0,0,0,0.02)]">
        
        <!-- Right: Profile Avatar Button with Volunteer Image -->
        <router-link 
          to="/profile" 
          class="w-9 h-9 rounded-full bg-[#043226] text-white font-bold text-xs flex items-center justify-center hover:ring-2 hover:ring-emerald-700/30 transition-all shadow-sm uppercase overflow-hidden"
          :title="displayName"
        >
          <img v-if="userImage" :src="userImage" :alt="displayName" class="w-full h-full object-cover" />
          <span v-else>{{ userInitials }}</span>
        </router-link>

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
import { ref, onMounted, onUnmounted } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const portalSettings = ref({})
const userEmail = ref('')
const displayName = ref('Volunteer')
const userInitials = ref('V')
const userImage = ref('')
const mobileMenuOpen = ref(false)
const showLogoutDialog = ref(false)
const loggingOut = ref(false)

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
    path: '/impact-badges', 
    label: 'Impact & Badges', 
    icon: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="7"></circle><polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"></polyline></svg>' 
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

onMounted(async () => {
  window.addEventListener('volunteer-image-updated', handleProfileImageUpdated)

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
  window.removeEventListener('volunteer-image-updated', handleProfileImageUpdated)
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
