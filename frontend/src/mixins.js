import store from '@/store/store'

export const filterMixin = {
    methods: {
        filterTransactions(transactions) {
            let trns = transactions.slice()
            const filter = store.state.filter
            if(filter.dateFrom) trns = trns.filter(trn => trn.date >= filter.dateFrom)
            if(filter.dateTo) trns = trns.filter(trn => trn.date <= filter.dateTo)
            if(filter.amountFrom) trns = trns.filter(trn => Number(trn.amount) >= Number(filter.amountFrom))
            if(filter.amountTo) trns = trns.filter(trn =>  Number(trn.amount) <=  Number(filter.amountTo))
            if(filter.type) trns = trns.filter(trn => trn.transaction_type === filter.type)
            if(filter.category) trns = trns.filter(trn =>  trn.category === filter.category)
            if(filter.author) trns = trns.filter(trn =>  trn.user === filter.author)
            return trns
        }
    }
}

export const sortMixin = {
    methods: {
        sortTransactions(transactions, key, descend) {
            let trns = transactions.slice()
            switch(key) {
                case 'Date':
                    if (descend) trns = trns.sort((a, b) => new Date(b.date) - new Date(a.date))
                    else trns = trns.sort((a, b) => new Date(a.date) - new Date(b.date))
                    break
                case 'Amount':
                    if(descend) {
                        trns = trns.sort((a, b) => { 
                            const amountA = (a.transaction_type === 'expense' ? a.amount * -1 : a.amount)
                            const amountB = (b.transaction_type === 'expense' ? b.amount * -1 : b.amount)
                            return amountB - amountA
                        })
                    } else {
                        trns = trns.sort((a, b) => { 
                            const amountA = (a.transaction_type === 'expense' ? a.amount * -1 : a.amount)
                            const amountB = (b.transaction_type === 'expense' ? b.amount * -1 : b.amount)
                            return amountA - amountB
                        })
                    }
                    break                
            }
            return trns
        }
    }
}