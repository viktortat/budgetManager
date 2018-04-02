<template>
    <div id="app" class="app">
        <router-view name="header"/>
        <router-view name="navbar"/>
        <router-view/>
    </div>
</template>

<script>


export default {
    
}
</script>

<style lang="stylus">
@import "./styles/global.styl"

.app
    @media screen and (max-width: 767px)
        padding-top: 64px
        padding-left: 0
        padding-right: 0
        padding-bottom: 64px
    padding: 96px
    min-height: 100.06vh

    background-color: #FCFDFF



</style>
