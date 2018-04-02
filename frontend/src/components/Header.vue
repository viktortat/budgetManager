<template>
    <header class="header">
        <button class="button">
            Přidat transakci
        </button>
        <div class="account is-size-4">
            <div class="account-photo"></div>
            <p class="account-email">panzelva@gmail.com</p>
        </div>
    </header>
</template>


<style lang="stylus" scoped>
@import "../styles/variables.styl"

.header
    @media screen and (max-width: 767px)
        padding-left: 16px
        padding-right: 16px
        height: 64px

    display: flex
    align-items: center
    justify-content: space-between
    position: fixed
    top: 0
    left: 0
    width: 100%
    height: 96px
    padding-left: 128px
    padding-right: 32px
    z-index: 25

    background-color: rgba(255, 255, 255, 0.6)

.account
    display: flex
    align-items: center 
    justify-content: space-between

    font-weight: 600

.account-photo    
    @media screen and (max-width: 767px)
        margin-right: 0
        width: 48px
        height: 48px

    width: 64px
    height: 64px
    margin-right: 32px

    background-color: $font-color-dark
    border-radius: 50%

.account-email
    @media screen and (max-width: 767px)
        display: none

</style>
