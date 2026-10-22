<template>
  <VolunteerLayout>
    <div class="max-w-7xl mx-auto space-y-6 pb-16">
      <!-- Top Breadcrumb & Header -->
      <div>
        <nav class="flex items-center gap-1.5 text-xs text-gray-400 font-medium mb-1">
          <router-link to="/" class="hover:text-emerald-700 transition-colors flex items-center gap-1">
            <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path>
              <polyline points="9 22 9 12 15 12 15 22"></polyline>
            </svg>
          </router-link>
          <span>&rsaquo;</span>
          <span class="text-gray-600">Profile Settings</span>
        </nav>

        <h1 class="text-2xl sm:text-3xl font-extrabold text-gray-900 tracking-tight">
          My Profile
        </h1>
        <p class="text-gray-500 text-sm mt-0.5">
          Manage your personal information, skills and account settings.
        </p>
      </div>

      <!-- Loading State -->
      <div v-if="profileResource.loading" class="flex justify-center py-16">
        <div class="flex flex-col items-center gap-3">
          <div class="w-10 h-10 border-4 border-emerald-200 border-t-emerald-600 rounded-full animate-spin"></div>
          <p class="text-sm font-medium text-gray-500">Loading profile...</p>
        </div>
      </div>

      <div v-else-if="profileResource.error" class="bg-red-50 text-red-600 p-6 rounded-2xl border border-red-100">
        {{ profileResource.error.message || profileResource.error }}
      </div>

      <!-- Real Profile Content -->
      <div v-else class="space-y-6">
        <!-- Top Hero Profile Card (faithful to design screenshot) -->
        <div class="bg-white rounded-3xl border border-gray-100 shadow-sm overflow-hidden relative">
          <!-- Top Emerald Botanical Banner with Wave -->
          <div class="h-32 sm:h-36 bg-gradient-to-r from-[#032e22] via-[#054434] to-[#075642] relative overflow-hidden">
            <!-- Translucent Organic Leaves Foliage on Right -->
            <div class="absolute right-0 top-0 bottom-0 w-80 pointer-events-none opacity-25 flex items-center justify-end pr-6">
              <svg class="h-full w-auto text-emerald-100" viewBox="0 0 320 160" fill="currentColor">
                <path d="M190,130 C170,80 210,25 285,15 C295,70 255,120 190,130 Z" />
                <path d="M150,150 C145,95 180,50 245,40 C250,95 215,140 150,150 Z" />
                <path d="M230,95 C240,55 275,35 305,30 C305,75 270,95 230,95 Z" />
                <path d="M110,160 C120,110 150,80 200,75 C195,125 160,155 110,160 Z" />
              </svg>
            </div>

            <!-- Gentle curved wave dividing dark green banner and white base -->
            <svg 
              class="absolute bottom-0 left-0 right-0 w-full h-10 sm:h-12 text-white" 
              viewBox="0 0 1200 120" 
              preserveAspectRatio="none"
              fill="currentColor"
            >
              <path d="M0,20 C180,95 380,10 650,45 C920,80 1080,25 1200,50 L1200,120 L0,120 Z"></path>
            </svg>
          </div>

          <!-- Bottom Details Section (White Background) -->
          <div class="px-6 sm:px-8 pb-6 pt-3 relative bg-white">
            <div class="flex flex-col sm:flex-row sm:items-end justify-between gap-6">
              
              <!-- Left: Avatar Card (Pops up across banner) + User Information (firmly on white) -->
              <div class="flex flex-col sm:flex-row items-center sm:items-end gap-5 sm:gap-6">
                
                <!-- White Rounded Card Container for Avatar - Negative top margin ONLY on avatar -->
                <div 
                  class="relative -mt-16 sm:-mt-20 bg-white p-2 sm:p-2.5 rounded-3xl shadow-lg border border-gray-100 flex-shrink-0 group cursor-pointer z-10"
                  @click="triggerPhotoUpload"
                >
                  <div class="w-24 h-24 sm:w-28 sm:h-28 rounded-2xl overflow-hidden bg-amber-100 flex items-center justify-center">
                    <img
                      v-if="profileData.image"
                      :src="profileData.image"
                      alt="Profile Avatar"
                      class="w-full h-full object-cover"
                    />
                    <div v-else class="w-full h-full bg-[#054434] text-white flex items-center justify-center font-bold text-2xl uppercase">
                      {{ (profileData.full_name || 'V').slice(0, 2) }}
                    </div>
                  </div>

                  <!-- Dark Green Camera Button Badge -->
                  <button
                    type="button"
                    class="absolute bottom-1 right-1 sm:bottom-1.5 sm:right-1.5 w-7 h-7 sm:w-8 sm:h-8 rounded-full bg-[#032e22] text-white flex items-center justify-center border-2 border-white shadow-md hover:bg-[#064e3b] transition-all"
                    title="Change Photo"
                  >
                    <svg class="w-3.5 h-3.5 sm:w-4 sm:h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                      <path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z"></path>
                      <circle cx="12" cy="13" r="4"></circle>
                    </svg>
                  </button>
                  <input
                    type="file"
                    ref="fileInput"
                    class="hidden"
                    accept="image/*"
                    @change="handlePhotoUpload"
                  />
                </div>

                <!-- Name, Email, Status & Joined Date - Sits completely on white background -->
                <div class="text-center sm:text-left space-y-1 pb-1">
                  <h2 class="text-2xl sm:text-3xl font-black text-gray-950 tracking-tight leading-snug">
                    {{ profileData.full_name || "Volunteer" }}
                  </h2>
                  <p class="text-xs sm:text-sm font-medium text-gray-500">
                    {{ profileData.email || "" }}
                  </p>

                  <!-- Badges: Status Pill + Joined Date -->
                  <div class="flex flex-wrap items-center justify-center sm:justify-start gap-2.5 pt-1.5">
                    <!-- Status Pill: Light green with solid dot -->
                    <span class="inline-flex items-center gap-1.5 px-3 py-0.5 rounded-full text-xs font-semibold bg-[#e6f4ea] text-[#137333] border border-[#ceead6]">
                      <span class="w-2 h-2 rounded-full bg-[#34a853]"></span>
                      <span>{{ profileData.status || "Active" }}</span>
                    </span>

                    <!-- Joined Date with Calendar Icon -->
                    <div v-if="profileData.joined_on" class="flex items-center gap-1.5 text-xs text-gray-500 font-medium">
                      <svg class="w-4 h-4 text-gray-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect>
                        <line x1="16" y1="2" x2="16" y2="6"></line>
                        <line x1="8" y1="2" x2="8" y2="6"></line>
                        <line x1="3" y1="10" x2="21" y2="10"></line>
                      </svg>
                      <span>Joined {{ formatJoinedDate(profileData.joined_on) }}</span>
                    </div>
                  </div>
                </div>

              </div>

              <!-- Right: Edit Profile Button -->
              <div class="flex justify-center sm:justify-end pb-1.5">
                <button
                  @click="toggleEdit"
                  class="px-4 py-2 bg-white border border-gray-200 hover:bg-gray-50 text-gray-800 text-xs font-bold rounded-xl transition-all shadow-sm flex items-center gap-2"
                >
                  <svg class="w-3.5 h-3.5 text-gray-600" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2">
                    <path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"></path>
                    <path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"></path>
                  </svg>
                  <span>{{ isEditing ? "Cancel Editing" : "Edit Profile" }}</span>
                </button>
              </div>

            </div>
          </div>
        </div>

        <!-- Main Two Column Grid (Left 65% / Right 35%) -->
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
          <!-- LEFT COLUMN (8 cols): Personal Info & Security -->
          <div class="lg:col-span-8 space-y-6">
            <!-- Card 1: Personal Information -->
            <div class="bg-white rounded-3xl border border-gray-100 p-6 sm:p-8 shadow-sm">
              <div class="flex items-center justify-between mb-6 pb-2 border-b border-gray-100">
                <div class="flex items-center gap-2.5">
                  <svg class="w-5 h-5 text-blue-600" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
                    <circle cx="12" cy="7" r="4"></circle>
                  </svg>
                  <h3 class="text-base font-bold text-gray-900">
                    Personal Information
                  </h3>
                </div>
                <button
                  @click="toggleEdit"
                  class="text-xs font-bold text-blue-600 hover:text-blue-700"
                >
                  {{ isEditing ? "Done" : "Edit" }}
                </button>
              </div>

              <!-- Inputs Grid -->
              <div class="space-y-4">
                <!-- Row 1: Full Name & Email -->
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                  <div>
                    <label class="block text-xs font-bold text-gray-700 mb-1.5">Full Name</label>
                    <input
                      type="text"
                      v-model="editForm.full_name"
                      :disabled="!isEditing"
                      class="w-full px-4 py-2.5 bg-gray-50/60 border border-gray-200 rounded-xl text-xs sm:text-sm font-medium text-gray-800 focus:outline-none focus:ring-2 focus:ring-emerald-600 disabled:opacity-80"
                    />
                  </div>
                  <div>
                    <label class="block text-xs font-bold text-gray-700 mb-1.5">Email Address</label>
                    <input
                      type="email"
                      v-model="editForm.email"
                      disabled
                      class="w-full px-4 py-2.5 bg-gray-50/60 border border-gray-200 rounded-xl text-xs sm:text-sm font-medium text-gray-500 cursor-not-allowed"
                    />
                  </div>
                </div>

                <!-- Row 2: Phone Number & Date of Birth -->
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                  <div>
                    <label class="block text-xs font-bold text-gray-700 mb-1.5">Phone Number</label>
                    <div class="relative">
                      <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none text-gray-400">
                        <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                          <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path>
                        </svg>
                      </div>
                      <input
                        type="text"
                        v-model="editForm.phone"
                        :disabled="!isEditing"
                        class="w-full pl-9 pr-4 py-2.5 bg-gray-50/60 border border-gray-200 rounded-xl text-xs sm:text-sm font-medium text-gray-800 focus:outline-none focus:ring-2 focus:ring-emerald-600 disabled:opacity-80"
                      />
                    </div>
                  </div>

                  <div>
                    <label class="block text-xs font-bold text-gray-700 mb-1.5">Date of Birth</label>
                    <div class="relative">
                      <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none text-gray-400">
                        <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                          <rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect>
                          <line x1="16" y1="2" x2="16" y2="6"></line>
                          <line x1="8" y1="2" x2="8" y2="6"></line>
                          <line x1="3" y1="10" x2="21" y2="10"></line>
                        </svg>
                      </div>
                      <input
                        type="text"
                        v-model="editForm.date_of_birth"
                        :disabled="!isEditing"
                        class="w-full pl-9 pr-4 py-2.5 bg-gray-50/60 border border-gray-200 rounded-xl text-xs sm:text-sm font-medium text-gray-800 focus:outline-none focus:ring-2 focus:ring-emerald-600 disabled:opacity-80"
                      />
                    </div>
                  </div>
                </div>

                <!-- Row 3: Address -->
                <div>
                  <label class="block text-xs font-bold text-gray-700 mb-1.5">Address</label>
                  <div class="relative">
                    <div class="absolute top-3 left-3 flex items-center pointer-events-none text-gray-400">
                      <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path>
                        <circle cx="12" cy="10" r="3"></circle>
                      </svg>
                    </div>
                    <input
                      type="text"
                      v-model="editForm.address"
                      :disabled="!isEditing"
                      class="w-full pl-9 pr-4 py-2.5 bg-gray-50/60 border border-gray-200 rounded-xl text-xs sm:text-sm font-medium text-gray-800 focus:outline-none focus:ring-2 focus:ring-emerald-600 disabled:opacity-80"
                    />
                  </div>
                </div>

                <!-- Row 4: Bio / About Me -->
                <div>
                  <label class="block text-xs font-bold text-gray-700 mb-1.5">Bio / About Me</label>
                  <div class="relative">
                    <div class="absolute top-3 left-3 pointer-events-none text-gray-400">
                      <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
                        <polyline points="14 2 14 8 20 8"></polyline>
                      </svg>
                    </div>
                    <textarea
                      rows="3"
                      v-model="editForm.bio"
                      :disabled="!isEditing"
                      maxlength="500"
                      class="w-full pl-9 pr-4 py-2.5 bg-gray-50/60 border border-gray-200 rounded-xl text-xs sm:text-sm font-medium text-gray-800 focus:outline-none focus:ring-2 focus:ring-emerald-600 disabled:opacity-80 resize-none"
                    ></textarea>
                  </div>
                  <div class="text-right text-[11px] text-gray-400 mt-1">
                    {{ editForm.bio ? editForm.bio.length : 0 }}/500
                  </div>
                </div>

                <!-- Save Changes Button when editing -->
                <div v-if="isEditing" class="pt-2 flex justify-end">
                  <button
                    @click="saveProfile"
                    :disabled="savingProfile"
                    class="px-6 py-2.5 bg-[#064e3b] hover:bg-[#043226] text-white text-xs font-bold rounded-xl transition-all shadow-sm"
                  >
                    {{ savingProfile ? "Saving..." : "Save Changes" }}
                  </button>
                </div>
              </div>
            </div>

            <!-- Card 2: Account Security -->
            <div class="bg-white rounded-3xl border border-gray-100 p-6 sm:p-8 shadow-sm">
              <div class="flex items-center justify-between mb-4 pb-2 border-b border-gray-100">
                <div class="flex items-center gap-2.5">
                  <svg class="w-5 h-5 text-emerald-600" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect>
                    <path d="M7 11V7a5 5 0 0 1 10 0v4"></path>
                  </svg>
                  <h3 class="text-base font-bold text-gray-900">
                    Account Security
                  </h3>
                </div>
                <button
                  @click="showPasswordModal = true"
                  class="text-xs font-bold text-blue-600 hover:text-blue-700"
                >
                  Change Password
                </button>
              </div>

              <!-- Password Field Display -->
              <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
                <div class="flex-1">
                  <label class="block text-xs font-bold text-gray-700 mb-1.5">Current Password</label>
                  <div class="relative">
                    <input
                      :type="showPassword ? 'text' : 'password'"
                      value="••••••••"
                      readonly
                      class="w-full px-4 py-2.5 bg-gray-50/60 border border-gray-200 rounded-xl text-xs sm:text-sm font-medium text-gray-800 tracking-widest focus:outline-none"
                    />
                    <button
                      type="button"
                      @click="showPassword = !showPassword"
                      class="absolute inset-y-0 right-0 pr-3 flex items-center text-gray-400 hover:text-gray-600"
                    >
                      <svg v-if="!showPassword" class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path>
                        <circle cx="12" cy="12" r="3"></circle>
                      </svg>
                      <svg v-else class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M17.94 17.94A10.07 10.07 0 0 1 12 20c-7 0-11-8-11-8a18.45 18.45 0 0 1 5.06-5.94M9.9 4.24A9.12 9.12 0 0 1 12 4c7 0 11 8 11 8a18.5 18.5 0 0 1-2.16 3.19m-6.72-1.07a3 3 0 1 1-4.24-4.24"></path>
                        <line x1="1" y1="1" x2="23" y2="23"></line>
                      </svg>
                    </button>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- RIGHT COLUMN (4 cols): Impact, Quick Stats & Skills -->
          <div class="lg:col-span-4 space-y-6">
            <!-- Card 1: Total Impact (Gradient Blue) -->
            <div class="bg-gradient-to-br from-[#1d4ed8] via-[#2563eb] to-[#0284c7] rounded-3xl p-6 text-white shadow-md flex items-center justify-between group">
              <div class="space-y-1">
                <div class="w-9 h-9 rounded-xl bg-white/20 backdrop-blur-md flex items-center justify-center mb-2">
                  <svg class="w-5 h-5 text-white" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M18 20V10M12 20V4M6 20v-6" />
                  </svg>
                </div>
                <p class="text-xs font-semibold text-blue-100 uppercase tracking-wider">
                  Total Impact
                </p>
                <h3 class="text-3xl font-black text-white leading-none">
                  {{ profileData.total_hours ? parseFloat(profileData.total_hours).toFixed(0) : 0 }} hrs
                </h3>
                <p class="text-xs text-blue-100/90 font-medium pt-1">
                  Hours Volunteered
                </p>
              </div>

              <div class="text-white/70">
                <svg class="w-6 h-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                  <path d="M9 18l6-6-6-6" />
                </svg>
              </div>
            </div>

            <!-- Card 2: 2x2 Quick Stats Grid -->
            <div class="grid grid-cols-2 gap-3">
              <!-- Total Assignments -->
              <div class="bg-white rounded-2xl p-4 border border-gray-100 shadow-sm flex items-start gap-3">
                <div class="w-9 h-9 rounded-xl bg-emerald-50 text-emerald-600 flex items-center justify-center flex-shrink-0">
                  <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect>
                    <line x1="16" y1="2" x2="16" y2="6"></line>
                    <line x1="8" y1="2" x2="8" y2="6"></line>
                  </svg>
                </div>
                <div>
                  <h4 class="text-xl font-black text-gray-900 leading-none">
                    {{ profileData.stats?.total_assignments || 0 }}
                  </h4>
                  <p class="text-[11px] font-medium text-gray-500 mt-1">
                    Total Assignments
                  </p>
                </div>
              </div>

              <!-- Completed -->
              <div class="bg-white rounded-2xl p-4 border border-gray-100 shadow-sm flex items-start gap-3">
                <div class="w-9 h-9 rounded-xl bg-emerald-50 text-emerald-600 flex items-center justify-center flex-shrink-0">
                  <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="20 6 9 17 4 12"></polyline>
                  </svg>
                </div>
                <div>
                  <h4 class="text-xl font-black text-gray-900 leading-none">
                    {{ profileData.stats?.completed_assignments || 0 }}
                  </h4>
                  <p class="text-[11px] font-medium text-gray-500 mt-1">
                    Completed
                  </p>
                </div>
              </div>

              <!-- Upcoming Shifts -->
              <div class="bg-white rounded-2xl p-4 border border-gray-100 shadow-sm flex items-start gap-3">
                <div class="w-9 h-9 rounded-xl bg-blue-50 text-blue-600 flex items-center justify-center flex-shrink-0">
                  <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <circle cx="12" cy="12" r="10"></circle>
                    <polyline points="12 6 12 12 16 14"></polyline>
                  </svg>
                </div>
                <div>
                  <h4 class="text-xl font-black text-gray-900 leading-none">
                    {{ profileData.stats?.upcoming_shifts || 0 }}
                  </h4>
                  <p class="text-[11px] font-medium text-gray-500 mt-1">
                    Upcoming Shifts
                  </p>
                </div>
              </div>

              <!-- Active Campaigns -->
              <div class="bg-white rounded-2xl p-4 border border-gray-100 shadow-sm flex items-start gap-3">
                <div class="w-9 h-9 rounded-xl bg-purple-50 text-purple-600 flex items-center justify-center flex-shrink-0">
                  <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path>
                    <circle cx="9" cy="7" r="4"></circle>
                    <path d="M23 21v-2a4 4 0 0 0-3-3.87"></path>
                    <path d="M16 3.13a4 4 0 0 1 0 7.75"></path>
                  </svg>
                </div>
                <div>
                  <h4 class="text-xl font-black text-gray-900 leading-none">
                    {{ profileData.stats?.active_campaigns || 0 }}
                  </h4>
                  <p class="text-[11px] font-medium text-gray-500 mt-1">
                    Active Campaigns
                  </p>
                </div>
              </div>
            </div>

            <!-- Card 3: Your Skills -->
            <div class="bg-white rounded-3xl border border-gray-100 p-6 shadow-sm">
              <div class="flex items-center justify-between mb-4 pb-2 border-b border-gray-100">
                <div class="flex items-center gap-2">
                  <svg class="w-5 h-5 text-amber-500" viewBox="0 0 24 24" fill="currentColor">
                    <polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon>
                  </svg>
                  <h3 class="text-base font-bold text-gray-900">Your Skills</h3>
                </div>
              </div>

              <!-- Skill Cards List -->
              <div v-if="skillsList.length > 0" class="space-y-2.5 mb-4">
                <div
                  v-for="(skill, i) in skillsList"
                  :key="i"
                  class="p-3 rounded-2xl flex items-center justify-between transition-colors"
                  :class="getSkillCardBg(i)"
                >
                  <div class="flex items-center gap-3">
                    <div
                      class="w-8 h-8 rounded-xl flex items-center justify-center flex-shrink-0"
                      :class="getSkillIconBg(i)"
                    >
                      <svg class="w-4 h-4 text-emerald-700" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <line x1="18" y1="20" x2="18" y2="10"></line>
                        <line x1="12" y1="20" x2="12" y2="4"></line>
                        <line x1="6" y1="20" x2="6" y2="14"></line>
                      </svg>
                    </div>
                    <div>
                      <h5 class="text-xs font-bold text-gray-900 leading-tight">
                        {{ skill.skill }}
                      </h5>
                      <p class="text-[10px] font-semibold text-gray-500 mt-0.5">
                        {{ skill.proficiency || "Intermediate" }}
                      </p>
                    </div>
                  </div>
                </div>
              </div>

              <div v-else class="text-xs text-gray-400 py-4 text-center">
                No skills listed on your volunteer profile yet.
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Change Password Modal -->
    <div
      v-if="showPasswordModal"
      class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/60 backdrop-blur-sm animate-fade-in"
    >
      <div class="bg-white rounded-3xl max-w-md w-full p-6 sm:p-8 shadow-2xl relative">
        <button
          @click="showPasswordModal = false"
          class="absolute top-5 right-5 text-gray-400 hover:text-gray-600 p-1.5 rounded-full hover:bg-gray-100"
        >
          <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <line x1="18" y1="6" x2="6" y2="18"></line>
            <line x1="6" y1="6" x2="18" y2="18"></line>
          </svg>
        </button>

        <h3 class="text-lg font-bold text-gray-900 mb-4">Change Password</h3>

        <div class="space-y-4">
          <div>
            <label class="block text-xs font-bold text-gray-700 mb-1">Current Password</label>
            <input
              type="password"
              v-model="pwdForm.old"
              class="w-full px-4 py-2 bg-gray-50 border border-gray-200 rounded-xl text-xs focus:ring-2 focus:ring-emerald-600"
            />
          </div>
          <div>
            <label class="block text-xs font-bold text-gray-700 mb-1">New Password</label>
            <input
              type="password"
              v-model="pwdForm.new"
              class="w-full px-4 py-2 bg-gray-50 border border-gray-200 rounded-xl text-xs focus:ring-2 focus:ring-emerald-600"
            />
          </div>
          <div class="flex justify-end gap-2 pt-2">
            <button
              @click="showPasswordModal = false"
              class="px-4 py-2 text-xs font-bold text-gray-600 hover:bg-gray-100 rounded-xl"
            >
              Cancel
            </button>
            <button
              @click="submitPasswordChange"
              class="px-5 py-2 bg-[#064e3b] text-white text-xs font-bold rounded-xl hover:bg-[#043226]"
            >
              Update Password
            </button>
          </div>
        </div>
      </div>
    </div>
  </VolunteerLayout>
