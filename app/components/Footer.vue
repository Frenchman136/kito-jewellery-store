<template>
  <footer class="bg-stone">
    <div class="container-x grid gap-10 py-16 md:grid-cols-3">
      <div>
        <p class="font-serif text-2xl font-semibold">Kito &amp; Co.</p>
        <p class="mt-3 max-w-xs text-sm text-mist">
          Everyday jewellery in silver and gold tones. This is a demo store built as a take-home project.
        </p>
      </div>
      <nav aria-label="Shop links">
        <p class="font-medium">Shop</p>
        <ul class="mt-3 space-y-2 text-sm text-mist">
          <li v-for="c in CATEGORIES" :key="c">
            <NuxtLink :to="`/?category=${c}`" class="hover:text-ink hover:underline hover:decoration-gold hover:underline-offset-4">{{ cap(c) }}</NuxtLink>
          </li>
        </ul>
      </nav>
      <nav aria-label="Help links">
        <p class="font-medium">Help</p>
        <ul class="mt-3 space-y-2 text-sm text-mist">
          <li><NuxtLink to="/cart" class="hover:text-ink hover:underline hover:decoration-gold hover:underline-offset-4">Your cart</NuxtLink></li>
          <li>Free gift wrap</li>
          <li>7-day returns</li>
        </ul>
      </nav>
    </div>
    <div class="border-t border-ivory/60">
      <p class="container-x py-5 text-sm text-mist">© {{ new Date().getFullYear() }} Kito &amp; Co.</p>
    </div>
  </footer>
</template>
