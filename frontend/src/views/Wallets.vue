<template>
    <main class="section top">
        <section class="create-wallet" @click="createWallet">
            <p>Nová peněženka</p>
        </section>
        <section class="wallets-wrapper">
            <wallets-wallet v-for="wallet in wallets" :key="wallet.id" :wallet="wallet" @pickWallet="pickWallet" />
        </section>
    </main>
</template>

<script>
import { mapState, mapMutations, mapActions } from 'vuex'

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
    ...mapActions([
      'refreshData',
      'loadWallets'
    ]),
    pickWallet (walletID) {
      const wallet = this.wallets.find(x => x.id === walletID)
      this.setWallet(wallet)
      this.refreshData()
      this.$router.push(this.$route.query.redirect || { name: 'Dashboard' })
    },
    createWallet () {
      this.$router.push({ name: 'WalletsNew' })
    }
  },
  components: {
    WalletsWallet
  },
  created () {
    this.loadWallets(true)
  }
}
</script>

<style lang="stylus" scoped>
@import "../styles/variables"

$padding-top-bottom = 1em
$border-color = #D9D9D9

.wallets-wrapper
    display: grid
    grid-template-columns: repeat(auto-fit, 300px)
    grid-gap: 10px
    margin: 10px

.create-wallet
    @media screen and (min-width: 768px)
        cursor: pointer

    display: flex
    align-items: center
    justify-content: center
    width: 100%
    padding-top: $padding-top-bottom
    padding-bottom: $padding-top-bottom

    border-bottom: 1px solid $border-color

    &:hover
        @media screen and (min-width: 768px)
            background-color: $border-color
</style>
