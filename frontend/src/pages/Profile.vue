<template>
  <VolunteerLayout>
    <div class="max-w-4xl mx-auto pb-16 md:pb-0">
      <div class="flex items-center gap-4 mb-8">
        <h1 class="text-3xl font-extrabold text-gray-900 tracking-tight">Profile Settings</h1>
      </div>
      
      <div v-if="profile.loading" class="flex justify-center py-20">
        <LoadingText>Loading your profile...</LoadingText>
      </div>
      
      <div v-else-if="profile.error" class="bg-red-50 text-red-600 p-4 rounded-xl shadow-sm border border-red-100">
        {{ profile.error.message || profile.error }}
      </div>
      
      <div v-else-if="profile.data" class="space-y-6">
        
        <!-- Header Card -->
        <div class="bg-white rounded-2xl shadow-sm border border-gray-100 overflow-hidden">
          <div class="h-32 bg-gradient-to-r from-primary to-secondary relative"></div>
          <div class="px-8 pb-8 relative">
            <div class="flex flex-col sm:flex-row items-center sm:items-end gap-6 -mt-16 mb-4">
              
              <!-- Avatar Upload -->
              <div class="relative group">
                <div class="w-32 h-32 rounded-2xl border-4 border-white shadow-lg overflow-hidden bg-gray-100 flex justify-center items-center">
                  <img v-if="profile.data.image" :src="profile.data.image" class="w-full h-full object-cover" />
                  <div v-else class="text-gray-400">
                    <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
                  </div>
                </div>
                <div class="absolute inset-0 rounded-2xl bg-black/50 opacity-0 group-hover:opacity-100 transition-opacity flex justify-center items-center border-4 border-transparent cursor-pointer" @click="triggerImageUpload">
                  <span class="text-white text-xs font-bold bg-black/40 px-2 py-1 rounded">Change</span>
                  <input type="file" ref="imageUploadInput" class="hidden" accept="image/*" @change="handleImageUpload" />
                </div>
              </div>
              
              <div class="text-center sm:text-left flex-1 pb-2">
                <h2 class="text-2xl font-bold text-gray-900 leading-none">{{ profile.data.full_name }}</h2>
                <p class="text-sm font-medium text-gray-500 mt-2">{{ profile.data.email }}</p>
                <div class="flex items-center justify-center sm:justify-start gap-2 mt-3">
                  <Badge :theme="profile.data.status === 'Active' ? 'green' : 'gray'">{{ profile.data.status }}</Badge>
                  <span class="text-xs text-gray-400">Joined {{ formatDate(profile.data.joined_on) }}</span>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Two Column Layout -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
          
          <!-- Left Column: Personal Info & Password -->
          <div class="md:col-span-2 space-y-6">
            <div class="bg-white rounded-2xl shadow-sm border border-gray-100 p-8">
              <h3 class="text-lg font-bold text-gray-900 mb-6 flex items-center gap-2">
                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="text-blue-500"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
                Contact Details
              </h3>
              
              <div class="space-y-5">
                <div>
                  <label class="block text-sm font-semibold text-gray-700 mb-1">Phone Number</label>
                  <input v-model="formData.phone" type="tel" class="w-full px-4 py-2 border border-gray-200 rounded-xl focus:ring-2 focus:ring-primary focus:border-primary outline-none transition-shadow bg-gray-50/50" />
                </div>
                <div>
                  <label class="block text-sm font-semibold text-gray-700 mb-1">Address</label>
                  <textarea v-model="formData.address" rows="3" class="w-full px-4 py-2 border border-gray-200 rounded-xl focus:ring-2 focus:ring-primary focus:border-primary outline-none transition-shadow bg-gray-50/50"></textarea>
                </div>
                <div class="pt-2 flex justify-end">
                  <Button variant="solid" theme="blue" :loading="savingInfo" @click="saveInfo">
                    Save Changes
                  </Button>
                </div>
              </div>
            </div>

            <!-- Password Update -->
            <div class="bg-white rounded-2xl shadow-sm border border-gray-100 p-8">
              <h3 class="text-lg font-bold text-gray-900 mb-6 flex items-center gap-2">
                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="text-secondary"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>
                Security
              </h3>
              
              <div class="space-y-4">
                <div v-if="pwdError" class="text-xs text-red-600 bg-red-50 p-2 rounded-lg font-medium">{{ pwdError }}</div>
                <div v-if="pwdSuccess" class="text-xs text-green-700 bg-green-50 p-2 rounded-lg font-medium">Password updated successfully!</div>
                
                <div>
                  <label class="block text-xs font-semibold text-gray-600 uppercase tracking-wider mb-1">Current Password</label>
                  <input v-model="pwdData.old" type="password" class="w-full px-4 py-2 border border-gray-200 rounded-xl focus:ring-2 focus:ring-secondary focus:border-secondary outline-none transition-shadow bg-gray-50/50" />
                </div>
                <div>
                  <label class="block text-xs font-semibold text-gray-600 uppercase tracking-wider mb-1">New Password</label>
                  <input v-model="pwdData.new" type="password" class="w-full px-4 py-2 border border-gray-200 rounded-xl focus:ring-2 focus:ring-secondary focus:border-secondary outline-none transition-shadow bg-gray-50/50" />
                </div>
                <div class="pt-2">
                  <Button variant="subtle" theme="cyan" :loading="savingPwd" @click="updatePassword">
                    Update Password
                  </Button>
                </div>
              </div>
            </div>
          </div>

          <!-- Right Column: Skills & Availability -->
          <div class="space-y-6">
            <div class="bg-gradient-to-br from-primary to-secondary rounded-2xl shadow-sm p-6 text-white text-center">
              <h3 class="text-lg font-bold mb-1 opacity-90">Total Impact</h3>
              <div class="text-5xl font-black">{{ profile.data.total_hours || 0 }}</div>
              <p class="text-sm opacity-80 mt-1">Hours Volunteered</p>
            </div>
            
            <div class="bg-white rounded-2xl shadow-sm border border-gray-100 p-6">
              <h3 class="text-base font-bold text-gray-900 mb-4 flex items-center gap-2">
                <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="text-yellow-500"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
                Your Skills
              </h3>
              <div v-if="!profile.data.skills || profile.data.skills.length === 0" class="text-sm text-gray-500">
                No skills listed yet.
              </div>
              <div v-else class="flex flex-wrap gap-2">
                <span 
                  v-for="(skill, i) in profile.data.skills" :key="i"
                  class="inline-flex items-center px-3 py-1 bg-gray-100 text-gray-800 text-xs font-semibold rounded-full"
                >
                  {{ skill.skill }} ({{ skill.proficiency }})
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
import { createResource, Button, LoadingText, Badge } from "frappe-ui"
import { ref, onMounted } from "vue"
import VolunteerLayout from "../components/VolunteerLayout.vue"

