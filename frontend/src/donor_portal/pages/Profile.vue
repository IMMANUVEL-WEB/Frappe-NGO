<template>
  <div class="space-y-6 w-full">
    <!-- Page Title & Breadcrumb -->
    <div
      class="flex flex-col sm:flex-row sm:items-center justify-between gap-3"
    >
      <div>
        <h2 class="text-xl font-black text-slate-900 tracking-tight">
          Donor Profile & Organization Account
        </h2>
        <p class="text-xs text-slate-500 font-medium mt-0.5">
          Read-only institutional registration details, compliance status, and
          authorized portal access parameters.
        </p>
      </div>
      <div class="flex items-center space-x-2">
        <router-link
          to="/donor-portal/grants"
          class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-xl border border-slate-200 text-xs font-semibold text-slate-700 bg-white hover:bg-slate-50 transition shadow-xs"
        >
          <svg
            class="w-4 h-4 text-emerald-600"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"
            />
          </svg>
          <span>View Grant Portfolio</span>
        </router-link>
      </div>
    </div>

    <!-- Loading Skeleton -->
    <div
      v-if="loading"
      class="h-96 bg-black rounded-2xl border border-slate-200 animate-pulse w-full"
    ></div>

    <div v-else-if="profile" class="space-y-6 w-full">
      <!-- Full-Width Hero Card -->
      <div
        class="relative overflow-hidden rounded-3xl bg-gradient-to-r from-slate-900 via-slate-800 to-emerald-950 p-6 md:p-8 text-black shadow-xl"
      >
        <!-- Background Decorative Glow -->
        <div
          class="absolute -right-20 -top-20 w-80 h-80 rounded-full bg-emerald-500/10 blur-3xl pointer-events-none"
        ></div>
        <div
          class="absolute right-1/3 -bottom-20 w-60 h-60 rounded-full bg-teal-500/10 blur-3xl pointer-events-none"
        ></div>

        <div
          class="relative z-10 flex flex-col lg:flex-row lg:items-center justify-between gap-6"
        >
          <!-- Left: Avatar & Identity -->
          <div class="flex items-center space-x-5">
            <div
              class="w-20 h-20 rounded-2xl bg-gradient-to-tr from-emerald-600 to-teal-400 text-black flex items-center justify-center text-3xl font-black shadow-lg shadow-emerald-500/25 shrink-0 border border-emerald-400/30"
            >
              {{ profile.donor_name ? profile.donor_name[0] : "D" }}
            </div>
            <div>
              <div class="flex flex-wrap items-center gap-2">
                <h3 class="text-2xl font-black tracking-tight text-black">
                  {{ profile.donor_name }}
                </h3>
                <span
                  class="inline-flex items-center gap-1 px-3 py-0.5 rounded-full text-xs font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 backdrop-blur-xs"
                >
                  <svg
                    class="w-3.5 h-3.5"
                    fill="currentColor"
                    viewBox="0 0 20 20"
                  >
                    <path
                      fill-rule="evenodd"
                      d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z"
                      clip-rule="evenodd"
                    />
                  </svg>
                  Verified Institutional Donor
                </span>
              </div>
              <p
                class="text-xs text-slate-300 mt-1 flex flex-wrap items-center gap-3"
              >
                <span class="flex items-center gap-1.5">
                  <svg
                    class="w-3.5 h-3.5 text-slate-400"
                    fill="none"
                    stroke="currentColor"
                    viewBox="0 0 24 24"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M16 12a4 4 0 10-8 0 4 4 0 008 0zm0 0v1.5a2.5 2.5 0 005 0V12a9 9 0 10-9 9m4.5-1.206a8.959 8.959 0 01-4.5 1.207"
                    />
                  </svg>
                  {{ profile.contact_email }}
                </span>
                <span class="text-slate-600">&bull;</span>
                <span class="flex items-center gap-1.5">
                  <svg
                    class="w-3.5 h-3.5 text-slate-400"
                    fill="none"
                    stroke="currentColor"
                    viewBox="0 0 24 24"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M3.055 11H5a2 2 0 012 2v1a2 2 0 002 2 2 2 0 012 2v2.945M8 3.935V5.5A2.5 2.5 0 0010.5 8h.5a2 2 0 012 2 2 2 0 104 0 2 2 0 012-2h1.064M15 20.488V18a2 2 0 012-2h3.064"
                    />
                  </svg>
                  Jurisdiction: {{ profile.country || "India" }}
                </span>
              </p>
            </div>
          </div>

          <!-- Right: Key Summary Badges -->
          <div class="flex items-center gap-3 shrink-0">
            <div
              class="bg-black/10 backdrop-blur-md rounded-2xl p-4 border border-black/10 min-w-[130px] text-center"
            >
              <span
                class="text-[10px] font-bold uppercase tracking-wider text-slate-300 block"
                >Active Grants</span
              >
              <span class="text-2xl font-black text-emerald-400 mt-0.5 block">{{
                profile.active_grants_count || 1
              }}</span>
              <span class="text-[10px] text-slate-400">Current Portfolio</span>
            </div>
            <div
              class="bg-black/10 backdrop-blur-md rounded-2xl p-4 border border-black/10 min-w-[130px] text-center"
            >
              <span
                class="text-[10px] font-bold uppercase tracking-wider text-slate-300 block"
                >Security Tier</span
              >
              <span class="text-sm font-black text-black mt-1 block"
                >Tier-1 Principal</span
              >
              <span class="text-[10px] text-emerald-300"
                >Audited & Verified</span
              >
            </div>
          </div>
        </div>
      </div>

      <!-- Main Full-Width Two-Column Layout -->
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 w-full">
        <!-- Left Column: Details & Inquiry (8 cols) -->
        <div class="lg:col-span-8 space-y-6">
          <!-- Institutional Entity Details Card -->
          <div
            class="bg-white rounded-2xl p-6 border border-slate-100 shadow-xs space-y-5"
          >
            <div
              class="flex items-center justify-between pb-3 border-b border-slate-100"
            >
              <div class="flex items-center space-x-2.5">
                <div
                  class="w-8 h-8 rounded-xl bg-blue-50 text-blue-600 flex items-center justify-center"
                >
                  <svg
                    class="w-4 h-4"
                    fill="none"
                    stroke="currentColor"
                    viewBox="0 0 24 24"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"
                    />
                  </svg>
                </div>
                <div>
                  <h3 class="text-sm font-bold text-slate-900 tracking-tight">
                    Institutional & Legal Parameters
                  </h3>
                  <p class="text-[11px] text-slate-400 font-medium">
                    Official registration metadata tied to donor account
                  </p>
                </div>
              </div>
              <span
                class="px-2.5 py-0.5 rounded-full text-[11px] font-bold bg-slate-100 text-slate-700"
              >
                Read-Only Record
              </span>
            </div>

            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <!-- Entity Legal Name -->
              <div
                class="p-3.5 rounded-xl bg-slate-50/70 border border-slate-100"
              >
                <span
                  class="text-[11px] font-bold uppercase tracking-wider text-slate-400 block mb-1"
                  >Entity Legal Name</span
                >
                <span class="font-bold text-slate-900 text-sm block">{{
                  profile.donor_name
                }}</span>
              </div>

              <!-- Entity Classification -->
              <div
                class="p-3.5 rounded-xl bg-slate-50/70 border border-slate-100"
              >
                <span
                  class="text-[11px] font-bold uppercase tracking-wider text-slate-400 block mb-1"
                  >Entity Classification</span
                >
                <span class="font-bold text-slate-900 text-sm block">{{
                  profile.supplier_type || "Institutional Donor"
                }}</span>
              </div>

              <!-- Primary Portal User -->
              <div
                class="p-3.5 rounded-xl bg-slate-50/70 border border-slate-100"
              >
                <span
                  class="text-[11px] font-bold uppercase tracking-wider text-slate-400 block mb-1"
                  >Primary Portal User</span
                >
                <span
                  class="font-bold text-slate-900 text-sm block truncate"
                  :title="profile.contact_email"
                >
                  {{ profile.contact_email }}
                </span>
              </div>

              <!-- Jurisdiction -->
              <div
                class="p-3.5 rounded-xl bg-slate-50/70 border border-slate-100"
              >
                <span
                  class="text-[11px] font-bold uppercase tracking-wider text-slate-400 block mb-1"
                  >Country Jurisdiction</span
                >
                <span class="font-bold text-slate-900 text-sm block">{{
                  profile.country || "India"
                }}</span>
              </div>

              <!-- Tax ID / PAN -->
              <div
                class="p-3.5 rounded-xl bg-slate-50/70 border border-slate-100"
              >
                <span
                  class="text-[11px] font-bold uppercase tracking-wider text-slate-400 block mb-1"
                  >Statutory Verification / PAN</span
                >
                <span class="font-bold text-slate-900 text-sm block">{{
                  profile.pan || "PAN Verified on File"
                }}</span>
              </div>

              <!-- Active Agreements -->
              <div
                class="p-3.5 rounded-xl bg-emerald-50/50 border border-emerald-100/70"
              >
                <span
                  class="text-[11px] font-bold uppercase tracking-wider text-emerald-700 block mb-1"
                  >Active Grant Agreements</span
                >
                <span class="font-black text-emerald-800 text-sm block"
                  >{{ profile.active_grants_count || 1 }} Active
                  Agreements</span
                >
              </div>
            </div>
          </div>

          <!-- Official Liaison Desk / Update Request Form -->
          <div
            class="bg-white rounded-2xl p-6 border border-slate-100 shadow-xs space-y-4"
          >
            <div
              class="flex items-center justify-between pb-3 border-b border-slate-100"
            >
              <div class="flex items-center space-x-2.5">
                <div
                  class="w-8 h-8 rounded-xl bg-emerald-50 text-emerald-600 flex items-center justify-center"
                >
                  <svg
                    class="w-4 h-4"
                    fill="none"
                    stroke="currentColor"
                    viewBox="0 0 24 24"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z"
                    />
                  </svg>
                </div>
                <div>
                  <h4 class="text-sm font-bold text-slate-900 tracking-tight">
                    Submit Inquiry to Liaison Officer
                  </h4>
                  <p class="text-[11px] text-slate-400 font-medium">
                    Contact modifications require formal compliance
                    re-verification by our Liaison & Finance teams.
                  </p>
                </div>
              </div>
              <button
                type="button"
                @click="showInquiry = !showInquiry"
                class="px-3 py-1.5 rounded-xl text-xs font-bold transition flex items-center gap-1.5"
                :class="
                  showInquiry
                    ? 'bg-slate-100 text-slate-700'
                    : 'bg-emerald-600 hover:bg-emerald-700 text-black shadow-xs'
                "
              >
                <span>{{ showInquiry ? "Hide Form" : "New Inquiry" }}</span>
              </button>
            </div>

            <!-- Notice when closed -->
            <div
              v-if="!showInquiry"
              class="p-4 rounded-xl bg-slate-50/70 border border-slate-100 text-xs text-slate-600 flex items-center justify-between"
            >
              <div class="flex items-center space-x-2.5">
                <svg
                  class="w-4 h-4 text-emerald-600 shrink-0"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
                  />
                </svg>
                <span
                  >Need to update legal address, bank disbursement mandates, or
                  authorized signatory emails?</span
                >
              </div>
              <button
                type="button"
                @click="showInquiry = true"
                class="text-xs font-bold text-emerald-600 hover:text-emerald-700 blackspace-nowrap ml-2"
              >
                Start Inquiry &rarr;
              </button>
            </div>

            <!-- Inquiry Form Container -->
            <div
              v-if="showInquiry"
              class="p-5 rounded-2xl bg-slate-50 border border-slate-200/80 space-y-4"
            >
              <div>
                <label class="block text-xs font-bold text-slate-700 mb-1"
                  >Inquiry Subject</label
                >
                <input
                  v-model="inquirySubject"
                  type="text"
                  placeholder="e.g. Request to update authorized representative email or bank KYC"
                  class="w-full px-3.5 py-2.5 rounded-xl border border-slate-200 bg-white text-xs text-slate-800 placeholder-slate-400 focus:ring-2 focus:ring-emerald-500/20 focus:border-emerald-500 focus:outline-none shadow-xs"
                />
              </div>

              <div>
                <label class="block text-xs font-bold text-slate-700 mb-1"
                  >Message Details</label
                >
                <textarea
                  v-model="inquiryMessage"
                  rows="4"
                  placeholder="Provide context and requested modifications for our Liaison & Finance teams..."
                  class="w-full px-3.5 py-2.5 rounded-xl border border-slate-200 bg-white text-xs text-slate-800 placeholder-slate-400 focus:ring-2 focus:ring-emerald-500/20 focus:border-emerald-500 focus:outline-none shadow-xs"
                ></textarea>
              </div>

              <div class="flex items-center justify-end space-x-3 pt-1">
                <button
                  type="button"
                  @click="showInquiry = false"
                  class="px-4 py-2 rounded-xl border border-slate-200 text-xs font-semibold text-slate-600 hover:bg-slate-100 transition"
                >
                  Cancel
                </button>
                <button
                  type="button"
                  :disabled="submitting"
                  @click="submitQuery"
                  class="px-5 py-2 rounded-xl bg-emerald-600 text-black text-xs font-bold hover:bg-emerald-700 transition shadow-md shadow-emerald-600/20 disabled:opacity-50 flex items-center gap-1.5"
                >
                  <svg
                    v-if="submitting"
                    class="animate-spin h-3.5 w-3.5 text-black"
                    viewBox="0 0 24 24"
                    fill="none"
                  >
                    <circle
                      class="opacity-25"
                      cx="12"
                      cy="12"
                      r="10"
                      stroke="currentColor"
                      stroke-width="4"
                    ></circle>
                    <path
                      class="opacity-75"
                      fill="currentColor"
                      d="M4 12a8 8 0 018-8v8H4z"
                    ></path>
                  </svg>
                  <span>{{
                    submitting ? "Transmitting..." : "Send Official Inquiry"
                  }}</span>
                </button>
              </div>
            </div>
          </div>
        </div>

        <!-- Right Column: Security, Compliance & Support (4 cols) -->
        <div class="lg:col-span-4 space-y-6">
          <!-- Security & Access Parameters Card -->
          <div
            class="bg-white rounded-2xl p-6 border border-slate-100 shadow-xs space-y-4"
          >
            <div
              class="flex items-center space-x-2.5 pb-3 border-b border-slate-100"
            >
              <div
                class="w-8 h-8 rounded-xl bg-purple-50 text-purple-600 flex items-center justify-center"
              >
                <svg
                  class="w-4 h-4"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"
                  />
                </svg>
              </div>
              <div>
                <h3 class="text-sm font-bold text-slate-900 tracking-tight">
                  Security & Governance
                </h3>
                <p class="text-[11px] text-slate-400 font-medium">
                  Access permissions & verification
                </p>
              </div>
            </div>

            <div class="space-y-3 text-xs">
              <div
                class="flex items-center justify-between p-2.5 rounded-xl bg-slate-50"
              >
                <span class="text-slate-500 font-medium">Authentication</span>
                <span class="font-bold text-slate-900"
                  >Frappe SSL Encrypted</span
                >
              </div>
              <div
                class="flex items-center justify-between p-2.5 rounded-xl bg-slate-50"
              >
                <span class="text-slate-500 font-medium">PII Protection</span>
                <span class="font-bold text-emerald-600"
                  >Zero Leakage Compliant</span
                >
              </div>
              <div
                class="flex items-center justify-between p-2.5 rounded-xl bg-slate-50"
              >
                <span class="text-slate-500 font-medium">Audit Trail</span>
                <span class="font-bold text-slate-900">Immutable Ledger</span>
              </div>
              <div
                class="flex items-center justify-between p-2.5 rounded-xl bg-slate-50"
              >
                <span class="text-slate-500 font-medium">KYC State</span>
                <span
                  class="inline-flex items-center gap-1 font-bold text-emerald-700"
                >
                  <span class="w-1.5 h-1.5 rounded-full bg-emerald-500"></span>
                  Fully Compliant
                </span>
              </div>
            </div>
          </div>

          <!-- Institutional Support Desk Card -->
          <div
            class="bg-gradient-to-br from-emerald-500/10 via-teal-500/5 to-slate-50 rounded-2xl p-6 border border-emerald-100/80 shadow-xs space-y-4"
          >
            <div class="flex items-center space-x-2.5">
              <div
                class="w-8 h-8 rounded-xl bg-emerald-600 text-black flex items-center justify-center font-bold text-sm shadow-xs"
              >
                ?
              </div>
              <div>
                <h4 class="text-sm font-bold text-slate-900 tracking-tight">
                  Liaison Support Desk
                </h4>
                <p class="text-[11px] text-slate-500 font-medium">
                  Dedicated Donor Relations Team
                </p>
              </div>
            </div>

            <p class="text-xs text-slate-600 leading-relaxed">
              Have questions regarding grant milestones, fund drawdown
              schedules, or financial utilization certificates?
            </p>

            <div class="pt-2 border-t border-emerald-200/40 space-y-2 text-xs">
              <div class="flex items-center justify-between text-slate-600">
                <span>Standard Response SLA:</span>
                <span class="font-bold text-slate-900">24 - 48 Hours</span>
              </div>
              <div class="flex items-center justify-between text-slate-600">
                <span>Department:</span>
                <span class="font-bold text-slate-900">Donor Engagement</span>
              </div>
            </div>

            <button
              type="button"
              @click="showInquiry = true"
              class="w-full mt-2 py-2 px-3 rounded-xl bg-slate-900 hover:bg-slate-800 text-black text-xs font-bold transition flex items-center justify-center gap-1.5"
            >
              <span>Contact Liaison Desk</span>
              <span>&rarr;</span>
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref } from "vue";
import { donorApi } from "../api";

const loading = ref(true);
const submitting = ref(false);
const profile = ref(null);
const showInquiry = ref(false);
const inquirySubject = ref("");
const inquiryMessage = ref("");

onMounted(async () => {
  try {
    const res = await donorApi.getProfile();
    if (res) profile.value = res;
  } catch (e) {
    console.error("Failed to load profile:", e);
  } finally {
    loading.value = false;
  }
});

async function submitQuery() {
  if (!inquirySubject.value || !inquiryMessage.value) {
    return alert("Please fill both subject and message.");
  }
  submitting.value = true;
  try {
    const res = await donorApi.submitQuery({
      subject: inquirySubject.value,
      message: inquiryMessage.value,
    });
    alert(res.message || "Inquiry sent successfully.");
    showInquiry.value = false;
    inquirySubject.value = "";
    inquiryMessage.value = "";
  } catch (e) {
    alert(e.message || "Failed to submit inquiry.");
  } finally {
    submitting.value = false;
  }
}
</script>
