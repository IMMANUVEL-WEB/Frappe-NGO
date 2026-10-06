<template>
  <div class="min-h-screen bg-login flex items-center justify-center p-4 py-12">
    <div class="w-full max-w-4xl bg-white/10 backdrop-blur-xl border border-white/20 rounded-2xl shadow-2xl overflow-hidden p-8">
      <div class="text-center mb-8">
        <h1 class="text-3xl font-extrabold text-white tracking-tight mb-2">Volunteer Application</h1>
        <p class="text-cyan-100 text-sm font-medium">Join our community and make an impact.</p>
      </div>

      <div v-if="success" class="bg-green-500/20 border border-green-500/50 text-green-200 p-6 rounded-xl text-center">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-12 w-12 mx-auto mb-4 text-green-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
        </svg>
        <h2 class="text-xl font-bold text-white mb-2">Application Submitted!</h2>
        <p class="text-sm">Thank you for your interest. We will review your application and email you shortly.</p>
        <router-link to="/account/login" class="mt-6 inline-block text-white hover:text-cyan-200 underline text-sm font-semibold">Return to Login</router-link>
      </div>

      <form v-else @submit.prevent="submitForm" class="space-y-5">
        <div v-if="error" class="bg-red-500/10 border border-red-500/50 text-red-200 p-3 rounded-lg text-sm text-center font-medium">
          {{ error }}
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-5">
          <div class="space-y-1">
            <label class="text-xs font-semibold text-gray-300 uppercase tracking-wider ml-1">Full Name</label>
            <input v-model="form.applicant_name" type="text" required class="block w-full px-4 py-3 border border-gray-600 rounded-xl leading-5 bg-gray-900/50 text-white placeholder-gray-500 focus:outline-none focus:border-white sm:text-sm" placeholder="John Doe" />
          </div>
          
          <div class="space-y-1">
            <label class="text-xs font-semibold text-gray-300 uppercase tracking-wider ml-1">Email Address</label>
            <input v-model="form.email" type="email" required class="block w-full px-4 py-3 border border-gray-600 rounded-xl leading-5 bg-gray-900/50 text-white placeholder-gray-500 focus:outline-none focus:border-white sm:text-sm" placeholder="you@example.com" />
          </div>

          <div class="space-y-1">
            <label class="text-xs font-semibold text-gray-300 uppercase tracking-wider ml-1">Phone Number</label>
            <input v-model="form.phone" type="tel" required class="block w-full px-4 py-3 border border-gray-600 rounded-xl leading-5 bg-gray-900/50 text-white placeholder-gray-500 focus:outline-none focus:border-white sm:text-sm" placeholder="+1234567890" />
          </div>

          <div class="space-y-1">
            <label class="text-xs font-semibold text-gray-300 uppercase tracking-wider ml-1">Date of Birth</label>
            <input v-model="form.date_of_birth" type="date" required class="block w-full px-4 py-3 border border-gray-600 rounded-xl leading-5 bg-gray-900/50 text-white placeholder-gray-500 focus:outline-none focus:border-white sm:text-sm" />
          </div>

          <div class="space-y-1 md:col-span-2">
            <label class="text-xs font-semibold text-gray-300 uppercase tracking-wider ml-1">Gender</label>
            <select v-model="form.gender" required class="block w-full px-4 py-3 border border-gray-600 rounded-xl leading-5 bg-gray-900/50 text-white focus:outline-none focus:border-white sm:text-sm">
              <option value="" disabled>Select Gender</option>
              <option value="Male">Male</option>
              <option value="Female">Female</option>
              <option value="Other">Other</option>
            </select>
          </div>
        </div>

        <div class="space-y-1">
          <label class="text-xs font-semibold text-gray-300 uppercase tracking-wider ml-1">Address</label>
          <textarea v-model="form.address" required rows="2" class="block w-full px-4 py-3 border border-gray-600 rounded-xl leading-5 bg-gray-900/50 text-white placeholder-gray-500 focus:outline-none focus:border-white sm:text-sm" placeholder="Your full address"></textarea>
        </div>

        <div class="pt-4 border-t border-gray-600/50">
          <div class="flex justify-between items-center mb-3">
            <label class="text-sm font-semibold text-white uppercase tracking-wider">Skills</label>
            <button type="button" @click="addSkill" class="text-xs font-bold text-cyan-300 hover:text-cyan-100 bg-cyan-900/30 px-3 py-1.5 rounded-lg border border-cyan-500/30 transition-all">+ Add Skill</button>
          </div>
          <div class="space-y-2">
            <div v-for="(skill, index) in form.skills" :key="'skill-'+index" class="flex gap-2 items-center bg-gray-900/50 p-2 rounded-xl border border-gray-600/50">
              <input v-model="skill.skill" type="text" placeholder="Skill (e.g. Teaching)" required class="flex-1 px-3 py-2 bg-transparent text-white border-none focus:outline-none text-sm" />
              <select v-model="skill.proficiency" required class="w-1/3 px-3 py-2 bg-gray-800 text-white border-none focus:outline-none rounded-lg text-sm">
                <option value="Beginner">Beginner</option>
                <option value="Intermediate">Intermediate</option>
                <option value="Advanced">Advanced</option>
              </select>
              <button type="button" @click="removeSkill(index)" class="text-red-400 hover:text-red-300 p-2 hover:bg-red-400/10 rounded-lg">?</button>
            </div>
            <p v-if="form.skills.length === 0" class="text-xs text-gray-400 italic">No skills added.</p>
          </div>
        </div>

        <div class="pt-4 border-t border-gray-600/50">
          <div class="flex justify-between items-center mb-3">
            <label class="text-sm font-semibold text-white uppercase tracking-wider">Availability</label>
            <button type="button" @click="addAvailability" class="text-xs font-bold text-cyan-300 hover:text-cyan-100 bg-cyan-900/30 px-3 py-1.5 rounded-lg border border-cyan-500/30 transition-all">+ Add Availability</button>
          </div>
          <div class="space-y-2">
            <div v-for="(avail, index) in form.availability" :key="'avail-'+index" class="flex flex-wrap md:flex-nowrap gap-2 items-center bg-gray-900/50 p-2 rounded-xl border border-gray-600/50">
              <select v-model="avail.day_of_week" required class="flex-1 min-w-[120px] px-3 py-2 bg-gray-800 text-white border-none focus:outline-none rounded-lg text-sm">
                <option value="" disabled>Select Day</option>
                <option v-for="day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']" :key="day" :value="day">{{day}}</option>
              </select>
              <input v-model="avail.from_time" type="time" required class="w-[110px] px-3 py-2 bg-gray-800 text-white border-none focus:outline-none rounded-lg text-sm" />
              <span class="text-gray-400 text-sm px-1">to</span>
              <input v-model="avail.to_time" type="time" required class="w-[110px] px-3 py-2 bg-gray-800 text-white border-none focus:outline-none rounded-lg text-sm" />
              <button type="button" @click="removeAvailability(index)" class="text-red-400 hover:text-red-300 p-2 hover:bg-red-400/10 rounded-lg">?</button>
            </div>
            <p v-if="form.availability.length === 0" class="text-xs text-gray-400 italic">No availability added.</p>
          </div>
        </div>

        <div class="pt-6 mt-4 flex flex-col md:flex-row gap-4 border-t border-gray-600/50">
          <router-link to="/account/login" class="w-full md:w-1/3 flex justify-center py-3 px-4 border border-gray-500 rounded-xl shadow-sm text-sm font-semibold text-gray-300 bg-transparent hover:bg-gray-800 transition-all text-center">Cancel</router-link>
          <button type="submit" :disabled="loading" class="w-full md:w-2/3 flex justify-center py-3 px-4 border border-transparent rounded-xl shadow-sm text-sm font-semibold text-login bg-white hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-white transition-all disabled:opacity-50">
            <span v-if="loading">Submitting...</span>
            <span v-else>Submit Application</span>
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { call } from 'frappe-ui'

const form = ref({
  applicant_name: '',
  email: '',
  phone: '',
  date_of_birth: '',
  gender: '',
  address: '',
  skills: [],
  availability: []
})

const loading = ref(false)
const error = ref('')
const success = ref(false)

function addSkill() {
  form.value.skills.push({ skill: '', proficiency: 'Beginner' })
}
function removeSkill(index) {
  form.value.skills.splice(index, 1)
}

function addAvailability() {
  form.value.availability.push({ day_of_week: '', from_time: '', to_time: '' })
}
function removeAvailability(index) {
  form.value.availability.splice(index, 1)
}

async function submitForm() {
  loading.value = true
  error.value = ''
  
  try {
    await call('ngo.api.volunteer.submit_application', {
      applicant_name: form.value.applicant_name,
      email: form.value.email,
      phone: form.value.phone,
      date_of_birth: form.value.date_of_birth,
      gender: form.value.gender,
      address: form.value.address,
      skills: JSON.stringify(form.value.skills),
      availability: JSON.stringify(form.value.availability)
    })
    success.value = true
  } catch (err) {
    error.value = err.message || err.exc || 'Failed to submit application. Please try again.'
  } finally {
    loading.value = false
  }
}
</script>
