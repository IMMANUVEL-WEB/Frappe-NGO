<template>
  <VolunteerLayout>
    <div class="max-w-6xl mx-auto pb-16 md:pb-0">
      <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center mb-8 gap-4">
        <div>
          <h1 class="text-3xl font-extrabold text-gray-900 tracking-tight">My Shifts</h1>
          <p class="text-gray-500 mt-1 text-sm font-medium">Your scheduled and past volunteering shifts.</p>
        </div>
        
        <div class="bg-white p-1 rounded-lg border border-gray-200 shadow-sm inline-flex">
          <button 
            @click="setTab('upcoming')" 
            :class="['px-4 py-2 text-sm font-semibold rounded-md transition-all', activeTab === 'upcoming' ? 'bg-blue-50 text-blue-700 shadow-sm' : 'text-gray-500 hover:text-gray-700']"
          >
            Upcoming
          </button>
          <button 
            @click="setTab('past')" 
            :class="['px-4 py-2 text-sm font-semibold rounded-md transition-all', activeTab === 'past' ? 'bg-blue-50 text-blue-700 shadow-sm' : 'text-gray-500 hover:text-gray-700']"
          >
            Past
          </button>
        </div>
      </div>
      
      <div v-if="shifts.loading" class="flex justify-center py-20">
        <LoadingText>Loading shifts...</LoadingText>
      </div>
      
      <div v-else-if="shifts.error" class="bg-red-50 text-red-600 p-4 rounded-xl shadow-sm border border-red-100">
        {{ shifts.error.message || shifts.error }}
      </div>
      
      <div v-else>
        <div v-if="!shifts.data || shifts.data.length === 0" class="flex flex-col items-center justify-center bg-white rounded-2xl border border-gray-100 p-16 shadow-sm">
          <div class="w-20 h-20 bg-gray-50 rounded-full flex items-center justify-center mb-6 text-gray-400">
            <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>
          </div>
          <p class="text-gray-500 font-medium text-lg">No {{ activeTab }} shifts found.</p>
        </div>
        
        <div v-else class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-6">
          <div 
            v-for="s in shifts.data" 
            :key="s.name"
            class="bg-white rounded-2xl p-6 shadow-sm border border-gray-100 hover:shadow-lg transition-all duration-300 transform hover:-translate-y-1 relative overflow-hidden"
          >
            <!-- Decorative accent based on status -->
            <div :class="['absolute top-0 left-0 right-0 h-1', getStatusGradient(s.participant_status)]"></div>
            
            <div class="flex justify-between items-start mb-4">
              <Badge :theme="getStatusTheme(s.participant_status)">
                {{ s.participant_status || s.status }}
              </Badge>
              <span class="text-xs font-bold text-gray-400">{{ s.name }}</span>
            </div>
            
            <h3 class="text-xl font-bold text-gray-900 leading-tight mb-2 line-clamp-2" :title="s.opportunity_title || s.opportunity">
              {{ s.opportunity_title || s.opportunity }}
            </h3>
            
            <p class="text-sm font-semibold text-gray-500 mb-6 line-clamp-1">
              Project: {{ s.project }}
            </p>
            
            <div class="bg-gray-50/80 rounded-xl p-4 flex flex-col gap-3">
              <div class="flex items-center gap-3">
                <div class="bg-blue-100 text-primary p-2 rounded-lg">
                  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>
                </div>
                <div>
                  <div class="text-xs font-bold text-gray-500 uppercase tracking-wider">Date</div>
                  <div class="font-bold text-gray-900">{{ formatDate(s.shift_date) }}</div>
                </div>
              </div>
              
              <div class="flex items-center gap-3">
                <div class="bg-cyan-100 text-cyan-600 p-2 rounded-lg">
                  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
                </div>
                <div>
                  <div class="text-xs font-bold text-gray-500 uppercase tracking-wider">Time</div>
                  <div class="font-bold text-gray-900">{{ formatTime(s.start_time) }} - {{ formatTime(s.end_time) }}</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </VolunteerLayout>
</template>

<script setup>
import { createResource, LoadingText, Badge } from "frappe-ui"
import { ref } from "vue"
import VolunteerLayout from "../components/VolunteerLayout.vue"

const activeTab = ref('upcoming')

const shifts = createResource({
  url: "ngo.api.volunteer.my_shifts",
  method: "GET",
  auto: true,
  params: {
    period: activeTab.value
  }
})

function setTab(tab) {
  activeTab.value = tab
  shifts.params.period = tab
  shifts.fetch()
}

function getStatusTheme(status) {
  if (status === 'Confirmed') return 'blue'
  if (status === 'Present') return 'green'
  if (status === 'Absent' || status === 'Cancelled') return 'red'
  return 'gray'
}

function getStatusGradient(status) {
  if (status === 'Confirmed') return 'bg-gradient-to-r from-blue-400 to-blue-600'
  if (status === 'Present') return 'bg-gradient-to-r from-green-400 to-green-600'
  if (status === 'Absent' || status === 'Cancelled') return 'bg-gradient-to-r from-red-400 to-red-600'
  return 'bg-gradient-to-r from-gray-300 to-gray-400'
}

function formatDate(dateStr) {
  if (!dateStr) return "-"
  return new Date(dateStr).toLocaleDateString("en-GB", {
    weekday: 'short', day: "numeric", month: "short", year: "numeric"
  })
}

function formatTime(timeStr) {
  if (!timeStr) return "-"
  const [h, m] = timeStr.split(':')
  const date = new Date()
  date.setHours(parseInt(h, 10))
  date.setMinutes(parseInt(m, 10))
  return date.toLocaleTimeString("en-US", { hour: 'numeric', minute: '2-digit' })
}
</script>
