<template>
    <div class="transaction">
        <div class="transaction-category" @click="goToDetail()">
            <aside class="transaction-category-stripe" :style="{backgroundColor: this.categories.find(x => x.id === transaction.category).color }"></aside>
            <p>{{ this.categories.find(x => x.id === transaction.category).name }}</p>
            <p class="transaction-date is-size-small">{{ transaction.date }}</p>
        </div>
        <div @click="goToDetail()" class="transaction-amount" :class="{'is-success': transaction.transaction_type === 'income', 'is-danger': transaction.transaction_type === 'expense'}">
            <span v-if="transaction.transaction_type === 'expense'">-</span> {{ transaction.amount | formatCurrency }}
        </div>
    </div>
</template>

<script>
export default {
    props: ['transaction', 'categories'],
    data() {
        return {
            selected: false
        }
    },
    methods: {
        goToDetail() {
            this.$router.push({ name: 'TransactionDetail', params: { id: this.transaction.id }})
        }
    }
}
</script>

<style lang="stylus" scoped>
@import "../styles/variables.styl"

.transaction
    display: flex
    width: 100%
    height: 60px
    margin-top: 10px
    position: relative

    background-color: #FFFFFF
    color: $font-color-dark
    font-weight: 600
    border-radius: $border-radius
    transition: all 0.3s ease-in-out

    &:hover
        background-color: #F2F2F2

.transaction-category, .transaction-amount
    height: 100%
    width: 100%

    line-height: 60px
    text-align: center
    overflow: hidden

    cursor: pointer

.transaction-category
    padding-left: 20px
    padding-top: 10px
    padding-bottom: 10px
    position: relative

    line-height: 20px
    text-align: left 

.transaction-amount
    padding-right: 20px

    text-align: right

.transaction-date
    font-weight: 400

.transaction-category-stripe 
    position: absolute
    left: 0
    top: 0
    height: 100%
    width: 4px

    border-radius: $border-radius 0 0 $border-radius
    transition: transform 0.3s ease-in-out

    &.selected
        transform: scaleX(8)

</style>

