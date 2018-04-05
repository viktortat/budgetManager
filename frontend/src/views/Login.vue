<template>
    <div>
        <h1>Login</h1>
        <form class="form">
            <p>
                <input type="text" id="username-login" class="input" v-model="email">
            </p>
            <p>
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
                this.$router.push({name: "Dashboard"});
            }).catch(err => {
                console.log(err);
            })
        }
    }
}
</script>

