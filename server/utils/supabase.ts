import { createClient, type SupabaseClient } from '@supabase/supabase-js'

let client: SupabaseClient | null = null

// Server-only helper. The service key never reaches the browser.
export function getClient(): SupabaseClient {
  if (client) return client
  const config = useRuntimeConfig()
  if (!config.supabaseUrl || !config.supabaseServiceKey) {
    throw createError({ statusCode: 500, statusMessage: 'Database is not configured' })
  }
  client = createClient(config.supabaseUrl, config.supabaseServiceKey, {
    auth: { persistSession: false }
  })
  return client
}
