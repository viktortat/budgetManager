<template>
    <div class="login">
        <h1>Přihlásit se</h1>
        <form class="form">
            <p>
                <label for="username-login">
                    <small>Email</small>                     
                </label>
                <input type="text" id="username-login" class="input" v-model="email">
            </p>
            <p>
                <label for="password-login">
                    <small>Heslo</small>                     
                </label>
                <input type="password" id="password-login" class="input" v-model="password">
            </p>
            <button class="button" @click.prevent="login">Přihlásit se</button>
        </form>
    </div>
</template>

<script>
import axios from 'axios';
import { mapActions } from "vuex";

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
            axios.post("/api/auth/login/", data).then(res => {
                this.logUserIn(res.data.token);
                this.$router.push(this.$route.query.redirect || {name: 'Wallets'});
            }).catch(err => {
                console.log(err);
            })
        }
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

</style>


