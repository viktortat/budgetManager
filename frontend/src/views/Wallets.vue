<template>
    <section class="section top wallets-wrapper">
        <h2>Vaše peněženky</h2>
        <div class="wallets">
            <div class="wallet wallet-create">
                <form>
                    <p>
                        <label for="wallet-name" class="label">
                            <p>Jméno peněženky</p>
                        </label>
                        <input type="text" id="wallet-name" class="input input-100" v-model="walletName">
                    </p>
                    <button class="button is-success" @click.prevent="createWallet()">Vytvořit peněženku</button>
                </form>
            </div>
            <div class="wallet" v-for="wallet in ownedWallets" :key="wallet.id" @click="setWalletAndRedirect(wallet)">
                <h2>{{ wallet.name }}</h2>
                <br>
                <h4 class="is-bold" :class="{'is-success': wallet.balance > 0, 'is-danger': wallet.balance < 0}">{{ wallet.balance | formatCurrency }}</h4>
                <br>
                <p v-for="user in wallet.users" :key="user.id">{{ user.email }}</p>
            </div>
        </div>
        <h2>Sdílené peněženky</h2>
        <div class="wallets">
            <div class="wallet" v-for="wallet in sharedWallets" :key="wallet.id" @click="setWalletAndRedirect(wallet)">
                <h2>{{ wallet.name }}</h2>
                <br>
                <h4 class="is-bold" :class="{'is-success': wallet.balance > 0, 'is-danger': wallet.balance < 0}">{{ wallet.balance | formatCurrency }}</h4>
                <br>
                <p>Majitel: {{ wallet.owner }}</p>
                <p v-for="user in wallet.users" :key="user.id">{{ user.email }}</p>
            </div>
        </div>
    </section>
</template>

<style lang="stylus" scoped>

</style>

<script>
import axios from 'axios'
import { mapState ,mapActions } from "vuex"

export default {
    data() {
        return {
            wallets: [],
            walletName: ""
        }
    },
    methods: {
        ...mapActions([
            "pickWallet",
            "logUserOut"
        ]),
        setWalletAndRedirect(wallet) {
            this.pickWallet(wallet);
            this.$router.push(this.$route.query.redirect || { name: 'Dashboard' })
        },
        createWallet() {
            if(this.walletName) {
                const data = {
                    'name': this.walletName
                }
                const url = "/api/wallets/"
                axios.post(url, data, { headers: { Authorization: 'JWT ' + this.$store.state.token }}).then(res => {
                    this.wallets.push(res.data)
                    this.$notify({
                        text: 'Peneženka byla vytvořena.',
                        type: 'success'
                    });
                }).catch(err => {
                    this.$notify({
                        text: 'Vyskytl se problém, zkuste to prosím později.',
                        type: 'error'
                    });
                })
                this.walletName = ""
            }
        },
        getWallets() {
            axios.get("/api/wallets/", { 
                headers: { Authorization: 'JWT ' + this.$store.state.token }
            }).then(res => {
                this.wallets = res.data;
            }).catch(error => {
                if(error.response.status === 401) {
                    this.logUserOut()
                }
            })
        }
    },
    computed: {
        ...mapState([
            'user'
        ]),
        ownedWallets() {
            let wallets = this.wallets.filter(wall => wall.owner === this.user.id)
            return wallets
        },
        sharedWallets() {
            let wallets = this.wallets.filter(wall => wall.owner !== this.user.id)
            return wallets
        }
    },
    created() {
        this.getWallets()
    }
}
</script>


<style lang="stylus" scoped>
@import "../styles/variables.styl"

.wallets-wrapper
    min-height: 100.06vh

    background-color: $background-color-primary

    & > h2
        padding-top: 1rem
        padding-bottom: 1rem
        padding-left: 1rem

.wallets
    display: grid;
    grid-template-columns: repeat(auto-fit, 300px);
    grid-gap: 10px;
    margin: 10px;

.wallet
    height: 250px;
    padding: 20px;

    background-color: #FFFFFF
    border-radius: $border-radius

    cursor: pointer

    &:hover
        background-color: #F2F2F2

.wallet-create
    display: flex
    align-items: center
    justify-content: center

    border: none

    cursor: unset

    &:hover
        background-color: #FFFFFF
    
    & input
        margin-bottom: 20px
    
    & .button
        width: 100%

</style>
