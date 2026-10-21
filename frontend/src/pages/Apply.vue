<template>
  <!-- Full-viewport responsive container -->
  <div class="min-h-screen lg:fixed lg:inset-0 lg:w-screen lg:h-screen lg:overflow-hidden bg-[#f8fafc] flex flex-col justify-between font-sans selection:bg-emerald-100 selection:text-emerald-900">
    
    <!-- Top Navigation Header -->
    <header class="bg-white border-b border-gray-100 px-6 lg:px-10 py-2.5 shrink-0 flex items-center justify-between shadow-[0_1px_3px_rgba(0,0,0,0.03)] z-20">
      <!-- Brand Logo & Title -->
      <router-link to="/account/login" class="flex items-center gap-2.5 group">
        <template v-if="settings.login_logo">
          <img :src="settings.login_logo" alt="Logo" class="h-8 w-auto object-contain" />
        </template>
        <template v-else>
          <div class="w-8 h-8 rounded-xl bg-[#064e3b] flex items-center justify-center text-white shadow-sm shrink-0 border border-emerald-500/30">
            <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none">
              <path d="M12 22V12" stroke="#34d399" stroke-width="2" stroke-linecap="round"/>
              <path d="M12 12C12 7.02944 16.0294 3 21 3C21 7.97056 16.9706 12 12 12Z" fill="#f59e0b"/>
              <path d="M12 14C12 9.02944 7.97056 5 3 5C3 9.97056 7.02944 14 12 14Z" fill="#10b981"/>
            </svg>
          </div>
        </template>
        <div>
          <div class="font-extrabold text-gray-900 text-sm lg:text-[15px] tracking-tight leading-none group-hover:text-emerald-800 transition-colors">
            {{ settings.login_portal_title || 'Kindred' }}
          </div>
          <div class="font-bold text-[#047857] text-[8px] tracking-[0.25em] uppercase leading-none mt-1">
            {{ settings.login_portal_subtitle || 'IMPACTSPHERE' }}
          </div>
        </div>
      </router-link>

      <!-- Header Right Utilities -->
      <div class="flex items-center gap-3 sm:gap-4">
        <!-- Field Support & FAQ -->
        <a 
          :href="settings.login_support_url || '#'" 
          class="hidden sm:flex items-center gap-1.5 text-xs font-medium text-gray-600 hover:text-gray-900 transition"
        >
          <svg class="w-3.5 h-3.5 text-gray-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="12" cy="12" r="10" />
            <path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3" />
            <line x1="12" y1="17" x2="12.01" y2="17" />
          </svg>
          <span>{{ settings.login_support_label || 'Field Support & FAQ' }}</span>
        </a>

        <!-- Systems Operational Status Badge -->
        <div class="flex items-center gap-1.5 px-2.5 py-1 rounded-full bg-emerald-50 border border-emerald-200/70 text-emerald-800 text-xs font-medium">
          <span class="relative flex h-2 w-2">
            <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
            <span class="relative inline-flex rounded-full h-2 w-2 bg-emerald-500"></span>
          </span>
          <span>{{ settings.login_status_badge || 'Systems Operational' }}</span>
        </div>

        <!-- Back to Login Button -->
        <router-link 
          to="/account/login" 
          class="flex items-center gap-1.5 px-3 py-1 text-xs font-semibold text-gray-700 hover:text-emerald-800 bg-white hover:bg-gray-50 border border-gray-200 rounded-lg transition shadow-sm"
        >
          <svg class="w-3.5 h-3.5 text-gray-500" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M15 3h4a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2h-4"></path>
            <polyline points="10 17 15 12 10 7"></polyline>
            <line x1="15" y1="12" x2="3" y2="12"></line>
          </svg>
          <span>Sign In</span>
        </router-link>
      </div>
    </header>

    <!-- Main Content Area: 2-Column Card -->
    <main class="flex-1 min-h-0 w-full max-w-5xl xl:max-w-6xl mx-auto px-4 py-3 sm:py-4 flex items-center justify-center overflow-hidden">
      <div class="w-full h-full lg:max-h-[calc(100vh-105px)] bg-white rounded-2xl lg:rounded-3xl shadow-[0_15px_50px_-10px_rgba(6,78,59,0.08)] border border-gray-100 overflow-hidden grid grid-cols-1 lg:grid-cols-12">
        
        <!-- Left Side: Customized Volunteer Recruitment Hero Banner (Distinct from login) -->
        <div class="lg:col-span-5 relative bg-gradient-to-br from-[#032e23] via-[#054233] to-[#021f17] p-6 lg:p-7 flex flex-col justify-between text-white overflow-hidden">
          
          <!-- Background Subtle Overlay Effects -->
          <div class="absolute inset-0 opacity-10 bg-[radial-gradient(#ffffff_1px,transparent_1px)] [background-size:16px_16px] pointer-events-none"></div>
          <div class="absolute -top-16 -right-16 w-56 h-56 bg-emerald-400/20 rounded-full blur-2xl pointer-events-none"></div>

          <!-- Top Hero Section -->
          <div class="relative z-10">
            <!-- Enrollment Badge -->
            <div class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-emerald-900/80 border border-emerald-500/30 text-emerald-300 text-[10px] font-bold tracking-wider uppercase backdrop-blur-sm">
              <svg class="w-3.5 h-3.5 text-emerald-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/>
              </svg>
              <span>VOLUNTEER ENROLLMENT</span>
            </div>

            <!-- Custom Inspiring Headline -->
            <h1 class="text-2xl sm:text-[26px] lg:text-[28px] font-extrabold text-white tracking-tight leading-[1.2] mt-3">
              Step Forward. Create Lasting Impact.
            </h1>

            <!-- Description -->
            <p class="text-emerald-100/85 text-xs leading-relaxed mt-2 font-normal">
              Join our dedicated volunteer community. Whether tutoring students, planting saplings, or coordinating local relief drives, your time drives tangible community change.
            </p>
          </div>

          <!-- Middle: Featured Volunteer Photo Card with Script Calligraphy -->
          <div class="relative my-3 rounded-2xl overflow-hidden shadow-lg border border-emerald-500/25 z-10 group">
            <img 
              :src="volunteersPlanting" 
              alt="Volunteers planting trees in the community" 
              class="w-full h-32 lg:h-36 object-cover object-center group-hover:scale-105 transition-transform duration-500"
            />
            <div class="absolute inset-0 bg-gradient-to-t from-black/85 via-black/30 to-transparent flex items-end justify-between p-3">
              <span class="font-script text-xl lg:text-2xl text-white drop-shadow-[0_2px_4px_rgba(0,0,0,0.8)]">
                Communities Thrive Together
              </span>
              <span class="text-[10px] uppercase font-bold tracking-wider bg-emerald-900/90 text-emerald-300 px-2 py-0.5 rounded border border-emerald-500/40">
                Field Active
              </span>
            </div>
          </div>

          <!-- Bottom: 3 Key Volunteer Benefits -->
          <div class="space-y-2 z-10 bg-emerald-950/40 p-3.5 rounded-2xl border border-emerald-500/20 backdrop-blur-sm">
            <div class="flex items-center gap-2.5">
              <div class="w-6 h-6 rounded-lg bg-emerald-800/80 text-emerald-300 flex items-center justify-center flex-shrink-0">
                <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg>
              </div>
              <div class="text-[11px] text-emerald-100 leading-tight">
                <strong class="text-white font-semibold">Verified Service Hours:</strong> Digital ledger for academic & corporate credits.
              </div>
            </div>

            <div class="flex items-center gap-2.5">
              <div class="w-6 h-6 rounded-lg bg-emerald-800/80 text-emerald-300 flex items-center justify-center flex-shrink-0">
                <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg>
              </div>
              <div class="text-[11px] text-emerald-100 leading-tight">
                <strong class="text-white font-semibold">Skill-Based Matching:</strong> Apply your expertise where it creates maximum value.
              </div>
            </div>

            <div class="flex items-center gap-2.5">
              <div class="w-6 h-6 rounded-lg bg-emerald-800/80 text-emerald-300 flex items-center justify-center flex-shrink-0">
                <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg>
              </div>
              <div class="text-[11px] text-emerald-100 leading-tight">
                <strong class="text-white font-semibold">Flexible Scheduling:</strong> Pick deployment shifts that align with your routine.
              </div>
            </div>
          </div>

        </div>

        <!-- Right Side: Application Form Panel (Mandatory constraints & numbers only) -->
        <div class="lg:col-span-7 p-6 lg:p-8 xl:p-10 flex flex-col justify-between bg-white overflow-y-auto">
          
          <!-- Success State Display -->
          <div v-if="success" class="my-auto py-8 text-center space-y-4">
            <div class="w-16 h-16 rounded-full bg-emerald-50 text-emerald-600 border border-emerald-200 flex items-center justify-center mx-auto shadow-sm">
              <svg class="w-8 h-8" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5">
                <path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7" />
              </svg>
            </div>
            
            <h2 class="text-2xl font-extrabold text-gray-900 tracking-tight">
              Application Submitted Successfully!
            </h2>
            
            <p class="text-xs lg:text-sm text-gray-600 max-w-md mx-auto leading-relaxed">
              Thank you for applying to be a volunteer. Our chapter deployment team will review your skills and contact details, and you will receive an invitation to access the portal shortly.
            </p>

            <div class="pt-4 max-w-xs mx-auto">
              <router-link 
                to="/account/login" 
                class="w-full py-2.5 px-4 rounded-xl text-xs lg:text-sm font-bold text-white bg-[#064e3b] hover:bg-[#043d2e] transition shadow-md flex items-center justify-center gap-2"
              >
                <span>Go to Volunteer Login</span>
                <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 18 15 12 9 6"></polyline></svg>
              </router-link>
            </div>
          </div>

          <!-- Application Form -->
          <div v-else>
            <!-- Form Icon Badge -->
            <div class="w-10 h-10 rounded-xl bg-emerald-50 border border-emerald-100/80 flex items-center justify-center text-emerald-700 mb-2 shadow-sm">
              <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2" />
                <circle cx="9" cy="7" r="4" />
                <line x1="19" y1="8" x2="19" y2="14" />
                <line x1="22" y1="11" x2="16" y2="11" />
              </svg>
            </div>

            <!-- Form Title & Subtitle -->
            <h2 class="text-2xl lg:text-[25px] font-extrabold text-gray-900 tracking-tight leading-tight">
              Apply to be a Volunteer
            </h2>
            <p class="text-xs text-gray-500 mt-1 leading-normal">
              Fields marked with an asterisk (<span class="text-red-500 font-bold">*</span>) are mandatory.
            </p>

            <!-- Error Banner -->
            <div v-if="error" class="mt-3 bg-red-50 border border-red-200 text-red-600 px-3 py-2 rounded-xl text-xs font-medium flex items-center gap-2 animate-pulse">
              <svg class="w-4 h-4 shrink-0 text-red-500" viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z" clip-rule="evenodd" />
              </svg>
              <span>{{ error }}</span>
            </div>

            <!-- Form Fields -->
            <form @submit.prevent="submitForm" class="space-y-3 mt-3.5">
              
              <!-- Row 1: Full Name & Email -->
              <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
                <!-- Full Name -->
                <div class="space-y-1">
                  <label class="block text-[10px] font-bold text-gray-700 uppercase tracking-wider">
                    Full Name <span class="text-red-500">*</span>
                  </label>
                  <div class="relative rounded-xl border border-gray-200 focus-within:border-emerald-700 focus-within:ring-2 focus-within:ring-emerald-700/15 transition shadow-sm bg-white">
                    <div class="absolute inset-y-0 left-0 pl-3.5 flex items-center pointer-events-none text-gray-400">
                      <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2" />
                        <circle cx="12" cy="7" r="4" />
                      </svg>
                    </div>
                    <input 
                      v-model="form.applicant_name" 
                      type="text" 
                      required 
                      placeholder="John Doe"
                      class="block w-full pl-10 pr-3.5 py-2 text-xs lg:text-sm text-gray-900 placeholder-gray-400 bg-transparent rounded-xl focus:outline-none"
                    />
                  </div>
                </div>

                <!-- Email Address -->
                <div class="space-y-1">
                  <label class="block text-[10px] font-bold text-gray-700 uppercase tracking-wider">
                    Email Address <span class="text-red-500">*</span>
                  </label>
                  <div class="relative rounded-xl border border-gray-200 focus-within:border-emerald-700 focus-within:ring-2 focus-within:ring-emerald-700/15 transition shadow-sm bg-white">
                    <div class="absolute inset-y-0 left-0 pl-3.5 flex items-center pointer-events-none text-gray-400">
                      <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <rect width="20" height="16" x="2" y="4" rx="2" />
                        <path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7" />
                      </svg>
                    </div>
                    <input 
                      v-model="form.email" 
                      type="email" 
                      required 
                      placeholder="you@example.com"
                      class="block w-full pl-10 pr-3.5 py-2 text-xs lg:text-sm text-gray-900 placeholder-gray-400 bg-transparent rounded-xl focus:outline-none"
                    />
                  </div>
                </div>
              </div>

              <!-- Row 2: Phone Number (ONLY NUMBERS, MANDATORY) & Date of Birth (MANDATORY) -->
              <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
                <!-- Phone Number: ONLY NUMBERS ALLOWED & MANDATORY -->
                <div class="space-y-1">
                  <label class="block text-[10px] font-bold text-gray-700 uppercase tracking-wider">
                    Phone Number <span class="text-red-500">*</span>
                    <span class="text-[9px] text-gray-400 font-normal ml-1">(Numbers only)</span>
                  </label>
                  <div class="relative rounded-xl border border-gray-200 focus-within:border-emerald-700 focus-within:ring-2 focus-within:ring-emerald-700/15 transition shadow-sm bg-white">
                    <div class="absolute inset-y-0 left-0 pl-3.5 flex items-center pointer-events-none text-gray-400">
                      <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/>
                      </svg>
                    </div>
                    <input 
                      v-model="form.phone" 
                      type="tel"
                      inputmode="numeric"
                      pattern="[0-9]*"
                      maxlength="15"
                      required
                      @input="onPhoneInput"
                      placeholder="9876543210"
                      class="block w-full pl-10 pr-3.5 py-2 text-xs lg:text-sm text-gray-900 placeholder-gray-400 bg-transparent rounded-xl focus:outline-none"
                    />
                  </div>
                </div>

                <!-- Date of Birth: MANDATORY -->
                <div class="space-y-1">
                  <label class="block text-[10px] font-bold text-gray-700 uppercase tracking-wider">
                    Date of Birth <span class="text-red-500">*</span>
                  </label>
                  <div class="relative rounded-xl border border-gray-200 focus-within:border-emerald-700 focus-within:ring-2 focus-within:ring-emerald-700/15 transition shadow-sm bg-white">
                    <div class="absolute inset-y-0 left-0 pl-3.5 flex items-center pointer-events-none text-gray-400">
                      <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <rect width="18" height="18" x="3" y="4" rx="2" />
                        <line x1="16" y1="2" x2="16" y2="6" />
                        <line x1="8" y1="2" x2="8" y2="6" />
                        <line x1="3" y1="10" x2="21" y2="10" />
                      </svg>
                    </div>
                    <input 
                      v-model="form.date_of_birth" 
                      type="date" 
                      required
                      class="block w-full pl-10 pr-3.5 py-2 text-xs lg:text-sm text-gray-900 bg-transparent rounded-xl focus:outline-none cursor-pointer"
                    />
                  </div>
                </div>
              </div>

              <!-- Row 3: Gender (MANDATORY) -->
              <div class="space-y-1">
                <label class="block text-[10px] font-bold text-gray-700 uppercase tracking-wider">
                  Gender <span class="text-red-500">*</span>
                </label>
                <div class="relative rounded-xl border border-gray-200 focus-within:border-emerald-700 focus-within:ring-2 focus-within:ring-emerald-700/15 transition shadow-sm bg-white">
                  <select 
                    v-model="form.gender" 
                    required
                    class="block w-full px-3.5 py-2 text-xs lg:text-sm text-gray-900 bg-transparent rounded-xl focus:outline-none cursor-pointer"
                  >
                    <option value="" disabled>Select Gender</option>
                    <option value="Male">Male</option>
                    <option value="Female">Female</option>
                    <option value="Other">Other</option>
                  </select>
                </div>
              </div>

              <!-- Row 4: Residential Address (MANDATORY) -->
              <div class="space-y-1">
                <label class="block text-[10px] font-bold text-gray-700 uppercase tracking-wider">
                  Residential Address <span class="text-red-500">*</span>
                </label>
                <div class="relative rounded-xl border border-gray-200 focus-within:border-emerald-700 focus-within:ring-2 focus-within:ring-emerald-700/15 transition shadow-sm bg-white">
                  <textarea 
                    v-model="form.address" 
                    required
                    rows="2" 
                    placeholder="Enter your street address, city, and pincode..."
                    class="block w-full px-3.5 py-2 text-xs lg:text-sm text-gray-900 placeholder-gray-400 bg-transparent rounded-xl focus:outline-none resize-none"
                  ></textarea>
                </div>
              </div>

              <!-- Row 5: Skills & Interests (MANDATORY) -->
              <div class="pt-2 border-t border-gray-100">
                <div class="flex justify-between items-center mb-2">
                  <div class="flex items-center gap-1.5">
                    <label class="block text-[10px] font-bold text-gray-700 uppercase tracking-wider">
                      Skills & Interests <span class="text-red-500">*</span>
                    </label>
                    <span class="text-[9px] bg-emerald-50 text-emerald-800 font-semibold px-2 py-0.5 rounded border border-emerald-200/60">
                      At least 1 required
                    </span>
                  </div>
                  <button 
                    type="button" 
                    @click="addSkill"
                    class="text-[11px] font-bold text-emerald-800 hover:text-emerald-900 bg-emerald-50 hover:bg-emerald-100 px-2.5 py-1 rounded-lg border border-emerald-200/60 transition"
                  >
                    + Add Skill
                  </button>
                </div>

                <div class="space-y-2">
                  <div 
                    v-for="(skill, index) in form.skills" 
                    :key="'skill-' + index"
                    class="flex items-center gap-2 p-1.5 rounded-xl border border-gray-200 bg-gray-50/60"
                  >
                    <select 
                      v-model="skill.skill" 
                      required 
                      class="flex-1 px-2.5 py-1.5 bg-white text-gray-900 border border-gray-200 rounded-lg text-xs focus:outline-none focus:border-emerald-700 cursor-pointer"
                    >
                      <option value="" disabled selected>Select a Skill...</option>
                      <option v-for="s in availableSkills" :key="s" :value="s">{{ s }}</option>
                    </select>

                    <select 
                      v-model="skill.proficiency" 
                      required 
                      class="w-1/3 px-2.5 py-1.5 bg-white text-gray-900 border border-gray-200 rounded-lg text-xs focus:outline-none focus:border-emerald-700 cursor-pointer"
                    >
                      <option value="Beginner">Beginner</option>
                      <option value="Intermediate">Intermediate</option>
                      <option value="Expert">Expert</option>
                    </select>

                    <button 
                      type="button" 
                      @click="removeSkill(index)"
                      class="text-red-500 hover:text-red-700 p-1.5 rounded-lg hover:bg-red-50 transition"
                      title="Remove skill"
                    >
                      <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
                    </button>
                  </div>

                  <p v-if="form.skills.length === 0" class="text-[11px] text-amber-600 font-medium italic">
                    ⚠️ Skills are mandatory. Please click "+ Add Skill" to select at least one skill.
                  </p>
                </div>
              </div>

              <!-- Row 6: Weekly Availability -->
              <div class="pt-2 border-t border-gray-100">
                <div class="flex justify-between items-center mb-2">
                  <label class="block text-[10px] font-bold text-gray-700 uppercase tracking-wider">
                    Weekly Availability (Optional)
                  </label>
                  <button 
                    type="button" 
                    @click="addAvailability"
                    class="text-[11px] font-bold text-emerald-800 hover:text-emerald-900 bg-emerald-50 hover:bg-emerald-100 px-2.5 py-1 rounded-lg border border-emerald-200/60 transition"
                  >
                    + Add Availability
                  </button>
                </div>

                <div class="space-y-2">
                  <div 
                    v-for="(avail, index) in form.availability" 
                    :key="'avail-' + index"
                    class="flex flex-wrap sm:flex-nowrap items-center gap-2 p-1.5 rounded-xl border border-gray-200 bg-gray-50/60"
                  >
                    <select 
                      v-model="avail.day_of_week" 
                      required 
                      class="flex-1 min-w-[100px] px-2.5 py-1.5 bg-white text-gray-900 border border-gray-200 rounded-lg text-xs focus:outline-none focus:border-emerald-700 cursor-pointer"
                    >
                      <option value="" disabled>Select Day</option>
                      <option v-for="day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']" :key="day" :value="day">
                        {{ day }}
                      </option>
                    </select>

                    <div class="flex items-center gap-1">
                      <input 
                        v-model="avail.from_time" 
                        type="time" 
                        required 
                        class="px-2 py-1.5 bg-white text-gray-900 border border-gray-200 rounded-lg text-xs focus:outline-none focus:border-emerald-700"
                      />
                      <span class="text-gray-400 text-xs">to</span>
                      <input 
                        v-model="avail.to_time" 
                        type="time" 
                        required 
                        class="px-2 py-1.5 bg-white text-gray-900 border border-gray-200 rounded-lg text-xs focus:outline-none focus:border-emerald-700"
                      />
                    </div>

                    <button 
                      type="button" 
                      @click="removeAvailability(index)"
                      class="text-red-500 hover:text-red-700 p-1.5 rounded-lg hover:bg-red-50 transition"
                    >
                      <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
                    </button>
                  </div>

                  <p v-if="form.availability.length === 0" class="text-[11px] text-gray-400 italic">
                    No availability slots added. Click "+ Add Availability" to specify your open hours.
                  </p>
                </div>
              </div>

              <!-- Submit Button -->
              <button 
                type="submit" 
                :disabled="loading"
                class="w-full mt-3 py-2.5 px-4 rounded-xl text-xs lg:text-sm font-bold text-white bg-[#064e3b] hover:bg-[#043d2e] focus:ring-2 focus:ring-emerald-700 focus:ring-offset-2 transition shadow-md flex items-center justify-center gap-2 disabled:opacity-70 group active:scale-[0.99]"
              >
                <span v-if="loading" class="flex items-center gap-2">
                  <svg class="animate-spin h-4 w-4 text-white" viewBox="0 0 24 24" fill="none">
                    <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                    <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                  </svg>
                  Submitting Application...
                </span>
                <span v-else class="flex items-center gap-2">
                  <span>Submit Application</span>
                  <svg class="w-4 h-4 transition-transform group-hover:translate-x-1" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M5 12h14" />
                    <path d="m12 5 7 7-7 7" />
                  </svg>
                </span>
              </button>

              <!-- Secondary Sign In Button -->
              <router-link 
                to="/account/login" 
                class="w-full py-2 px-4 rounded-xl text-xs lg:text-sm font-bold text-[#064e3b] bg-emerald-50 hover:bg-emerald-100 border border-emerald-200/60 focus:ring-2 focus:ring-emerald-700 transition flex items-center justify-center gap-2 text-center shadow-sm"
              >
                <svg class="w-3.5 h-3.5 text-emerald-700" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M15 3h4a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2h-4"></path>
                  <polyline points="10 17 15 12 10 7"></polyline>
                  <line x1="15" y1="12" x2="3" y2="12"></line>
                </svg>
                <span>Already registered? Sign In to Dashboard</span>
              </router-link>

            </form>
          </div>

          <!-- Bottom Security Encryption Badges -->
          <div class="mt-4 pt-3 border-t border-gray-100 flex flex-col sm:flex-row items-center justify-between text-[10.5px] text-gray-400 gap-1">
            <div class="flex items-center gap-1.5">
              <svg class="w-3.5 h-3.5 text-emerald-600" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <rect width="18" height="11" x="3" y="11" rx="2" ry="2" />
                <path d="M7 11V7a5 5 0 0 1 10 0v4" />
              </svg>
              <span>{{ settings.login_encryption_note || 'Protected by 256-bit encryption' }}</span>
            </div>
            <div>
              {{ settings.login_powered_by_note || 'Secure connection powered by Frappe Framework' }}
            </div>
          </div>

        </div>

      </div>
    </main>

    <!-- Bottom Page Footer -->
    <footer class="w-full max-w-6xl mx-auto px-6 py-2 shrink-0 flex flex-col sm:flex-row items-center justify-between text-[11px] text-gray-500 gap-2 border-t border-gray-100/80 z-20">
      <div>
        {{ settings.login_footer_copyright || '© 2026 Non Governmental Organisation. All rights reserved.' }}
      </div>
      <div class="flex items-center gap-2 sm:gap-3 flex-wrap justify-center">
        <template v-for="(link, idx) in footerLinks" :key="idx">
          <span v-if="idx > 0" class="text-gray-300">•</span>
          <a href="#" class="hover:text-gray-800 transition hover:underline">{{ link }}</a>
        </template>
      </div>
    </footer>
  </div>
