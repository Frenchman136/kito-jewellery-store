# Kito & Co. - take-home store
Needs Node 20 or newer.
Live: <add your Vercel URL>   Repo: <add your GitHub URL>

A small jewellery store: product grid, product pages, cart (localStorage) and a mocked checkout. Server-rendered for SEO.

## Run locally
```bash
npm install
cp .env.example .env        # fill in the three values
npm run dev                 # http://localhost:3000
```
Database setup (once): create a Supabase project, open the SQL editor, run `supabase/schema.sql` then `supabase/seed.sql`. Copy the project URL and the `service_role` key into `.env`.

To regenerate the sample images and seed file: `python3 scripts/generate_assets.py`.

## Stack and why
- **Nuxt 4 (SSR)**: pages arrive as full HTML, so search engines read real content.
- **Tailwind 4**: fast to build, and the brand colours/fonts live in one `@theme` block in `app/assets/css/main.css`.
- **Supabase (Postgres)**: quick hosted database with Row Level Security.
- **Pinia**: small, typed state for the cart and toast.
- **@nuxt/image**: resizes and converts photos to webp/avif.

## Key decisions
- One `products` table. Price is an integer (KES has no decimals needed), so no rounding bugs.
- The browser never talks to Supabase. It calls our own `/api/*` routes, and the service key lives only in server config.
- RLS is on: public can read, nobody can write with a public key.
- Cart lives in localStorage and is loaded after mount, so server and browser HTML match (no hydration warnings).
- Checkout is mocked and says so. `/cart` and `/checkout` are `noindex` and blocked in robots.txt.
- "New season" label is ink on a gold-soft pill (gold text on ivory fails contrast at small sizes).

## SEO
- Unique `<title>` and description per page; product titles come from the product name.
- Open Graph + Twitter tags, canonical URL on home and product pages.
- Product JSON-LD (name, image, sku, brand, price, currency, availability).
- `/sitemap.xml` built from the database; `/robots.txt` present.
- Unknown product slug returns a real 404 status.
- Images: explicit width/height (no layout shift), lazy loading, eager + high priority for hero and main product image.
- Lighthouse (mobile) before/after: <fill in after deploying>
- Rich Results Test: <fill in after deploying>

## What I'd improve with more time
Real checkout (M-Pesa/card), search + filters + sorting, pagination, admin page to manage products, order table, tests, image CDN with real photography (social previews work best with JPG/WebP rather than SVG), i18n, full accessibility audit.

## AI use
<Write 3-5 sentences in your own words. Example: "I used Claude to scaffold the project from my written spec and to draft the seed data. I wrote down the design decisions (palette, type scale, page flow, data model) myself and reviewed every file. I deployed and tested on Vercel/Supabase myself and fixed whatever broke.">
