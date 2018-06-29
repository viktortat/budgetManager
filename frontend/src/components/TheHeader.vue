<template>
  <header class="header">
    <div
      v-if="['Wallets', 'WalletsDetail', 'WalletsNew'].indexOf(this.$route.name) === -1"
      class="header-burger"
      @click="toggleMenu()">
      <icon
        name="bars"
        scale="2" />
    </div>
    <div
      v-if="['WalletsDetail', 'WalletsNew'].indexOf(this.$route.name) !== -1"
      class="navbar-wallets-back"
      @click="goToWallets">
      <icon
        name="chevron-left"
        scale="2" />
    </div>
    <h1 class="header-heading">{{ this.$route.meta.name }}</h1>
    <app-button
      v-if="['Wallets', 'WalletsDetail', 'WalletsNew'].indexOf(this.$route.name) !== -1"
      class="button"
      @click="logUserOut()">
      Odhlásit se
    </app-button>
    <div
      v-else
      class="header-filter"
      @click="toggleFilter()"><icon
        name="filter"
        scale="2" /></div>
  </header>
</template>

<script>
import { mapActions } from "vuex";

import AppButton from "@/components/AppButton.vue";

export default {
  methods: {
    ...mapActions(["toggleMenu", "logUserOut", "toggleFilter"]),
    goToWallets() {
      this.$router.push({ name: "Wallets" });
    }
  },
  components: { AppButton }
};
</script>

<style lang="stylus" scoped>
@import '../styles/variables'

.header
    @media screen and (max-width: 767px)
        padding-left: 64px
        padding-right: 16px

    display: flex
    align-items: center
    justify-content: space-between
    position: fixed
    top: 0
    left: 0
    width: 100vw
    height: 56px
    padding-left: 240px
    padding-right: 32px
    z-index: 25

    background-color: rgba(255, 255, 255, 1)

    border-bottom: solid 1px #E5E5E5

.header-left
    display: flex
    align-items: center

.header-burger, .header-filter, .navbar-wallets-back
    position: absolute
    top: 0
    width: 54px
    height: 54px

    cursor: pointer

.header-burger
    @media screen and (max-width: 767px)
        display: flex
        justify-content: center
        align-items: center

    display: none
    left: 0

.header-filter
    right: 16px
    display: flex
    justify-content: center
    align-items: center

.navbar-wallets-back
    left: 0
    display: flex
    justify-content: center
    align-items: center

.header-heading
    font-size: $FONT-SIZE * 1.5
    font-weight: 400

</style>
