<template>
    <div class="section settings-wrapper">
        
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

.settings-wrapper
    min-height: 100.06vh

    background-color: $background-color-primary

</style>
