import { getApiCategories, getApiTransactions, getCurrentUser, getApiBudgets } from '@/utils.js'
import router from '@/router/router'
import axios from 'axios'

export const actions = {
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