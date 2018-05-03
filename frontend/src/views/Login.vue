<template>
    <main class="login">
        <h1 class="login-heading">Přihlásit se</h1>
        <div class="login-form">
            <p>
                <app-label for="username-login" class="label">Email</app-label>
                <app-input type="text" id="username-login" class="input" v-model="email" placeholder="Email"></app-input>
            </p>
            <p>
                <app-label for="password-login" class="label">Heslo</app-label>
                <app-input type="password" id="password-login" class="input" v-model="password" placeholder="Heslo"></app-input>
            </p>
            <app-button class="button" @click="login()">Přihlásit se</app-button>
        </div>
    </main>
</template>

<script>
import { mapActions } from "vuex";

import AppButton from '@/components/AppButton.vue'
import AppInput from '@/components/AppInput.vue'
import AppLabel from '@/components/AppLabel.vue'

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
            this.$axios.post("/auth/login/", data).then(res => {
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
        AppButton,
        AppInput,
        AppLabel
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
    
    & .button
        align-self: flex-end

.login-heading
    margin-bottom: 30px

.login-form
    display: flex
    flex-flow: column

    & > *
        margin-bottom: 30px

</style>


