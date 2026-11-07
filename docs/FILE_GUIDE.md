# File guide (so you can explain every file)
Nuxt 4 layout: everything the browser runs is in `app/`; `server/`, `public/`, `supabase/` stay at the root. Paths below without a folder prefix are inside `app/`.

**Config**
- `nuxt.config.ts` - modules, fonts (display=swap), image formats, sitemap source, route rules (`/` cached with ISR, `/cart` and `/checkout` client-only), private vs public runtime config.
- `app/assets/css/main.css` - Tailwind 4 `@theme` (brand colours, fonts, radius, shadow), type scale, gold focus ring, reduced-motion, `.btn-primary` (pill + sliding gold underline), `.container-x`, `.section-y`.

**Server (runs only on the server)**
- `server/utils/supabase.ts` - creates the Supabase client with the service key.
- `server/api/products/index.get.ts` - list products, optional `?category=` (checked against a whitelist).
- `server/api/products/[slug].get.ts` - one product + up to 4 related; real 404 if missing.
- `server/api/__sitemap__/urls.ts` - product URLs for the sitemap.

**State**
- `stores/cart.ts` - items, `hydrate()` from localStorage, add/setQty/remove/clear, `count`/`subtotal`. Quantity capped at min(stock, 10).
- `stores/toast.ts` - message + 2.5 s auto-hide.

**Pages**
- `pages/index.vue` - home SEO, hero, chips, product grid with loading / error / empty states.
- `pages/products/[slug].vue` - fetch, 404 handling, gallery, quantity, add to cart, related, mobile sticky bar.
- `pages/cart.vue` - skeleton until hydrated, empty state, rows, summary, mocked checkout.
- `pages/checkout/success.vue` - demo confirmation (noindex).
- `error.vue` - friendly 404 / error page.

**Components**: `Header`, `Footer`, `Hero`, `CategoryChips`, `ProductCard` (stretched-link pattern so the card is one link and the Add button is valid HTML), `QtyStepper`, `CartItem`, `Toast`, `SkeletonCard`, `AppImage` (NuxtImg for photos, plain img for SVG).

**SEO helper**: `composables/useProductSeo.ts` - meta, OG, canonical, Product JSON-LD.

**Data**: `supabase/schema.sql` (table + RLS), `supabase/seed.sql` (12 products), `scripts/generate_assets.py` (draws the original SVG images and writes the seed).

## Deploy checklist
1. Push to a public GitHub repo. 2. Create Supabase project, run schema + seed. 3. Import repo in Vercel (Nuxt detected). 4. Add env vars `SUPABASE_URL`, `SUPABASE_SERVICE_KEY`, `NUXT_PUBLIC_SITE_URL`. 5. Edit the Sitemap line in `public/robots.txt` to your live URL and redeploy. 6. Check `/sitemap.xml`, `/robots.txt`, view-source on a product page, an unknown slug (404), Lighthouse mobile, and Google's Rich Results Test.
