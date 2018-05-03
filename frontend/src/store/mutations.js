import moment from 'moment'

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

    deleteTransaction: (state, payload) => {
        let transactions = state.transactions.slice()
        transactions.splice(payload, 1)
        state.transactions = transactions
    },
    addTransaction: (state, payload) => {
        let transactions = state.transactions.slice()
        transactions.unshift(payload)
        state.transactions = transactions
    },

    setIsMenuActive: (state, payload) => {
        state.isMenuActive = payload
    },
    setIsFilterActive: (state, payload) => {
        state.isFilterActive = payload
    },

    // filter
    updateDateFrom: (state, payload) => {
        state.filter.dateFrom = payload
    },
    updateDateTo: (state, payload) => {
        state.filter.dateTo = payload
    },
    updateType: (state, payload) => {
        state.filter.type = payload
    },
    resetFilter: (state, payload) => {
        state.filter = {
            dateFrom: moment().startOf('month').format('YYYY-MM-DD'),
            dateTo: moment().endOf('month').format('YYYY-MM-DD'),
            type: '',        
        }
    }
}