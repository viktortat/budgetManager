<template>
    <div class="dashboard-budget">
        <h5 class="is-bold">{{ budget.name }}</h5>
        <div class="budget-amount is-bold">
            <div>{{ categoryBalance | formatCurrency }}</div>
            <div>z</div>
            <div>{{ budget.amount | formatCurrency }}</div>
        </div>
        <footer class="budget-footer">
            <div class="budget-progress" :style="{ 'backgroundColor': categories.find(x => x.id === budget.category).color, transform: 'scaleX(' + categoryPercentile + ')' }"></div>
        </footer>
    </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import moment from 'moment'

export default {
    props: ['budget', 'dateFrom', 'dateTo'],
    methods: {
        getDateTo() {
            return moment(this.dateFrom).endOf('month').format('YYYY-MM-DD')
        },
        calculateCategoryBalance() {
            let transactions = this.transactions.filter(trn => trn.date >= this.dateFrom && trn.date <= this.getDateTo() && trn.category === this.budget.category)
            let balance = 0
            for (let trn of transactions) {
                if (trn.transaction_type === "expense") {
                    balance += Number(trn.amount)
                }
            }
            return balance
        }
    },
    computed: {
        ...mapState([
            'categories',
            'transactions'
        ]),
        categoryBalance() {
            return this.calculateCategoryBalance()
        },
        categoryPercentile() {
            const onePercent = (Number(this.budget.amount)) / 100
            return ((this.calculateCategoryBalance() / onePercent) < 100 ? (this.calculateCategoryBalance() / onePercent) : 100)
        }
    }
}
</script>


<style lang="stylus" scoped>

.dashboard-budget
    position: relative
    padding: 10px
    padding-bottom: 40px
    margin-top: 10px

    & > h5
        margin-bottom: 10px

.budget-amount
    width: 100%
    display: flex
    justify-content: space-between

.budget-footer
    position: absolute
    bottom: 10px
    left: 10px
    right: 10px
    height: 20px
    padding-left: 20px
    padding-right: 20px
    display: flex
    align-items: center 
    justify-content: space-between

    & span
        padding: 2px
        background-color: rgba(255, 255, 255, 0.8)

    & > div
        z-index: 10

.budget-progress 
    position: absolute
    left: 0
    top: 0
    bottom: 0
    z-index: 5
    width: 1%
    transform: scaleX(0)
    transform-origin: left

    background-color: #FFFFFF

    transition: transform 0.4s ease-in-out

</style>