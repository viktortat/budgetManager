<template>
    <div id="app" class="app">
        <router-view name="header"/> 
        <router-view name="navbar"/>
        <transition name="fade" mode="out-in">
            <router-view/>
        </transition>
        <notifications/>
    </div>
</template>

<style lang="stylus">
@import "./styles/global.styl"

.app
    @media screen and (max-width: 767px)
        min-height: 100vh

    min-height: 100.06vh


.fade-enter-active, .fade-leave-active
  transition: opacity 0.4s

.fade-enter, .fade-leave-to
  opacity: 0


</style>
