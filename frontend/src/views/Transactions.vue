<template>
    <main class="section">
        <transactions-date></transactions-date>
        <section class="transactions">
            <app-transaction v-for="transaction in transactions" :key="transaction.id" :transaction=transaction></app-transaction>
        </section>
    </main>
</template>


<script>
import AppTransaction from '@/components/AppTransaction.vue'
import TransactionsDate from '@/components/TransactionsDate.vue'

import { filterMixin, sortMixin } from '@/mixins'

export default {
    mixins: [filterMixin, sortMixin],
    data() {
        return {
            sortBy: '',
            descend: false
        }
    },
    methods: {
        processTransactions() {
            let transactions = this.filterTransactions(this.$store.state.transactions)
            return this.sortTransactions(transactions, this.sortBy, this.descend)
        }
    },
    computed: {
        transactions() {
            return this.processTransactions()
        }
    },
    components: {
        AppTransaction,
        TransactionsDate
    }
}
</script>


<style lang="stylus" scoped>

.section    
    @media screen and (min-width: 768px)
        font-size: 20px

    padding-top: calc(2em + 56px)

.transactions
    display: flex
    flex-flow: column
    align-items: center

    
</style>
