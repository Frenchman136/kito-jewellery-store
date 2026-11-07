// Feeds product URLs to @nuxtjs/sitemap
export default defineEventHandler(async () => {
  const { data, error } = await getClient().from('products').select('slug, created_at')
  if (error) throw createError({ statusCode: 500, statusMessage: 'Could not build sitemap' })
  return (data ?? []).map((r) => ({ loc: '/products/' + r.slug, lastmod: r.created_at }))
})
