<template>
  <VolunteerLayout>
    <div class="max-w-6xl mx-auto pb-16 md:pb-0">
      
      <!-- Hero Header -->
      <div class="relative bg-gray-900 rounded-3xl overflow-hidden mb-10 shadow-2xl">
        <div class="absolute inset-0 opacity-20">
          <svg class="h-full w-full" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="none"><defs><pattern id="dots" x="0" y="0" width="16" height="16" patternUnits="userSpaceOnUse"><circle fill="#ffffff" cx="2" cy="2" r="1.5"></circle></pattern></defs><rect x="0" y="0" width="100%" height="100%" fill="url(#dots)"></rect></svg>
        </div>
        <div class="absolute inset-0 bg-gradient-to-r from-blue-600/50 to-cyan-500/50 mix-blend-multiply"></div>
        <div class="relative px-8 py-14 md:px-12 md:py-20 flex flex-col md:flex-row items-center justify-between gap-8 text-white z-10 text-center md:text-left">
          <div class="max-w-2xl">
            <h1 class="text-4xl md:text-5xl font-black tracking-tight mb-4 leading-tight">Find Your Next <br class="hidden md:block"/>Volunteer Opportunity</h1>
            <p class="text-lg md:text-xl text-gray-200 font-medium">Discover open roles and projects where your skills can make a real difference in the community.</p>
          </div>
          <div class="w-24 h-24 md:w-32 md:h-32 bg-white/10 backdrop-blur-md rounded-full flex items-center justify-center border border-white/20 shadow-inner">
            <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="text-white"><circle cx="12" cy="12" r="10"></circle><path d="M12 8v4l3 3"></path></svg>
          </div>
        </div>
      </div>
      
      <div v-if="opportunities.loading" class="flex justify-center py-20">
        <LoadingText>Loading opportunities...</LoadingText>
      </div>
      
      <div v-else-if="opportunities.error" class="bg-red-50 text-red-600 p-4 rounded-xl shadow-sm border border-red-100">
        {{ opportunities.error.message || opportunities.error }}
      </div>
      
      <div v-else>
        <div v-if="!opportunities.data || opportunities.data.length === 0" class="flex flex-col items-center justify-center bg-white rounded-2xl border border-gray-100 p-16 shadow-sm">
          <div class="w-20 h-20 bg-gray-50 rounded-full flex items-center justify-center mb-6 text-gray-400">
            <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>
          </div>
          <p class="text-gray-500 font-medium text-lg">No open opportunities found at this time.</p>
          <p class="text-gray-400 text-sm mt-2">Please check back later!</p>
        </div>
        
        <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          <div 
            v-for="opp in opportunities.data" 
            :key="opp.name"
            class="bg-white rounded-2xl border border-gray-100 shadow-sm hover:shadow-xl transition-all duration-300 transform hover:-translate-y-1 flex flex-col overflow-hidden relative group"
          >
            <!-- Top Gradient Bar -->
            <div class="h-2 bg-gradient-to-r from-cyan-400 to-blue-500 w-full group-hover:h-3 transition-all duration-300"></div>
            
            <div class="p-6 flex flex-col flex-1">
              <div class="flex justify-between items-start mb-3">
                <Badge theme="blue" class="font-bold tracking-wide">Open Role</Badge>
                <div v-if="opp.vacancies" class="flex items-center gap-1 text-xs font-bold text-gray-500 bg-gray-100 px-2 py-1 rounded">
                  <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>
                  {{ opp.vacancies }} slots
                </div>
              </div>
              
              <h3 class="text-xl font-bold text-gray-900 mb-2 leading-tight">{{ opp.title }}</h3>
              <p class="text-sm font-semibold text-blue-600 mb-4 flex items-center gap-1.5">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"></path></svg>
                {{ opp.project }}
              </p>
              
              <div v-if="opp.location" class="flex items-center gap-2 text-sm text-gray-600 font-medium mb-3">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="text-gray-400"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
                {{ opp.location }}
              </div>
              
              <div v-if="opp.application_deadline" class="flex items-center gap-2 text-sm text-gray-600 font-medium mb-4">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="text-gray-400"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>
                Apply by {{ formatDate(opp.application_deadline) }}
              </div>
              
              <div class="prose prose-sm prose-gray max-w-none text-gray-600 mb-6 flex-1 line-clamp-3" v-html="opp.description"></div>
              
              <div v-if="opp.required_skills" class="mb-6">
                <p class="text-xs font-bold text-gray-400 uppercase tracking-wider mb-2">Required Skills</p>
                <div class="flex flex-wrap gap-2">
                  <span 
                    v-for="skill in opp.required_skills.split(',')" 
                    :key="skill"
                    class="inline-flex items-center px-2.5 py-1 rounded-md text-xs font-semibold bg-blue-50 text-blue-700 border border-blue-100"
                  >
                    {{ skill.trim() }}
                  </span>
                </div>
              </div>
              
              <div class="mt-auto pt-4 border-t border-gray-100">
                <Button 
                  v-if="!opp.has_interest"
                  @click="submitInterest(opp)"
                  variant="solid" 
                  theme="blue"
                  class="w-full justify-center group-hover:bg-blue-600 shadow-sm"
                  :loading="submitting === opp.name"
                  :disabled="submitting"
                >
                  Apply Now
                </Button>
                <div v-else class="flex items-center justify-center gap-2 py-2 px-4 bg-green-50 text-green-700 font-bold text-sm rounded-xl border border-green-100">
                  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>
                  Application Submitted
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
import { createResource, LoadingText, Badge, Button } from "frappe-ui"
import { ref } from "vue"
import VolunteerLayout from "../components/VolunteerLayout.vue"

const submitting = ref(null)

const opportunities = createResource({
  url: "ngo.api.volunteer.open_opportunities",
  method: "GET",
  auto: true
})

async function submitInterest(opp) {
  submitting.value = opp.name
  try {
    const res = await fetch('/api/method/ngo.api.volunteer.submit_interest', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        opportunity: opp.name
      })
    })
    
    if (res.ok) {
      opp.has_interest = true
    } else {
      const err = await res.json()
      alert(err.message || "Failed to submit interest")
    }
  } catch (error) {
    alert("An error occurred")
  } finally {
    submitting.value = null
  }
}

function formatDate(dateStr) {
  if (!dateStr) return "-"
  return new Date(dateStr).toLocaleDateString("en-GB", {
    day: "numeric", month: "short", year: "numeric"
  })
}
</script>

<style>
.line-clamp-3 {
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;  
  overflow: hidden;
}
.line-clamp-1 {
  display: -webkit-box;
  -webkit-line-clamp: 1;
  -webkit-box-orient: vertical;  
  overflow: hidden;
}
</style>
