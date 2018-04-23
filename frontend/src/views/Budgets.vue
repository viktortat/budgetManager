<template>
    <section class="section budgets-wrapper">
        <div class="budgets">
            <div class="budget budget-create">
                <input type="text" class="input input-100" placeholder="Jméno rozpočtu" v-model="name">
                <input type="number" class="input input-100" placeholder="Velikost rozpočtu" v-model="amount">
                <select type="text" class="input input-100" placeholder="Kategorie" v-model="category">
                    <option value="" selected></option>
                    <option v-for="category in categories" :key="category.id" :value="category.id">{{ category.name }}</option>
                </select>
                <button class="button is-100 is-success" @click="createBudget()">Přidat</button>
            </div>
            <budget v-for="budget in budgets" :key="budget.id" :budget="budget" />
        </div>
    </section>
</template>


<script>
import Budget from '@/components/Budget.vue'
import { mapState, mapActions } from 'vuex'
import axios from 'axios'

export default {
    data() {
        return {
            name: "",
            amount: "",
            category: ""
        }
    },
    methods: {
        ...mapActions([
            'loadData',
            'refreshData'
        ]),
        createBudget() {
            const data = {
                'name': this.name,
                'amount': this.amount,
                'category': this.category
            }
            const url = '/api/budgets/'
            axios.post(url, data, { headers: { Authorization: 'JWT ' + this.$store.state.token }}).then(res => {
                this.refreshData()
                this.$notify({
                    text: 'Rozpočet byl vytvořen.',
                    type: 'success'
                });
            }).catch(error => {
                this.$notify({
                    text: 'Vyskytl se problém, zkuste to prosím později.',
                    type: 'error'
                });                
            })
        }
    },
    computed: {
        ...mapState([
            'categories',
            'budgets'
        ])
    },
    components: {
        Budget
    },
    created() {
        this.loadData()
    }
}
</script>


<style lang="stylus" scoped>
@import "../styles/variables.styl"

.budgets-wrapper
    min-height: 100vh

    background-color: $background-color-primary

.budgets
    position: relative
    display: grid
    grid-template-columns: repeat(auto-fit, 300px)
    grid-gap: 10px
    justify-content: center
    margin-left: 10px
    margin-top: 10px
    margin-bottom: 10px
    margin-right: 10px

.budget
    position: relative
    height: 250px
    padding-left: 20px
    padding-right: 20px
    padding-top: 20px
    padding-bottom: 20px
    display: flex
    flex-flow: column
    justify-content: space-between

    border-radius: $border-radius
    background-color: #FFFFFF

</style>
