<template>
    <main class="section">
        <section class="budget-detail-wrapper">
            <div class="budget-detail-form">
                <div class="budget-detail-form-item">
                    <app-label class="label" for="budget-name">Jméno</app-label>
                    <app-input v-model="budget.name" class="input" id="budget-name" type="text" />
                </div>
                <div class="budget-detail-form-item">
                    <app-label class="label" for="budget-color">Velikost</app-label>
                    <app-input v-model="budget.amount" class="input" id="budget-color" type="number" />
                </div>
                <div class="budget-detail-form-item">
                    <app-label class="label" for="budget-categories">Kategorie</app-label>
                    <app-select :multiple="true" :empty="false" v-model="budget.categories" class="input">
                        <option v-for="category in categories" :value="category.id" :key="category.id">{{ category.name }}</option>
                    </app-select>
                </div>
                <app-button class="button is-success" @click="createOrUpdateBudget" >
                    <span v-if="isNew">Přidat</span>
                    <span v-else>Upravit</span>
                </app-button>
            </div>
        </section>
    </main>
</template>

<script>
import { mapActions, mapState } from 'vuex'

import AppDateInput from '@/components/AppDateInput.vue'
import AppButton from '@/components/AppButton.vue'
import AppInput from '@/components/AppInput.vue'
import AppLabel from '@/components/AppLabel.vue'
import AppSelect from '@/components/AppSelect.vue'

export default {
  data () {
    return {
      budget: {
        name: '',
        categories: [],
        amount: ''
      },
      isNew: false
    }
  },
  computed: {
    ...mapState([
      'categories',
      'token',
      'wallet',
      'budgets'
    ])
  },
  methods: {
    ...mapActions([
      'loadData',
      'refreshData'
    ]),
    createOrUpdateBudget () {
      const data = {
        name: this.budget.name,
        amount: this.budget.amount,
        categories: this.budget.categories
      }
      if (this.isNew) {
        const url = '/budgets/'
        this.$axios.post(url, data, { headers: { Authorization: 'JWT ' + this.token }}).then(response => {
          this.resetBudget()
          this.refreshData()
        })
      } else {
        const url = '/budgets/' + this.budget.id + '/'
        this.$axios.patch(url, data, { headers: { Authorization: 'JWT ' + this.token }}).then(response => {
          this.refreshData()
        })
      }
    },
    resetBudget () {
      this.budget.name = ''
      this.budget.amount = ''
      this.budget.categories = []
    }
  },
  components: {
    AppInput,
    AppLabel,
    AppSelect,
    AppButton
  },
  created () {
    this.loadData()
    const budgetID = this.$route.params.id
    if (!budgetID) this.isNew = true
    else if (Number(budgetID)) {
      const budget = this.budgets.find(x => x.id == budgetID)
      this.budget = Object.assign({}, budget)
    } else this.$router.push('/')
  }
}
</script>

<style lang="stylus" scoped>

.budget-detail-wrapper
    @media screen and (min-width: 768px)
        font-size: 20px

    display: flex
    flex-flow: column
    justify-content: center
    align-items: center
    width: 100%
    height: 100%
    padding-top: 20px

    & .button
        align-self: flex-end

.budget-detail-form
    display: flex
    flex-flow: column

.budget-detail-form-item
    margin-bottom: 20px

</style>
