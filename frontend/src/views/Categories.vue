<template>
    <main class="section">
        <app-date-slider />
        <section class="categories">
            <div class="create-category" @click="createCategory">
                <p>Nová kategorie</p>
            </div>
            <categories-category v-for="category in categories" :key="category.id" :category="category" />
        </section>
    </main>
</template>


<script>
import { mapState } from 'vuex'

import AppDateSlider from '@/components/AppDateSlider.vue'
import CategoriesCategory from '@/components/CategoriesCategory.vue'
import AppButton from '@/components/AppButton.vue'

export default {
    computed: {
        ...mapState([
            'categories'
        ])
    },
    methods: {
        createCategory() {
            this.$router.push({name: 'CategoriesNew'})
        }
    },
    components: {
        CategoriesCategory,
        AppDateSlider,
        AppButton
    }
}
</script>


<style lang="stylus" scoped>

$padding-top-bottom = 1em
$border-color = #D9D9D9

.section    
    @media screen and (min-width: 768px)
        font-size: 20px

    padding-top: calc(2em + 56px)

.categories
    display: flex
    flex-flow: column
    align-items: center

.create-category
    @media screen and (min-width: 768px)
        cursor: pointer

    display: flex
    align-items: center
    justify-content: center
    width: 100%
    max-width: 43.750em
    padding-top: $padding-top-bottom
    padding-bottom: $padding-top-bottom

    border-bottom: 1px solid $border-color

    &:hover 
        @media screen and (min-width: 768px)
            background-color: $border-color

</style>
