<script setup lang="ts">
const toast = useToastStore()
</script>

<template>
  <div class="pointer-events-none fixed inset-x-0 bottom-24 z-50 flex justify-center px-4 md:bottom-8" role="status" aria-live="polite">
    <Transition
      enter-active-class="transition duration-200 ease-out" enter-from-class="translate-y-2 opacity-0"
      leave-active-class="transition duration-200 ease-out" leave-to-class="translate-y-2 opacity-0"
    >
      <p v-if="toast.visible" class="rounded-full bg-ink px-5 py-2.5 text-sm text-white shadow-soft">{{ toast.message }}</p>
    </Transition>
  </div>
</template>
