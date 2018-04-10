<template>
    <div class="section">
        <h1>Nastavení</h1>
    </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
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
