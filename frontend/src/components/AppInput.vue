<template>
  <input
    :value="value"
    @input="$emit('input', $event.target.value)">
</template>

<script>
export default { props: { value: { type: String } } };
</script>

<style lang="stylus" scoped>
@import '../styles/input.styl'
</style>
