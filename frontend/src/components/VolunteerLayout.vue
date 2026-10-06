<template>
  <div class="min-h-screen bg-gray-50 flex flex-col md:flex-row font-sans">
    
    <!-- Mobile Header -->
    <div class="md:hidden bg-white border-b border-gray-200 px-4 py-3 flex justify-between items-center shadow-sm sticky top-0 z-20">
      <div class="font-bold text-xl bg-clip-text text-transparent bg-gradient-to-r from-primary to-secondary">
        Volunteer Portal
      </div>
      <button @click="mobileMenuOpen = !mobileMenuOpen" class="text-gray-600 hover:text-primary transition-colors p-1">
        <svg v-if="!mobileMenuOpen" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>
        <svg v-else xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
      </button>
    </div>

    <!-- Sidebar -->
    <div :class="[
      'fixed md:static inset-y-0 left-0 transform md:transform-none md:flex flex-col w-64 bg-sidebar border-r border-gray-200 z-10 transition-transform duration-300 ease-in-out shadow-xl md:shadow-none',
      mobileMenuOpen ? 'translate-x-0' : '-translate-x-full'
    ]">
      <div class="p-6 hidden md:block">
        <h2 class="text-2xl font-extrabold bg-clip-text text-transparent bg-gradient-to-r from-primary to-secondary tracking-tight">Volunteer Portal</h2>
      </div>
      
      <nav class="flex-1 px-4 py-4 md:py-0 space-y-2 mt-16 md:mt-0 overflow-y-auto">
        <router-link 
          v-for="item in navItems" 
          :key="item.path" 
          :to="item.path"
          class="flex items-center gap-3 px-4 py-3 text-sm font-medium rounded-xl transition-all duration-200 group relative overflow-hidden"
          :class="[
            $route.path === item.path 
              ? 'text-blue-700 bg-blue-50/80 shadow-sm border border-blue-100' 
              : 'text-gray-600 hover:bg-gray-50 hover:text-gray-900'
          ]"
          @click="mobileMenuOpen = false"
        >
          <div :class="[
            'p-1.5 rounded-lg transition-colors',
            $route.path === item.path ? 'bg-blue-100 text-primary' : 'bg-gray-100 text-gray-500 group-hover:bg-gray-200 group-hover:text-gray-700'
          ]" v-html="item.icon"></div>
          {{ item.label }}
        </router-link>
      </nav>

      <!-- Logout Section -->
      <div class="p-4 border-t border-gray-100 bg-gray-50/50">
        <div class="mb-3 px-2">
          <p class="text-xs font-semibold text-gray-400 uppercase tracking-wider mb-1">Logged in as</p>
          <p class="text-sm font-medium text-gray-700 truncate" :title="userEmail">{{ userEmail }}</p>
        </div>
        <button 
          @click="showLogoutDialog = true" 
          class="w-full flex items-center justify-center gap-2 px-4 py-2.5 bg-white border border-gray-200 text-gray-700 text-sm font-medium rounded-xl hover:bg-red-50 hover:text-red-600 hover:border-red-200 transition-all shadow-sm"
        >
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"></path><polyline points="16 17 21 12 16 7"></polyline><line x1="21" y1="12" x2="9" y2="12"></line></svg>
          Sign Out
        </button>
      </div>
    </div>
    
    <!-- Overlay for mobile sidebar -->
    <div 
      v-if="mobileMenuOpen" 
      @click="mobileMenuOpen = false"
      class="fixed inset-0 bg-gray-900/50 backdrop-blur-sm z-0 md:hidden"
    ></div>

    <!-- Main Content -->
    <div class="flex-1 overflow-auto bg-gray-50/30">
      <div class="p-4 md:p-8 max-w-6xl mx-auto h-full">
        <!-- Route Transition -->
        <slot />
      </div>
    </div>

    <!-- Logout Dialog -->
    <Dialog 
      v-model="showLogoutDialog"
      :options="{
        title: 'Sign Out',
        message: 'Are you sure you want to sign out of the Volunteer Portal? You will need to enter your credentials to log back in.',
        actions: [
          {
            label: 'Sign Out',
            theme: 'red',
            variant: 'solid',
            onClick: logout
          },
          {
            label: 'Cancel',
            onClick: () => { showLogoutDialog = false }
          }
        ]
      }"
    />

  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { Dialog, Button } from 'frappe-ui'

const router = useRouter()
const userEmail = ref('')
const mobileMenuOpen = ref(false)
const showLogoutDialog = ref(false)
const loggingOut = ref(false)

const navItems = [
  { path: '/', label: 'Dashboard', icon: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="7" height="9" rx="1"></rect><rect x="14" y="3" width="7" height="5" rx="1"></rect><rect x="14" y="12" width="7" height="9" rx="1"></rect><rect x="3" y="16" width="7" height="5" rx="1"></rect></svg>' },
  { path: '/opportunities', label: 'Opportunities', icon: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><path d="M12 8v4l3 3"></path></svg>' },
  { path: '/assignments', label: 'My Assignments', icon: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>' },
  { path: '/shifts', label: 'My Shifts', icon: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>' },
  { path: '/attendance', label: 'Attendance', icon: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>' },
  { path: '/profile', label: 'Profile Settings', icon: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>' },
]

onMounted(async () => {
  try {
    const res = await fetch('/api/method/frappe.auth.get_logged_user')
    const data = await res.json()
    if (data.message) {
      userEmail.value = data.message
    }
  } catch (e) {
    console.error(e)
  }
})

async function logout() {
  loggingOut.value = true
  try {
    await fetch('/api/method/logout', { method: 'POST' })
    window.location.href = '/frontend/account/login'
  } catch (e) {
    console.error(e)
    loggingOut.value = false
    showLogoutDialog.value = false
  }
}
</script>

<style>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.2s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
