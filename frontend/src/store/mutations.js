export const mutations = {
    setUser: (state, payload) => {
        state.user = payload
    },
    setToken: (state, payload) => {
        state.token = payload
    },
    setWallet: (state, payload) => {
        state.wallet = payload
    },

    setWallets: (state, payload) => {
        state.wallets = payload
    },
    setCategories: (state, payload) => {
        state.categories = payload
    },
    setTransactions: (state, payload) => {
        state.transactions = payload
    },
    setBudgets: (state, payload) => {
        state.budgets = payload
    },

    setIsMenuActive: (state, payload) => {
        state.isMenuActive = payload
    }
}