<template>
    <section class="balance-wrapper">
        <div class="balance" @click="balanceComplete = !balanceComplete" v-if="balanceComplete">
            <p class="balance-heading">Součet celkem</p>
            <p :class="{'is-positive': getCompleteBalance > 0, 'is-negative': getCompleteBalance < 0}">{{ getCompleteBalance | formatNumber | formatCurrency }}</p>
        </div>
        <div class="balance" @click="balanceComplete = !balanceComplete" v-else>
            <p class="balance-heading">Součet za období</p>
            <p :class="{'is-positive': getBalance > 0, 'is-negative': getBalance < 0}">{{ getBalance | formatNumber | formatCurrency }}</p>
        </div>
        <div class="balance">
            <p class="balance-heading">Změna</p>
            <p :class="{'is-positive': getChange > 0, 'is-negative': getChange < 0}">{{ getChange | formatNumber | formatCurrency }}</p>
        </div>
    </section>
</template>


<script>
import { filterMixin, dateMixin, balanceMixin } from '@/mixins'

export default {
    mixins: [filterMixin, dateMixin, balanceMixin],
    data() {
        return {
            balanceComplete: false
        }
    },
    computed: {
        getBalance() {
            return this.calculateBalance(this.filterTransactions(this.$store.state.transactions))
        },
        getChange() {
            return this.calculateChange(this.$store.state.transactions)
        },
        getCompleteBalance() {
            return this.calculateBalance(this.$store.state.transactions)
        }
    },
    methods: {
        calculateChange(transactions) {
            const thisPeriod = this.calculateBalance(this.filterTransactions(transactions))
            const date = this.subtractDate(this.$store.state.filter.dateFrom, this.$store.state.filter.dateTo)
            const lastPeriod = this.calculateBalance(this.filterTransactions(transactions, null, date.dateFrom, date.dateTo))
            return thisPeriod - lastPeriod
        }
    }
}
</script>


<style lang="stylus" scoped>
@import '../styles/variables'

$border-color = #D9D9D9

.balance-wrapper
    width: 100%
    max-width: 43.75em
    height: 3.5em
    padding: 10px
    display: flex
    justify-content: space-between

    font-weight: 600

    border-bottom: 1px solid $border-color

.balance
    height: calc(3.5em - 20px)
    display: flex
    flex-flow: column
    justify-content: space-between
    align-items: flex-end
    
    &:first-child
        align-items: flex-start

.balance-heading
    font-size: 0.875em
    font-weight: 400

.is-positive 
    color: $SUCCESS-COLOR

.is-negative
    color: $DANGER-COLOR

</style>
