<template>
    <section>
        <h1>Home</h1>
        <router-link :to="{name: 'Login'}" tag="button" class="button">Login</router-link>
        <button class="button" @click="notify()">notification</button>
    </section>
</template>

<script>
export default {
    methods: {
        notify() {
            this.$notify({
                text: 'Hello user! This is a notification!',
                type: 'success'
            });
        }
    }
}
</script>   

<style lang="stylus" scoped>

</style>

