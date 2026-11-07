<script setup lang="ts">
const props = defineProps<{ error: { statusCode: number; statusMessage?: string } }>()
const is404 = computed(() => props.error.statusCode === 404)
useSeoMeta({ title: is404.value ? 'Page not found | Kito & Co.' : 'Something went wrong | Kito & Co.', robots: 'noindex' })
const goHome = () => clearError({ redirect: '/' })
</script>

<template>
  <div class="flex min-h-screen flex-col">
    <Header />
    <main class="container-x section-y flex-1 text-center">
      <p class="price text-mist">{{ error.statusCode }}</p>
      <h1 class="mt-3">{{ is404 ? 'We could not find that page' : 'Something went wrong' }}</h1>
      <p class="mx-auto mt-4 max-w-md text-mist">
        {{ is404 ? 'The link may be old, or the piece may no longer be in the collection.' : 'Please try again in a moment.' }}
      </p>
      <button class="btn-primary mt-8" @click="goHome">Back to the shop</button>
    </main>
    <Footer />
  </div>
</template>
