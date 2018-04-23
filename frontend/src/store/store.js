import Vue from 'vue'
import Vuex from 'vuex'

import router from '@/router/router'
import axios from 'axios'

import { getApiCategories, getApiTransactions, getCurrentUser, getApiBudgets } from '@/utils.js'

import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [createPersistedState({
    paths: ['token', 'isUserLoggedIn', 'user'],
  })],
  state: {
    user: {},
    token: '',
    isUserLoggedIn: false,
    wallet: null,
    budgets: [],
    categories: [],
    transactions: [],
    invitations: [],
    isMenuActive: false
  },
  mutations: {
    setToken: (state, payload) => {
      state.token = payload
    },
    setIsUserLoggedIn: (state, payload) => {
      state.isUserLoggedIn = payload
    },
    setWallet: (state, payload) => {
      state.wallet = payload
    },
    setBudgets: (state, payload) => {
      state.budgets = payload
    },
    setCategories: (state, payload) => {
      state.categories = payload
    },
    setTransactions: (state, payload) => {
      state.transactions = payload
    },
    setUser: (state, payload) => {
      state.user = payload
    },
    setIsMenuActive: (state, payload) => {
      if (payload) {
        if(payload == 'true') payload = true
        else payload = false
        state.isMenuActive = payload
      }
      else state.isMenuActive = !state.isMenuActive
    }
  },
  actions: {
    toggleMenu: (context, payload) => {
      context.commit('setIsMenuActive', payload)
    },
    logUserIn: (context, payload) => {
      context.commit('setToken', payload)
      context.commit('setIsUserLoggedIn', true)
      axios.all([getCurrentUser(payload)]).then(
        axios.spread((user) => {
          context.commit('setUser', user.data)
        })
      )
    },
    logUserOut: (context, payload) => {
      context.commit('setToken', '')
      context.commit('setIsUserLoggedIn', false)
      context.commit('setUser', {})
      context.dispatch('dumpData', "")
      router.push({ name: 'Login' })
    },
    pickWallet: ({ commit }, payload) => {
      commit('setWallet', payload)
    },
    loadData: (context, payload) => {
      if (context.state.transactions.length === 0 || context.state.transactions.length === 0) {
        const walletID = context.state.wallet.id
        const token = context.state.token
        axios.all([getApiCategories(walletID, token), getApiTransactions(walletID, token), getApiBudgets(walletID, token)]).then(
          axios.spread((cat, tran, budg) => {
            context.commit('setTransactions', tran.data)
            context.commit('setCategories', cat.data)
            context.commit('setBudgets', budg.data)
          })
        )
      }
    },
    refreshData: (context, payload) => {
      const walletID = context.state.wallet.id
      const token = context.state.token
      axios.all([getApiCategories(walletID, token), getApiTransactions(walletID, token), getApiBudgets(walletID, token)]).then(
        axios.spread((cat, tran, budg) => {
          context.commit('setTransactions', tran.data)
          context.commit('setCategories', cat.data)
          context.commit('setBudgets', budg.data)
        })
      )
    },
    dumpData: (context, payload) => {
      context.commit('setWallet', null)
      context.commit('setCategories', [])
      context.commit('setTransactions', [])
      context.commit('setBudgets', [])
    }
  }
})
