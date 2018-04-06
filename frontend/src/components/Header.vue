<template>
    <header class="header">
        <button class="button">
            Přidat transakci
        </button>
        <div class="account is-size-5" v-if="isUserLoggedIn">
            <p class="account-email">panzelva@gmail.com</p>
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
            'wallet'
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

.account-email
    @media screen and (max-width: 767px)
        display: none

</style>
