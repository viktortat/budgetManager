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
    min-height: 100.06vh

</style>
