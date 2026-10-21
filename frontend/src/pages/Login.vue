<template>
  <!-- Fixed full-viewport container with NO scrolling -->
  <div class="fixed inset-0 w-screen h-screen overflow-hidden bg-[#f8fafc] flex flex-col justify-between font-sans selection:bg-emerald-100 selection:text-emerald-900">
    <!-- Top Navigation Header (Fixed at top) -->
    <header class="bg-white border-b border-gray-100 px-6 lg:px-10 py-2.5 shrink-0 flex items-center justify-between shadow-[0_1px_3px_rgba(0,0,0,0.03)] z-20">
      <!-- Brand Logo & Title -->
      <div class="flex items-center gap-2.5">
        <template v-if="settings.login_logo">
          <img :src="settings.login_logo" alt="Logo" class="h-8 w-auto object-contain" />
        </template>
        <template v-else>
          <div class="w-8 h-8 rounded-xl bg-[#064e3b] flex items-center justify-center text-white shadow-sm shrink-0">
            <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M12 2v6" />
              <path d="M12 18v4" />
              <path d="M4.93 4.93l4.24 4.24" />
              <path d="M14.83 14.83l4.24 4.24" />
              <path d="M2 12h6" />
              <path d="M18 12h4" />
              <path d="M4.93 19.07l4.24-4.24" />
              <path d="M14.83 9.17l4.24-4.24" />
              <circle cx="12" cy="12" r="3" fill="currentColor" />
            </svg>
          </div>
        </template>
        <div>
          <div class="font-extrabold text-gray-900 text-sm lg:text-[15px] tracking-tight leading-none">
            {{ settings.login_portal_title || 'Non Governmental Organisation' }}
          </div>
          <div class="font-bold text-[#047857] text-[8px] tracking-[0.25em] uppercase leading-none mt-1">
            {{ settings.login_portal_subtitle || 'IMPACTSPHERE' }}
          </div>
        </div>
      </div>

      <!-- Header Right Utilities -->
      <div class="flex items-center gap-3 sm:gap-4">
        <!-- Language Switcher -->
        <div v-if="settings.login_enable_language_selector !== 0" class="relative hidden sm:block">
          <button 
            type="button"
            class="flex items-center gap-1.5 px-2.5 py-1 rounded-lg border border-gray-200/80 bg-white text-xs font-medium text-gray-700 shadow-sm hover:bg-gray-50 transition"
          >
            <svg class="w-3.5 h-3.5 text-gray-500" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <circle cx="12" cy="12" r="10" />
              <line x1="2" y1="12" x2="22" y2="12" />
              <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z" />
            </svg>
            <span>English (US)</span>
            <svg class="w-3 h-3 text-gray-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <polyline points="6 9 12 15 18 9" />
            </svg>
          </button>
        </div>

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
      </div>
    </header>

    <!-- Main Content Area: Centered, fills remaining space with NO scroll -->
    <main class="flex-1 min-h-0 w-full max-w-5xl xl:max-w-6xl mx-auto px-4 py-3 sm:py-4 flex items-center justify-center overflow-hidden">
      <div class="w-full h-full max-h-[calc(100vh-105px)] bg-white rounded-2xl lg:rounded-3xl shadow-[0_15px_50px_-10px_rgba(6,78,59,0.08)] border border-gray-100 overflow-hidden grid grid-cols-1 lg:grid-cols-12">
        
        <!-- Left Banner: Hero Section (Forest Green) -->
        <div class="lg:col-span-5 relative bg-gradient-to-br from-[#064e3b] via-[#043e2f] to-[#02281e] p-6 lg:p-8 flex flex-col justify-between text-white overflow-hidden">
          <!-- Background Subtle Overlay -->
          <div class="absolute inset-0 opacity-10 bg-[radial-gradient(#ffffff_1px,transparent_1px)] [background-size:16px_16px] pointer-events-none"></div>
          <div class="absolute -top-20 -right-20 w-64 h-64 bg-emerald-400/20 rounded-full blur-2xl pointer-events-none"></div>

          <!-- Top Hero Text -->
          <div>
            <!-- Pill Badge -->
            <div class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-emerald-900/80 border border-emerald-500/30 text-emerald-300 text-[10px] font-bold tracking-wider uppercase backdrop-blur-sm">
              <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <circle cx="12" cy="12" r="10" />
                <line x1="2" y1="12" x2="22" y2="12" />
                <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z" />
              </svg>
              <span>{{ settings.login_hero_badge || 'GLOBAL VOLUNTEER COMMUNITY' }}</span>
            </div>

            <!-- Headline -->
            <h1 class="text-2xl sm:text-[26px] lg:text-[30px] font-extrabold text-white tracking-tight leading-[1.2] mt-3 lg:mt-4">
              {{ settings.login_hero_title || 'Empowering communities, together.' }}
            </h1>

            <!-- Description -->
            <p class="text-emerald-100/80 text-xs leading-relaxed mt-2.5 font-normal">
              {{ settings.login_hero_description || 'Sign in to claim regional volunteer shifts, track community outcomes, and manage verified field contributions in real time.' }}
            </p>
          </div>

          <!-- Middle: Statistics Strip -->
          <div class="p-3 rounded-2xl bg-emerald-950/50 backdrop-blur-md border border-emerald-500/20 grid grid-cols-3 divide-x divide-emerald-500/20 text-center shadow-inner my-3">
            <div class="px-2">
              <div class="text-lg lg:text-xl font-black text-white tracking-tight">
                {{ settings.login_stat1_value || '120k+' }}
              </div>
              <div class="text-[9px] font-bold text-emerald-300/80 uppercase tracking-wider mt-0.5">
                {{ settings.login_stat1_label || 'HOURS LOGGED' }}
              </div>
            </div>
            <div class="px-2">
              <div class="text-lg lg:text-xl font-black text-amber-400 tracking-tight">
                {{ settings.login_stat2_value || '48' }}
              </div>
              <div class="text-[9px] font-bold text-emerald-300/80 uppercase tracking-wider mt-0.5">
                {{ settings.login_stat2_label || 'CHAPTERS' }}
              </div>
            </div>
            <div class="px-2">
              <div class="text-lg lg:text-xl font-black text-white tracking-tight">
                {{ settings.login_stat3_value || '99.8%' }}
              </div>
              <div class="text-[9px] font-bold text-emerald-300/80 uppercase tracking-wider mt-0.5">
                {{ settings.login_stat3_label || 'VERIFIED' }}
              </div>
            </div>
          </div>

          <!-- Bottom: Testimonial Card -->
          <div class="p-3.5 lg:p-4 rounded-2xl bg-emerald-950/45 backdrop-blur-md border border-emerald-500/20 text-left shadow-lg">
            <!-- Star Rating -->
            <div class="flex gap-1 text-amber-400 mb-2">
              <svg v-for="i in Number(settings.login_testimonial_stars || 5)" :key="i" class="w-3.5 h-3.5 fill-current" viewBox="0 0 20 20">
                <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
              </svg>
            </div>

            <!-- Quote -->
            <p class="text-emerald-100 text-[11px] lg:text-xs italic leading-relaxed mb-2.5">
              {{ settings.login_testimonial_quote || '"Every hour deployed across local food distributions and emergency shelters directly shifts the needle for our neighborhood families."' }}
            </p>

            <!-- Author / Chapter Lead -->
            <div class="flex items-center gap-2.5">
              <template v-if="settings.login_testimonial_avatar_image">
                <img :src="settings.login_testimonial_avatar_image" alt="Author" class="w-7 h-7 rounded-full object-cover shrink-0 border border-emerald-400/40" />
              </template>
              <template v-else>
                <div class="w-7 h-7 rounded-full bg-orange-600 text-white font-bold text-[10px] flex items-center justify-center shrink-0 shadow-sm">
                  {{ settings.login_testimonial_avatar_initials || 'EC' }}
                </div>
              </template>
              <div class="min-w-0">
                <div class="text-xs font-bold text-white leading-tight truncate">
                  {{ settings.login_testimonial_author || 'Elena Cruz' }}
                </div>
                <div class="text-[10px] text-emerald-300/80 leading-tight truncate mt-0.5">
                  {{ settings.login_testimonial_role || 'Pacific Chapter Deployment Lead' }}
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Right Panel: Login Form -->
        <div class="lg:col-span-7 p-6 lg:p-8 xl:p-10 flex flex-col justify-between bg-white overflow-hidden">
          <!-- Top Area: Icon, Title & Form -->
          <div>
            <!-- Form Icon Badge (Clean & fully visible) -->
            <div class="w-10 h-10 rounded-xl bg-emerald-50 border border-emerald-100/80 flex items-center justify-center text-emerald-700 mb-3 shadow-sm">
              <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2" />
                <circle cx="9" cy="7" r="4" />
                <path d="M22 21v-2a4 4 0 0 0-3-3.87" />
                <path d="M16 3.13a4 4 0 0 1 0 7.75" />
              </svg>
            </div>

            <!-- Form Title & Subtitle -->
            <h2 class="text-2xl lg:text-[26px] font-extrabold text-gray-900 tracking-tight leading-tight">
              {{ settings.login_form_title || 'Welcome back, changemaker' }}
            </h2>
            <p class="text-xs text-gray-500 mt-1 leading-normal">
              {{ settings.login_form_subtitle || 'Log in to access your deployment shifts, impact ledger, and verified hours.' }}
            </p>

            <!-- Social / SSO Login Buttons -->
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-2.5 mt-3.5">
              <button 
                v-if="settings.login_show_google_login !== 0"
                type="button" 
                @click="handleGoogleLogin"
                class="flex items-center justify-center gap-2 py-2 px-3 rounded-xl border border-gray-200 text-xs font-semibold text-gray-700 hover:bg-gray-50 hover:border-gray-300 transition shadow-sm"
              >
                <svg class="w-4 h-4 shrink-0" viewBox="0 0 24 24">
                  <path fill="#4285F4" d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z" />
                  <path fill="#34A853" d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z" />
                  <path fill="#FBBC05" d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.06H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.94l2.85-2.22.81-.63z" />
                  <path fill="#EA4335" d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.06l3.66 2.84c.87-2.6 3.3-4.52 6.16-4.52z" />
                </svg>
                <span>{{ settings.login_google_label || 'Google Account' }}</span>
              </button>

              <button 
                v-if="settings.login_show_sso_login !== 0"
                type="button" 
                @click="handleSSOLogin"
                class="flex items-center justify-center gap-2 py-2 px-3 rounded-xl border border-gray-200 text-xs font-semibold text-gray-700 hover:bg-gray-50 hover:border-gray-300 transition shadow-sm"
              >
                <svg class="w-4 h-4 text-emerald-700 shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="m21 2-2 2m-1.5 1.5L14 9l-2-2-4 4-2-2-4 4 5 5 1-1 4-4-2-2 3.5-3.5M19 7l2 2" />
                  <circle cx="15.5" cy="8.5" r="1.5" />
                </svg>
                <span>{{ settings.login_sso_label || 'NGO SSO Portal' }}</span>
              </button>
            </div>

            <!-- Divider -->
            <div class="relative my-3 text-center">
              <div class="absolute inset-0 flex items-center">
                <div class="w-full border-t border-gray-200/80"></div>
              </div>
              <div class="relative inline-block bg-white px-2.5 text-[9px] font-bold text-gray-400 tracking-wider uppercase">
                {{ settings.login_divider_text || 'OR SIGN IN WITH EMAIL' }}
              </div>
            </div>

            <!-- Main Sign-in Form -->
            <form @submit.prevent="login" class="space-y-2.5">
              <!-- Error Banner -->
              <div v-if="error" class="bg-red-50 border border-red-200 text-red-600 px-3 py-1.5 rounded-xl text-xs font-medium flex items-center gap-2 animate-pulse">
                <svg class="w-3.5 h-3.5 shrink-0" viewBox="0 0 20 20" fill="currentColor">
                  <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z" clip-rule="evenodd" />
                </svg>
                <span>{{ error }}</span>
              </div>

              <!-- Email Field -->
              <div class="space-y-1">
                <label class="block text-[10px] font-bold text-gray-700 uppercase tracking-wider">
                  {{ settings.login_email_label || 'VOLUNTEER EMAIL ADDRESS' }}
                </label>
                <div class="relative rounded-xl border border-gray-200 focus-within:border-emerald-700 focus-within:ring-2 focus-within:ring-emerald-700/15 transition shadow-sm bg-white">
                  <div class="absolute inset-y-0 left-0 pl-3.5 flex items-center pointer-events-none text-gray-400">
                    <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                      <rect width="20" height="16" x="2" y="4" rx="2" />
                      <path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7" />
                    </svg>
                  </div>
                  <input 
                    v-model="email" 
                    type="email" 
                    required 
                    :placeholder="settings.login_email_placeholder || 'you@example.com'"
                    class="block w-full pl-10 pr-3.5 py-2 text-xs lg:text-sm text-gray-900 placeholder-gray-400 bg-transparent rounded-xl focus:outline-none"
                  />
                </div>
              </div>

              <!-- Password Field -->
              <div class="space-y-1">
                <div class="flex items-center justify-between">
                  <label class="block text-[10px] font-bold text-gray-700 uppercase tracking-wider">
                    {{ settings.login_password_label || 'PASSWORD' }}
                  </label>
                  <a 
                    :href="settings.login_forgot_password_url || '#'" 
                    @click.prevent="handleForgotPassword"
                    class="text-xs font-semibold text-amber-700 hover:text-amber-800 transition hover:underline"
                  >
                    {{ settings.login_forgot_password_label || 'Forgot password?' }}
                  </a>
                </div>
                <div class="relative rounded-xl border border-gray-200 focus-within:border-emerald-700 focus-within:ring-2 focus-within:ring-emerald-700/15 transition shadow-sm bg-white">
                  <div class="absolute inset-y-0 left-0 pl-3.5 flex items-center pointer-events-none text-gray-400">
                    <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                      <rect width="18" height="11" x="3" y="11" rx="2" ry="2" />
                      <path d="M7 11V7a5 5 0 0 1 10 0v4" />
                    </svg>
                  </div>
                  <input 
                    v-model="password" 
                    :type="showPassword ? 'text' : 'password'" 
                    required 
                    placeholder="••••••••••••••••"
                    class="block w-full pl-10 pr-10 py-2 text-xs lg:text-sm text-gray-900 placeholder-gray-400 bg-transparent rounded-xl focus:outline-none"
                  />
                  <!-- Toggle Visibility -->
                  <button 
                    type="button" 
                    @click="showPassword = !showPassword"
                    class="absolute inset-y-0 right-0 pr-3.5 flex items-center text-gray-400 hover:text-gray-600 transition"
                  >
                    <svg v-if="!showPassword" class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                      <path d="M2 12s3-7 10-7 10 7 10 7-3 7-10 7-10-7-10-7Z" />
                      <circle cx="12" cy="12" r="3" />
                    </svg>
                    <svg v-else class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                      <path d="m15 18-.722-3.25" />
                      <path d="M2 8a10.645 10.645 0 0 0 20 0" />
                      <path d="m20 15-1.726-2.05" />
                      <path d="m4 15 1.726-2.05" />
                      <path d="m9 18 .722-3.25" />
                    </svg>
                  </button>
                </div>
              </div>

              <!-- Remember Me & Security Guard -->
              <div class="flex items-center justify-between pt-0.5">
                <label class="flex items-center gap-2 cursor-pointer select-none">
                  <input 
                    v-model="rememberMe" 
                    type="checkbox" 
                    class="w-4 h-4 rounded text-[#064e3b] border-gray-300 focus:ring-emerald-700 cursor-pointer"
                  />
                  <span class="text-xs text-gray-600">
                    {{ settings.login_remember_me_label || 'Remember this station for 30 days' }}
                  </span>
                </label>
                <div class="flex items-center gap-1.5 text-xs font-semibold text-emerald-800">
                  <svg class="w-3.5 h-3.5 fill-current" viewBox="0 0 24 24">
                    <path d="M12 1L3 5v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V5l-9-4z" />
                  </svg>
                  <span>{{ settings.login_security_badge_label || 'Frappe Guard' }}</span>
                </div>
              </div>

              <!-- Submit Button (Primary Forest Green) -->
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
                  Authenticating...
                </span>
                <span v-else class="flex items-center gap-2">
                  <span>{{ settings.login_submit_button_label || 'Sign In to Dashboard' }}</span>
                  <svg class="w-4 h-4 transition-transform group-hover:translate-x-1" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M5 12h14" />
                    <path d="m12 5 7 7-7 7" />
                  </svg>
                </span>
              </button>

              <!-- Secondary Apply Button -->
              <router-link 
                :to="settings.login_apply_button_url || '/apply'" 
                class="w-full py-2 px-4 rounded-xl text-xs lg:text-sm font-bold text-[#064e3b] bg-emerald-50 hover:bg-emerald-100 border border-emerald-200/60 focus:ring-2 focus:ring-emerald-700 transition flex items-center justify-center gap-2 text-center shadow-sm"
              >
                <svg class="w-3.5 h-3.5 text-orange-600" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z" />
                </svg>
                <span>{{ settings.login_apply_button_label || 'Apply to be a Volunteer' }}</span>
              </router-link>
            </form>
          </div>

          <!-- Bottom Security & Badge Scan Section -->
          <div class="mt-3">
            <!-- Physical Deployment Hub Scan -->
            <div v-if="settings.login_show_badge_scan !== 0" class="pt-2 border-t border-gray-100 flex items-center justify-between text-xs">
              <div class="flex items-center gap-2 text-gray-500">
                <svg class="w-3.5 h-3.5 text-gray-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <rect width="5" height="5" x="3" y="3" rx="1" />
                  <rect width="5" height="5" x="16" y="3" rx="1" />
                  <rect width="5" height="5" x="3" y="16" rx="1" />
                  <path d="M21 16h-3a2 2 0 0 0-2 2v3" />
                  <path d="M21 21v.01" />
                  <path d="M12 7v3a2 2 0 0 1-2 2H7" />
                  <path d="M3 12h.01" />
                  <path d="M12 3h.01" />
                  <path d="M12 16v.01" />
                  <path d="M16 12h1" />
                  <path d="M21 12v.01" />
                  <path d="M12 21v-1" />
                </svg>
                <span>{{ settings.login_badge_scan_text || 'At a physical deployment hub?' }}</span>
              </div>
              <a 
                :href="settings.login_badge_scan_url || '#'" 
                class="font-bold text-gray-800 hover:text-emerald-800 hover:underline transition"
              >
                {{ settings.login_badge_scan_link_label || 'Scan Volunteer Badge' }}
              </a>
            </div>

            <!-- Footer Security Encryption Badges -->
            <div class="mt-2 pt-2 border-t border-gray-100 flex flex-col sm:flex-row items-center justify-between text-[10.5px] text-gray-400 gap-1">
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
      </div>
    </main>

    <!-- Bottom Page Footer (Fixed at bottom) -->
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
import { ref, computed } from 'vue'
import { session } from '../data/session'
import { useRouter } from 'vue-router'
import { createResource } from 'frappe-ui'

