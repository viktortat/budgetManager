<template>
    <header class="header">
        <div class="header-burger" @click="toggleMenu()" v-if="this.$route.name !== 'Wallets'"><icon name="bars" scale="2" /></div>
        <h1 class="header-heading">{{ this.$route.meta.name }}</h1>
        <app-button class="button" @click="logUserOut()" v-if="this.$route.name === 'Wallets'">Odhlásit se</app-button>
        <div class="header-filter" @click="toggleFilter()" v-else><icon name="filter" scale="2" /></div>
    </header>
</template>

<script>
import { mapActions } from 'vuex'

import AppButton from '@/components/AppButton.vue'

export default {
    methods: {
        ...mapActions([
            "toggleMenu",
            "logUserOut",
            "toggleFilter"
        ])
    },
    components: {
        AppButton
    }
}
</script>

<style lang="stylus" scoped>
@import '../styles/variables'

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

.header-burger, .header-filter
    position: absolute
    top: 0
    width: 54px
    height: 54px
    
    cursor: pointer

.header-burger
    @media screen and (max-width: 767px)
        display: flex
        justify-content: center
        align-items: center 

    display: none
    left: 0

.header-filter
    right: 16px
    display: flex
    justify-content: center
    align-items: center 

.header-heading 
    font-size: $FONT-SIZE * 1.5
    font-weight: 400

</style>
