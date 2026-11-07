<script setup lang="ts">
const props = defineProps<{
  product: { slug: string; name: string; price: number; currency: string; category: string
             material?: string | null; images: string[]; stock: number }
}>()

const cart = useCartStore()
const toast = useToastStore()
const soldOut = computed(() => props.product.stock <= 0)
const lowStock = computed(() => props.product.stock > 0 && props.product.stock <= 3)

function quickAdd() {
  cart.add(props.product, 1)
  toast.show('Added to cart')
}
</script>

<template>
  <!--
    The whole card acts as one link: the name link stretches over the card with an
    ::after pseudo-element. The "Add to cart" button sits above it (z-10), so it
    works without navigating, and no <button> is nested inside an <a>.
  -->
  <article class="group relative">
    <div class="relative aspect-square overflow-hidden rounded-card bg-white">
      <AppImage
        :src="product.images[0]"
        :alt="`${product.name}${product.material ? ', ' + product.material : ''}`"
        :width="600" :height="600"
        class="h-full w-full object-cover transition-transform duration-300 ease-out group-hover:scale-[1.04]"
      />
      <span v-if="soldOut" class="badge absolute left-3 top-3 bg-mist text-white">Sold out</span>
      <span v-else-if="lowStock" class="badge absolute left-3 top-3 bg-rose text-white">Low stock</span>

      <button
        v-if="!soldOut" type="button"
        class="btn-primary absolute inset-x-3 bottom-3 z-10 hidden py-2.5! opacity-0 transition-opacity duration-200 focus-visible:opacity-100 group-hover:opacity-100 md:inline-flex"
        :aria-label="`Add ${product.name} to cart`"
        @click="quickAdd"
      >Add to cart</button>
    </div>

    <div class="mt-3">
      <h3 class="font-sans! text-base! font-medium!">
        <NuxtLink
          :to="`/products/${product.slug}`"
          class="after:absolute after:inset-0 after:rounded-card focus-visible:outline-none focus-visible:after:outline focus-visible:after:outline-2 focus-visible:after:outline-offset-2 focus-visible:after:outline-gold"
        >{{ product.name }}</NuxtLink>
      </h3>
      <p class="text-sm capitalize text-mist">{{ product.category }}</p>
      <p class="price mt-1">{{ formatPrice(product.price, product.currency) }}</p>
    </div>
  </article>
</template>
