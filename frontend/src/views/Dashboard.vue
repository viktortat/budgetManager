<template>
    <section id="dashboard" class="dashboard-wrapper section">
        <div class="dashboard-filters">
            <div class="dashboard-filter">
                <button class="button is-square" @click="subtractDate()"><i class="fas fa-angle-left"></i></button>
                <flat-pickr v-model="dateFrom" class="input" id="dashboard-date-from"></flat-pickr>
                <flat-pickr v-model="dateTo" class="input" id="dashboard-date-to"></flat-pickr>
                <button class="button is-square" @click="addDate()"><i class="fas fa-angle-right"></i></button>
            </div>
            <div class="dashboard-filter">
                <button class="button is-link" @click="setFilterDate('thisMonth')">současný měsíc</button>
                <button class="button is-link" @click="setFilterDate('lastMonth')">minulý měsíc</button>
                <button class="button is-link" @click="setFilterDate('thisYear')">současný rok</button>
                <button class="button is-link" @click="setFilterDate('lastYear')">minulý rok</button>
            </div>
        </div>
        <div class="columns">
            <div class="column column-small">
                <h4>Stav</h4>
                <br>
                <p class="is-size-1 is-bold">{{ wallet.balance | formatCurrency }}</p>
            </div>
            <div class="column column-small">
                <h4>Příjmy</h4>
                <br>
                <p class="is-size-1 is-bold">{{ computeIncome | formatCurrency }}</p>
            </div>
            <div class="column column-small">
                <h4>Výdaje</h4>
                <br>
                <p class="is-size-1 is-bold">{{ computeExpenses | formatCurrency }}</p>
            </div>
            <div class="column column-small">
                <h4>Změna</h4>
                <br>
                <p class="is-size-1 is-bold" :class="{'is-danger': computeChange < 0, 'is-success': computeChange > 0}">{{ computeChange | formatCurrency }}</p>
            </div>
        </div>
        <div class="columns">
            <div class="column"></div>
            <div class="column"></div>
            <div class="column">
                <p v-if="categoriesDataset.datasets[0].data.length === 0">Žádná data k zobrazení...</p>
                <doughnut-chart v-else :chartData="categoriesDataset" :options="categoriesOptions" />
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
            if(this.isMonthSelected()) {
                this.dateTo = moment(this.dateTo).subtract(1, 'months').endOf('month').format('YYYY-MM-DD')
                this.dateFrom = moment(this.dateFrom).subtract(1, 'months').startOf('month').format('YYYY-MM-DD')
            } else if (this.isYearSelected()) {
                this.dateTo = moment(this.dateTo).subtract(1, 'years').endOf('year').format('YYYY-MM-DD')
                this.dateFrom = moment(this.dateFrom).subtract(1, 'years').startOf('year').format('YYYY-MM-DD')
            } else {
                let difference = moment.duration(moment(this.dateTo).diff(moment(this.dateFrom))).asDays()
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
                    data.datasets[0].data.push((balance/expenses)*100)
                    data.datasets[0].backgroundColor.push(cat.color)
                    data.labels.push(cat.name)
                }
            }
            return data
        },
        categoriesOptions() {
            const options = {
                responsive: true,
                maintainAspectRatio: false,
                tooltips: {
                    callbacks: {
                        label: (tooltipItem, data) => {
                            let dataset = data.datasets[tooltipItem.datasetIndex];
                            let total = dataset.data.reduce(function(previousValue, currentValue, currentIndex, array) {
                                return previousValue + currentValue;
                            })
                            let currentValue = dataset.data[tooltipItem.index];
                            let precentage = Math.floor(((currentValue/total) * 100)+0.5)
                            return precentage + " %"
                        }
                    }
                } 
            }
            return options
        },
        transactionsDataset() {
            let data = {
                datasets: [{ data: [], backgroundColor: [], borderColor: [], lineTension: 0 }],
                labels: []
            }
            let dateFrom = this.dateFrom
            let dateTo = this.dateTo
            for(var i = 0; i < 6; i++) {
                let transactions = this.transactions.filter(trn => trn.date >= dateFrom && trn.date < dateTo)
                data.datasets[0].data.unshift(Number(this.calculateBalance(0, transactions)))
                if(this.isMonthSelected()) {
                    data.labels.unshift(moment(dateFrom).format('MMMM'))
                    dateFrom = moment(dateFrom).subtract(1, 'months').format('YYYY-MM-DD')
                    dateTo = moment(dateTo).subtract(1, 'months').format('YYYY-MM-DD')
                } else if (this.isYearSelected()) {
                    data.labels.unshift(moment(dateFrom).format('YYYY'))
                    dateFrom = moment(dateFrom).subtract(1, 'years').format('YYYY-MM-DD')
                    dateTo = moment(dateTo).subtract(1, 'years').format('YYYY-MM-DD')
                } else {
                    data.labels.unshift(moment(dateFrom).format('DD MMMM YYYY') + " – " + moment(dateTo).subtract(1, 'days').format('DD MMMM YYYY'))
                    let difference = moment.duration(moment(this.dateTo).diff(moment(this.dateFrom))).asDays()
                    dateTo = moment(dateTo).subtract(difference, 'days').format('YYYY-MM-DD')
                    
                    dateFrom = moment(dateFrom).subtract(difference, 'days').format('YYYY-MM-DD')
                }
            }
            data.datasets[0].backgroundColor.push('#d3eafb')
            data.datasets[0].borderColor.push('#2599ee')
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
        }
    },
    components: {
        Transaction,
        flatPickr,
        DoughnutChart,
        LineChart
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
    @media screen and (max-width: 767px)
        display: none

    margin: 10px
    margin-bottom: 0
    padding: 10px
    display: inline-flex
    flex-flow: column
    align-items: center

    background-color: #FFFFFF

.dashboard-filter
    margin-bottom: 20px
    display: inline-flex
    align-items: center
    
    &:last-child
        margin-bottom: 0

    & > *
        margin-right: 10px

        &:last-child
            margin-right: 0

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

    &.column-small
        min-height: 10vh

</style>
