<template>
    <div @click="pickWallet" class="wallet">
        {{ wallet.name }}
    </div>
</template>


<script>
export default {
    props: {
        wallet: {
            type: Object
        }
    },
    data() {
        return {

        }
    },
    methods: {
        pickWallet() {
            this.$emit("pickWallet", this.wallet.id)
        }
    }
}
</script>


<style lang="stylus" scoped>
@import "../styles/variables"

.wallet
    height: 300px
    padding: 20px

    border: solid 1px #E5E5E5
    border-radius: $BORDER-RADIUS

    cursor: pointer

</style>
