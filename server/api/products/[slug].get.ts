// GET /api/products/:slug  ->  { product, related }
export default defineEventHandler(async (event) => {
  const slug = getRouterParam(event, 'slug')
  const supabase = getClient()

  const { data: product, error } = await supabase
    .from('products')
    .select('*')
    .eq('slug', slug)
    .single()

  // PGRST116 = "no rows". Send a real 404 so search engines drop bad URLs.
  if (error?.code === 'PGRST116' || (!error && !product)) {
    throw createError({ statusCode: 404, statusMessage: 'Product not found' })
  }
  if (error) throw createError({ statusCode: 500, statusMessage: 'Could not load product' })

  const { data: related } = await supabase
    .from('products')
    .select('id, slug, name, price, currency, category, material, images, stock')
    .eq('category', product.category)
    .neq('slug', product.slug)
    .limit(4)

  return { product, related: related ?? [] }
})
