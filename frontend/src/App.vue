<template>
  <div>
    <router-view v-if="!settings.loading" />
  </div>
</template>

<script setup>
import { createResource } from 'frappe-ui'
import { onMounted } from 'vue'

const settings = createResource({
  url: 'ngo.api.volunteer.get_portal_settings',
  auto: true,
  onSuccess(data) {
    if (data) {
      if (data.primary_color) {
        document.documentElement.style.setProperty('--primary-color', data.primary_color)
      }
      if (data.secondary_color) {
        document.documentElement.style.setProperty('--secondary-color', data.secondary_color)
      }
      if (data.login_color) {
        document.documentElement.style.setProperty('--login-color', data.login_color)
      }
      if (data.sidebar_color) {
        document.documentElement.style.setProperty('--sidebar-color', data.sidebar_color)
      }
    }
  }
})
</script>