</template>

<script setup>
import volunteersPlanting from "@/assets/volunteers_planting.jpg"

import { ref, computed, onMounted } from "vue";
import { call, createResource } from "frappe-ui";

const availableSkills = ref([]);

// Load portal settings dynamically from Frappe backend
const settingsResource = createResource({
  url: 'ngo.api.volunteer.get_portal_settings',
  method: 'GET',
  auto: true,
});

const settings = computed(() => settingsResource.data || {});

const footerLinks = computed(() => {
  const raw = settings.value.login_footer_links || 'Terms of Service | Volunteer Privacy Notice | Accessibility';
  return raw.split(/[|,•]/).map(s => s.trim()).filter(Boolean);
});

onMounted(async () => {
  try {
    const res = await call("ngo.api.volunteer.get_all_skills");
    if (res) {
      availableSkills.value = res;
    }
  } catch (e) {
    console.error(e);
  }
});

// Initialize form with 1 default skill row so user can pick immediately
const form = ref({
  applicant_name: "",
  email: "",
  phone: "",
  date_of_birth: "",
  gender: "",
  address: "",
  skills: [{ skill: "", proficiency: "Beginner" }],
  availability: [],
});

const loading = ref(false);
const error = ref("");
const success = ref(false);

// Phone input handler: strictly allow numbers only
function onPhoneInput(e) {
  if (form.value.phone) {
    form.value.phone = form.value.phone.replace(/[^0-9]/g, '');
  }
}

