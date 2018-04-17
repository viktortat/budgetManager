<template>
    <section id="dashboard" class="dashboard-wrapper section">
        <div class="dashboard-filters">
            <button class="button" @click="subtractDate()"><i class="fas fa-angle-left"></i></button>
            <div class="dashboard-filter">
                <flat-pickr v-model="dateFrom" class="input"></flat-pickr>
                <flat-pickr v-model="dateTo" class="input"></flat-pickr>
            </div>
            <button class="button" @click="addDate()"><i class="fas fa-angle-right"></i></button>
        </div>
        <div class="columns">
            <div class="column">
                <p>{{ calculateExpenses }}</p>
                <p>{{ calculateIncome }}</p>
            </div>
            <div class="column">
                <doughnut-chart :chartData="categoriesDataset" :options="{responsive: true, maintainAspectRatio: false}" />
            </div>
        </div>
        <div class="columns">
            <div class="column">
                <line-chart :chartData="transactionsDataset" :options="{responsive: true, maintainAspectRatio: false}" />
            </div>
        </div>
    </section>
</template>


<script>
import axios from 'axios'
import moment from 'moment'
import { mapState, mapActions } from 'vuex'
import Transaction from '@/components/TransactionSimple.vue'
import DoughnutChart from '@/components/DoughnutChart.js'
import LineChart from '@/components/LineChart.js'

import flatPickr from 'vue-flatpickr-component'
import 'flatpickr/dist/flatpickr.css'

export default {
    data() {
        return {
            difference: 0,
            dateTo: moment().endOf('month').format('YYYY-MM-DD'), 
            dateFrom: moment().startOf('month').format('YYYY-MM-DD')
        }
    },
    methods: {
        ...mapActions([
            'loadData'
        ]),
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
            if(this.walkByMonth()) {
                this.dateTo = moment(this.dateTo).subtract(1, 'months').endOf('month').format('YYYY-MM-DD')
                this.dateFrom = moment(this.dateFrom).subtract(1, 'months').startOf('month').format('YYYY-MM-DD')
            } else {
                let difference = moment.duration(moment(this.dateTo).diff(moment(this.dateFrom))).asDays()
                this.dateTo = moment(this.dateTo).subtract(difference, 'days').format('YYYY-MM-DD')
                this.dateFrom = moment(this.dateFrom).subtract(difference, 'days').format('YYYY-MM-DD')
            }
        },
        addDate() {
            if(this.walkByMonth()) {
                this.dateTo = moment(this.dateTo).add(1, 'months').endOf('month').format('YYYY-MM-DD')
                this.dateFrom = moment(this.dateFrom).add(1, 'months').startOf('month').format('YYYY-MM-DD')
            } else {
                let difference = moment.duration(moment(this.dateTo).diff(moment(this.dateFrom))).asDays()
                this.dateTo = moment(this.dateTo).add(difference, 'days').format('YYYY-MM-DD')
                this.dateFrom = moment(this.dateFrom).add(difference, 'days').format('YYYY-MM-DD')
            }
        },
        walkByMonth() {
            let dateTo = moment(this.dateTo).endOf('month').format('YYYY-MM-DD')
            let dateFrom = moment(this.dateFrom).startOf('month').format('YYYY-MM-DD')
            return moment(dateFrom).isSame(moment(this.dateFrom)) && moment(dateTo).isSame(moment(this.dateTo))
        }
    },
    computed: {
        ...mapState([
            'wallet',
            'transactions',
            'categories'
        ]),
        categoriesDataset() {
            let data = {
                datasets: [{ data: [], backgroundColor: [] }],
                labels: []
            }   
            let transactions = this.transactions.filter(trn => trn.date >= this.dateFrom && trn.date <= this.dateTo)
            let categories = this.categories.slice()
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
                    data.datasets[0].data.push(balance)
                    data.datasets[0].backgroundColor.push(cat.color)
                    data.labels.push(cat.name)
                }
            }
            return data
        },
        transactionsDataset() {
            let data = {
                datasets: [{ data: [], backgroundColor: [], borderColor: [] }],
                labels: []
            }
            let dateFrom = this.dateFrom
            let dateTo = this.dateTo
            for(var i = 0; i < 6; i++) {
                let transactions = this.transactions.filter(trn => trn.date >= dateFrom && trn.date <= dateTo)
                data.datasets[0].data.unshift(Number(this.calculateBalance(0, transactions)))
                data.labels.unshift(moment(dateFrom).format('MMMM'))
                dateFrom = moment(dateFrom).subtract(1, 'months').format('YYYY-MM-DD')
                dateTo = moment(dateTo).subtract(1, 'months').format('YYYY-MM-DD')
            }
            data.datasets[0].backgroundColor.push('#d3eafb')
            data.datasets[0].borderColor.push('#2599ee')
            return data
        },
        calculateExpenses() {
            let transactions = this.transactions.filter(trn => trn.date >= this.dateFrom && trn.date <= this.dateTo)
            let balance = 0
            for (let trn of transactions) {
                if(trn.transaction_type === 'expense') {
                    balance += Number(trn.amount)
                }
            }
            return balance
        },
        calculateIncome() {
            let transactions = this.transactions.filter(trn => trn.date >= this.dateFrom && trn.date <= this.dateTo)
            let balance = 0
            for (let trn of transactions) {
                if(trn.transaction_type === 'income') {
                    balance += Number(trn.amount)
                }
            }
            return balance
        }
    },
    components: {
        Transaction,
        flatPickr,
        DoughnutChart,
        LineChart
    },
    filters: {
        parseMonth(value) {
            return moment(value).format('MMMM YYYY')
        }
    },
    created() {
        this.loadData() 
    }
}
</script>


<style lang="stylus" scoped>
@import "../styles/variables.styl"

.dashboard-wrapper
    @media screen and (max-width: 767px)
        min-height: 100vh
        
    min-height: 100.06vh

    background-color: $background-color-primary

.dashboard-filters
    display: flex
    justify-content: space-between
    align-items: center
    flex-wrap: wrap
    margin: 10px
    padding: 10px

    border-radius: $border-radius
    background-color: #FFFFFF

.columns 
    display: flex
    flex-wrap: wrap
    margin: 10px

.column
    flex: 1 1 auto
    min-height: 33vh
    max-height: 50vh
    width: 300px
    padding: 20px

    border-radius: $border-radius
    background-color: #FFFFFF

</style>
