<template>
    <div class="colorpicker-wrapper">
        <transition name="fade">
            <div class="colorpicker-background" v-if="visible" @click="visible = !visible" :style="{ 'background-color': background }"></div>
        </transition>
        <div class="colorpicker-picked-color" :style="{ 'background-color': pickedColor }" @click="visible = !visible"></div>
        <transition name="fade">
            <div class="colorpicker-popup" :class="{compact: compact}" v-if="visible" :style="{ 'grid-template-columns': ' 1fr'.repeat(columns) }">
                <div class="colorpicker-popup-color" :class="{compact: compact}" v-for="color in colors" :key="color" :style="{ 'background-color': color }" @click="pickColor(color)"></div>
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
    value: {
      type: String
    },
    columns: {
      type: Number,
      default: 4
    },
    background: {
      type: String
    },
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
  methods: {
    pickColor(color) {
      this.pickedColor = color;
      this.visible = false;
      this.$emit("input", this.pickedColor);
    }
  },
  watch: {
    value(newVal) {
      this.pickedColor = newVal;
    }
  },
  mounted() {
    this.pickedColor = this.value;
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
