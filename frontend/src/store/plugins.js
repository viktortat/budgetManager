import createPersistedState from 'vuex-persistedstate'

export const plugins = [
    createPersistedState({
        paths: ['token', 'user', 'wallet', 'transactions', 'categories', 'budgets', 'wallets'],
    })
]
