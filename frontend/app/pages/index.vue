<template>
  <div class="flex flex-col items-center justify-center h-screen">
    <UFileUpload highlight icon="i-lucide-image" label="Upload your CSV file" v-model="value" class="w-96 min-h-48"
      accept="text/csv" />
  </div>
</template>

<script setup lang="ts">
const value = ref(null);
</script>