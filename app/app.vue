<script setup lang="ts">
const cart = useCartStore()
// localStorage only exists in the browser, so load the cart after mount
onMounted(() => cart.hydrate())
</script>

<template>
  <div class="flex min-h-screen flex-col">
    <a href="#main" class="sr-only focus:not-sr-only focus:absolute focus:left-4 focus:top-4 focus:z-50 focus:rounded-full focus:bg-ink focus:px-4 focus:py-2 focus:text-white">Skip to content</a>
    <Header />
    <main id="main" class="flex-1"><NuxtPage /></main>
    <Footer />
    <Toast />
  </div>
</template>
