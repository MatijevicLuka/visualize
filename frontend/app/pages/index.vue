<template>
  <div class="flex flex-col items-center justify-center h-screen">
    <!-- <h1 class="text-3xl font-bold mb-4">Start here</h1> -->
    <!-- <USeparator color="secondary" class="w-64 mb-6" /> -->
    <UFileUpload color="secondary" highlight icon="i-lucide-image" label="Upload your CSV file" v-model="value" class="w-96 min-h-48"
      accept="text/csv" />
  </div>
</template>

<script setup lang="ts">

const value = ref(null);
</script>