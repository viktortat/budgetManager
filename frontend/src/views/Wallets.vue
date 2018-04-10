<template>
    <div class="wallets-wrapper">
        <h1>Peněženky</h1>
        <p v-if="wallets.length == 0">There are no wallets!</p>
        <div class="wallets">
            <div class="wallet" v-for="wallet in wallets" :key="wallet.id" @click="setWalletAndRedirect(wallet)">
                <h2>{{ wallet.name }}</h2>
                <br>
                <h4 class="is-bold" :class="{'is-success': wallet.balance > 0, 'is-danger': wallet.balance < 0}"><span v-if="wallet.balance < 0">-</span>{{ wallet.balance | formatCurrency }}</h4>
                <br>
                <p>Majitel: {{ wallet.owner }}</p>
                <p v-for="user in wallet.users" :key="user.id">{{ user.email }}</p>
            </div>
        </div>
    </div>
</template>

<style lang="stylus" scoped>

</style>

<script>
import axios from 'axios'
import { mapActions } from "vuex"

export default {
    data() {
        return {
            wallets: []
        }
    },
    methods: {
        ...mapActions([
            "pickWallet"
        ]),
        setWalletAndRedirect(wallet) {
            this.pickWallet(wallet);
            this.$router.push(this.$route.query.redirect || { name: 'Dashboard' })
        }
    },
    computed: {
        ownedWallets() {
            
        },
        sharedWallets() {

        }
    },
    created() {
        axios.get("/api/wallets/", { 
            headers: { Authorization: 'JWT ' + this.$store.state.token }
        }).then(res => {
            this.wallets = res.data;
        }).catch(err => {
            console.log(err);
        });
    }
}
</script>


<style lang="stylus" scoped>
.wallets-wrapper 
    padding-top: 96px

.wallets
    display: flex
    flex-flow: row
    flex-wrap: wrap

.wallet
    width: 272px
    height: 200px
    margin-top: 24px
    margin-left: 24px
    padding: 10px

    background-color: white
    border-radius: $border-radius
    box-shadow: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24)
    transition: all 0.3s cubic-bezier(.25,.8,.25,1);

    cursor: pointer

    &:hover
        box-shadow: 0 10px 20px rgba(0,0,0,0.19), 0 6px 6px rgba(0,0,0,0.23);
</style>
