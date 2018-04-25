<template>
    <div class="transaction">
        <div class="transaction-category" @click="selected =! selected">
            <aside class="transaction-category-stripe" :class="{selected: this.selected}" :style="{backgroundColor: this.categories.find(x => x.id === transaction.category).color }"></aside>
            <p>{{ this.categories.find(x => x.id === transaction.category).name }}</p>
            <p class="transaction-date is-size-small">{{ transaction.date }}</p>
        </div>
        <div @click="goToDetail()" class="transaction-owner">{{ getUserEmail }}</div>
        <div @click="goToDetail()" class="transaction-notes">{{ transaction.notes }}<span v-if="!transaction.notes">--</span></div>
        <div @click="goToDetail()" class="transaction-amount" :class="{'is-success': transaction.transaction_type === 'income', 'is-danger': transaction.transaction_type === 'expense'}">
            <span v-if="transaction.transaction_type === 'expense'">-</span> {{ transaction.amount | formatCurrency }}
        </div>
    </div>
</template>

<script>


export default {
    props: ['transaction', 'categories', 'wallet'],
    data() {
        return {
            selected: false
        }
    },
    methods: {
        goToDetail() {
            this.$router.push({ name: 'TransactionDetail', params: { id: this.transaction.id }})
        }
    },
    computed: {
        getUserEmail() {
            const user = this.wallet.users.find(x => x.id === this.transaction.user)
            if(user) return user.email
            else return ""
        }
    }
}
</script>

<style lang="stylus" scoped>
@import "../styles/variables.styl"

.transaction
    @media screen and (min-width: 768px)
        &:hover
            background-color: #F2F2F2
    
    position: relative
    display: flex
    height: 60px
    margin-bottom: 10px
    margin-left: 10px
    margin-right: 10px

    background-color: #FFFFFF
    color: $font-color-dark
    font-weight: 600
    border-radius: $border-radius
    transition: all 0.3s ease-in-out


.transaction-category, .transaction-owner, .transaction-notes, .transaction-amount
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

.transaction-owner 
    @media screen and (min-width: 620px)
        display: block    

    display: none

.transaction-notes
    @media screen and (min-width: 1020px)
        display: block  
  
    display: none

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

