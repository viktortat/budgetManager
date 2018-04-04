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
    min-height: 100.06vh

    background-color: #FCFDFF

</style>
