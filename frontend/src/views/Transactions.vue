<template>
    <main class="section">
        <section class="transactions">
            <app-transaction v-for="transaction in transactions" :key="transaction.id" :transaction=transaction></app-transaction>
        </section>
    </main>
</template>


<script>
import { mapState } from 'vuex'

import AppTransaction from '@/components/AppTransaction.vue'

export default {
    computed: {
        ...mapState([
            'transactions'
        ])
    },
    components: {
        AppTransaction
    }
}
</script>


<style lang="stylus" scoped>

.transactions
    display: flex
    flex-flow: column
    align-items: center

    
</style>
