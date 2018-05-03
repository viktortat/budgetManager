<template>
    <section>

    </section>
</template>


<script>
import { mapActions, mapState } from 'vuex'

export default {
    computed: {
        ...mapState([
            'transactions',
            'categories',
            'budgets'
        ])
    },
    methods: {
        ...mapActions([
            'loadData'
        ])
    },
    created() {
        this.loadData()
    }
}
</script>


<style lang="stylus" scoped>


</style>