</template>

<script setup>
import { createResource } from "frappe-ui"
import { ref, computed } from "vue"
import VolunteerLayout from "../components/VolunteerLayout.vue"

const isEditing = ref(false)
const savingProfile = ref(false)
const showPasswordModal = ref(false)
const showPassword = ref(false)
const fileInput = ref(null)

const pwdForm = ref({
  old: "",
  new: "",
})

const editForm = ref({
  full_name: "",
  email: "",
  phone: "",
  date_of_birth: "",
  address: "",
  bio: "",
})

// Backend profile resource
const profileResource = createResource({
  url: "ngo.api.volunteer.my_profile",
  method: "GET",
  auto: true,
  onSuccess(data) {
    if (data) {
      editForm.value.full_name = data.full_name || ""
      editForm.value.email = data.email || ""
      editForm.value.phone = data.phone || ""
      editForm.value.address = data.address || ""
      editForm.value.bio = data.bio || ""
      if (data.date_of_birth) {
        editForm.value.date_of_birth = formatDateOfBirth(data.date_of_birth)
      }
    }
  },
})

const profileData = computed(() => {
  return profileResource.data || {}
})

const skillsList = computed(() => {
  if (profileResource.data && Array.isArray(profileResource.data.skills)) {
    return profileResource.data.skills
  }
  return []
})

