<template>
    <div id="app" class="app">
        <router-view name="header" /> 

        <transition name="slide-left" mode="out-in">
            <router-view name="navbar" />
        </transition>

        <transition name="fade" mode="out-in">
            <router-view />
        </transition>

        <notifications />
        <the-filter />
        <app-modal />
    </div>
</template>

<script>
import TheFilter from '@/components/TheFilter.vue'
import AppModal from '@/components/AppModal.vue'

export default {
    // name
    // mixins
    // extending of other components
    // props
	// data
	// computed
    // methods
    // watch
    // components
    // lifecycle hooks

    components: {
        TheFilter,
        AppModal
    }
}
</script>


<style lang="stylus">
// @rules   
// Layout and box-model properties (margin, padding, box-sizing, overflow, position, display, width/height, etc.)
// Typographic properties (font-, line-height, letter-spacing, text-, etc.)
// Stylistic properties (color, background-*, animation, border, etc.)
// UI properties (appearance, cursor, user-select, pointer-events, etc.)
// Pseudo-elements (::after, ::before, ::selection, etc.)
// Pseudo-selectors (:hover, :focus, :active, etc.)
// Nested elements

@import "./styles/reset"
@import "./styles/variables"
@import url('https://fonts.googleapis.com/css?family=Montserrat:200,400,500,600')
@import './styles/input.styl'

.app
    @media screen and (max-width: 767px)
        min-height: 100vh

    min-height: 100.06vh
    position: relative

    font-family: 'Montserrat', sans-serif
    font-size: $FONT-SIZE
    font-weight: 400
    line-height: 1

    color: $FONT-COLOR-DARK

.section
    @media screen and (max-width: 767px)
        padding-left: 0
        padding-top: 56px
        padding-right: 0
        padding-bottom: 10px

    padding-left: 208px
    padding-top: 56px
    padding-right: 0
    padding-bottom: 10px

    &.top
        padding-left: 0

.fa-icon
    width: auto
    height: 1em

    max-width: 100%
    max-height: 100%


.slide-enter-active, .slide-leave-active 
    transition: all .4s ease

.slide-enter
    transform: translateX(100%)
    opacity: 0

.slide-leave-to
    transform: translateX(-100%)
    opacity: 0


.slide-left-enter-active, .slide-left-leave-active 
    transition: all .4s ease

.slide-left-enter, .slide-left-leave-to
    transform: translateX(-100%)
    opacity: 0


.slide-right-enter-active, .slide-right-leave-active 
    transition: all .4s ease

.slide-right-enter, .slide-right-leave-to
    transform: translateX(100%)
    opacity: 0


.fade-enter-active, .fade-leave-active 
    transition: opacity .4s ease

.fade-enter, .fade-leave-to
    opacity: 0


.list-complete-item
    transition: all 1s
    display: inline-block
    margin-right: 10px

.list-complete-enter, .list-complete-leave-to
    opacity: 0
    transform: translateY(30px)

.list-complete-leave-active 
    position: absolute


</style>

