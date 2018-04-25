<template>
    <div id="app" class="app">
        <transition name="slide-down" appear>
            <router-view name="header"/> 
        </transition>
        <transition name="slide-right" appear>
            <router-view name="navbar"/>
        </transition>
        <transition name="fade" mode="out-in" appear>
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

.slide-down-enter-active, .slide-down-leave-active
    transition: all 0.5s
.slide-down-enter, .slide-down-leave-to
    transform: translateY(-100%)
    opacity: 0

.slide-right-enter-active, .slide-right-leave-active
    transition: all 0.5s
.slide-right-enter, .slide-right-leave-to
    transform: translateX(-100%)
    opacity: 0

</style>
