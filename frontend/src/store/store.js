import Vue from 'vue'
import Vuex from 'vuex'

import router from '@/router/router'
import axios from 'axios'

import { getApiCategories, getApiTransactions, getCurrentUser } from '@/utils.js'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    user: {},
    token: '',
    isUserLoggedIn: false,
    wallet: null,
    categories: [],
    transactions: [],
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
      if (payload) state.isMenuActive = payload
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
    logUserOut: ({ commit }, payload) => {
      commit('setToken', '')
      commit('setIsUserLoggedIn', false)
      commit('setUser', {})
      router.push({ name: 'Login' })
    },
    pickWallet: ({ commit }, payload) => {
      commit('setWallet', payload)
    },
    loadData: (context, payload) => {
      if (context.state.transactions.length === 0 || context.state.transactions.length === 0) {
        const walletID = context.state.wallet.id
        const token = context.state.token
        axios.all([getApiCategories(walletID, token), getApiTransactions(walletID, token)]).then(
          axios.spread((cat, tran) => {
            context.commit('setTransactions', tran.data)
            context.commit('setCategories', cat.data)
          })
        )
      }
    },
    refreshData: (context, payload) => {
      const walletID = context.state.wallet.id
      const token = context.state.token
      axios.all([getApiCategories(walletID, token), getApiTransactions(walletID, token)]).then(
        axios.spread((cat, tran) => {
          context.commit('setTransactions', tran.data)
          context.commit('setCategories', cat.data)
        })
      )
    }
  },
  getters: {

  }
})