function getSkillCardBg(idx) {
  if (idx % 3 === 0) return "bg-emerald-50/70 border border-emerald-100/80"
  if (idx % 3 === 1) return "bg-amber-50/70 border border-amber-100/80"
  return "bg-blue-50/70 border border-blue-100/80"
}

function getSkillIconBg(idx) {
  if (idx % 3 === 0) return "bg-emerald-100"
  if (idx % 3 === 1) return "bg-amber-100"
  return "bg-blue-100"
}

function formatJoinedDate(dateStr) {
  if (!dateStr) return ""
  const d = new Date(dateStr)
  return d.toLocaleDateString("en-US", { month: "long", year: "numeric" })
}

function formatDateOfBirth(dateStr) {
  if (!dateStr) return ""
  const d = new Date(dateStr)
  return d.toLocaleDateString("en-GB", {
    day: "numeric",
    month: "long",
    year: "numeric",
  })
}

function toggleEdit() {
  isEditing.value = !isEditing.value
}

function triggerPhotoUpload() {
  if (fileInput.value) {
    fileInput.value.click()
  }
}

function getCsrfToken() {
  return window.csrf_token || (window.frappe ? window.frappe.csrf_token : "") || ""
}

async function handlePhotoUpload(event) {
  const file = event.target.files[0]
  if (!file) return

  const formData = new FormData()
  formData.append("file", file)

  const csrf = getCsrfToken()
  try {
    const res = await fetch("/api/method/ngo.api.volunteer.upload_profile_image", {
      method: "POST",
      headers: {
        ...(csrf && { "X-Frappe-CSRF-Token": csrf }),
      },
      body: formData,
    })
    const data = await res.json()
    if (data.message && data.message.file_url) {
      const fileUrl = data.message.file_url
      await profileResource.fetch()
      window.dispatchEvent(new CustomEvent('volunteer-image-updated', { detail: { image: fileUrl } }))
    } else if (data.exc) {
      alert("Upload failed: " + (data._server_messages || "Could not upload image"))
    }
  } catch (err) {
    console.error("Photo upload error:", err)
    alert("Could not upload photo. Please try again.")
  } finally {
    if (event.target) event.target.value = ""
  }
}

