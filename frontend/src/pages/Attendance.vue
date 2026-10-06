<template>
  <VolunteerLayout>
    <div class="max-w-6xl mx-auto pb-16 md:pb-0">
      <div class="flex flex-col md:flex-row justify-between items-start md:items-center mb-8 gap-6">
        <div>
          <h1 class="text-3xl font-extrabold text-gray-900 tracking-tight">Attendance Record</h1>
          <p class="text-gray-500 mt-1 text-sm font-medium">Track the hours you've contributed.</p>
        </div>
        
        <div class="flex items-center gap-3 w-full md:w-auto">
          <input 
            type="date" 
            v-model="filters.from_date" 
            class="px-4 py-2 border border-gray-200 rounded-lg text-sm bg-white shadow-sm focus:outline-none focus:ring-2 focus:ring-primary w-full md:w-auto"
            title="From Date"
          />
          <span class="text-gray-400 font-medium">to</span>
          <input 
            type="date" 
            v-model="filters.to_date" 
            class="px-4 py-2 border border-gray-200 rounded-lg text-sm bg-white shadow-sm focus:outline-none focus:ring-2 focus:ring-primary w-full md:w-auto"
            title="To Date"
          />
          <Button @click="applyFilters" variant="solid" theme="blue" class="px-6 shadow-sm">
            Filter
          </Button>
        </div>
      </div>
      
      <div v-if="attendance.loading" class="flex justify-center py-20">
        <LoadingText>Loading records...</LoadingText>
      </div>
      
      <div v-else-if="attendance.error" class="bg-red-50 text-red-600 p-4 rounded-xl shadow-sm border border-red-100">
        {{ attendance.error.message || attendance.error }}
      </div>
      
      <div v-else class="space-y-6">
        <div class="bg-gradient-to-r from-primary to-secondary rounded-2xl shadow-sm p-6 text-white flex flex-col md:flex-row items-center justify-between gap-6">
          <div class="flex items-center gap-4">
            <div class="w-12 h-12 bg-white/20 rounded-full flex items-center justify-center backdrop-blur-sm">
              <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
            </div>
            <div>
              <h2 class="text-lg font-bold opacity-90">Total Hours in Period</h2>
              <p class="text-sm text-blue-100">Based on your current filter</p>
            </div>
          </div>
          <div class="text-4xl font-black">{{ attendance.data.period_total || 0 }} <span class="text-xl font-bold opacity-80">hrs</span></div>
        </div>
        
        <div class="bg-white rounded-2xl border border-gray-100 shadow-sm overflow-hidden">
          <div v-if="!attendance.data.data || attendance.data.data.length === 0" class="flex flex-col items-center justify-center p-16">
            <div class="w-20 h-20 bg-gray-50 rounded-full flex items-center justify-center mb-4 text-gray-300">
              <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
            </div>
            <p class="text-gray-500 font-medium">No attendance records found for this period.</p>
          </div>
          
          <div v-else class="overflow-x-auto">
            <table class="w-full text-left border-collapse">
              <thead>
                <tr class="bg-gray-50/80 border-b border-gray-100 text-xs uppercase tracking-wider text-gray-500 font-bold">
                  <th class="px-6 py-4 rounded-tl-xl">Date</th>
                  <th class="px-6 py-4">Opportunity</th>
                  <th class="px-6 py-4">Status</th>
                  <th class="px-6 py-4">In Time</th>
                  <th class="px-6 py-4">Out Time</th>
                  <th class="px-6 py-4 text-right rounded-tr-xl">Hours</th>
                </tr>
              </thead>
              <tbody class="divide-y divide-gray-100 text-sm font-medium text-gray-700">
                <tr v-for="row in attendance.data.data" :key="row.name" class="hover:bg-gray-50/50 transition-colors">
                  <td class="px-6 py-4 whitespace-nowrap">{{ formatDate(row.date) }}</td>
                  <td class="px-6 py-4">
                    <div class="text-gray-900 font-bold">{{ row.opportunity_title || '-' }}</div>
                    <div class="text-xs text-gray-500 mt-0.5">{{ row.project || '-' }}</div>
                  </td>
                  <td class="px-6 py-4">
                    <Badge :theme="row.status === 'Present' ? 'green' : (row.status === 'Absent' ? 'red' : 'orange')">
                      {{ row.status }}
                    </Badge>
                  </td>
                  <td class="px-6 py-4 whitespace-nowrap">{{ formatTime(row.in_time) }}</td>
                  <td class="px-6 py-4 whitespace-nowrap">{{ formatTime(row.out_time) }}</td>
                  <td class="px-6 py-4 whitespace-nowrap text-right font-bold text-primary">
                    {{ row.total_hours ? parseFloat(row.total_hours).toFixed(1) : '0.0' }}
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  </VolunteerLayout>
</template>

<script setup>
import { createResource, LoadingText, Badge, Button } from "frappe-ui"
import { ref } from "vue"
import VolunteerLayout from "../components/VolunteerLayout.vue"

const filters = ref({
  from_date: "",
  to_date: ""
})

const attendance = createResource({
  url: "ngo.api.volunteer.my_attendance",
  method: "GET",
  auto: true
})

function applyFilters() {
  const p = {}
  if (filters.value.from_date) p.from_date = filters.value.from_date
  if (filters.value.to_date) p.to_date = filters.value.to_date
  attendance.params = p
  attendance.fetch()
}

function formatDate(dateStr) {
  if (!dateStr) return "-"
  return new Date(dateStr).toLocaleDateString("en-GB", {
    day: "numeric", month: "short", year: "numeric"
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
