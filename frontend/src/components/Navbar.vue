<template>
    <nav class="navbar">
        <div class="navbar-menu is-size-small">
            <router-link :to="{name: 'Dashboard'}" class="navbar-menu-item"><i class="fas fa-chart-line"></i> <span>Přehled</span></router-link>
            <router-link :to="{name: 'Transactions'}" class="navbar-menu-item"><i class="fas fa-credit-card"></i> <span>Transakce</span></router-link>
            <router-link :to="{name: 'Categories'}" class="navbar-menu-item"><i class="fas fa-list"></i> <span>Kategorie</span></router-link>
            <router-link :to="{name: 'Settings'}" class="navbar-menu-item"><i class="fas fa-cogs"></i> <span>Nastavení</span></router-link>
        </div>
    </nav>
</template>


<style lang="stylus" scoped>
.navbar
    // @rules   
    @media screen and (max-width: 767px)
        display: flex
        align-items: center
        bottom: 0
        width: 100%
        height: 64px

    // Layout and box-model properties (margin, padding, box-sizing, overflow, position, display, width/height, etc.)
    position: fixed
    left: 0
    bottom: 0
    height: 100%
    width: 96px
    z-index: 50

    // Typographic properties (font-, line-height, letter-spacing, text-, etc.)
    // Stylistic properties (color, background-*, animation, border, etc.)
    box-shadow: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24)
    background-color: #FFFFFF

    // UI properties (appearance, cursor, user-select, pointer-events, etc.)
    // Pseudo-elements (::after, ::before, ::selection, etc.)
    // Pseudo-selectors (:hover, :focus, :active, etc.)
    // Nested elements

.navbar-menu
    @media screen and (max-width: 767px)
        display: flex
        justify-content: space-around
        width: 100%
        padding-top: 0

    padding-top: 32px

    color: inherit

.navbar-menu-item
    @media screen and (max-width: 767px)
        margin-bottom: 0
    margin-bottom: 64px
    display: flex
    flex-flow: column
    align-items: center

    font-weight: 600
    text-decoration: none

    color: inherit

    cursor: pointer
   
    &:hover
        color: #7B76F4
    
    & > svg
        padding-bottom: 3px

</style>
