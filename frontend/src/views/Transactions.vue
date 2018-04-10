<template>
    <div class="section">
        <div class="filter-wrapper">
            <div>
                <label for="filter-date-from" class="label">
                    <p>Datum od:</p>
                </label>
                <flat-pickr v-model="dateFrom" class="input"></flat-pickr>
            </div>
            <div>
                <label for="filter-date-to" class="label">
                    <p>Datum do:</p>
                </label>
                <flat-pickr v-model="dateTo" class="input"></flat-pickr>
            </div>
            <div>
                <label for="filter-amount-from" class="label">
                    <p>Částka od:</p>
                </label>
                <input type="number" class="input" id="filter-amount-from" v-model="amountFrom"> 
            </div>
            <div>
                <label for="filter-amount-to" class="label">
                    <p>Částka do:</p>
                </label>
                <input type="number" class="input" id="filter-amount-to" v-model="amountTo">
            </div>
            <button class="button" @click="clearFilter()">Clear</button>
        </div>
        <transaction v-for="(transaction, index) in filteredTransactions" :key="index" :transaction="transaction" :categories="categories" :wallet="wallet" />
    </div>
</template>

<script>
import Transaction from '@/components/TransactionExtended.vue'
import { mapState, mapActions } from 'vuex'

import flatPickr from 'vue-flatpickr-component'
import 'flatpickr/dist/flatpickr.css'

export default {
    data() {
        return {
            dateFrom: "",
            dateTo: "",
            amountFrom: "",
            amountTo: ""
        }
    },
    computed: {
        ...mapState([
            'transactions',
            'categories',
            'wallet'
        ]),
        filteredTransactions() {
            let transactions = this.transactions.slice();
            if(this.dateFrom !== "") transactions = transactions.filter(trn => trn.date >= this.dateFrom);
            if(this.dateTo !== "") transactions = transactions.filter(trn => trn.date <= this.dateTo);
            if(this.amountFrom !== "") transactions = transactions.filter(trn => Number(trn.amount) >= Number(this.amountFrom));
            if(this.amountTo !== "") transactions = transactions.filter(trn =>  Number(trn.amount) <=  Number(this.amountTo));
            return transactions;
        }
    },  
    methods: {
        ...mapActions([
            'loadData'
        ]),
        clearFilter() {
            this.dateFrom = "";
            this.dateTo = "";
            this.amountFrom = "";
            this.amountTo = "";
        }
    },
    components: {
        Transaction,
        flatPickr
    },
    created() {
        this.loadData();
    }
}
</script>

<style lang="stylus" scoped>
@import "../styles/variables.styl"
.transactions-wrapper
    @media screen and (max-width: 767px)
        padding-top: 16px

    display: flex
    flex-flow: column
    align-items: center
    padding-top: 122px

.filter-wrapper
    @media screen and (min-width: 1020px)
        width: 900px

    @media screen and (min-width: 620px) and (max-width: 1019px)
        width: 600px

    display: flex
    flex-wrap: wrap
    justify-content: space-between
    padding: 20px
    width: 300px
    min-height: 200px
    margin-left: 10px
    margin-top: 10px
    margin-bottom: 10px
    margin-right: 10px

    background-color: #ffffff
    border-radius: $border-radius

</style>
