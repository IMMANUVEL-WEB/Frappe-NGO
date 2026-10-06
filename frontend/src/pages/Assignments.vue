<template>
  <VolunteerLayout>
    <div class="max-w-4xl mx-auto pb-16 md:pb-0">
      <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center mb-6 gap-4">
        <h1 class="text-2xl font-bold">My Assignments</h1>
        
        <!-- Status Filter -->
        <div class="flex items-center gap-2">
          <span class="text-sm font-medium text-gray-600">Status:</span>
          <select 
            v-model="statusFilter"
            @change="assignments.fetch()"
            class="form-select text-sm border-gray-300 rounded-md shadow-sm focus:border-primary focus:ring-primary"
          >
            <option value="">All</option>
            <option value="Assigned">Assigned</option>
            <option value="Active">Active</option>
            <option value="Completed">Completed</option>
            <option value="Withdrawn">Withdrawn</option>
          </select>
        </div>
      </div>
      
      <div v-if="assignments.loading" class="flex justify-center py-10">
        <LoadingText>Loading assignments...</LoadingText>
      </div>
      
      <div v-else-if="assignments.error" class="bg-red-50 text-red-600 p-4 rounded-lg">
        {{ assignments.error.message || assignments.error }}
      </div>
      
      <div v-else>
        <div v-if="!assignments.data || assignments.data.length === 0" class="bg-white p-10 text-center text-gray-500 rounded-lg shadow-sm border border-gray-100">
          No assignments found matching the selected status.
        </div>
        
        <div v-else class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div 
            v-for="assignment in assignments.data" 
            :key="assignment.name"
            class="bg-white p-5 rounded-lg shadow-sm border border-gray-100 hover:shadow-md transition-shadow"
          >
            <div class="flex justify-between items-start mb-2">
              <h2 class="text-lg font-bold text-gray-900 line-clamp-1" :title="assignment.opportunity_title">
                {{ assignment.opportunity_title }}
              </h2>
              <Badge :theme="getStatusTheme(assignment.status)" size="sm">{{ assignment.status }}</Badge>
            </div>
            
            <div class="text-sm text-gray-600 font-medium mb-3">
              {{ assignment.project }}
            </div>
            
            <div class="space-y-1 text-sm text-gray-600">
              <div class="flex items-center gap-2">
                <span class="font-medium w-12 text-gray-500">Role:</span>
                <span>{{ assignment.role || 'Volunteer' }}</span>
              </div>
              <div class="flex items-center gap-2">
                <span class="font-medium w-12 text-gray-500">Dates:</span>
                <span>
                  {{ formatDate(assignment.from_date) }} 
                  {{ assignment.to_date ? ' - ' + formatDate(assignment.to_date) : ' onwards' }}
                </span>
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

const statusFilter = ref("")

const assignments = createResource({
  url: "ngo.api.volunteer.my_assignments",
  method: "GET",
  makeParams() {
    return statusFilter.value ? { status: statusFilter.value } : {}
  },
  auto: true
})

function formatDate(dateStr) {
  if (!dateStr) return ""
  return new Date(dateStr).toLocaleDateString("en-GB", {
    day: "numeric", month: "short", year: "numeric"
  })
}

function getStatusTheme(status) {
  const map = {
    'Active': 'green',
    'Assigned': 'blue',
    'Completed': 'gray',
    'Withdrawn': 'red'
  }
  return map[status] || 'gray'
}
</script>
