// Unique meta, Open Graph, canonical link and Product JSON-LD for one product page
export function useProductSeo(product: {
  slug: string; name: string; description: string; price: number
  currency: string; images: string[]; stock: number; material?: string | null
}) {
  const siteUrl = useRuntimeConfig().public.siteUrl.replace(/\/$/, '')
  const abs = (u: string) => (u.startsWith('http') ? u : siteUrl + u)

  const title = `${product.name} | Kito & Co.`
  const description = product.description.slice(0, 155)
  const url = `${siteUrl}/products/${product.slug}`
  const images = product.images.map(abs)

  useSeoMeta({
    title,
    description,
    ogTitle: title,
    ogDescription: description,
    ogImage: images[0],
    ogType: 'website',
    ogUrl: url,
    twitterCard: 'summary_large_image'
  })

  useHead({
    link: [{ rel: 'canonical', href: url }],
    script: [{
      type: 'application/ld+json',
      innerHTML: JSON.stringify({
        '@context': 'https://schema.org',
        '@type': 'Product',
        name: product.name,
        description: product.description,
        sku: product.slug,
        image: images,
        brand: { '@type': 'Brand', name: 'Kito & Co.' },
        offers: {
          '@type': 'Offer',
          url,
          priceCurrency: product.currency || 'KES',
          price: product.price,
          availability: product.stock > 0
            ? 'https://schema.org/InStock'
            : 'https://schema.org/OutOfStock'
        }
      })
    }]
  })
}
