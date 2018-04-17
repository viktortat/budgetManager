<template>
    <div id="app" class="app">
        <router-view name="header"/>
        <router-view name="navbar"/>
        <router-view/>
        <notifications/>
    </div>
</template>

<style lang="stylus">
@import "./styles/global.styl"

.app
    @media screen and (max-width: 767px)
        min-height: 100vh

    min-height: 100.06vh

</style>
