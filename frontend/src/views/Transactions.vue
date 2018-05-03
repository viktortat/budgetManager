<template>
    <main class="section">
        <transactions-date></transactions-date>
        <section class="transactions">
            <app-transaction v-for="transaction in transactions" :key="transaction.id" :transaction=transaction></app-transaction>
        </section>
    </main>
</template>


<script>
import { mapState } from 'vuex'

import AppTransaction from '@/components/AppTransaction.vue'
import TransactionsDate from '@/components/TransactionsDate.vue'

import { filterMixin } from '@/mixins'

export default {
    mixins: [filterMixin],
    computed: {
        transactions() {
            let transactions = this.$store.state.transactions
            return transactions.sort((a, b) => new Date(b.date) - new Date(a.date))
        }
    },
    components: {
        AppTransaction,
        TransactionsDate
    }
}
</script>


<style lang="stylus" scoped>

.transactions
    display: flex
    flex-flow: column
    align-items: center

    
</style>
