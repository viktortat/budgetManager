<template>
    <div class="section categories-wrapper">
        <div class="categories">
            <div class="category category-create">
                <p>
                    <label for="category-name" class="label">
                        <p>Jméno kategorie</p>
                    </label>
                    <input type="text" id="category-name" class="input input-100" v-model="categoryName">
                </p>
                <p>
                    <label for="category-color" class="label">
                        <p>Barva kategorie</p>
                    </label>
                    <input type="text" id="category-color" class="input input-100" v-model="categoryColor">
                </p>
                <button class="button is-success" @click.prevent="createCategory()">Přidat kategorii</button>
            </div>
            <div class="category" v-for="category in categories" :key="category.id">
                <h3 class="is-bold">{{ category.name }}</h3>
                <p>Transakcí: {{ category.transactions.length }}</p>
                <p class="is-bold" :class="{'is-success': Number(category.balance) > 0, 'is-danger': Number(category.balance) < 0 }">{{ category.balance | formatCurrency }}</p>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

import { mapState, mapActions } from 'vuex';

export default {
    data() {
        return {
            categoryName: "",
            categoryColor: ""
        }
    },
    computed: {
        ...mapState([
            'wallet',
            'transactions',
            'categories'
        ]),
    },
    methods: {
        ...mapActions([
            'loadData'
        ]),
        createCategory() {
            if(this.categoryName && this.categoryColor) {  
                const url = "/api/categories/"              
                const data = {
                    "name": this.categoryName,
                    "color": this.categoryColor,
                    "wallet": this.wallet.id
                }
                axios.post(url, data, { headers: { Authorization: 'JWT ' + this.$store.state.token }}).then(res => {
                    this.categories.push(res.data)
                }).catch(err => {

                })
                this.categoryName = ""
                this.categoryColor = ""
            }
        }
    },
    created() {
        this.loadData();
    }
}
</script>

<style lang="stylus" scoped>
@import "../styles/variables.styl"

.categories-wrapper
    min-height: 100.06vh

    background-color: $background-color-primary

.categories
    position: relative
    display: grid
    grid-template-columns: repeat(auto-fit, 260px)
    grid-gap: 10px
    justify-content: center
    margin-left: 10px
    margin-top: 10px
    margin-bottom: 10px
    margin-right: 10px

.category
    height: 260px
    padding-left: 20px
    padding-right: 20px
    padding-top: 20px
    padding-bottom: 20px
    display: flex
    flex-flow: column
    justify-content: space-between

    border-radius: $border-radius
    background-color: #FFFFFF

    cursor: pointer

    &:hover
        background-color: #F2F2F2

.category-create
    cursor: unset
    justify-content: center
    align-items: center

    &:hover
        background-color: #FFFFFF

    & input
        margin-bottom: 20px
    
    & .button
        width: 100%

</style>
