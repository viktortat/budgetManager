<template>
    <div class="category">
        <aside class="category-color" :style="{ backgroundColor: category.color }"></aside>
        <div class="category-left">
            <p class="category-text-big">{{ category.name | shortenString(14) }}</p>
            <p class="category-text-small">Transakcí celkem: {{ category.transactions.length }}</p>
        </div>
        <div class="category-options" key="option" v-if="options">
            <app-button class="button category-option is-danger" key="1" @click="confirmDeleting(category.id)"><icon name="trash" /></app-button>
            <app-button class="button category-option" key="2" @click="goToDetail(category.id)"><icon name="pencil-alt" /></app-button>
            <app-button class="button category-option is-warning" key="3"  @click="options = false"><icon name="times" /></app-button>
        </div>
        <div class="category-right" key="info" v-else @click="options = true" >
            <p class="category-text-big" :class="{'is-positive': categoryBalance > 0, 'is-negative': categoryBalance < 0}">{{ categoryBalance | formatNumber | formatCurrency }}</p>
            <p class="category-text-small">Transakcí za období: {{ categoryTransactionsAmount }}</p>
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
        category: {
            type: Object
        }
    },
    data() {
        return {
            options: false
        }
    },
    computed: {
        ...mapState([
            'token'
        ]),
        categoryBalance() {
            return this.calculateBalance(this.getTransactions())
        },
        categoryTransactionsAmount() {
            return this.getTransactions().length
        }
    },
    methods: {
        ...mapActions([
            'refreshData'
        ]),
        getTransactions() {
            let trns = this.filterTransactionsByDate(this.$store.state.transactions)
            return this.filterTransactionsByCategory(trns, this.category.id)
        },
        goToDetail(id) {
            this.$router.push({ 'name': 'CategoriesDetail', params: {'id': id} })
        },
        confirmDeleting(id) {
            const params = {
                title: 'Smazání kategorie',
                message: 'Tato akce nenávratně smaže kategorii a všechny její transakce. Přejete si pokračovat?', 
                showConfirmButton: true,
                onConfirm: () => {
                    return this.deleteCategory(id)
                }
            }
            this.$modal.show(params)
        },
        deleteCategory(id) {
            const url = '/categories/' + id + '/'
            this.$axios.delete(url, { headers: { Authorization: 'JWT ' + this.token }}).then(response => {
                this.refreshData()
            })
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
$padding-top-bottom = 0.625em
$border-color = #D9D9D9

.category
    @media screen and (min-width: 768px)
        font-size: 20px

    position: relative
    width: 100%
    max-width: 43.750em
    height: $height
    padding-left: 13px
    padding-right: 10px
    padding-top: $padding-top-bottom 
    padding-bottom: $padding-top-bottom
    display: flex
    justify-content: space-between
    align-items: center

    border-bottom: 1px solid $border-color

.category-color
    position: absolute
    width: 3px
    height: calc(100% - 10px)
    top: 5px
    left: 0

.category-left, .category-right
    height: $height - $padding-top-bottom * 2 
    width: 50%
    display: flex
    flex-flow: column
    justify-content: space-between
    align-items: flex-start

.category-right
    align-items: flex-end

.category-text-big
    font-size: 0.875em
    font-weight: 600

.category-text-small
    font-size: 0.75em
    font-weight: 400

.category-options
    width: 8.750em
    display: flex
    justify-content: space-around
    align-items: center

.category-option
    width: 1.875em
    height: 1.875em
    display: flex
    justify-content: center
    align-items: center

    color: #FFFFFF
    border-radius: 50%

.is-positive 
    color: $SUCCESS-COLOR

.is-negative
    color: $DANGER-COLOR

</style>
