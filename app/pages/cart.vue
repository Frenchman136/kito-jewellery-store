<script setup lang="ts">
useSeoMeta({ title: 'Your Cart | Kito & Co.', robots: 'noindex' })
const cart = useCartStore()

// Mock checkout: no payment, just empty the cart and show a confirmation
function checkout() {
  cart.clear()
  navigateTo('/checkout/success')
}
</script>

<template>
  <div class="container-x py-12 lg:py-16">
    <h1>Your cart</h1>

    <div v-if="!cart.ready" class="mt-10 animate-pulse space-y-4" aria-hidden="true">
      <div class="h-24 rounded-card bg-stone" /><div class="h-24 rounded-card bg-stone" />
    </div>

    <div v-else-if="cart.isEmpty" class="mt-10 rounded-card bg-stone px-6 py-16 text-center">
      <p class="font-serif text-2xl">Your cart is empty</p>
      <p class="mt-2 text-mist">Pick a piece you love and it will wait for you here.</p>
      <NuxtLink to="/" class="btn-primary mt-6">Back to the shop</NuxtLink>
    </div>

    <div v-else class="mt-10 grid gap-10 lg:grid-cols-[1fr_380px]">
      <ul class="divide-y divide-stone border-y border-stone">
        <CartItem v-for="item in cart.items" :key="item.slug" :item="item" />
      </ul>

      <aside class="h-fit rounded-card bg-stone p-6 shadow-soft" aria-label="Order summary">
        <h2 class="text-2xl!">Summary</h2>
        <dl class="mt-5 space-y-3 text-sm">
          <div class="flex justify-between"><dt class="text-mist">Subtotal</dt><dd class="price">{{ formatPrice(cart.subtotal) }}</dd></div>
          <div class="flex justify-between"><dt class="text-mist">Delivery</dt><dd>Calculated at checkout</dd></div>
          <div class="flex justify-between border-t border-ivory pt-3 text-base"><dt class="font-medium">Total</dt><dd class="price">{{ formatPrice(cart.subtotal) }}</dd></div>
        </dl>
        <button class="btn-primary mt-6 w-full" @click="checkout">Checkout</button>
        <NuxtLink to="/" class="mt-4 block text-center text-sm underline decoration-gold decoration-2 underline-offset-4">Continue shopping</NuxtLink>
      </aside>
    </div>
  </div>
</template>
