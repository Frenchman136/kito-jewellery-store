-- Run this in the Supabase SQL editor, then run seed.sql
create table if not exists public.products (
  id          uuid primary key default gen_random_uuid(),
  slug        text unique not null,
  name        text not null,
  description text not null,
  price       integer not null,               -- KES as a whole number, no decimals
  currency    text not null default 'KES',
  category    text not null,                  -- rings | necklaces | earrings | bracelets
  material    text,
  images      text[] not null,                -- first image is the main one
  stock       integer not null default 0,
  created_at  timestamptz default now()
);

alter table public.products enable row level security;

-- Anyone can read. There are no insert/update/delete policies, so the public key cannot write.
create policy "Public read products" on public.products
  for select using (true);
