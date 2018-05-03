<template>
    <div id="app" class="app">
        <router-view name="header" /> 
        <router-view name="navbar" />
        <router-view />
        <notifications />
        <the-filter />
    </div>
</template>

<script>
import TheFilter from '@/components/TheFilter.vue'

export default {
    // name
    // mixins
    // extending of other components
    // props
	// data
	// computed
    // components
    // methods
    // watch
    // lifecycle hooks

    components: {
        TheFilter
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

.app
    min-height: 100vh
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

</style>

