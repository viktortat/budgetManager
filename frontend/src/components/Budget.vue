<template>
    <div class="budget" v-if="!editMode" @click="editMode = !editMode">
        <h3 class="is-bold">{{ budget.name }}</h3>
        <p>{{ this.categories.find(x => x.id === budget.category).name }}</p>
        <div class="budget-amount is-bold">
            <div>{{ categoryBalance | formatCurrency }}</div>
            <div>z</div>
            <div>{{ budget.amount | formatCurrency }}</div>
        </div>
        <footer class="budget-footer">
            <div class="budget-progress" :style="{ 'backgroundColor': this.categories.find(x => x.id === budget.category).color, width: categoryPercentile+'%' }"></div>
        </footer>
    </div>
    <div class="budget" v-else-if="!menuMode">
        <button class="button is-100" @click="close(false, false, false)">Zavřít</button>
        <button class="button is-success is-100" @click="menuMode = !menuMode">Upravit</button>
        <div>
            <transition name="move" mode="out-in">
                <button :key="1" class="button is-danger is-100" @click="deleteCheck = !deleteCheck" v-if="!deleteCheck">Smazat</button>
                <button :key="2" class="button is-danger is-100" @click="deleteBudget()" v-else >Opravdu?</button>
            </transition>
        </div>
    </div>
    <div class="budget" v-else>
        <input type="text" class="input input-100" v-model="name" placeholder="Jméno">
        <input type="text" class="input input-100" v-model="amount" placeholder="Částka">
        <select type="text" class="input input-100" v-model="category" placeholder="Kategorie"> 
            <option v-for="cat in categories" :key="cat.id" :value="cat.id">{{ cat.name }}</option>
        </select>
        <div class="budget-edit">
            <button class="button" @click="close(false, false, false)">Zavřít</button>
            <button class="button is-success" @click="editBudget()">Uložit</button>
        </div>
    </div>
</template>


<script>
import axios from 'axios'
import moment from 'moment'
import { mapActions, mapState } from 'vuex'

export default {
    props: ["budget"],
    data() {
        return {
            dateTo: moment().endOf('month').format('YYYY-MM-DD'), 
            dateFrom: moment().startOf('month').format('YYYY-MM-DD'),
            editMode: false,
            menuMode: false,
            deleteCheck: false,
            name: '',
            amount: '',
            category: ''
        }
    },
    methods: {
        ...mapActions([
            'refreshData'
        ]),
        close(editMode, menuMode, deleteCheck) {
            this.editMode = editMode
            this.menuMode = menuMode
            this.deleteCheck = deleteCheck
            this.name = this.budget.name
            this.amount = this.budget.amount
            this.category = this.budget.category
        },
        deleteBudget() {
            const url = '/api/budgets/' + this.budget.id + "/"
            axios.delete(url, { headers: { Authorization: 'JWT ' + this.$store.state.token }}).then(res => {
                this.refreshData()
                this.$notify({
                    text: 'Rozpočet byl smazán.',
                    type: 'success'
                });
            }).catch(error => {
                this.$notify({
                    text: 'Vyskytl se problém, zkuste to prosím později.',
                    type: 'error'
                });
            })
        },
        editBudget() {
            const data = {
                'name': this.name,
                'amount': this.amount,
                'category': this.category
            }
            const url = '/api/budgets/' + this.budget.id + "/"
            axios.patch(url, data, { headers: { Authorization: 'JWT ' + this.$store.state.token }}).then(res => {
                this.refreshData()
                this.$notify({
                    text: 'Rozpočet byl smazán.',
                    type: 'success'
                })
                this.close(false, false, false)
            }).catch(error => {
                this.$notify({
                    text: 'Vyskytl se problém, zkuste to prosím později.',
                    type: 'error'
                })
            })
        },
        calculateCategoryBalance() {
            let transactions = this.transactions.filter(trn => trn.date >= this.dateFrom && trn.date <= this.dateTo && trn.category === this.budget.category)
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
            "categories",
            "transactions"
        ]),
        categoryBalance() {
            return this.calculateCategoryBalance()
        },
        categoryPercentile() {
            const onePercent = (Number(this.budget.amount)) / 100
            return ((this.calculateCategoryBalance() / onePercent) < 100 ? (this.calculateCategoryBalance() / onePercent) : 100)
        }
    },
    created() {
        this.name = this.budget.name
        this.amount = this.budget.amount
        this.category = this.budget.category
    }
}
</script>


<style lang="stylus" scoped>
@import "../styles/variables.styl"

.budget-edit
    width: 100%
    display: flex
    justify-content: space-between

    & > .button
        border-radius: 0

        &:first-child
            border-radius: $border-radius 0 0 $border-radius
        
        &:last-child
            border-radius: 0 $border-radius $border-radius 0

.budget-footer
    position: absolute
    bottom: 0
    left: 0
    width: 100%
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

.budget-amount
    width: 100%
    display: flex
    justify-content: space-between

.budget-progress 
    position: absolute
    left: 0
    top: 0
    bottom: 0
    width: 0%
    z-index: 5

    background-color: #FFFFFF

</style>
