<template>
    <header class="header is-size-5">
        <div class="header-burger" @click="toggleMenu()">2</div>
        <h1 class="is-size-5">{{ $route.meta.name }}</h1>
    </header>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
    computed: {
        ...mapState([
            'isUserLoggedIn',
            'wallet',
            'user'
        ])
    },
    methods: {
        ...mapActions([
            "toggleMenu"
        ])
    },
    created() {

    }
}
</script>

<style lang="stylus" scoped>
@import "../styles/variables.styl"

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
        display: block 

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
