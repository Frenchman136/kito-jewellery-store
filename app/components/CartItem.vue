<script setup lang="ts">
import type { CartLine } from '~/stores/cart'
defineProps<{ item: CartLine }>()
const cart = useCartStore()
</script>

<template>
  <li class="flex gap-4 py-5">
    <NuxtLink :to="`/products/${item.slug}`" class="h-24 w-24 shrink-0 overflow-hidden rounded-card bg-white">
      <AppImage :src="item.image" :alt="item.name" :width="200" :height="200" class="h-full w-full object-cover" />
    </NuxtLink>
    <div class="flex flex-1 flex-col justify-between">
      <div class="flex justify-between gap-4">
        <NuxtLink :to="`/products/${item.slug}`" class="font-medium hover:underline hover:decoration-gold hover:underline-offset-4">{{ item.name }}</NuxtLink>
        <p class="price">{{ formatPrice(item.price * item.qty) }}</p>
      </div>
      <div class="flex items-center justify-between">
        <QtyStepper :model-value="item.qty" :max="item.max" @update:model-value="cart.setQty(item.slug, $event)" />
        <button type="button" class="text-sm text-mist underline underline-offset-4 hover:text-ink" :aria-label="`Remove ${item.name} from cart`" @click="cart.remove(item.slug)">Remove</button>
      </div>
      <p class="text-sm text-mist">{{ formatPrice(item.price) }} each</p>
    </div>
  </li>
</template>
