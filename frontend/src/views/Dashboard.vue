<template>
    <div id="dashboard" class="dashboard section">
        <div class="card card-bilance">
            <div class="card-heading">
                <h2>Bilance</h2>
            </div>
            <h3>Zůstatek</h3>
            <p class="is-size-2 is-bold is-right">{{ wallet.balance | formatCurrency }}</p>
            <h3>Změna</h3>
            <p class="is-size-2 is-bold is-right"><i class="fas fa-angle-up is-success"></i> {{ calculateDifference | formatCurrency }}</p>
            <small class="is-right">Oproti minulému měsíci</small>
            <h3>Počet Transakcí</h3>
            <div class="level">
                <div>
                    <p class="is-size-2 is-bold">{{ calculateTransactionsFromLastWeek }} <i class="fas fa-angle-up is-success"></i></p>
                    <small>Za minulý týden</small>
                </div>
                <div>
                    <p class="is-size-2 is-bold is-right"><i class="fas fa-angle-up is-success"></i> {{calculateTransactionsFromLastMonth}}</p>
                    <small class="is-right">Za minulý měsíc</small>
                </div>
            </div>
        </div>
        <div class="card">
            <div class="card-heading">
                <h2>Transakce</h2>
                <router-link :to="{name: 'Transactions'}" class="is-link-light">
                    <i class="fas fa-angle-double-right is-size-3"></i>
                </router-link>
            </div>
            <transaction v-for="(transaction, index) in lastTransactions" :key="index" :transaction="transaction" :categories="categories" />
        </div>
        <div class="card">
            <div class="card-heading">
                <h2>Karta</h2>
            </div>
        </div>
        <div class="card">
            <div class="card-heading">
                <h2>Karta</h2>
            </div>
        </div>
        <div class="card card-wide card-graph">
            <bar-graph/>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import moment from 'moment'

import Transaction from '@/components/Transaction.vue'
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

.dashboard
    @media screen and (min-width: 1344px) and (max-width: 1919px)
        grid-template-columns: repeat(2, 480px)

    @media screen and (min-width: 768px) and (max-width: 1343px)
        grid-template-columns: 480px

    @media screen and (max-width: 767px)
        grid-template-columns: 1fr
        grid-gap: 0
        padding-left: 0
        padding-top: 16px
        margin: 64px 0

    display: grid
    grid-template-columns: repeat(3, 480px)
    grid-gap: 48px
    justify-content: center
    padding-left: 48px
    padding-top: 122px

.card
    @media screen and (max-width: 767px)
        width: 100vw
        box-shadow: unset
        border-radius: 0
        padding: 16px
        padding-top: 96px
        
    position: relative
    width: 480px
    height: 480px
    padding: 32px
    padding-top: 96px
    
    box-shadow: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24)
    border-radius: $border-radius
    background-color: #FFFFFF

    & > h3
        padding-top: 32px
        padding-bottom: 16px

.card-wide
    @media screen and (min-width: 768px) and (max-width: 1343px)
        width: 480px
    
    @media screen and (max-width: 767px)
        width: 100vw

    width: 1008px

.card-heading
    @media screen and (max-width: 767px)
        border-radius: 0

    display: flex
    align-items: center
    justify-content: space-between
    position: absolute
    left: 0
    top: 0
    height: 96px
    width: 100%
    padding-left: 32px
    padding-right: 32px

    font-weight: 600
    
    color: $font-color-light
    background-color: #7B76F4
    background: linear-gradient(to bottom right, #7B76F4, #7784FB)
    border-radius: $border-radius $border-radius 0 0 

.card-graph
    padding-top: 32px

.card-bilance
    & small 
        padding-top: 8px


</style>
