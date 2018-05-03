<template>
    <label>
        <p>
            <slot></slot>
        </p>
    </label>
</template>


<script>
export default {

}
</script>


<style lang="stylus" scoped>
@import '../styles/variables'

.label
    font-size: 12px

    & > p
        padding-bottom: 7px

</style>
