import router from '@/router/router'
import axios from 'axios'

export const actions = {
  // user actions
  logUserIn: (context, payload) => {
    context.commit('setToken', payload)
    const url = '/auth/users/current/'
    axios.get(url, { headers: { Authorization: 'JWT ' + payload }}).then(response => {
      context.commit('setUser', response.data)
    })
  },
  logUserOut: (context, payload) => {
    context.commit('setToken', '')
    context.commit('setUser', {})
    context.dispatch('dumpData', '')
    router.push({ name: 'Login' })
  },

  // data actions
  loadTransactions: (context, payload) => {
    if (payload) {
      const walletID = context.state.wallet.id
      const token = context.state.token
      const url = '/transactions/' + '?wallet=' + walletID
      axios.get(url, { headers: { Authorization: 'JWT ' + token }}).then(response => {
        context.commit('setTransactions', response.data)
      })
    }
  },
  loadCategories: (context, payload) => {
    if (payload) {
      const walletID = context.state.wallet.id
      const token = context.state.token
      const url = '/categories/' + '?wallet=' + walletID
      axios.get(url, { headers: { Authorization: 'JWT ' + token }}).then(response => {
        context.commit('setCategories', response.data)
      })
    }
  },
  loadBudgets: (context, payload) => {
    if (payload) {
      const walletID = context.state.wallet.id
      const token = context.state.token
      const url = '/budgets/' + '?wallet=' + walletID
      axios.get(url, { headers: { Authorization: 'JWT ' + token }}).then(response => {
        context.commit('setBudgets', response.data)
      })
    }
  },
  loadWallets: (context, payload) => {
    if (payload) {
      const token = context.state.token
      const url = '/wallets/'
      axios.get(url, { headers: { Authorization: 'JWT ' + token }}).then(response => {
        context.commit('setWallets', response.data)
      }).catch(error => {})
    }
  },

  loadData: (context, payload) => {
    const dataIsNotLoaded = context.state.transactions.length === 0 && context.state.categories.length === 0 && context.state.budgets.length === 0
    context.dispatch('loadTransactions', dataIsNotLoaded)
    context.dispatch('loadCategories', dataIsNotLoaded)
    context.dispatch('loadBudgets', dataIsNotLoaded)
  },
  refreshData: (context, payload) => {
    context.dispatch('loadTransactions', true)
    context.dispatch('loadCategories', true)
    context.dispatch('loadBudgets', true)
  },
  dumpData: (context, payload) => {
    context.commit('setWallet', null)
    context.commit('setWallets', [])
    context.commit('setCategories', [])
    context.commit('setTransactions', [])
    context.commit('setBudgets', [])
  },

  // menu
  toggleMenu: (context, payload) => {
    if (payload === undefined) context.commit('setIsMenuActive', !context.state.isMenuActive)
    else context.commit('setIsMenuActive', payload)
  },
  toggleFilter: (context, payload) => {
    if (payload === undefined) context.commit('setIsFilterActive', !context.state.isFilterActive)
    else context.commit('setIsFilterActive', payload)
  }
}
