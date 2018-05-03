<template>
    <select @input="$emit('input', $event.target.value)" :value="value">
        <option v-if="empty" value=""></option>
        <slot></slot>
        <option v-for="item in content" :key="item[contentKey]" :value="item[contentValue]">{{ item[contentName] }}</option>
    </select>
</template>


<script>
export default {
    props: {
        value: [String, Number],
        content: [Array, Object],
        contentKey: {
            type: String,
            default: 'id'
        },
        contentValue: {
            type: String,
            default: 'id'
        },
        contentName: {
            type: String,
            default: 'name'
        },
        empty: {
            type: Boolean,
            default: true
        }
    }
}
</script>


<style lang="stylus" scoped>
@import '../styles/input.styl'
</style>
