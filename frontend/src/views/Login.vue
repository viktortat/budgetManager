<template>
    <section class="login">
        <h1 class="is-bold">Přihlásit se</h1>
        <div class="form">
            <p>
                <label for="username-login" class="label">
                    <p>Email</p>                     
                </label>
                <input type="text" id="username-login" class="input input-medium" v-model="email">
            </p>
            <p>
                <label for="password-login" class="label">
                    <p>Heslo</p>                     
                </label>
                <input type="password" id="password-login" class="input input-medium" v-model="password">
            </p>
            <app-button class="button" @click="login()">Přihlásit se</app-button>
        </div>
    </section>
</template>

<script>
import { mapActions } from "vuex";

import AppButton from '@/components/AppButton.vue'

export default {
    data() {
        return {
            email: "",
            password: ""
        }
    },
    methods: {
        ...mapActions([
            "logUserIn"
        ]),
        login() {
            const data = {
                "email": this.email,
                "password": this.password 
            };
            this.$axios.post("/api/auth/login/", data).then(res => {
                this.logUserIn(res.data.token);
                this.$router.push(this.$route.query.redirect || {name: 'Wallets'});
            }).catch(err => {
                this.$notify({
                    text: 'Vyskytl se problém, zkuste to prosím později.',
                    type: 'error'
                });
            })
        }
    },
    components: {
        AppButton
    }
}
</script>


<style lang="stylus" scoped>
@import "../styles/variables.styl"

.login
    display: flex
    flex-flow: column
    justify-content: center
    align-items: center
    width: 100%
    height: 100vh

    & h1
        font-weight: 600
        padding-bottom: 60px
    
    & .button
        align-self: flex-end

    & small
        font-weight: 600

    & input
        margin-bottom: 30px

</style>


