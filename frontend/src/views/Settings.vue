<template>
    <section class="section settings-wrapper">
        <div class="settings-container">
            <header class="settings-header">
                <h3>Peněženka</h3>
            </header>
            <div class="settings">
                <div>
                    <label for="settings-wallet-name" class="label">
                        <p>Jméno</p>
                    </label>
                    <input type="text" id="settings-wallet-name" class="input input-100" v-model="walletName">
                </div>
                <div>
                    <p class="is-bold">Uživatelé</p>
                    <p v-for="user in wallet.users" :key="user.id">{{ user.email }}</p>
                </div>
            </div>
            <footer class="settings-footer">
                <div></div>
                <button class="button is-success" @click="editWalletName()">Uložit</button>
            </footer>
        </div>
    </section>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import axios from 'axios'

export default {
    data() {
        return {
            walletName: ''
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
                    text: 'Peneženka byla prejmenována.',
                    type: 'success'
                })
            }).catch(err => {
                this.$notify({
                    text: 'Vyskytl se problém, zkuste to prosím později.',
                    type: 'error'
                })
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
    created() {
        this.loadData();
        this.walletName = this.wallet.name
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
</style>
