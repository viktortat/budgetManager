<template>
    <button @click="$emit('click')">
        <slot>button</slot>
    </button>
</template>

<style lang="stylus" scoped>
@import '../styles/variables'

.button
    height: 45px
    width: 156px

    font-family: inherit
    font-size: 1em
    font-weight: 500

    color: $FONT-COLOR-LIGHT
    background-color: $PRIMARY-COLOR
    border-radius: $BORDER-RADIUS

    cursor: pointer

    &:hover
        background-color: $PRIMARY-COLOR-LIGHT

    &:active
        background-color: $PRIMARY-COLOR-DARK
        box-shadow: inset 0px 2px 0px 0px rgba(0,0,0,0.3)

    &:focus
        outline: 0

    &.is-warning
        &:hover
            background-color: $WARNING-COLOR-LIGHT

        &:active
            background-color: $WARNING-COLOR-DARK
            box-shadow: inset 0px 2px 0px 0px rgba(0,0,0,0.3);

        background-color: $WARNING-COLOR

    &.is-success
        &:hover
            background-color: $SUCCESS-COLOR-LIGHT

        &:active
            background-color: $SUCCESS-COLOR-DARK
            box-shadow: inset 0px 2px 0px 0px rgba(0,0,0,0.3);

        background-color: $SUCCESS-COLOR

    &.is-danger
        &:hover
            background-color: $DANGER-COLOR-LIGHT

        &:active
            background-color: $DANGER-COLOR-DARK
            box-shadow: inset 0px 2px 0px 0px rgba(0,0,0,0.3);

        background-color: $DANGER-COLOR

    &.is-100
        width: 100%

    &.is-square
        width: 45px

    &.is-link
        height: unset
        width: unset

        color: $PRIMARY-COLOR

        background-color: unset

        &:hover
            color: $PRIMARY-COLOR-LIGHT

        &:active
            color: $PRIMARY-COLOR-DARK
            box-shadow: unset

</style>
