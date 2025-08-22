<template>
  <div class="flex flex-col items-center justify-center h-screen">
    <!-- <h1 class="text-3xl font-bold mb-4">Start here</h1> -->
    <!-- <USeparator color="secondary" class="w-64 mb-6" /> -->
    <UFileUpload highlight label="Upload your CSV file" v-model="value" class="w-96 min-h-48" accept="text/csv" />

    <!-- show loading modal if value is not null -->
    <UModal v-if="loading" v-model="value" :title="'Loading...'" :closeable="false" :size="'sm'">
      <div class="flex items-center justify-center h-32">
        <h1>Loading</h1>
      </div>
    </UModal>
  </div>
</template>

<script setup lang="ts">

const value = ref(null);
const loading = ref(false);

// loading state change after value is set
watch(value, (newValue) => {
  if (newValue) {
    loading.value = true;
    setTimeout(() => {
      loading.value = false;
    }, 2000); // Simulate loading time
  }
});


</script>