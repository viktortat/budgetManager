<template>
    <section class="balance-wrapper">
        <div class="balance">
            <p class="balance-heading">Příjmy</p>
            <p :class="{'is-positive': getIncome > 0, 'is-negative': getIncome < 0}">{{ getIncome | formatNumber | formatCurrency }}</p>
        </div>
        <div class="balance">
            <p class="balance-heading">Výdaje</p>
            <p :class="{'is-positive': getExpense > 0, 'is-negative': getExpense < 0}">{{ getExpense | formatNumber | formatCurrency }}</p>
        </div>
    </section>
</template>

<script>
import { filterMixin, balanceMixin } from "@/mixins";

export default {
  mixins: [filterMixin, balanceMixin],
  computed: {
    getExpense() {
      const trns = this.filterTransactionsByDate(
        this.filterTransactionsByType(this.$store.state.transactions, "expense")
      );
      return this.calculateBalance(trns);
    },
    getIncome() {
      const trns = this.filterTransactionsByDate(
        this.filterTransactionsByType(this.$store.state.transactions, "income")
      );
      return this.calculateBalance(trns);
    }
  }
};
</script>

<style lang="stylus" scoped>
@import '../styles/variables'

$border-color = #D9D9D9

.balance-wrapper
    width: 100%
    max-width: 43.750em
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
