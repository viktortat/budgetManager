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

</style>
