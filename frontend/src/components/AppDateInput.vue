<template>
    <flat-pickr @input="$emit('input', $event)" :value="value"></flat-pickr>
</template>


<script>
import flatPickr from 'vue-flatpickr-component'
import 'flatpickr/dist/flatpickr.css'

export default {
    props: ['value'],
    components: {
        flatPickr
    },
}
</script>


<style lang="stylus" scoped>
@import '../styles/input.styl'
</style>
