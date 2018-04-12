<template>
    <nav class="navbar" :class="{'is-active': isMenuActive}">
        <header class="navbar-header"></header>
        <div class="navbar-menu">
            <div class="navbar-button-wrapper">
                <router-link :to="{name: 'TransactionNew'}" tag="button" class="button is-success">Nová transakce</router-link>
            </div>
            <router-link :to="{name: 'Dashboard'}" class="navbar-item is-size-5" active-class="is-active"><div><i class="fas fa-chart-area"></i></div>Přehled</router-link>
            <router-link :to="{name: 'Transactions'}" class="navbar-item is-size-5" active-class="is-active"><div><i class="fas fa-credit-card"></i></div>Transakce</router-link>
            <router-link :to="{name: 'Categories'}" class="navbar-item is-size-5" active-class="is-active"><div><i class="fas fa-list"></i></div>Kategorie</router-link>
            <router-link :to="{name: 'Settings'}" class="navbar-item is-size-5" active-class="is-active"><div><i class="fas fa-cogs"></i></div>Nastavení</router-link>
        </div>
        <footer class="navbar-footer">
            <div class="navbar-account">
                <div class="navbar-account-photo"></div>
            </div>
            <div></div>
            <div class="is-size-5 navbar-logout" @click="logUserOut"><i class="fas fa-sign-out-alt"></i></div>
        </footer>
        <div class="navbar-negative-space" :class="{'is-active': isMenuActive}" @click="toggleMenu()"></div>
    </nav>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
    data() {
        return {

        }
    },
    computed: {
        ...mapState([
            "isMenuActive"
        ])
    },
    methods: {
        ...mapActions([
            "toggleMenu",
            "logUserOut"
        ])
    }
}
</script>

<style lang="stylus" scoped>
@import "../styles/variables.styl"

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
    transition: transform 0.3s ease-in-out
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
