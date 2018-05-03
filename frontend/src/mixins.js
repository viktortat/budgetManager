import store from '@/store/store'

export const filterMixin = {
    methods: {
        filterTransactions(transactions) {
            
        }
    },
    created() {
        console.log(store.state.filter)
    }
}

export const sortMixin = {
    methods: {
        sortTransactions(transactions) {
            
        }
    },
    created() {
        console.log(store.state.filter)
    }
}