<template>
    <div class="budget">
        <p class="budget-name budget-text-big">{{ budget.name }}</p>
        <p class="budget-amount">
            <span class="budget-text-big">{{ budgetBalance | formatNumber | formatCurrency }}</span><span class="budget-text-small"> z {{ budget.amount | formatNumber | formatCurrency }}</span>
        </p>
        <div class="budget-bar">
            <div class="budget-bar-progress" :style="{ transform: 'scaleX(' + budgetPercentsCapped + ')' }" :class="{'is-full': budgetPercents > 1}"></div>
            <div class="budget-bar-percents budget-text-small">{{ budgetPercents | formatNumber | formatPercents }}</div>
        </div>
        <div class="budget-bar-info budget-text-small">
            <p>{{ $moment(filter.dateFrom).startOf('month').format('DD.MM.YYYY') }}</p>
            <p>{{ $moment(filter.dateFrom).endOf('month').format('DD.MM.YYYY') }}</p>
        </div>

        <div class="budget-options" key="option" v-if="options">
            <app-button class="button budget-option is-danger" key="1" @click="deleteBudget(budget.id)"><icon name="trash" /></app-button>
            <app-button class="button budget-option" key="2" @click="goToDetail(budget.id)"><icon name="pencil-alt" /></app-button>
            <app-button class="button budget-option is-warning" key="3"  @click="options = false"><icon name="times" /></app-button>
        </div>
        <div class="budget-options-button" v-else @click="options = true">
            <icon name="ellipsis-v" />
        </div>
    </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import { filterMixin, balanceMixin } from '@/mixins'

import AppButton from '@/components/AppButton.vue'

export default {
  mixins: [filterMixin, balanceMixin],
  props: {
    budget: {
      type: Object
    }
  },
  data () {
    return {
      options: false
    }
  },
  computed: {
    ...mapState([
      'budgets',
      'filter',
      'categories',
      'transactions',
      'token'
    ]),
    budgetBalance () {
      return this.calculateExpenses(this.getTransactions())
    },
    budgetPercents () {
      return this.budgetBalance / this.budget.amount
    },
    budgetPercentsCapped () {
      const val = this.budgetBalance / this.budget.amount
      return val > 1 ? 1 : val
    }
  },
  methods: {
    ...mapActions([
      'refreshData'
    ]),
    getTransactions () {
      const trns = this.filterTransactionsByDate(this.$store.state.transactions)
      let finalTrns = []
      for (let category of this.budget.categories) {
        finalTrns = finalTrns.concat(this.filterTransactionsByCategory(trns, category))
      }
      return finalTrns
    },
    deleteBudget (id) {
      const index = this.$store.state.budgets.indexOf(this.budget)
      const url = '/budgets/' + id + '/'
      this.$axios.delete(url, { headers: { Authorization: 'JWT ' + this.token }}).then(response => {
        this.refreshData()
      })
    },
    goToDetail (id) {
      this.$router.push({ 'name': 'BudgetsDetail', params: { 'id': id } })
    }
  },
  components: {
    AppButton
  }
}
</script>

<style lang="stylus" scoped>
@import '../styles/variables'

$height = 3.5em
$padding-top-bottom = 1em
$border-color = #D9D9D9

.budget
    @media screen and (min-width: 768px)
        font-size: 20px

    position: relative
    width: 100%
    max-width: 43.750em
    padding-left: 10px
    padding-right: 10px
    padding-top: $padding-top-bottom
    padding-bottom: $padding-top-bottom

    border-bottom: 1px solid $border-color

.budget-name
    margin-bottom: 0.5em

.budget-amount
    margin-bottom: 1em

.budget-bar-info
    display: flex
    justify-content: space-between
    align-items: center

.budget-text-big
    font-size: 0.875em
    font-weight: 600

.budget-text-small
    font-size: 0.75em

.budget-bar
    position: relative
    width: 100%
    height: 1.25em
    margin-bottom: 0.5em

    background-color: $border-color

.budget-bar-progress
    position: absolute
    left: 0
    top: 0
    bottom: 0
    width: 100%

    transform: scaleX(0.5)
    transform-origin: left

    background-color: $SUCCESS-COLOR

.is-full
    background-color: $DANGER-COLOR

.budget-bar-percents
    position: absolute
    top: 50%
    left: 1em
    transform: translateY(-50%)

    font-weight: 600

    color: $FONT-COLOR-LIGHT

.budget-options-button
    @media screen and (min-width: 768px)
        cursor: pointer

    position: absolute
    top: 1em
    right: 1em
    width: 2em
    height: 2em
    display: flex
    justify-content: center
    align-items: center

.budget-options
    position: absolute
    top: 1em
    right: 1em
    width: 8.75em
    display: flex
    justify-content: space-around
    align-items: center

.budget-option
    width: 1.875em
    height: 1.875em
    display: flex
    justify-content: center
    align-items: center

    color: #FFFFFF
    border-radius: 50%

</style>
