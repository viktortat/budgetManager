<template>
    <router-link :to="{name: 'Transactions'}" class="transaction">
        <aside></aside>
        <div class="transaction-info">
            <small><i class="far fa-calendar"></i> 27.3.2018</small>
            <h5>Potraviny</h5>
            <small><i class="fas fa-pencil-alt"></i> Poznámka</small>
        </div>
        <p class="is-size-4 is-bold is-right">200 000,- Kč</p>
    </router-link>    
</template>


<style lang="stylus" scoped>
@import "../styles/variables.styl"

.transaction
    @media screen and (max-width: 767px)
        width: 100%
    
    display: flex
    justify-content: space-between
    align-items: center
    position: relative
    width: 416px
    height: 64px
    margin-top: 24px
    padding-left: 16px
    padding-right: 16px

    color: $font-color-dark
    text-decoration: none

    cursor: pointer

    & > aside
        position: absolute
        left: 0
        height: 100%
        width: 3px

        background-color: red

.transaction-info
    display: flex
    flex-flow: column
    justify-content: space-between
    height: 100%

</style>

