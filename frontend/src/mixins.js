export const filterMixin = {
    methods: {
        filterTransactions(transactions, categoryID, dateFrom, dateTo) {
            let trns = transactions.slice()
            const filter = this.$store.state.filter

            if(filter.amountFrom) trns = trns.filter(trn => Number(trn.amount) >= Number(filter.amountFrom))
            if(filter.amountTo) trns = trns.filter(trn => Number(trn.amount) <=  Number(filter.amountTo))
            if(filter.author) trns = trns.filter(trn => trn.user === filter.author)

            trns = this.filterTransactionsByDate(trns, dateFrom, dateTo)
            trns = this.filterTransactionsByType(trns, filter.type)
            trns = this.filterTransactionsByCategory(trns, categoryID)
            
            return trns
        },
        filterTransactionsByDate(transactions, dateFrom, dateTo) {
            let trns = transactions.slice()
            const filter = this.$store.state.filter

            if(dateFrom && dateTo) {
                trns = trns.filter(trn => trn.date >= dateFrom)
                trns = trns.filter(trn => trn.date <= dateTo)
            } else {
                trns = trns.filter(trn => trn.date >= filter.dateFrom)
                trns = trns.filter(trn => trn.date <= filter.dateTo)
            }
            return trns
        },
        filterTransactionsByCategory(transactions, categoryID) {
            let trns = transactions.slice()
            const filter = this.$store.state.filter

            if(categoryID) trns = trns.filter(trn => trn.category == categoryID)
            else if(filter.category) trns = trns.filter(trn => trn.category == filter.category)

            return trns
        },
        filterTransactionsByType(transactions, type) {
            let trns = transactions.slice()
            const filter = this.$store.state.filter

            if(type) trns = trns.filter(trn => trn.transaction_type === type)
            else if(filter.type) trns = trns.filter(trn => trn.transaction_type === filter.type)

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


export const dateMixin = {
    methods: {
        subtractDate(dateFrom, dateTo) {
            if(this.isMonth(dateFrom, dateTo)) {
                dateTo = this.$moment(dateTo).subtract(1, 'months').endOf('month').format('YYYY-MM-DD')
                dateFrom = this.$moment(dateFrom).subtract(1, 'months').startOf('month').format('YYYY-MM-DD')
            } else if (this.isYear(dateFrom, dateTo)) {
                dateTo = this.$moment(dateTo).subtract(1, 'years').endOf('year').format('YYYY-MM-DD')
                dateFrom = this.$moment(dateFrom).subtract(1, 'years').startOf('year').format('YYYY-MM-DD')
            } else {
                let difference = this.$moment.duration(this.$moment(dateTo).diff(this.$moment(dateFrom))).asDays()
                if (difference === 0) difference = 1
                dateTo = this.$moment(dateTo).subtract(difference, 'days').format('YYYY-MM-DD')
                dateFrom = this.$moment(dateFrom).subtract(difference, 'days').format('YYYY-MM-DD')
            }

            return {'dateFrom': dateFrom, 'dateTo': dateTo}
        },
        addDate(dateFrom, dateTo) {
            if(this.isMonth(dateFrom, dateTo)) {
                dateTo = this.$moment(dateTo).add(1, 'months').endOf('month').format('YYYY-MM-DD')
                dateFrom = this.$moment(dateFrom).add(1, 'months').startOf('month').format('YYYY-MM-DD')
            } else if (this.isYear(dateFrom, dateTo)) {
                dateTo = this.$moment(dateTo).add(1, 'years').endOf('year').format('YYYY-MM-DD')
                dateFrom = this.$moment(dateFrom).add(1, 'years').startOf('year').format('YYYY-MM-DD')
            } else {
                let difference = this.$moment.duration(this.$moment(dateTo).diff(this.$moment(dateFrom))).asDays()
                if (difference === 0) difference = 1
                dateTo = this.$moment(dateTo).add(difference, 'days').format('YYYY-MM-DD')
                dateFrom = this.$moment(dateFrom).add(difference, 'days').format('YYYY-MM-DD')
            }       

            return {'dateFrom': dateFrom, 'dateTo': dateTo}
        },
        isMonth(dateFrom, dateTo) {
            const startOfPeriod = this.$moment(dateFrom).startOf('month').format('YYYY-MM-DD')
            const endtOfPeriod = this.$moment(dateTo).endOf('month').format('YYYY-MM-DD')
            const diference = this.$moment.duration(this.$moment(endtOfPeriod).diff(this.$moment(startOfPeriod))).asDays()

            return this.$moment(startOfPeriod).isSame(this.$moment(dateFrom)) && this.$moment(endtOfPeriod).isSame(this.$moment(dateTo)) && diference > 26 && diference < 32
        },
        isYear(dateFrom, dateTo) {
            const startOfPeriod = this.$moment(dateFrom).startOf('year').format('YYYY-MM-DD')
            const endtOfPeriod = this.$moment(dateTo).endOf('year').format('YYYY-MM-DD')
            const diference = this.$moment.duration(this.$moment(endtOfPeriod).diff(this.$moment(startOfPeriod))).asDays()

            return this.$moment(startOfPeriod).isSame(this.$moment(dateFrom)) && this.$moment(endtOfPeriod).isSame(this.$moment(dateTo)) && diference > 360 && diference < 370
        }
    }
}

export const balanceMixin = {
    methods: {
        calculateBalance(transactions) {
            let trns = transactions.slice()
            let balance = 0
            for(let trn of trns) {
                if(trn.transaction_type === 'expense') balance -= Number(trn.amount)
                else balance += Number(trn.amount)
            }
            return balance
        },
        calculateExpenses(transactions) {
            let trns = transactions.slice()
            let balance = 0
            for(let trn of trns) {
                if(trn.transaction_type === 'expense') balance += Number(trn.amount)
            }
            return balance
        }
    }
}