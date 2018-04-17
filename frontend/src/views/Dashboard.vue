<template>
    <section id="dashboard" class="dashboard-wrapper section">
        <div class="dashboard-filters">
            <button class="button" @click="subtractMonth()"><i class="fas fa-angle-left"></i></button>
            <div class="dashboard-filter">
                <p>Zvolený měsíc: {{ month | parseMonth }}</p>
            </div>
            <button class="button" @click="addMonth()"><i class="fas fa-angle-right"></i></button>
        </div>
        <div class="columns">
            <div class="column"></div>
            <div class="column">
                <doughnut-chart :chartData="categoriesDataset" :options="{responsive: true, maintainAspectRatio: false}" />
            </div>
        </div>
        <div class="columns">
            <div class="column">
                <line-chart :chartData="getTransactions" :options="{responsive: true, maintainAspectRatio: false}" />
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
            month: ''
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
        addMonth() {
            this.month = moment(this.month).add(1, 'month')
        },
        subtractMonth() {
            this.month = moment(this.month).subtract(1, 'month')
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
            const categories = this.categories.slice().filter(cat => cat.balance < 0).sort((a, b) => {
                return b.balance - a.balance
            })
            for(let cat of categories) {
                data.datasets[0].data.push(cat.balance)
                data.datasets[0].backgroundColor.push(cat.color)
                data.labels.push(cat.name)
            }
            return data
        },
        // lastTransactions() {
        //     return this.transactions.slice(0, 5);
        // },
        getTransactions() {
            let data = {
                datasets: [{ data: [], backgroundColor: [], borderColor: [] }],
                labels: []
            }
            let dateFrom = moment(this.month).startOf('month').format('YYYY-MM-DD')
            let dateTo =  moment(this.month).endOf('month').format('YYYY-MM-DD')
            for(var i = 0; i < 6; i++) {
                dateFrom = moment(this.month).subtract(i, 'months').startOf('month').format('YYYY-MM-DD')
                dateTo = moment(this.month).subtract(i, 'months').endOf('month').format('YYYY-MM-DD')
                let transactions = this.transactions.filter(trns => trns.date >= dateFrom && trns.date <= dateTo);
                data.datasets[0].data.unshift(Number(this.calculateBalance(0, transactions)))
                data.labels.unshift(moment(dateFrom).format('MMMM'))
            }
            data.datasets[0].backgroundColor.push('#d3eafb')
            data.datasets[0].borderColor.push('#2599ee')
            return data
        },
        // calculateDifference() {
        //     const lastMonthFirstDay = moment().subtract(1, 'months').startOf('month').format('YYYY-MM-DD');
        //     const lastMonthLastDay = moment().subtract(1, 'months').endOf('month').format('YYYY-MM-DD');
        //     const thisMonthFirstDay = moment().startOf('month').format('YYYY-MM-DD');
        //     const thisMonthLastDay = moment().endOf('month').format('YYYY-MM-DD');

        //     const lastMonthTransactions = this.transactions.filter(trns => trns.date > lastMonthFirstDay && trns.date < lastMonthLastDay);
        //     const thisMonthTransactions = this.transactions.filter(trns => trns.date > thisMonthFirstDay && trns.date < thisMonthLastDay);
            
        //     let balanceLastMonth = this.calculateBalance(0, lastMonthTransactions);
        //     let balanceThisMonth = this.calculateBalance(0, thisMonthTransactions);

        //     return balanceThisMonth - balanceLastMonth;
        // },
        // calculateTransactionsFromLastMonth() {
        //     const thisMonthFirstDay = moment().startOf('month').format('YYYY-MM-DD');
        //     const thisMonthLastDay = moment().endOf('month').format('YYYY-MM-DD');
        //     const thisMonthTransactions = this.transactions.filter(trns => trns.date > thisMonthFirstDay && trns.date < thisMonthLastDay);
        //     return thisMonthTransactions.length;
        // },
        // calculateTransactionsFromLastWeek() {
        //     const thisMonthFirstDay = moment().startOf('week').format('YYYY-MM-DD');
        //     const thisMonthLastDay = moment().endOf('week').format('YYYY-MM-DD');
        //     const thisMonthTransactions = this.transactions.filter(trns => trns.date > thisMonthFirstDay && trns.date < thisMonthLastDay);
        //     return thisMonthTransactions.length;
        // }
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
        this.month = moment().startOf('month').format('YYYY-MM-DD')
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
