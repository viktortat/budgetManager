<template>
    <input :type="type" @input="$emit('input', $event.target.value)" :value="value">
</template>


<script>
export default {
    props: {
        type: {
            type: String,
            default: 'text'
        },
        value: {}

    }
}
</script>


<style lang="stylus" scoped>
@import '../styles/variables'

.input
    width: 200px
    height: 40px
    padding-left: 10px

    font-size: inherit
    font-family: inherit 

    background-color: #F2F2F2
    border-radius: $BORDER-RADIUS

    &.input-medium 
        width: 280px

    &.input-large 
        width: 300px

    &.input-100 
        width: 100%

input[type=number]::-webkit-inner-spin-button, 
input[type=number]::-webkit-outer-spin-button
    -webkit-appearance: none
    margin: 0

</style>

