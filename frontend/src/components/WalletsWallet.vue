<template>
    <div class="wallet">
        <p class="wallet-heading" v-if="!options">
            {{ wallet.name }}
        </p>
        <app-button class="button wallet-button" @click="pickWallet">Vybrat</app-button>
        <div class="wallet-options" key="option" v-if="options">
            <app-button class="button wallet-option is-danger" key="1" @click="confirmDeleting"><icon name="trash" /></app-button>
            <app-button class="button wallet-option" key="2" @click="goToDetail"><icon name="pencil-alt" /></app-button>
            <app-button class="button wallet-option is-warning" key="3"  @click="options = false"><icon name="times" /></app-button>
        </div>
        <div class="wallet-options-button" v-else @click="options = true">
            <icon name="ellipsis-v" />
        </div>
    </div>
</template>

<script>
import { mapState, mapActions } from "vuex";

import AppButton from "@/components/AppButton.vue";

export default {
  props: {
    wallet: {
      type: Object
    }
  },
  data() {
    return {
      options: false
    };
  },
  computed: {
    ...mapState(["token"])
  },
  methods: {
    ...mapActions(["refreshData", "loadWallets"]),
    pickWallet() {
      this.$emit("pickWallet", this.wallet.id);
    },
    confirmDeleting() {
      const params = {
        title: "Smazání peněženky",
        message:
          "Tato akce nenávratně smaže peněženku a všechny její transakce a kategorie.<br>Přejete si pokračovat?",
        showConfirmButton: true,
        onConfirm: () => {
          return this.deleteWallet();
        }
      };
      this.$modal.show(params);
    },
    deleteWallet() {
      const url = "/wallets/" + this.wallet.id + "/";
      this.$axios
        .delete(url, { headers: { Authorization: "JWT " + this.token } })
        .then(() => {
          this.loadWallets(true);
        });
    },
    goToDetail() {
      this.$router.push({
        name: "WalletsDetail",
        params: { id: this.wallet.id }
      });
    }
  },
  components: {
    AppButton
  }
};
</script>

<style lang="stylus" scoped>
@import "../styles/variables"

.wallet
    position: relative
    height: 300px
    padding: 20px

    border: solid 1px #E5E5E5
    border-radius: $BORDER-RADIUS

.wallet-heading
    font-size: 1.5em

.wallet-button
    position: absolute
    bottom: 1.25em
    right: 1.25em

.wallet-options-button
    @media screen and (min-width: 768px)
        cursor: pointer

    position: absolute
    top: 0.75em
    right: 0.5em
    width: 2em
    height: 2em
    display: flex
    justify-content: center
    align-items: center

.wallet-options
    position: absolute
    top: 1em
    right: 0.5em
    width: 8.75em
    display: flex
    justify-content: space-around
    align-items: center

.wallet-option
    width: 1.875em
    height: 1.875em
    display: flex
    justify-content: center
    align-items: center

    color: #FFFFFF
    border-radius: 50%
</style>
