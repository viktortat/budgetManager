<template>
    <div id="app" class="app">
        <router-view name="header"/>
        <router-view name="navbar"/>
        <router-view/>
    </div>
</template>

<style lang="stylus">
@import "./styles/global.styl"

html 
    background-color: #F4F7FA

.app
    min-height: 100.06vh

    //background-color: #FCFDFF
</style>
