<template>
    <section class="section settings-wrapper">
        <div class="settings-container">
            <header class="settings-header">
                <h3>Peněženka</h3>
            </header>
            <div class="settings">
                <div>
                    <h5 class="is-bold">Jméno</h5>
                    <input type="text" id="settings-wallet-name" class="input input-100" v-model="walletName">
                </div>
            </div>
            <footer class="settings-footer">
                <div></div>
                <button class="button is-success" @click="editWalletName()">Uložit</button>
            </footer>
        </div>
        <div class="settings-container">
            <header class="settings-header">
                <h3>Pozvat uživatele</h3>
            </header>
            <div class="settings">
                <div>
                    <label for="settings-invite" class="label"><p>Email</p></label>
                    <input type="email" class="input input-100" id="settings-invite" v-model="inviteUser">
                </div>
            </div>
            <footer class="settings-footer">
                <div></div>
                <button class="button is-success" @click="inviteUserByEmail()">Pozvat</button>
            </footer>
        </div>
        <div class="settings-container">
            <header class="settings-header">
                <h3>Uživatelé</h3>
            </header>
            <div class="settings">
                <wallet-user v-for="user in wallet.users" :key="user.id" :user="user" />
            </div>
            <div class="settings">
                <wallet-invitation v-for="invitation in invitations" :key="invitation.id" :invitation="invitation" />
            </div>
        </div>
    </section>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import axios from 'axios'
import WalletUser from '@/components/WalletUser.vue'
import WalletInvitation from '@/components/WalletInvitation.vue'
import { tokenCheck } from '@/mixins.js'

export default {
    data() {
        return {
            walletName: '',
            inviteUser: '',
            invitations: []
        }
    },
    methods: {
        ...mapActions([
            'loadData',
            'refreshData'
        ]),
        editWalletName() {
            const data = {
                'name': this.walletName
            }
            const url = '/api/wallets/' + this.wallet.id + '/'
            axios.patch(url, data, { headers: { Authorization: 'JWT ' + this.$store.state.token }}).then(res => {
                this.refreshData()
                this.$notify({
                    text: 'Peněženka byla uložena.',
                    type: 'success'
                })
            }).catch(err => {
                this.$notify({
                    text: 'Vyskytl se problém, zkuste to prosím později.',
                    type: 'error'
                })
            })
        },
        inviteUserByEmail() {
            if(this.inviteUser) {
                const data = {
                    'invited_id': this.inviteUser,
                    'wallet': this.wallet.id
                }
                const url = '/api/invitations/create/'
                axios.post(url, data, { headers: { Authorization: 'JWT ' + this.$store.state.token }}).then(res => {
                    this.$notify({
                        text: 'Uživatel pozván.',
                        type: 'success'
                    })
                    this.loadInvitesData()
                }).catch(err => {
                    this.$notify({
                        text: err.response.data,
                        type: 'error'
                    })                
                })
            }
        },
        loadInviteData() {
            const url = '/api/invitations/' + '?wallet=' + this.wallet.id + '&status=pending'
            axios.get(url, { headers: { Authorization: 'JWT ' + this.$store.state.token }}).then(res => {
                this.invitations = res.data
            })
        }
    },
    computed: {
        ...mapState([
            'wallet',
            'categories',
            'transactions'
        ])
    },
    components: {
        WalletUser,
        WalletInvitation
    },
    mixins: [tokenCheck],
    created() {
        this.loadData();
        this.walletName = this.wallet.name

        this.loadInviteData()
    }
}
</script>

<style lang="stylus" scoped>
@import "../styles/variables.styl"

.settings-wrapper
    @media screen and (max-width: 767px)
        min-height: 100vh
        
    min-height: 100.06vh

    background-color: $background-color-primary

.settings-container
    position: relative
    padding: 20px
    padding-top: 72px
    padding-bottom: 72px
    margin: 10px

    background-color: #FFFFFF
    border-radius: $border-radius

.settings-header
    position: absolute
    top: 0
    left: 0
    width: 100%
    height: 52px
    padding-left: 20px
    display: flex
    align-items: center
    justify-content: space-between

.settings-footer
    position: absolute
    bottom: 0
    left: 0
    width: 100%
    padding: 20px
    display: flex
    justify-content: space-between
    align-items: center

.settings
    & > div
        margin-bottom: 20px

    & h5
        margin-left: 5px
        margin-bottom: 5px

</style>
