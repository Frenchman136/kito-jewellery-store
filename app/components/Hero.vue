<template>
  <section class="border-b border-stone">
    <div class="container-x grid items-center gap-10 py-12 md:grid-cols-2 lg:py-20">
      <div class="order-2 md:order-1">
        <!-- Gold text on ivory fails contrast at small sizes, so the label is ink on a gold-soft pill with a gold line -->
        <p class="inline-flex items-center gap-3 rounded-full bg-gold-soft px-4 py-1.5 text-sm font-medium text-ink">
          <span class="h-px w-6 bg-gold" aria-hidden="true" />New season
        </p>
        <h1 class="mt-5 max-w-xl">Jewellery made to be worn every day</h1>
        <p class="mt-5 max-w-md text-mist">
          Simple pieces in silver and gold tones that go from the office to the weekend without a second thought.
        </p>
        <a href="#shop" class="btn-primary mt-8">Shop the collection</a>
      </div>
      <div class="order-1 overflow-hidden rounded-card bg-white shadow-soft md:order-2">
        <AppImage
          src="/images/hero.svg"
          alt="Silver and gold rings, hoops and a fine chain arranged on a warm stone surface"
          :width="800" :height="800" sizes="sm:100vw md:50vw" eager
          class="h-full w-full object-cover"
        />
      </div>
    </div>
  </section>
</template>
