<template>
    <div class="section">
        <h1>Transakce</h1>
        <transaction v-for="(transaction, index) in transactions" :key="index" :transaction="transaction" :categories="categories" />
    </div>
</template>

<script>
import Transaction from '@/components/Transaction.vue'
import { mapState } from 'vuex'

export default {
    data() {
        return {

        }
    },
    computed: {
        ...mapState([
            'transactions',
            'categories'
        ]),
    },
    components: {
        Transaction
    }
}
</script>

<style lang="stylus" scoped>
@import "../styles/variables.styl"


</style>
