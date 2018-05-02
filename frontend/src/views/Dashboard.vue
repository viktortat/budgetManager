<template>
    <section class="dashboard section">
        <div>
            <h4>Stav</h4>
            <p>{{ wallet.balance | formatCurrency }}</p>
        </div>
        <div>
            <h4>Příjmy</h4>
            <p>{{ computeIncome | formatCurrency }}</p>
        </div>
        <div>
            <h4>Výdaje</h4>
            <p>{{ computeExpenses | formatCurrency }}</p>
        </div>
        <div>
            <h4>Změna</h4>
            <p :class="{'is-danger': computeChange < 0, 'is-success': computeChange > 0}">{{ computeChange | formatCurrency }}</p>
        </div>
    </section>
</template>


<script>
import axios from 'axios'
import moment from 'moment'
import { mapState, mapActions } from 'vuex'

import AppButton from '@/components/AppButton.vue'
import AppInput from '@/components/AppInput.vue'

import flatPickr from 'vue-flatpickr-component'
import 'flatpickr/dist/flatpickr.css'

export default {
    data() {
        return {
            dateTo: moment().endOf('month').format('YYYY-MM-DD'), 
            dateFrom: moment().startOf('month').format('YYYY-MM-DD'),
            test: ""
        }
    },
    methods: {
        ...mapActions([
            'loadData'
        ]),
        filterTransactions() {
            return this.transactions.filter(trn => trn.date >= this.dateFrom && trn.date <= this.dateTo)
        },
        calculateBalance(balance, transactions) {
            for(let transaction of transactions) {
                if(transaction.transaction_type === "income") {
                    balance += Number(transaction.amount);
                } else {
                    balance -= Number(transaction.amount);
                }
            }
            return balance;
        },
        subtractDate() {
            if(this.isMonthSelected()) {
                this.dateTo = moment(this.dateTo).subtract(1, 'months').endOf('month').format('YYYY-MM-DD')
                this.dateFrom = moment(this.dateFrom).subtract(1, 'months').startOf('month').format('YYYY-MM-DD')
            } else if (this.isYearSelected()) {
                this.dateTo = moment(this.dateTo).subtract(1, 'years').endOf('year').format('YYYY-MM-DD')
                this.dateFrom = moment(this.dateFrom).subtract(1, 'years').startOf('year').format('YYYY-MM-DD')
            } else {
                let difference = moment.duration(moment(this.dateTo).diff(moment(this.dateFrom))).asDays()
                if (difference === 0) difference = 1
                this.dateTo = moment(this.dateTo).subtract(difference, 'days').format('YYYY-MM-DD')
                this.dateFrom = moment(this.dateFrom).subtract(difference, 'days').format('YYYY-MM-DD')
            }
        },
        addDate() {
            if(this.isMonthSelected()) {
                this.dateTo = moment(this.dateTo).add(1, 'months').endOf('month').format('YYYY-MM-DD')
                this.dateFrom = moment(this.dateFrom).add(1, 'months').startOf('month').format('YYYY-MM-DD')
            } else if (this.isYearSelected()) {
                this.dateTo = moment(this.dateTo).add(1, 'years').endOf('year').format('YYYY-MM-DD')
                this.dateFrom = moment(this.dateFrom).add(1, 'years').startOf('year').format('YYYY-MM-DD')
            } else {
                let difference = moment.duration(moment(this.dateTo).diff(moment(this.dateFrom))).asDays()
                if (difference === 0) difference = 1
                this.dateTo = moment(this.dateTo).add(difference, 'days').format('YYYY-MM-DD')
                this.dateFrom = moment(this.dateFrom).add(difference, 'days').format('YYYY-MM-DD')
            }
        },
        isMonthSelected() {
            let dateTo = moment(this.dateTo).endOf('month').format('YYYY-MM-DD')
            let dateFrom = moment(this.dateFrom).startOf('month').format('YYYY-MM-DD')
            let diference = moment.duration(moment(dateTo).diff(moment(dateFrom))).asDays()
            return moment(dateFrom).isSame(moment(this.dateFrom)) && moment(dateTo).isSame(moment(this.dateTo)) && diference > 26 && diference < 32
        },
        isYearSelected() {
            let dateTo = moment(this.dateTo).endOf('year').format('YYYY-MM-DD')
            let dateFrom = moment(this.dateFrom).startOf('year').format('YYYY-MM-DD')
            let diference = moment.duration(moment(dateTo).diff(moment(dateFrom))).asDays()
            return moment(dateFrom).isSame(moment(this.dateFrom)) && moment(dateTo).isSame(moment(this.dateTo)) && diference > 360 && diference < 370
        },
        setFilterDate(value) {
            switch(value) {
                case 'thisMonth':
                    this.dateTo = moment().endOf('month').format('YYYY-MM-DD'), 
                    this.dateFrom = moment().startOf('month').format('YYYY-MM-DD')
                    break
                case 'lastMonth':
                    this.dateTo = moment().subtract(1, 'months').endOf('month').format('YYYY-MM-DD')
                    this.dateFrom = moment().subtract(1, 'months').startOf('month').format('YYYY-MM-DD')
                    break
                case 'thisYear':
                    this.dateTo = moment().endOf('year').format('YYYY-MM-DD')
                    this.dateFrom = moment().startOf('year').format('YYYY-MM-DD')
                    break
                case 'lastYear':
                    this.dateTo = moment().subtract(1, 'years').endOf('year').format('YYYY-MM-DD')
                    this.dateFrom = moment().subtract(1, 'years').startOf('year').format('YYYY-MM-DD')
                    break
            }
        },
        calculateExpenses() {
            let transactions = this.filterTransactions()
            let balance = 0
            for (let trn of transactions) {
                if(trn.transaction_type === 'expense') {
                    balance += Number(trn.amount)
                }
            }
            return balance
        },
        calculateIncome() {
            let transactions = this.filterTransactions()
            let balance = 0
            for (let trn of transactions) {
                if(trn.transaction_type === 'income') {
                    balance += Number(trn.amount)
                }
            }
            return balance
        }
    },
    computed: {
        ...mapState([
            'wallet',
            'transactions',
            'categories',
            'budgets'
        ]),
        categoriesDataset() {
            let data = {
                labels: [],
                series: []
            }   
            let transactions = this.filterTransactions()
            let categories = this.categories.slice()
            const expenses = this.calculateExpenses()
            for (let cat of categories) {
                let balance = 0
                for (var i = 0; i < cat.transactions.length; i++) {
                    let trn = transactions.find(x => x.id === cat.transactions[i])
                    if(trn) {
                        if (trn.transaction_type === "expense") {
                            balance += Number(trn.amount)
                        }
                    }
                }
                if(balance) {
                    data.series.push((balance/expenses)*100)
                    data.labels.push(cat.name)
                }
            }
            return data
        },
        transactionsDataset() {
            let data = {
                series: [
                    []
                ],
                labels: []
            }
            let dateFrom = this.dateFrom
            let dateTo = this.dateTo
            for(var i = 0; i < 6; i++) {
                let transactions = this.transactions.filter(trn => trn.date >= dateFrom && trn.date <= dateTo)
                data.series[0].unshift(Number(this.calculateBalance(0, transactions)))
                if(this.isMonthSelected()) {
                    data.labels.unshift(moment(dateFrom).format('MMMM'))
                    dateFrom = moment(dateFrom).subtract(1, 'months').format('YYYY-MM-DD')
                    dateTo = moment(dateTo).subtract(1, 'months').format('YYYY-MM-DD')
                } else if (this.isYearSelected()) {
                    data.labels.unshift(moment(dateFrom).format('YYYY'))
                    dateFrom = moment(dateFrom).subtract(1, 'years').format('YYYY-MM-DD')
                    dateTo = moment(dateTo).subtract(1, 'years').format('YYYY-MM-DD')
                } else {
                    data.labels.unshift(moment(dateFrom).format('DD MMMM YYYY') + " – " + moment(dateTo).format('DD MMMM YYYY'))
                    let difference = moment.duration(moment(this.dateTo).diff(moment(this.dateFrom))).asDays()
                    dateTo = moment(dateTo).subtract(difference + 1, 'days').format('YYYY-MM-DD')
                    dateFrom = moment(dateFrom).subtract(difference + 1, 'days').format('YYYY-MM-DD')
                }
            }
            return data
        },
        computeExpenses() {
            return Math.round(this.calculateExpenses() * 100) / 100
        },
        computeIncome() {
            return Math.round(this.calculateIncome() * 100) / 100
        },
        computeChange() {
            return Math.round((this.calculateIncome() - this.calculateExpenses()) * 100) / 100
        },
        currentMonth() {
            return moment(this.dateFrom).format('YYYY MMMM')
        }
    },
    components: {
        flatPickr,
        AppButton,
        AppInput
    },
    created() {
        this.loadData() 
    }
}
</script>


<style lang="stylus" scoped>

.dashboard
    display: grid
    grid-template-columns: repeat(auto-fit, minmax(260px, 1fr))
    grid-gap: 10px

</style>
