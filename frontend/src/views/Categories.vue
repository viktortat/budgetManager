<template>
    <div class="section-md">
        <h1 class="is-bold">Kategorie</h1>
        <p v-for="category in categories" :key="category.id">{{ category.name }}</p>
    </div>
</template>

<script>
import { mapState, mapActions } from 'vuex';

export default {
    computed: {
        ...mapState([
            'wallet',
            'transactions',
            'categories'
        ]),
    },
    methods: {
        ...mapActions([
            'loadData'
        ])
    },
    created() {
        this.loadData();
    }
}
</script>

<style lang="stylus" scoped>
@import "../styles/variables.styl"

</style>