async function saveProfile() {
  savingProfile.value = true
  const csrf = getCsrfToken()
  try {
    const res = await fetch("/api/method/ngo.api.volunteer.update_my_profile", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        ...(csrf && { "X-Frappe-CSRF-Token": csrf }),
      },
      body: JSON.stringify({
        full_name: editForm.value.full_name,
        phone: editForm.value.phone,
        date_of_birth: editForm.value.date_of_birth,
        address: editForm.value.address,
        bio: editForm.value.bio,
      }),
    })
    const data = await res.json()
    if (!data.exc) {
      isEditing.value = false
      await profileResource.fetch()
      window.dispatchEvent(new CustomEvent('volunteer-profile-updated', {
        detail: { full_name: editForm.value.full_name }
      }))
    } else {
      alert("Error saving profile: " + (data._server_messages || "Failed to update profile"))
    }
  } catch (err) {
    console.error("Save profile error:", err)
    alert("An error occurred while saving profile changes.")
  } finally {
    savingProfile.value = false
  }
}

async function submitPasswordChange() {
  if (!pwdForm.value.old || !pwdForm.value.new) {
    alert("Please enter both current and new passwords")
    return
  }
  const csrf = getCsrfToken()
  try {
    const res = await fetch("/api/method/frappe.core.doctype.user.user.update_password", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        ...(csrf && { "X-Frappe-CSRF-Token": csrf }),
      },
      body: JSON.stringify({
        old_password: pwdForm.value.old,
        new_password: pwdForm.value.new,
      }),
    })
    const data = await res.json()
    if (!data.exc) {
      showPasswordModal.value = false
      pwdForm.value.old = ""
      pwdForm.value.new = ""
      alert("Password updated successfully!")
    } else {
      alert("Could not update password. Please check your current password.")
    }
  } catch (err) {
    alert("Could not update password. Please check your current password.")
  }
}
</script>
