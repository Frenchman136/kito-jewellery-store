<script setup lang="ts">
defineProps<{ modelValue: string }>()
const emit = defineEmits<{ 'update:modelValue': [value: string] }>()
const chips = ['all', ...CATEGORIES]
</script>

<template>
  <div class="flex flex-wrap gap-2" role="group" aria-label="Filter by category">
    <button
      v-for="c in chips" :key="c" type="button"
      :aria-pressed="modelValue === c"
      class="rounded-full border px-5 py-2 text-sm font-medium transition-colors duration-200 ease-out"
      :class="modelValue === c ? 'border-ink bg-ink text-white' : 'border-stone bg-ivory text-ink hover:border-gold'"
      @click="emit('update:modelValue', c)"
    >{{ cap(c) }}</button>
  </div>
</template>
