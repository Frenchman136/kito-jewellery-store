<script setup lang="ts">
const props = withDefaults(defineProps<{ modelValue: number; min?: number; max?: number }>(), { min: 1, max: 10 })
const emit = defineEmits<{ 'update:modelValue': [value: number] }>()
const btn = 'inline-flex h-10 w-10 items-center justify-center text-lg transition-colors hover:bg-stone disabled:cursor-not-allowed disabled:text-mist/50 disabled:hover:bg-transparent'
</script>

<template>
  <div class="inline-flex items-center rounded-full border border-stone bg-ivory">
    <button type="button" :class="[btn, 'rounded-l-full']" :disabled="modelValue <= min" aria-label="Decrease quantity" @click="emit('update:modelValue', modelValue - 1)">−</button>
    <span class="price w-10 text-center" aria-live="polite">{{ modelValue }}</span>
    <button type="button" :class="[btn, 'rounded-r-full']" :disabled="modelValue >= max" aria-label="Increase quantity" @click="emit('update:modelValue', modelValue + 1)">+</button>
  </div>
</template>
