import { defineStore } from 'pinia'

export interface CartLine {
  slug: string
  name: string
  price: number
  image: string
  qty: number
  max: number // most the shopper can buy: min(stock, 10)
}

const KEY = 'kito-cart'
const MAX_PER_ITEM = 10

export const useCartStore = defineStore('cart', {
  state: () => ({
    items: [] as CartLine[],
    ready: false // true once localStorage has been read in the browser
  }),

  getters: {
    count: (s) => s.items.reduce((n, i) => n + i.qty, 0),
    subtotal: (s) => s.items.reduce((n, i) => n + i.price * i.qty, 0),
    isEmpty: (s) => s.items.length === 0
  },

  actions: {
    hydrate() {
      try {
        const saved = localStorage.getItem(KEY)
        if (saved) {
          const parsed = JSON.parse(saved)
          this.items = Array.isArray(parsed) ? parsed : []
        }
      } catch {
        this.items = [] // bad JSON or storage blocked: start empty
      }
      this.ready = true
    },

    add(product: { slug: string; name: string; price: number; images: string[]; stock: number }, qty = 1) {
      const max = Math.min(product.stock || MAX_PER_ITEM, MAX_PER_ITEM)
      const found = this.items.find((i) => i.slug === product.slug)
      if (found) {
        found.qty = Math.min(found.qty + qty, max)
        found.max = max
      } else {
        this.items.push({
          slug: product.slug,
          name: product.name,
          price: product.price,
          image: product.images[0],
          qty: Math.min(qty, max),
          max
        })
      }
      this.persist()
    },

    setQty(slug: string, qty: number) {
      if (qty <= 0) return this.remove(slug)
      const item = this.items.find((i) => i.slug === slug)
      if (item) item.qty = Math.min(qty, item.max)
      this.persist()
    },

    remove(slug: string) {
      this.items = this.items.filter((i) => i.slug !== slug)
      this.persist()
    },

    clear() {
      this.items = []
      this.persist()
    },

    persist() {
      if (!import.meta.client) return
      try {
        localStorage.setItem(KEY, JSON.stringify(this.items))
      } catch { /* storage full or blocked: cart still works for this visit */ }
    }
  }
})
