<template>
  <VolunteerLayout>
    <div class="max-w-6xl mx-auto pb-16 md:pb-0">
      <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center mb-8 gap-4">
        <div>
          <h1 class="text-3xl font-extrabold text-gray-900 tracking-tight">Dashboard</h1>
          <p class="text-gray-500 mt-1 text-sm font-medium">Welcome back, let's make an impact today.</p>
        </div>
      </div>
      
      <div v-if="dashboard.loading" class="flex justify-center py-20">
        <LoadingText>Loading your dashboard...</LoadingText>
      </div>
      
      <div v-else-if="dashboard.error" class="bg-red-50 text-red-600 p-4 rounded-xl shadow-sm border border-red-100">
        {{ dashboard.error.message || dashboard.error }}
      </div>
      
      <div v-else class="space-y-8">
        
        <!-- Key Metrics Cards -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div class="bg-gradient-to-br from-primary to-blue-700 p-6 rounded-2xl shadow-lg shadow-blue-500/20 text-white transform hover:-translate-y-1 transition-transform duration-300">
            <h3 class="text-blue-100 font-semibold mb-2 text-sm uppercase tracking-wider">Total Impact</h3>
            <div class="text-5xl font-black mb-2">{{ dashboard.data.total_hours || 0 }}</div>
            <p class="text-blue-100 text-sm font-medium">Hours Volunteered</p>
          </div>
          
          <div class="bg-gradient-to-br from-cyan-500 to-cyan-600 p-6 rounded-2xl shadow-lg shadow-cyan-500/20 text-white transform hover:-translate-y-1 transition-transform duration-300">
            <h3 class="text-cyan-100 font-semibold mb-2 text-sm uppercase tracking-wider">This Month</h3>
            <div class="text-5xl font-black mb-2">{{ dashboard.data.hours_this_month || 0 }}</div>
            <p class="text-cyan-100 text-sm font-medium">Hours Contributed</p>
          </div>
          
          <div class="bg-white border border-gray-100 p-6 rounded-2xl shadow-lg hover:shadow-xl transition-shadow duration-300 flex flex-col justify-between">
            <div>
              <h3 class="text-gray-500 font-semibold mb-2 text-sm uppercase tracking-wider">Active Assignments</h3>
              <div class="text-5xl font-black text-gray-900">{{ dashboard.data.active_assignments || 0 }}</div>
            </div>
            <router-link to="/assignments" class="text-primary text-sm font-bold mt-4 flex items-center gap-1 hover:text-blue-700 transition-colors">
              View all
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
            </router-link>
          </div>
        </div>

        <!-- Next Shift & Upcoming -->
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
          
          <div class="bg-white rounded-2xl shadow-sm border border-gray-100 p-6 flex flex-col h-full">
            <h2 class="text-xl font-bold text-gray-900 mb-6 flex items-center gap-2">
              <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" class="text-orange-500"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
              Next Up
            </h2>
            
            <div v-if="dashboard.data.next_shift" class="flex-1 bg-gradient-to-r from-gray-900 to-gray-800 rounded-xl p-6 text-white shadow-inner flex flex-col justify-center">
              <div class="text-sm font-semibold text-gray-400 uppercase tracking-wider mb-2">Shift Details</div>
              <h3 class="text-2xl font-bold mb-4">{{ dashboard.data.next_shift.opportunity_title }}</h3>
              
              <div class="space-y-3">
                <div class="flex items-center gap-3">
                  <div class="w-8 h-8 rounded-full bg-white/10 flex items-center justify-center">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>
                  </div>
                  <div>
                    <div class="text-sm font-medium text-gray-300">Date</div>
                    <div class="font-bold">{{ formatDate(dashboard.data.next_shift.date) }}</div>
                  </div>
                </div>
                
                <div class="flex items-center gap-3">
                  <div class="w-8 h-8 rounded-full bg-white/10 flex items-center justify-center">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
                  </div>
                  <div>
                    <div class="text-sm font-medium text-gray-300">Time</div>
                    <div class="font-bold">{{ formatTime(dashboard.data.next_shift.start_time) }} - {{ formatTime(dashboard.data.next_shift.end_time) }}</div>
                  </div>
                </div>
              </div>
            </div>
            <div v-else class="flex-1 flex flex-col items-center justify-center bg-gray-50 rounded-xl p-8 border border-dashed border-gray-200">
              <div class="w-16 h-16 bg-gray-100 rounded-full flex items-center justify-center mb-4 text-gray-400">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="17 8 12 3 7 8"></polyline><line x1="12" y1="3" x2="12" y2="15"></line></svg>
              </div>
              <p class="text-gray-500 font-medium text-center">No shifts scheduled right now.</p>
              <router-link to="/opportunities" class="mt-4">
                <Button variant="subtle">Find Opportunities</Button>
              </router-link>
            </div>
          </div>
          
          <div class="bg-white rounded-2xl shadow-sm border border-gray-100 p-6 flex flex-col h-full">
            <div class="flex justify-between items-center mb-6">
              <h2 class="text-xl font-bold text-gray-900 flex items-center gap-2">
                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" class="text-blue-500"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
                Upcoming Shifts
              </h2>
              <router-link to="/shifts" class="text-sm font-semibold text-primary hover:text-blue-800 transition-colors">See all</router-link>
            </div>
            
            <div v-if="!dashboard.data.upcoming_shifts || dashboard.data.upcoming_shifts.length === 0" class="flex-1 flex flex-col items-center justify-center bg-gray-50 rounded-xl p-8">
              <p class="text-gray-500 font-medium text-center">No upcoming shifts scheduled.</p>
            </div>
            <div v-else class="space-y-4">
              <div 
                v-for="(shift, idx) in dashboard.data.upcoming_shifts" 
                :key="idx" 
                class="flex flex-col sm:flex-row justify-between items-start sm:items-center p-4 bg-gray-50 hover:bg-gray-100 rounded-xl transition-colors gap-4"
              >
                <div>
                  <h4 class="font-bold text-gray-900">{{ shift.opportunity_title }}</h4>
                  <p class="text-sm font-medium text-gray-500">{{ formatDate(shift.date) }} • {{ formatTime(shift.start_time) }}</p>
                </div>
                <Badge theme="blue">Scheduled</Badge>
              </div>
            </div>
          </div>

        </div>
      </div>
    </div>
  </VolunteerLayout>
</template>

<script setup>
import { createResource, LoadingText, Badge, Button } from "frappe-ui"
import VolunteerLayout from "../components/VolunteerLayout.vue"

const dashboard = createResource({
  url: "ngo.api.volunteer.my_dashboard",
  method: "GET",
  auto: true
})

function formatDate(dateStr) {
  if (!dateStr) return "-"
  return new Date(dateStr).toLocaleDateString("en-GB", {
    day: "numeric", month: "short", year: "numeric"
  })
}

function formatTime(timeStr) {
  if (!timeStr) return "-"
  // timeStr is usually HH:MM:SS
  const [h, m] = timeStr.split(':')
  const date = new Date()
  date.setHours(parseInt(h, 10))
  date.setMinutes(parseInt(m, 10))
  return date.toLocaleTimeString("en-US", { hour: 'numeric', minute: '2-digit' })
}
</script>
