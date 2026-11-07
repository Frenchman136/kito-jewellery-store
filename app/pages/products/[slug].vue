<script setup lang="ts">
const route = useRoute()
const slug = route.params.slug as string
const cart = useCartStore()
const toast = useToastStore()

const { data, error } = await useFetch(`/api/products/${slug}`, { key: `product-${slug}` })

// Real 404 (status code is set during SSR, which is what search engines see)
if (error.value || !data.value) {
  throw createError({ statusCode: 404, statusMessage: 'Product not found', fatal: true })
}

const product = data.value.product
const related = data.value.related
useProductSeo(product)

const activeImage = ref(product.images[0])
const qty = ref(1)
const soldOut = product.stock <= 0
const max = Math.min(product.stock, 10)
const alt = (i: number) => `${product.name}${product.material ? ', ' + product.material : ''} (view ${i + 1})`

function addToCart() {
  cart.add(product, qty.value)
  toast.show('Added to cart')
}
</script>

<template>
  <div class="container-x pb-28 pt-8 md:pb-16">
    <nav aria-label="Breadcrumb" class="text-sm text-mist">
      <ol class="flex flex-wrap items-center gap-2">
        <li><NuxtLink to="/" class="hover:text-ink hover:underline hover:decoration-gold hover:underline-offset-4">Home</NuxtLink></li>
        <li aria-hidden="true">/</li>
        <li><NuxtLink :to="`/?category=${product.category}`" class="capitalize hover:text-ink hover:underline hover:decoration-gold hover:underline-offset-4">{{ product.category }}</NuxtLink></li>
        <li aria-hidden="true">/</li>
        <li aria-current="page" class="text-ink">{{ product.name }}</li>
      </ol>
    </nav>

    <div class="mt-6 grid gap-10 lg:grid-cols-2 lg:gap-16">
      <!-- Gallery -->
      <div>
        <div class="aspect-square overflow-hidden rounded-card bg-white">
          <AppImage :src="activeImage" :alt="alt(product.images.indexOf(activeImage))" :width="900" :height="900" sizes="sm:100vw lg:50vw" eager class="h-full w-full object-cover" />
        </div>
        <ul class="mt-3 flex gap-3">
          <li v-for="(img, i) in product.images" :key="img">
            <button
              type="button" :aria-label="`Show image ${i + 1}`" :aria-pressed="img === activeImage"
              class="h-20 w-20 overflow-hidden rounded-card border-2 bg-white transition-colors"
              :class="img === activeImage ? 'border-gold' : 'border-transparent hover:border-stone'"
              @click="activeImage = img"
            >
              <AppImage :src="img" :alt="alt(i)" :width="160" :height="160" class="h-full w-full object-cover" />
            </button>
          </li>
        </ul>
      </div>

      <!-- Info -->
      <div>
        <h1>{{ product.name }}</h1>
        <p class="price mt-3 text-2xl">{{ formatPrice(product.price, product.currency) }}</p>
        <p v-if="soldOut" class="mt-2 text-sm font-medium text-mist">Sold out</p>
        <p v-else-if="product.stock <= 3" class="mt-2 text-sm font-medium text-rose">Low stock: only {{ product.stock }} left</p>

        <p class="mt-6 max-w-prose text-mist">{{ product.description }}</p>

        <dl class="mt-6 divide-y divide-stone border-y border-stone text-sm">
          <div v-if="product.material" class="flex justify-between py-3"><dt class="text-mist">Material</dt><dd class="font-medium">{{ product.material }}</dd></div>
          <div class="flex justify-between py-3"><dt class="text-mist">Category</dt><dd class="font-medium capitalize">{{ product.category }}</dd></div>
          <div class="flex justify-between py-3"><dt class="text-mist">Availability</dt><dd class="font-medium">{{ soldOut ? 'Sold out' : 'In stock' }}</dd></div>
        </dl>

        <div class="mt-8 flex items-center gap-4">
          <QtyStepper v-model="qty" :max="soldOut ? 1 : max" />
        </div>
        <button class="btn-primary mt-4 hidden w-full md:inline-flex md:w-auto md:min-w-64" :disabled="soldOut" @click="addToCart">
          {{ soldOut ? 'Sold out' : 'Add to cart' }}
        </button>

        <p class="mt-6 rounded-card bg-gold-soft px-4 py-3 text-sm">Free gift wrap • 7-day returns • Secure packaging</p>
      </div>
    </div>

    <!-- Related -->
    <section v-if="related.length" class="mt-20" aria-labelledby="related-heading">
      <h2 id="related-heading" class="mb-8">You may also like</h2>
      <div class="grid grid-cols-2 gap-x-4 gap-y-8 lg:grid-cols-4 lg:gap-x-6">
        <ProductCard v-for="p in related" :key="p.id" :product="p" />
      </div>
    </section>

    <!-- Mobile sticky bar -->
    <div class="fixed inset-x-0 bottom-0 z-30 border-t border-stone bg-ivory/95 p-3 backdrop-blur md:hidden">
      <button class="btn-primary w-full" :disabled="soldOut" @click="addToCart">
        {{ soldOut ? 'Sold out' : `Add to cart • ${formatPrice(product.price * qty, product.currency)}` }}
      </button>
    </div>
  </div>
</template>