const imageUploadInput = ref(null)
const savingInfo = ref(false)
const savingPwd = ref(false)
const pwdError = ref("")
const pwdSuccess = ref(false)

const formData = ref({
  phone: '',
  address: ''
})

const pwdData = ref({
  old: '',
  new: ''
})

const profile = createResource({
  url: "ngo.api.volunteer.my_profile",
  method: "GET",
  auto: true,
  onSuccess(data) {
    formData.value.phone = data.phone || ''
    formData.value.address = data.address || ''
  }
})

function triggerImageUpload() {
  imageUploadInput.value.click()
}

async function handleImageUpload(e) {
  const file = e.target.files[0]
  if (!file) return
  
  const form = new FormData()
  form.append('file', file, file.name)
  form.append('is_private', 0)
  form.append('folder', 'Home/Attachments')

  try {
    // 1. Upload file
    const uploadRes = await fetch('/api/method/upload_file', {
      method: 'POST',
      body: form,
      headers: {
        'Accept': 'application/json'
      }
    })
    const uploadData = await uploadRes.json()
    
    if (uploadData.message && uploadData.message.file_url) {
      const fileUrl = uploadData.message.file_url
      
      // 2. Save to volunteer profile
      await fetch('/api/method/ngo.api.volunteer.update_my_profile', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          image: fileUrl
        })
      })
      
      // Refresh
      profile.fetch()
    }
  } catch (error) {
    alert("Failed to upload image")
    console.error(error)
  }
}

async function saveInfo() {
  savingInfo.value = true
  try {
    await fetch('/api/method/ngo.api.volunteer.update_my_profile', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        phone: formData.value.phone,
        address: formData.value.address
      })
    })
    await profile.fetch()
  } catch (err) {
    alert(err.message || "Failed to save profile")
  } finally {
    savingInfo.value = false
  }
}

async function updatePassword() {
  pwdError.value = ""
  pwdSuccess.value = false
  
  if (!pwdData.value.old || !pwdData.value.new) {
    pwdError.value = "Please fill in both fields"
    return
  }
  
  savingPwd.value = true
  try {
    const res = await fetch('/api/method/ngo.api.volunteer.update_password', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        old_password: pwdData.value.old,
        new_password: pwdData.value.new
      })
    })
    
    const data = await res.json()
    if (!res.ok || data.exc) {
      throw new Error(data.message || "Failed to update password")
    }
    
    pwdSuccess.value = true
    pwdData.value = { old: '', new: '' }
    
  } catch (err) {
    let msg = err.message
    if (msg && msg.includes("Incorrect old password")) {
      msg = "Incorrect current password"
    }
    pwdError.value = msg || "An error occurred"
  } finally {
    savingPwd.value = false
  }
}

function formatDate(dateStr) {
  if (!dateStr) return "-"
  return new Date(dateStr).toLocaleDateString("en-GB", {
    month: "long", year: "numeric"
  })
}
</script>
