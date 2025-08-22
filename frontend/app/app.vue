<template>
  <UApp>
    <NuxtRouteAnnouncer />
    <NuxtPage />
  </UApp>
</template>

<script setup lang="ts">

useHead({
  title: 'Visio',
  meta: [
    { name: 'description', content: 'Visualize your data easily' },
    { name: 'viewport', content: 'width=device-width, initial-scale=1' }
  ]
});

</script>