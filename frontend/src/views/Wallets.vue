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
        <h2>Pozvánky</h2>
        <div class="invitations">
            <div class="invitation" v-for="invitation in invitations" :key="invitation.id">
                <h5>Uživatel<br><br>{{ invitation.creator.email }}<br><br>Vás pozval do své peněženky!</h5>
                <div class="invitation-buttons">
                    <button class="button is-success" @click="acceptInvitation(invitation.id)">Přijmout</button>
                    <button class="button is-danger" @click="declineInvitation(invitation.id)">Odmítnout</button>
                </div>
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
            walletName: "",
            invitations: []
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
                this.loadInviteData()
            }).catch(error => {
                if(error.response.status === 401) {
                    this.logUserOut()
                }
            })
        },
        loadInviteData() {
            const url = '/api/invitations/' + '?invited=' + this.user.id
            axios.get(url, { headers: { Authorization: 'JWT ' + this.$store.state.token }}).then(res => {
                this.invitations = res.data
            })
        },
        acceptInvitation(invitation_id) {
            const data = {
                'id': invitation_id,
                'status': 'accepted'
            }
            const url = '/api/invitations/resolve/'
            axios.post(url, data, { headers: { Authorization: 'JWT ' + this.$store.state.token }}).then(res => {
                console.log(res)
            })
        },
        declineInvitation(invitation_id) {
            const data = {
                'id': invitation_id,
                'status': 'refused'
            }
            const url = '/api/invitations/resolve/'
            axios.post(url, data, { headers: { Authorization: 'JWT ' + this.$store.state.token }}).then(res => {
                console.log(res)
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
    @media screen and (max-width: 767px)
        min-height: 100vh
        
    min-height: 100.06vh

    background-color: $background-color-primary

    & > h2
        padding-top: 1rem
        padding-bottom: 1rem
        padding-left: 1rem

.wallets
    display: grid
    grid-template-columns: repeat(auto-fit, 300px)
    grid-gap: 10px
    margin: 10px

.wallet
    @media screen and (min-width: 768px)
        &:hover
            background-color: #F2F2F2

    height: 250px
    padding: 20px

    background-color: #FFFFFF
    border-radius: $border-radius

    cursor: pointer

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

.invitations
    display: grid
    grid-template-columns: repeat(auto-fit, 300px)
    grid-gap: 10px
    margin: 10px

.invitation
    display: flex
    flex-flow: column
    justify-content: space-between
    height: 250px
    padding: 20px

    background-color: #FFFFFF
    border-radius: $border-radius

.invitation-buttons
    width: 100%
    display: flex
    justify-content: space-between

    & > .button
        border-radius: 0

        &:first-child
            border-radius: $border-radius 0 0 $border-radius
        
        &:last-child
            border-radius: 0 $border-radius $border-radius 0

</style>
