import { defineStore } from 'pinia'

let timer: ReturnType<typeof setTimeout> | undefined

export const useToastStore = defineStore('toast', {
  state: () => ({ message: '', visible: false }),
  actions: {
    show(message: string) {
      this.message = message
      this.visible = true
      clearTimeout(timer)
      timer = setTimeout(() => (this.visible = false), 2500)
    }
  }
})
