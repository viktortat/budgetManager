<template>
    <main class="section">
        <app-date-slider/>
        <section class="budgets">
            <div class="create-budget" @click="createBudget">
                <p>Nový rozpočet</p>
            </div>
            <budgets-budget v-for="budget in budgets" :budget="budget" :key="budget.id" />
        </section>
    </main>
</template>

<script>
import { mapState } from 'vuex'

import BudgetsBudget from '@/components/BudgetsBudget.vue'
import AppDateSlider from '@/components/AppDateSlider.vue'

export default {
  computed: {
    ...mapState([
      'budgets'
    ])
  },
  methods: {
    createBudget () {
      this.$router.push({name: 'BudgetsNew'})
    }
  },
  components: {
    BudgetsBudget,
    AppDateSlider
  }
}
</script>

<style lang="stylus" scoped>

$padding-top-bottom = 1em
$border-color = #D9D9D9

.section
    @media screen and (min-width: 768px)
        font-size: 20px

    padding-top: calc(2em + 56px)

.budgets
    display: flex
    flex-flow: column
    align-items: center

.create-budget
    @media screen and (min-width: 768px)
        cursor: pointer

    display: flex
    align-items: center
    justify-content: center
    width: 100%
    max-width: 43.750em
    padding-top: $padding-top-bottom
    padding-bottom: $padding-top-bottom

    border-bottom: 1px solid $border-color

    &:hover
        @media screen and (min-width: 768px)
            background-color: $border-color
</style>
