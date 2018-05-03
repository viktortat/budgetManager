<template>
    <nav class="navbar" :class="{'is-active': isMenuActive}">
        <header class="navbar-header"></header>
        <div class="navbar-menu">
            <div class="navbar-button-wrapper">
                <app-button class="button is-success" @click="createTransaction()">Nová transakce</app-button>
            </div>
            <router-link :to="{name: 'Dashboard'}" class="navbar-item is-size-5" active-class="is-active"><div><icon name='chart-area'/></div>Přehled</router-link>
            <router-link :to="{name: 'Transactions'}" class="navbar-item is-size-5" active-class="is-active"><div><icon name='credit-card'/></div>Transakce</router-link>
            <router-link :to="{name: 'Categories'}" class="navbar-item is-size-5" active-class="is-active"><div><icon name='list'/></div>Kategorie</router-link>
            <router-link :to="{name: 'Budgets'}" class="navbar-item is-size-5" active-class="is-active"><div><icon name='dollar-sign'/></div>Rozpočty</router-link>
            <router-link :to="{name: 'Settings'}" class="navbar-item is-size-5" active-class="is-active"><div><icon name='cogs'/></div>Nastavení</router-link>
        </div>
        <footer class="navbar-footer">
            <div class="is-size-5 navbar-account" @click="changeWallet()">
                <icon name='archive'/>
            </div>
            <div></div>
            <div class="is-size-5 navbar-logout" @click="logUserOut()"><icon name='sign-out-alt'/></div>
        </footer>
        <div class="navbar-negative-space" :class="{'is-active': isMenuActive}" @click="toggleMenu(false)"></div>
    </nav>
</template>

<script>
import { mapState, mapActions, mapMutations } from 'vuex'

import AppButton from '@/components/AppButton.vue'

export default {
    computed: {
        ...mapState([
            "isMenuActive"
        ])
    },
    methods: {
        ...mapActions([
            "logUserOut",
            'toggleMenu'
        ]),
        changeWallet() {
            this.$store.dispatch('dumpData', '')
            this.$router.push({name: 'Wallets'})
        },
        createTransaction() {
            console.log("pushed")
            this.$router.push({name: 'TransactionNew'})
        }
    },
    components: {
        AppButton
    }
}
</script>

<style lang="stylus" scoped>

$navbar-color-primary = #19232E
$navbar-color-secondary = #242f3d
$navbar-color-tertiary = #1E2835
$navbar-color-active = #53A6FA

.navbar
    @media screen and (max-width: 767px)
        transform: translateX(-105%)

    position: fixed
    left: 0
    width: 208px
    height: 100vh
    padding-top: 56px
    padding-bottom: 56px
    z-index: 50

    background-color: $navbar-color-primary
    color: #CCCCCC

    &.is-active
        transform: translateX(0)

.navbar-header
    position: absolute
    top: 0
    width: 100%
    height: 56px

    background-color: $navbar-color-secondary

.navbar-menu 
    background-color: $navbar-color-tertiary 

.navbar-item
    display: block
    position: relative
    padding-left: 70px
    padding-top: 18px
    padding-bottom: 18px

    text-decoration: none
    color: inherit

    & > div
        position: absolute
        left: 30px
        height: 100%

    &.is-active
        color: $navbar-color-active

        &::after
            content: ""
            position: absolute
            width: 3px
            height: 100%
            left: 0
            top: 0

            background-color: $navbar-color-active

    &:hover
        background-color: rgba(255, 255, 255, 0.05);

.navbar-button-wrapper 
    padding-top: 30px
    padding-bottom: 30px
    display: flex
    justify-content: center

.navbar-footer
    position: absolute
    bottom: 0
    width: 100%
    height: 56px
    padding-left: 56px
    padding-right: 18px
    display: flex
    justify-content: space-between
    align-items: center

    background-color: $navbar-color-tertiary

.navbar-account
    position: absolute
    left: 0
    top: 0
    width: 56px
    height: 56px
    display: flex
    align-items: center
    justify-content: center 
    
    cursor: pointer

    background-color: $navbar-color-secondary

.navbar-account-photo
    width: 32px
    height: 32px
    position: absolute
    top: 50%
    left: 50%
    transform: translate(-50%, -50%)

    border-radius: 50%
    background-color: $navbar-color-active

.navbar-logout
    cursor: pointer

.navbar-negative-space
    visibility: hidden
    position: fixed
    left: 208px
    top: 0
    width: 100vw
    height: 100vh
    opacity: 0

    background-color: rgba(0, 0, 0, 0.2)
    transition: opacity 0.3s ease-in-out 0.1s

    &.is-active
        visibility: visible
        opacity: 1

</style>
