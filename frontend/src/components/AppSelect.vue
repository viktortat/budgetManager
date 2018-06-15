<template>
    <select v-model="selected" :multiple="multiple">
        <option v-if="empty" value=""></option>
        <slot></slot>
        <option v-for="item in content" :key="item[contentKey]" :value="item[contentValue]">{{ item[contentName] }}</option>
    </select>
</template>

<script>
export default {
  props: {
    value: [String, Number, Array],
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
    },
    multiple: {
      type: Boolean,
      default: false
    }
  },
  computed: {
    selected: {
      get () {
        return this.value
      },
      set (value) {
        this.$emit('input', value)
      }
    }
  }
}
</script>

<style lang="stylus" scoped>
@import '../styles/input.styl'
</style>
