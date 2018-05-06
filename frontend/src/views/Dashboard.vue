<template>
    <main class="section">
        <app-date-slider />
        <section class="dashboard">
            <app-balance />
            <div class="graph">
                <vue-chartist :data="balanceDataset" :options="{fullWidth: true, chartPadding: 20}" type='Line' :ratio="'ct-golden-section'" />
            </div>
            <dashboard-income-and-expense />
            <div class="graph">
                <vue-chartist :data="categoriesDataset" :options="{fullWidth: true, chartPadding: 20}" type='Pie' :ratio="'ct-perfect-fifth'" />
            </div>
        </section>
    </main>
</template>


<script>
import { mapActions, mapState } from 'vuex'

import AppDateSlider from '@/components/AppDateSlider.vue'
import AppBalance from '@/components/AppBalance.vue'
import DashboardIncomeAndExpense from '@/components/DashboardIncomeAndExpense.vue'
import VueChartist from '@/components/VueChartist.vue'

import { filterMixin, dateMixin, balanceMixin } from '@/mixins'

export default {
    mixins: [filterMixin, dateMixin, balanceMixin],
    computed: {
        ...mapState([
            'transactions',
            'categories',
            'budgets',
            'filter'
        ]),
        balanceDataset() {
            let data = {
                series: [
                    []
                ],
                labels: []
            }

            let dateFrom = this.filter.dateFrom
            let dateTo = this.filter.dateTo

            for(var i = 0; i < 6; i++) {
                let transactions = this.filterTransactionsByDate(this.transactions, dateFrom, dateTo)
                data.series[0].unshift(this.calculateBalance(transactions))

                if(this.isMonth(dateFrom, dateTo)) data.labels.unshift(this.$moment(dateFrom).format('MMMM'))
                else if(this.isYear(dateFrom, dateTo)) data.labels.unshift(this.$moment(dateFrom).format('YYYY'))

                let dateObj = this.subtractDate(dateFrom, dateTo)
                dateFrom = dateObj.dateFrom
                dateTo = dateObj.dateTo
            }
            return data
        },
        categoriesDataset() {
            let data = {
                series: [],
                labels: []
            }

            let transactions = this.filterTransactionsByDate(this.transactions, this.filter.dateFrom, this.filter.dateTo)
            let categories = this.categories.slice()
            const expenses = this.calculateExpenses(transactions)
            for (let cat of categories) {
                let balance = 0
                for (let i = 0; i < cat.transactions.length; i++) {
                    let trn = transactions.find(x => x.id === cat.transactions[i])
                    if(trn) {
                        if (trn.transaction_type === "expense") {
                            balance += Number(trn.amount)
                        }
                    }
                }
                data.series.push(balance)
                data.labels.push(cat.name)
            }
            return data
        }
    },
    methods: {
        ...mapActions([
            'loadData'
        ])
    },
    components: {
        AppDateSlider,
        AppBalance,
        DashboardIncomeAndExpense,
        VueChartist
    },
    created() {
        this.loadData()
    }
}
</script>


<style lang="stylus" scoped>

.section    
    @media screen and (min-width: 768px)
        font-size: 20px

    padding-top: calc(2em + 56px)

.dashboard
    display: flex
    flex-flow: column
    align-items: center

.graph
    width: 100%
    max-width: 43.75em
</style>
