const CATEGORIES = ['rings', 'necklaces', 'earrings', 'bracelets']

// GET /api/products?category=rings
export default defineEventHandler(async (event) => {
  const { category } = getQuery(event)

  let query = getClient()
    .from('products')
    .select('id, slug, name, price, currency, category, material, images, stock')
    .order('created_at', { ascending: false })

  // Only accept known categories, ignore anything else
  if (typeof category === 'string' && CATEGORIES.includes(category)) {
    query = query.eq('category', category)
  }

  const { data, error } = await query
  if (error) throw createError({ statusCode: 500, statusMessage: 'Could not load products' })
  return data
})
