<script setup lang="ts">
useSeoMeta({ title: 'Order Received | Kito & Co.', robots: 'noindex' })
</script>

<template>
  <div class="container-x section-y text-center">
    <div class="mx-auto flex h-14 w-14 items-center justify-center rounded-full bg-gold-soft" aria-hidden="true">
      <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#1C1A19" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.5l4.5 4.5L19 7.5" /></svg>
    </div>
    <h1 class="mt-6">Thank you!</h1>
    <p class="mx-auto mt-4 max-w-md text-mist">This is a demo store, no payment was taken.</p>
    <NuxtLink to="/" class="btn-primary mt-8">Back to the shop</NuxtLink>
  </div>
</template>
