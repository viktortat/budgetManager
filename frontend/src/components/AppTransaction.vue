<template>
    <div class="transaction">
        <aside class="transaction-category-bar" :style="{ backgroundColor: this.categories.find(x => x.id === transaction.category).color }"></aside>
        <div class="transaction-left">
            <div class="transaction-small-text">{{ transaction.date }}</div>
            <div class="transaction-big-text">{{ this.categories.find(x => x.id === transaction.category).name | shortenString(12) }}</div>
            <div class="transaction-small-text">{{ transaction.notes | shortenString(12) }}</div>
        </div>
        <div class="transaction-options" key="option" v-if="options">
            <app-button class="button transaction-option is-danger" key="1" @click="deleteTransaction(transaction.id)"><icon name="trash" /></app-button>
            <app-button class="button transaction-option" key="2" @click="goToDetail(transaction.id)"><icon name="pencil-alt" /></app-button>
            <app-button class="button transaction-option is-warning" key="3"  @click="options = false"><icon name="times" /></app-button>
        </div>
        <div class="transaction-right" key="price" v-else @click="options = true">{{ transaction.amount | formatCurrency }}</div>
    </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

import AppButton from '@/components/AppButton.vue'

export default {
    props: {
        transaction: {
            type: Object
        }
    },
    data() {
        return {
            options: false,
            checked: false
        }
    },
    computed: {
        ...mapState([
            'categories',
            'token'
        ])
    },
    methods: {
        ...mapActions([
            'refreshData'
        ]),
        goToDetail(id) {
            this.$router.push({ 'name': 'TransactionsDetail', params: { 'id': id } })
        },
        deleteTransaction(id) {
            const index = this.$store.state.transactions.indexOf(this.transaction)
            const url = '/transactions/' + id + '/'
            this.$axios.delete(url, { headers: { Authorization: 'JWT ' + this.token }}).then(response => {
                this.$store.commit('deleteTransaction', index)
                // this.refreshData()
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

$height = 56px
$padding-top-bottom = 5px

.transaction
    position: relative
    width: 100%
    max-width: 700px
    height: $height
    padding-left: 13px
    padding-right: 10px
    padding-top: $padding-top-bottom 
    padding-bottom: $padding-top-bottom
    margin-top: 5px
    margin-bottom: 5px
    display: flex
    justify-content: space-between
    align-items: center

.transaction-category-bar
    position: absolute
    width: 3px
    height: calc(100% - 10px)
    top: 5px
    left: 0

.transaction-right, .transaction-options, .transaction-left
    height: $height - $padding-top-bottom * 2 
    width: 50%
    display: flex
    justify-content: flex-end
    align-items: center

.transaction-left
    flex-flow: column
    justify-content: space-between
    align-items: unset

.transaction-small-text
    font-size: 12px
    font-weight: 400

.transaction-big-text
    font-size: 14px
    font-weight: 500

.transaction-options
    width: 140px
    display: flex
    justify-content: space-around
    align-items: center

.transaction-option
    width: 30px
    height: 30px
    display: flex
    justify-content: center
    align-items: center

    color: #FFFFFF
    border-radius: 50%

</style>