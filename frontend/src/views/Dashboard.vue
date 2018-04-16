<template>
    <section id="dashboard" class="dashboard-wrapper section">
        <div class="dashboard-filters">
            <div class="dashboard-filter">
                <label for="dashboard-date-from" class="label">
                    <p>Datum od:</p>
                </label>
                <flat-pickr v-model="dateFrom" class="input input-100" id="dashboard-date-from"></flat-pickr>
            </div>
            <div class="filter">
                <label for="dashboard-date-to" class="label">
                    <p>Datum do:</p>
                </label>
                <flat-pickr v-model="dateTo" class="input input-100" id="dashboard-date-to"></flat-pickr>
            </div>
        </div>
        <div class="columns">
            <div class="column"></div>
            <div class="column">
                <doughnut-chart :data="categoriesDataset" :options="{responsive: true, maintainAspectRatio: false}"/>
            </div>
        </div>
        <div class="columns">
            <div class="column"></div>
        </div>
    </section>
</template>

<script>
import axios from 'axios'
import moment from 'moment'
import { mapState, mapActions } from 'vuex'
import Transaction from '@/components/TransactionSimple.vue'
import PieChart from '@/components/PieChart.js'
import DoughnutChart from '@/components/DoughnutChart.js'

import flatPickr from 'vue-flatpickr-component'
import 'flatpickr/dist/flatpickr.css'

export default {
    data() {
        return {
            difference: 0,
            dateFrom: "",
            dateTo: ""
        }
    },
    methods: {
        ...mapActions([
            'loadData'
        ]),
        // calculateBalance(balance, transactions) {
        //     for(let transaction of transactions) {
        //         if(transaction.transaction_type === "income") {
        //             balance =+ transaction.amount;
        //         } else {
        //             balance =- transaction.amount;
        //         }
        //     }
        //     return balance;
        // }
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
        }
        // lastTransactions() {
        //     return this.transactions.slice(0, 5);
        // },
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
        PieChart,
        DoughnutChart
    },
    created() {
        this.loadData()
        this.dateFrom = moment().startOf('month').format('YYYY-MM-DD')
        this.dateTo = moment().endOf('month').format('YYYY-MM-DD')
    }
}
</script>



<style lang="stylus" scoped>
@import "../styles/variables.styl"

.dashboard-wrapper
    min-height: 100.06vh

    background-color: $background-color-primary

.dashboard-filters
    display: flex
    justify-content: center
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
