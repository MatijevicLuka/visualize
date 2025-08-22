<template>
    <UModal
        v-model="show"
        :title="props.message"
        :closeable="true"
        :size="'sm'"
        />
</template>

<script setup lang="ts">

const props = defineProps<{
    message: string;
}>();

const show = ref(true);
</script>