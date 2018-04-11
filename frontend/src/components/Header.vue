<template>
    <header class="header">
        <router-link :to="{name: 'TransactionNew'}" tag="button" class="button is-success" v-if="wallet !== null">
            Přidat transakci
        </router-link>
        <div v-else></div>
        <div class="account is-size-5" v-if="isUserLoggedIn">
            <p class="account-email">{{ user.email }}</p>
        </div>
        <div class="account is-size-5" v-else>
            <router-link :to="{name: 'Login'}" class="is-link-dark">
                <p>Přihlásit se</p>
            </router-link>
        </div>
    </header>
</template>

<script>
import { mapState } from 'vuex'

export default {
    computed: {
        ...mapState([
            'isUserLoggedIn',
            'wallet',
            'user'
        ])
    }
}
</script>



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
    width: 100vw
    height: 76px
    padding-left: 118px
    padding-right: 32px
    z-index: 25

    background-color: rgba(255, 255, 255, 1)
    box-shadow: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24)

.account
    display: flex
    align-items: center 
    justify-content: space-between

    font-weight: 600

.account-email
    @media screen and (max-width: 767px)
        display: none

</style>
