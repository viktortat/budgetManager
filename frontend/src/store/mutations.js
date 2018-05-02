export const mutations = {
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
            if (payload == 'true') payload = true
            else payload = false
            state.isMenuActive = payload
        }
        else state.isMenuActive = !state.isMenuActive
    }
}