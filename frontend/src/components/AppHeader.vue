<template>
    <header class="header">
        <div class="header-burger" @click="toggleMenu()" v-if="this.$route.name !== 'Wallets'"><i class="fas fa-bars fa-2x"></i></div>
        <h1 class="is-size-4">{{ this.$route.meta.name }}</h1>
        <app-button class="button" @click="logUserOut()" v-if="this.$route.name === 'Wallets'">Odhlásit se</app-button>
    </header>
</template>

<script>
import { mapActions } from 'vuex'

import AppButton from '@/components/AppButton.vue'

export default {
    methods: {
        ...mapActions([
            "toggleMenu",
            "logUserOut"
        ])
    },
    components: {
        AppButton
    }
}
</script>

<style lang="stylus" scoped>

.header
    @media screen and (max-width: 767px)
        padding-left: 64px
        padding-right: 16px

    display: flex
    align-items: center
    justify-content: space-between
    position: fixed
    top: 0
    left: 0
    width: 100vw
    height: 56px
    padding-left: 240px
    padding-right: 32px
    z-index: 25

    background-color: rgba(255, 255, 255, 1)

    border-bottom: solid 1px #E5E5E5

.header-burger
    @media screen and (max-width: 767px)
        display: flex
        justify-content: center
        align-items: center 

    display: none
    position: absolute
    left: 0
    top: 0
    width: 54px
    height: 54px
    
    cursor: pointer

.account
    display: flex
    align-items: center 
    justify-content: space-between

    font-weight: 600

.account-email
    @media screen and (max-width: 767px)
        display: none

</style>
