<template>
  <flat-pickr
    :value="value"
    class="input"
    @input="$emit('input', $event)"/>
</template>

<script>
import flatPickr from "vue-flatpickr-component";
import "flatpickr/dist/flatpickr.css";

export default {
  components: { flatPickr },
  props: { value: { type: String } }
};
</script>

<style lang="stylus" scoped>
@import '../styles/input.styl'
</style>
