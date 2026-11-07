<script setup lang="ts">
const siteUrl = useRuntimeConfig().public.siteUrl.replace(/\/$/, '')
const title = 'Handmade Jewellery in Kenya | Kito & Co.'
const description = 'Shop rings, necklaces, earrings and bracelets in sterling silver and gold tones. Simple everyday pieces with free gift wrap and 7-day returns.'

useSeoMeta({
  title, description,
  ogTitle: title, ogDescription: description, ogType: 'website', ogUrl: siteUrl + '/',
  ogImage: siteUrl + '/images/hero.svg', twitterCard: 'summary_large_image'
})
useHead({ link: [{ rel: 'canonical', href: siteUrl + '/' }] })

const route = useRoute()
const valid = (v: unknown) => (typeof v === 'string' && (CATEGORIES as readonly string[]).includes(v) ? v : 'all')
const category = ref('all')

// Header links use /?category=rings. Read it in the browser so the cached home page stays generic.
onMounted(() => (category.value = valid(route.query.category)))
watch(() => route.query.category, (v) => (category.value = valid(v)))

const query = computed(() => (category.value === 'all' ? {} : { category: category.value }))
const { data: products, pending, error, refresh } = await useFetch('/api/products', { query })
</script>

<template>
  <div>
    <Hero />
    <section id="shop" class="container-x section-y scroll-mt-20" aria-labelledby="shop-heading">
      <h2 id="shop-heading" class="mb-6">The collection</h2>
      <CategoryChips v-model="category" class="mb-10" />

      <div v-if="pending" class="grid grid-cols-2 gap-x-4 gap-y-8 md:grid-cols-3 lg:grid-cols-4 lg:gap-x-6">
        <SkeletonCard v-for="n in 8" :key="n" />
      </div>

      <div v-else-if="error" class="rounded-card bg-stone px-6 py-12 text-center">
        <p class="font-medium">We could not load the products.</p>
        <p class="mt-1 text-sm text-mist">Check your connection and try again.</p>
        <button class="btn-primary mt-6" @click="refresh()">Try again</button>
      </div>

      <p v-else-if="!products?.length" class="rounded-card bg-stone px-6 py-12 text-center text-mist">
        No pieces in this category yet.
      </p>

      <div v-else class="grid grid-cols-2 gap-x-4 gap-y-8 md:grid-cols-3 lg:grid-cols-4 lg:gap-x-6">
        <ProductCard v-for="p in products" :key="p.id" :product="p" />
      </div>
    </section>
  </div>
</template>
