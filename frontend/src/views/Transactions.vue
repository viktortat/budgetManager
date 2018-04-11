<template>
    <div class="section-md">
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
            <div>
                <label for="filter-transaction-type" class="label">
                    <p>Typ transakce</p>                     
                </label>
                <select id="filter-transaction-type" class="input" v-model="type">
                    <option value="" selected>Příjem a Výdej</option>
                    <option value="income">Příjem</option>
                    <option value="expense">Výdej</option>
                </select>
            </div>
            <div>
                <label for="filter-category" class="label">
                    <p>Kategorie</p>                     
                </label>
                <select id="filter-category" class="input" v-model="category">
                    <option value="" selected>Vše ({{ categories.length }})</option>
                    <option v-for="category in categories" :key="category.id" :value="category.id">{{ category.name }}</option>
                </select>
            </div>
            <div>
                <label for="filter-category" class="label">
                    <p>Autor</p>                     
                </label>
                <select id="filter-category" class="input" v-model="author">
                    <option value="" selected>Vše ({{ wallet.users.length }})</option>
                    <option v-for="user in wallet.users" :key="user.id" :value="user.id">{{ user.email }}</option>
                </select>
            </div>
            <button class="button" @click="clearFilter()">Clear</button>
        </div>
        <transition-group name="fade">
            <transaction v-for="(transaction, index) in filteredTransactions" :key="index" :transaction="transaction" :categories="categories" :wallet="wallet" />
        </transition-group>
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
            dateFrom: '',
            dateTo: '',
            amountFrom: '',
            amountTo: '',
            type: '',
            category: '',
            author: ''
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
            if(this.type !== "") transactions = transactions.filter(trn => trn.transaction_type === this.type);
            if(this.category !== "") transactions = transactions.filter(trn =>  trn.category === this.category);
            if(this.author !== "") transactions = transactions.filter(trn =>  trn.user === this.author);
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
            this.type = '',
            this.category = ''
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

.fade-enter-active, .fade-leave-active {
    transition: opacity .5s;
}
.fade-enter, .fade-leave-to {
    opacity: 0;
}
</style>
