<script setup lang="ts">
// One image component for the whole site.
// Real photos go through <NuxtImg> (resizing, webp/avif). SVG files are served as-is.
const props = withDefaults(defineProps<{
  src: string
  alt: string
  width: number
  height: number
  sizes?: string
  eager?: boolean
}>(), { sizes: 'sm:50vw md:25vw', eager: false })

const isSvg = computed(() => props.src.toLowerCase().endsWith('.svg'))
</script>

<template>
  <img
    v-if="isSvg"
    :src="src" :alt="alt" :width="width" :height="height"
    :loading="eager ? 'eager' : 'lazy'"
    :fetchpriority="eager ? 'high' : 'auto'"
    decoding="async"
  >
  <NuxtImg
    v-else
    :src="src" :alt="alt" :width="width" :height="height" :sizes="sizes"
    format="webp" quality="80"
    :loading="eager ? 'eager' : 'lazy'"
    :fetchpriority="eager ? 'high' : 'auto'"
  />
</template>
