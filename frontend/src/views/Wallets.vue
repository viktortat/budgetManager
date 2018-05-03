<template>
    <main class="section top">
        <section class="wallets-wrapper">
            <wallets-wallet v-for="wallet in wallets" :key="wallet.id" :wallet="wallet" @pickWallet="pickWallet" ></wallets-wallet>
        </section>
    </main>
</template>


<script>
import { mapState, mapMutations } from 'vuex'

import WalletsWallet from '@/components/WalletsWallet.vue'

export default {
    name: 'Wallets',
    computed: {
        ...mapState([
            'wallets'
        ])
    },
    methods: {
        ...mapMutations([
            'setWallets',
            'setWallet'
        ]),
        getWallets() {
            const url = '/wallets/'
            this.$axios.get(url, { headers: { Authorization: 'JWT ' + this.$store.state.token }}).then(response => {
                this.setWallets(response.data)
            }).catch(error => {})
        },
        pickWallet(walletID) {
            const wallet = this.wallets.find(x => x.id === walletID)
            this.setWallet(wallet)
            this.$router.push(this.$route.query.redirect || { name: 'Dashboard' })
        }
    },
    components: {
        WalletsWallet
    },
    created() {
        this.getWallets()
    }
}
</script>


<style lang="stylus" scoped>
@import "../styles/variables"

.wallets-wrapper
    display: grid
    grid-template-columns: repeat(auto-fit, 300px)
    grid-gap: 10px
    margin: 10px

</style>
