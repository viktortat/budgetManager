<template>
    <div id="dashboard" class="dashboard-wrapper section">
        <div class="columns">
            <div class="column"></div>
            <div class="column"></div>
            <div class="column"></div>
        </div>
        <div class="columns">
            <div class="column"></div>
            <div class="column"></div>
        </div>
        <div class="columns">
            <div class="column"></div>
        </div>
        <div class="columns">
            <div class="column"></div>
            <div class="column"></div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import moment from 'moment'

import Transaction from '@/components/TransactionSimple.vue'
import BarGraph from '@/components/LineChart.vue'

import { tokenMixin } from '@/mixins.js'
import { mapState, mapActions } from 'vuex'

export default {
    mixins: [tokenMixin],
    data() {
        return {
            difference: 0
        }
    },
    methods: {
        ...mapActions([
            'loadData'
        ]),
        calculateBalance(balance, transactions) {
            for(let transaction of transactions) {
                if(transaction.transaction_type === "income") {
                    balance =+ transaction.amount;
                } else {
                    balance =- transaction.amount;
                }
            }
            return balance;
        }
    },
    computed: {
        ...mapState([
            'wallet',
            'transactions',
            'categories'
        ]),
        lastTransactions() {
            return this.transactions.slice(0, 5);
        },
        calculateDifference() {
            const lastMonthFirstDay = moment().subtract(1, 'months').startOf('month').format('YYYY-MM-DD');
            const lastMonthLastDay = moment().subtract(1, 'months').endOf('month').format('YYYY-MM-DD');
            const thisMonthFirstDay = moment().startOf('month').format('YYYY-MM-DD');
            const thisMonthLastDay = moment().endOf('month').format('YYYY-MM-DD');

            const lastMonthTransactions = this.transactions.filter(trns => trns.date > lastMonthFirstDay && trns.date < lastMonthLastDay);
            const thisMonthTransactions = this.transactions.filter(trns => trns.date > thisMonthFirstDay && trns.date < thisMonthLastDay);
            
            let balanceLastMonth = this.calculateBalance(0, lastMonthTransactions);
            let balanceThisMonth = this.calculateBalance(0, thisMonthTransactions);

            return balanceThisMonth - balanceLastMonth;
        },
        calculateTransactionsFromLastMonth() {
            const thisMonthFirstDay = moment().startOf('month').format('YYYY-MM-DD');
            const thisMonthLastDay = moment().endOf('month').format('YYYY-MM-DD');
            const thisMonthTransactions = this.transactions.filter(trns => trns.date > thisMonthFirstDay && trns.date < thisMonthLastDay);
            return thisMonthTransactions.length;
        },
        calculateTransactionsFromLastWeek() {
            const thisMonthFirstDay = moment().startOf('week').format('YYYY-MM-DD');
            const thisMonthLastDay = moment().endOf('week').format('YYYY-MM-DD');
            const thisMonthTransactions = this.transactions.filter(trns => trns.date > thisMonthFirstDay && trns.date < thisMonthLastDay);
            return thisMonthTransactions.length;
        }
    },
    components: {
        Transaction,
        BarGraph
    },
    created() {
        this.loadData();
    }
}
</script>



<style lang="stylus" scoped>
@import "../styles/variables.styl"

.dashboard-wrapper
    min-height: 100.06vh

    background-color: $background-color-primary

.columns 
    display: flex
    flex-wrap: wrap

.column
    flex: 1 1 auto
    min-height: 300px
    width: 300px
    padding: 20px

.column:nth-child(1n), .auto-grid-item:nth-child(1n)
    background-color: aqua

.column:nth-child(2n), .auto-grid-item:nth-child(2n)
    background-color: beige

.column:nth-child(3n), .auto-grid-item:nth-child(3n) 
    background-color: cadetblue

.column:nth-child(4n), .auto-grid-item:nth-child(4n)
    background-color: darksalmon

</style>
