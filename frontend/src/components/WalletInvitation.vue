<template>
    <div class="user-wrapper">
        <div>{{ invitation.invited.email }}</div>
        <div class="controls-wrapper">
            <div>Status: {{ invitation.status }}</div>
            <button class="button is-danger is-square"><i class="fas fa-times"></i></button>
        </div>
    </div>
</template>


<script>
import { mapState, mapActions } from 'vuex'

import axios from 'axios'
export default {
    props: ['invitation'],
    data() {
        return {

        }
    },
    methods: {

    },
    computed: {
        ...mapState([
            'wallet'
        ]),
    },
}
</script>


<style lang="stylus" scoped>

.user-wrapper
    display: flex
    justify-content: space-between
    align-items: center
    padding: 10px
    margin-bottom: 10px
    height: 65px    

.controls-wrapper
    display: flex
    align-items: center

    & > div
        margin-right: 30px

</style>
