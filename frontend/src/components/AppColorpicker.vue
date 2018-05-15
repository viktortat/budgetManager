<template>
    <div class="colorpicker-wrapper">
        <div class="colorpicker-picked-color" :style="{ 'background-color': pickedColor }" @click="visible = !visible"></div>
        <transition name="roll">
            <div class="colorpicker-popup" v-if="visible" :style="{ 'grid-template-columns': ' 1fr'.repeat(columns) }">
                <div class="colorpicker-popup-color" v-for="color in sortedColors" :key="color" :style="{ 'background-color': color }" @click="pickColor(color)"></div>
            </div>
        </transition>
    </div>
</template>


<script>
import { baseColors } from './AppColorpickerColors'

export default {
    props: {
        colors: {
            type: Array,
            default: () => baseColors
        },
        value: {
            type: String
        },
        columns: {
            type: Number,
            default: 4
        }
    },
    data() {
        return {
            visible: false,
            pickedColor: ''
        }
    },
    computed: {
        sortedColors() {
            return this.colors
        }
    },
    methods: {
        pickColor(color) {
            this.pickedColor = color
            this.visible = false
            this.$emit('input', this.pickedColor)
        }
    },
    watch: {
        value(newVal) {
            this.pickedColor = newVal
        }
    },
    mounted() {
        this.pickedColor = this.value
    }
}
</script>


<style lang="stylus" scoped>

.colorpicker-wrapper
    position: relative

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
    @media screen and (min-width: 768px)
        top: 70px
        right: unset
        position: absolute
        
    position: fixed
    right: 10px
    display: grid
    grid-gap: 10px
    padding: 10px
    box-sizing: border-box

    border: 1px solid lightgrey
    border-radius: 10px
    background-color: #FFFFFF

    transform-origin: top left
    // transform: translateX(calc(60px - 100%))

.colorpicker-popup-color    
    @media screen and (min-width: 768px)
        cursor: pointer
    
    width: 60px
    height: 60px 

    border: 1px solid lightgrey
    border-radius: 10px

// transitions
.roll-enter-active, .roll-leave-active 
    transition: transform .3s ease-in-out, opacity .3s ease-in-out

.roll-enter, .roll-leave-to 
    opacity: 0
    transform: translateY(-30px)

</style>