const router = useRouter()
const email = ref('')
const password = ref('')
const rememberMe = ref(true)
const showPassword = ref(false)
const loading = ref(false)
const error = ref('')

// Load portal settings dynamically from Frappe backend
const settingsResource = createResource({
  url: 'ngo.api.volunteer.get_portal_settings',
  method: 'GET',
  auto: true,
})

const settings = computed(() => settingsResource.data || {})

const footerLinks = computed(() => {
  const raw = settings.value.login_footer_links || 'Terms of Service | Volunteer Privacy Notice | Accessibility'
  return raw.split(/[|,•]/).map(s => s.trim()).filter(Boolean)
})

function handleGoogleLogin() {
  const url = settings.value.login_google_url && settings.value.login_google_url !== '#'
    ? settings.value.login_google_url
    : '/api/method/frappe.integrations.oauth2_logins.custom?provider=google'
  window.location.href = url
}

function handleSSOLogin() {
  const url = settings.value.login_sso_url && settings.value.login_sso_url !== '#'
    ? settings.value.login_sso_url
    : '/api/method/frappe.integrations.oauth2_logins.custom?provider=openid'
  window.location.href = url
}

function handleForgotPassword() {
  if (settings.value.login_forgot_password_url && settings.value.login_forgot_password_url !== '#') {
    window.location.href = settings.value.login_forgot_password_url
  } else {
    // Default Frappe forgot password route
    window.location.href = '/update-password'
  }
}

async function login() {
  loading.value = true
  error.value = ''
  
  try {
    await session.login.submit({
      email: email.value,
      password: password.value
    })
    
    if (session.login.error) {
      throw new Error(session.login.error)
    }
  } catch (err) {
    const rawError = String(err.message || session.login.error || err || '')
    if (rawError.includes('AuthenticationError') || rawError.includes('Invalid Login') || rawError.includes('401')) {
      error.value = 'Invalid email or password. Please check your credentials.'
    } else {
      error.value = 'An error occurred during login. Please try again later.'
    }
  } finally {
    loading.value = false
  }
}
</script>
