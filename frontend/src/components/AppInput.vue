<template>
    <input @input="$emit('input', $event.target.value)" :value="value">
</template>


<script>
export default {
    props: ['value']
}
</script>


<style lang="stylus" scoped>
@import '../styles/variables'

$border-color = #D9D9D9

.input
    width: 250px
    height: 45px
    padding-left: 18px

    font-size: 14px
    font-weight: 400
    font-family: inherit 

    background-color: #FFFFFF
    border-radius: $BORDER-RADIUS
    border: 1px solid $border-color

    &::placeholder
        color: $border-color

    &:hover
        border: 1px solid #808080

    &:focus
        border: 1px solid $PRIMARY-COLOR
        outline: none



input[type=number]::-webkit-inner-spin-button, 
input[type=number]::-webkit-outer-spin-button
    -webkit-appearance: none
    margin: 0

</style>

