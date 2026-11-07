<script setup lang="ts">
const cart = useCartStore()
const open = ref(false)
const route = useRoute()
watch(() => route.fullPath, () => (open.value = false))

const links = [
  { label: 'Shop', to: '/' },
  ...CATEGORIES.map((c) => ({ label: cap(c), to: `/?category=${c}` }))
]
</script>

<template>
  <header class="sticky top-0 z-40 border-b border-stone bg-ivory/85 backdrop-blur">
    <div class="container-x flex h-16 items-center justify-between">
      <NuxtLink to="/" class="font-serif text-2xl font-semibold tracking-tight">Kito &amp; Co.</NuxtLink>

      <nav aria-label="Main" class="hidden items-center gap-8 md:flex">
        <NuxtLink
          v-for="l in links" :key="l.label" :to="l.to"
          class="text-sm font-medium decoration-gold decoration-2 underline-offset-8 hover:underline"
        >{{ l.label }}</NuxtLink>
      </nav>

      <div class="flex items-center gap-2">
        <NuxtLink to="/cart" class="relative inline-flex h-11 w-11 items-center justify-center rounded-full hover:bg-stone" aria-label="Open cart">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
            <path d="M6 7h12l-1 13H7L6 7Z" /><path d="M9 7a3 3 0 0 1 6 0" />
          </svg>
          <!-- aria-live span is always in the DOM so screen readers announce changes -->
          <span aria-live="polite" class="absolute -right-0.5 -top-0.5">
            <span v-if="cart.ready && cart.count > 0" class="flex h-5 min-w-5 items-center justify-center rounded-full bg-gold px-1 text-xs font-semibold text-ink">
              <span class="sr-only">Items in cart: </span>{{ cart.count }}
            </span>
          </span>
        </NuxtLink>

        <button
          class="inline-flex h-11 w-11 items-center justify-center rounded-full hover:bg-stone md:hidden"
          :aria-expanded="open" aria-controls="mobile-menu" aria-label="Toggle menu"
          @click="open = !open"
        >
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" aria-hidden="true">
            <path v-if="!open" d="M4 7h16M4 12h16M4 17h16" /><path v-else d="M6 6l12 12M18 6L6 18" />
          </svg>
        </button>
      </div>
    </div>

    <nav v-if="open" id="mobile-menu" aria-label="Mobile" class="border-t border-stone bg-ivory md:hidden">
      <ul class="container-x py-2">
        <li v-for="l in links" :key="l.label">
          <NuxtLink :to="l.to" class="block py-3 text-base font-medium">{{ l.label }}</NuxtLink>
        </li>
      </ul>
    </nav>
  </header>
</template>
