<template>
    <section class="section transactions-wrapper">
        <div class="show-filter" v-if="filtersHidden && showFilterButton" @click="filtersHidden = !filtersHidden">
            Ukázat filtry
        </div>
        <div class="filters" v-else>
            <div class="filter">
                <label for="filter-date-from" class="label">
                    <p>Datum od:</p>
                </label>
                <flat-pickr v-model="dateFrom" class="input input-100"></flat-pickr>
            </div>
            <div class="filter">
                <label for="filter-date-to" class="label">
                    <p>Datum do:</p>
                </label>
                <flat-pickr v-model="dateTo" class="input input-100"></flat-pickr>
            </div>
            <div class="filter">
                <label for="filter-amount-from" class="label">
                    <p>Částka od:</p>
                </label>
                <input type="number" class="input input-100" id="filter-amount-from" v-model="amountFrom"> 
            </div>
            <div class="filter">
                <label for="filter-amount-to" class="label">
                    <p>Částka do:</p>
                </label>
                <input type="number" class="input input-100" id="filter-amount-to" v-model="amountTo">
            </div>
            <div class="filter">
                <label for="filter-transaction-type" class="label">
                    <p>Typ transakce</p>                     
                </label>
                <select id="filter-transaction-type" class="input input-100" v-model="type">
                    <option value="" selected>Příjem a Výdej</option>
                    <option value="income">Příjem</option>
                    <option value="expense">Výdej</option>
                </select>
            </div>
            <div class="filter">
                <label for="filter-category" class="label">
                    <p>Kategorie</p>                     
                </label>
                <select id="filter-category" class="input input-100" v-model="category">
                    <option value="" selected>Vše ({{ categories.length }})</option>
                    <option v-for="category in categories" :key="category.id" :value="category.id">{{ category.name }}</option>
                </select>
            </div>
            <div class="filter">
                <label for="filter-category" class="label">
                    <p>Autor</p>                     
                </label>
                <select id="filter-category" class="input input-100" v-model="author">
                    <option value="" selected>Vše ({{ wallet.users.length }})</option>
                    <option v-for="user in wallet.users" :key="user.id" :value="user.id">{{ user.email }}</option>
                </select>
            </div>
            <footer class="filters-footer">
                <app-button class="button" @click="filtersHidden = !filtersHidden" v-if="showFilterButton">Zavřít</app-button>
                <div v-else></div>
                <app-button class="button is-danger" @click="clearFilter()">Reset filtru</app-button>
            </footer>
        </div>
        <transition-group name="fade">
            <transaction v-for="(transaction, index) in filteredTransactions" :key="index" :transaction="transaction" :categories="categories" :wallet="wallet" />
        </transition-group>
    </section>
</template>

<script>
import { mapState, mapActions } from 'vuex'

import flatPickr from 'vue-flatpickr-component'
import 'flatpickr/dist/flatpickr.css'

import AppButton from '@/components/AppButton.vue'
import Transaction from '@/components/TransactionExtended.vue'

export default {
    data() {
        return {
            dateFrom: '',
            dateTo: '',
            amountFrom: '',
            amountTo: '',
            type: '',
            category: '',
            author: '',
            filtersHidden: true,
            showFilterButton: true
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
            this.dateFrom = ""
            this.dateTo = ""
            this.amountFrom = ""
            this.amountTo = ""
            this.type = ''
            this.category = ''
            this.author = ''
        }
    },
    components: {
        Transaction,
        flatPickr,
        AppButton
    },
    created() {
        this.loadData();
        if (window.innerWidth > 768) {
            this.filtersHidden = false
            this.showFilterButton = false
        }
    }
}
</script>

<style lang="stylus" scoped>
@import "../styles/variables.styl"

.transactions-wrapper
    @media screen and (max-width: 767px)
        min-height: 100vh
        
    min-height: 100.06vh

    background-color: $BACKGROUND-COLOR-PRIMARY

.show-filter
    display: flex
    justify-content: center
    align-items: center
    margin: 10px
    height: 50px

    background-color: #FFFFFF
    border-radius: $BORDER-RADIUS

.filters        
    position: relative
    display: grid
    grid-template-columns: repeat(auto-fit, minmax(260px, 1fr))
    grid-gap: 10px
    padding-left: 20px
    padding-right: 20px
    padding-top: 20px
    padding-bottom: 75px
    margin-left: 10px
    margin-top: 10px
    margin-bottom: 10px
    margin-right: 10px

    background-color: #FFFFFF
    border-radius: $BORDER-RADIUS

.filters-footer
    position: absolute
    bottom: 0
    left: 0
    width: 100%
    padding: 20px
    display: flex
    justify-content: space-between
    align-items: center

.fade-enter-active, .fade-leave-active
    transition: opacity 0.5s

.fade-enter, .fade-leave-to
    opacity: 0

</style>
