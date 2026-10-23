<template>
  <div class="space-y-6 max-w-4xl">
    <div>
      <h2 class="text-xl font-bold text-slate-900 tracking-tight">
        Donor Profile
      </h2>
      <p class="text-xs text-slate-500 font-medium">
        Read-only institutional details and authorized portal access parameters.
      </p>
    </div>

    <div
      v-if="loading"
      class="h-64 bg-white rounded-2xl border border-slate-200 animate-pulse"
    ></div>

    <div
      v-else-if="profile"
      class="bg-white rounded-2xl p-6 border border-slate-200/90 shadow-xs space-y-6"
    >
      <div class="flex items-center space-x-4 pb-6 border-b border-slate-100">
        <div
          class="w-16 h-16 rounded-2xl bg-emerald-600 text-white flex items-center justify-center text-2xl font-black shadow-lg shadow-emerald-500/20"
        >
          {{ profile.donor_name ? profile.donor_name[0] : "D" }}
        </div>
        <div>
          <h3 class="text-lg font-bold text-slate-900">
            {{ profile.donor_name }}
          </h3>
          <span
            class="inline-block mt-1 px-2.5 py-0.5 rounded-full text-xs font-bold bg-emerald-100 text-emerald-800 border border-emerald-200"
          >
            Registered Donor Entity
          </span>
        </div>
      </div>

      <div class="grid grid-cols-1 sm:grid-cols-2 gap-6 text-xs">
        <div>
          <span
            class="text-slate-400 font-semibold uppercase tracking-wider block mb-1"
            >Entity Type</span
          >
          <span class="font-bold text-slate-800 text-sm">{{
            profile.supplier_type
          }}</span>
        </div>
        <div>
          <span
            class="text-slate-400 font-semibold uppercase tracking-wider block mb-1"
            >Primary Portal User</span
          >
          <span class="font-bold text-slate-800 text-sm">{{
            profile.contact_email
          }}</span>
        </div>
        <div>
          <span
            class="text-slate-400 font-semibold uppercase tracking-wider block mb-1"
            >Country Jurisdiction</span
          >
          <span class="font-bold text-slate-800 text-sm">{{
            profile.country
          }}</span>
        </div>
        <div>
          <span
            class="text-slate-400 font-semibold uppercase tracking-wider block mb-1"
            >Active Grant Agreements</span
          >
          <span class="font-bold text-emerald-600 text-sm"
            >{{ profile.active_grants_count }} Active</span
          >
        </div>
      </div>

      <!-- Inquire Card -->
      <div class="mt-6 pt-6 border-t border-slate-100">
        <h4 class="text-sm font-bold text-slate-900 mb-2">
          Need to update your entity details?
        </h4>
        <p class="text-xs text-slate-500 mb-4">
          Institutional contact modifications require formal compliance
          re-verification by our Liaison & Finance teams.
        </p>
        <button
          type="button"
          @click="showInquiry = !showInquiry"
          class="px-4 py-2 rounded-xl bg-slate-900 text-black text-xs font-bold hover:bg-slate-800 transition"
        >
          Submit Inquiry to Liaison Officer
        </button>

        <div
          v-if="showInquiry"
          class="mt-4 p-4 rounded-xl bg-slate-50 border border-slate-200 space-y-3"
        >
          <div>
            <label class="block text-xs font-bold text-slate-700 mb-1"
              >Subject</label
            >
            <input
              v-model="inquirySubject"
              type="text"
              placeholder="e.g. Update authorized representative email"
              class="w-full px-3 py-2 rounded-lg border border-slate-300 text-xs focus:ring-2 focus:ring-emerald-500 focus:outline-none"
            />
          </div>
          <div>
            <label class="block text-xs font-bold text-slate-700 mb-1"
              >Message</label
            >
            <textarea
              v-model="inquiryMessage"
              rows="3"
              placeholder="Provide context on requested changes..."
              class="w-full px-3 py-2 rounded-lg border border-slate-300 text-xs focus:ring-2 focus:ring-emerald-500 focus:outline-none"
            ></textarea>
          </div>
          <button
            type="button"
            @click="submitQuery"
            class="px-4 py-1.5 rounded-lg bg-emerald-600 text-white text-xs font-bold hover:bg-emerald-700 transition"
          >
            Send Inquiry
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref } from "vue";
import { donorApi } from "../api";

const loading = ref(true);
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
  if (!inquirySubject.value || !inquiryMessage.value)
    return alert("Please fill both subject and message.");
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
  }
}
</script>
