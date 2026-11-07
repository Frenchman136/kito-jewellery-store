// Same output on server and browser (fixed locale avoids hydration mismatch)
export const formatPrice = (n: number, currency = 'KES') =>
  `${currency} ${n.toLocaleString('en-US')}`

export const CATEGORIES = ['rings', 'necklaces', 'earrings', 'bracelets'] as const
export const cap = (s: string) => s.charAt(0).toUpperCase() + s.slice(1)
