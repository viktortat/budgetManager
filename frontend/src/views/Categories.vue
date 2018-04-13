<template>
    <section class="section categories-wrapper">
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
            <category v-for="category in categories" :key="category.id" :category='category'></category>
        </div>
    </section>
</template>

<script>
import axios from 'axios'
import { mapState, mapActions } from 'vuex'
import Category from '@/components/Category.vue'

export default {
    data() {
        return {
            categoryName: '',
            categoryColor: ''
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
                    this.$notify({
                        text: 'Kategorie byla vytvořena.',
                        type: 'success'
                    });
                }).catch(err => {
                    this.$notify({
                        text: 'Vyskytl se problém, zkuste to prosím později.',
                        type: 'error'
                    });
                })
                this.categoryName = ""
                this.categoryColor = ""
            }
        }
    },
    components: {
        Category
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
    position: relative
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
    overflow: hidden

    cursor: pointer

.category-create
    cursor: unset
    align-items: center
    
    & .button
        width: 100%

</style>