function addSkill() {
  form.value.skills.push({ skill: "", proficiency: "Beginner" });
}

function removeSkill(index) {
  form.value.skills.splice(index, 1);
}

function addAvailability() {
  form.value.availability.push({ day_of_week: "", from_time: "", to_time: "" });
}

function removeAvailability(index) {
  form.value.availability.splice(index, 1);
}

function validateEmail(email) {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
}

async function submitForm() {
  error.value = "";

  // 1. Full Name validation
  if (!form.value.applicant_name || !form.value.applicant_name.trim()) {
    error.value = "Full Name is mandatory.";
    return;
  }

  // 2. Email Address validation
  if (!form.value.email || !form.value.email.trim() || !validateEmail(form.value.email.trim())) {
    error.value = "A valid Email Address is mandatory.";
    return;
  }

  // 3. Phone Number: Mandatory & numbers only
  if (!form.value.phone || !form.value.phone.trim()) {
    error.value = "Phone Number is mandatory.";
    return;
  }
  const cleanPhone = form.value.phone.trim();
  if (!/^\d+$/.test(cleanPhone)) {
    error.value = "Phone Number must contain only digits.";
    return;
  }
  if (cleanPhone.length < 7 || cleanPhone.length > 15) {
    error.value = "Phone Number must be between 7 and 15 digits.";
    return;
  }

  // 4. Date of Birth: Mandatory
  if (!form.value.date_of_birth) {
    error.value = "Date of Birth is mandatory.";
    return;
  }

  // 5. Gender: Mandatory
  if (!form.value.gender) {
    error.value = "Gender is mandatory. Please select your gender.";
    return;
  }

  // 6. Address: Mandatory
  if (!form.value.address || !form.value.address.trim()) {
    error.value = "Residential Address is mandatory.";
    return;
  }

  // 7. Skills & Interests: Mandatory (at least one skill with a value selected)
  if (!form.value.skills || form.value.skills.length === 0) {
    error.value = "Skills & Interests are mandatory. Please add at least one skill.";
    return;
  }
  const validSkills = form.value.skills.filter(s => s.skill && s.skill.trim());
  if (validSkills.length === 0) {
    error.value = "Please select a skill from the dropdown for your skill entry.";
    return;
  }

  loading.value = true;

  try {
    const res = await call("ngo.api.volunteer.submit_application", {
      applicant_name: form.value.applicant_name.trim(),
      email: form.value.email.trim(),
      phone: cleanPhone,
      date_of_birth: form.value.date_of_birth,
      gender: form.value.gender,
      address: form.value.address.trim(),
      skills: JSON.stringify(validSkills),
      availability: JSON.stringify(form.value.availability || []),
    });

    if (res && res.status === "error") {
      error.value = res.message;
    } else {
      success.value = true;
    }
  } catch (err) {
    error.value =
      err.message ||
      err.exc ||
      "Failed to submit application. Please try again.";
  } finally {
    loading.value = false;
  }
}
</script>
