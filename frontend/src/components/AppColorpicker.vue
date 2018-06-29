<template>
  <div class="colorpicker-wrapper">
    <transition name="fade">
      <div
        v-if="visible"
        :style="{ 'background-color': background }"
        class="colorpicker-background"
        @click="visible = !visible"/>
    </transition>
    <div
      :style="{ 'background-color': pickedColor }"
      class="colorpicker-picked-color"
      @click="visible = !visible"/>
    <transition name="fade">
      <div
        v-if="visible"
        :class="{compact: compact}"
        :style="{ 'grid-template-columns': ' 1fr'.repeat(columns) }"
        class="colorpicker-popup">
        <div
          v-for="color in colors"
          :class="{compact: compact}"
          :key="color"
          :style="{ 'background-color': color }"
          class="colorpicker-popup-color"
          @click="pickColor(color)"/>
      </div>
    </transition>
  </div>
</template>

<script>
import { materialcolorsdark } from "./AppColorpickerColors";

export default {
  props: {
    colors: {
      type: Array,
      default: () => materialcolorsdark
    },
    value: { type: String },
    columns: {
      type: Number,
      default: 4
    },
    background: { type: String },
    compact: {
      type: Boolean,
      default: false
    }
  },
  data() {
    return {
      visible: false,
      pickedColor: ""
    };
  },
  watch: {
    value(newVal) {
      this.pickedColor = newVal;
    }
  },
  mounted() {
    this.pickedColor = this.value;
  },
  methods: {
    pickColor(color) {
      this.pickedColor = color;
      this.visible = false;
      this.$emit("input", this.pickedColor);
    }
  }
};
</script>

<style lang="stylus" scoped>

.colorpicker-wrapper
    position: relative
    z-index: 500

.colorpicker-background
    position: fixed
    top: 0
    left: 0
    right: 0
    bottom: 0

    background-color: rgba(0, 0, 0, 0.2)

.colorpicker-picked-color
    @media screen and (min-width: 768px)
        cursor: pointer

    width: 60px
    height: 60px
    padding: 10px
    box-sizing: border-box

    border: 1px solid lightgrey
    border-radius: 10px

.colorpicker-popup
    @media screen and (max-width: 767px)
        position: fixed
        top: 50%
        left: 50%
        transform: translate(-50%, -50%)

    max-width: 90vw
    max-height: 90vh
    top: 70px
    right: unset
    position: absolute
    display: grid
    grid-gap: 10px
    padding: 10px
    box-sizing: border-box

    border: 1px solid lightgrey
    border-radius: 10px
    background-color: #FFFFFF

    overflow: auto

    &.compact
        grid-gap: 0

.colorpicker-popup-color
    @media screen and (min-width: 768px)
        cursor: pointer

    width: 60px
    height: 60px

    border: 1px solid lightgrey
    border-radius: 10px

&.compact
    width: 25px
    height: 25px

    border: none
    border-radius: 0

// transitions
.fade-enter-active, .fade-leave-active
    transition: opacity .3s ease-in-out

.fade-enter, .fade-leave-to
    opacity: 0

</style>
