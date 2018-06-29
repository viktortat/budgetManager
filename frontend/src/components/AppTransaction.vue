<template>
  <div class="transaction">
    <aside
      :style="{ backgroundColor: this.categories.find(x => x.id === transaction.category).color }"
      class="transaction-category-bar"/>
    <div class="transaction-left">
      <div class="transaction-small-text">{{ this.$moment(transaction.date).format('DD.MM.YYYY') }}</div>
      <div class="transaction-big-text">{{ this.categories.find(x => x.id === transaction.category).name | shortenString(12) }}</div>
      <div class="transaction-small-text">{{ transaction.notes | shortenString(12) }}</div>
    </div>
    <div
      v-if="options"
      key="option"
      class="transaction-options">
      <app-button
        key="1"
        class="button transaction-option is-danger"
        @click="confirmDeleting(transaction.id)"><icon name="trash" /></app-button>
      <app-button
        key="2"
        class="button transaction-option"
        @click="goToDetail(transaction.id)"><icon name="pencil-alt" /></app-button>
      <app-button
        key="3"
        class="button transaction-option is-warning"
        @click="options = false"><icon name="times" /></app-button>
    </div>
    <div
      v-else
      key="price"
      :class="{'is-positive': transaction.transaction_type === 'income', 'is-negative': transaction.transaction_type === 'expense'}"
      class="transaction-right"
      @click="options = true">
      {{ transaction.amount | formatCurrency | appendMinusSign(transaction.transaction_type) }}
    </div>
  </div>
</template>

<script>
import { mapActions, mapState } from "vuex";

import AppButton from "@/components/AppButton.vue";

export default {
  props: { transaction: { type: Object } },
  data() {
    return {
      options: false,
      checked: false
    };
  },
  computed: {
    ...mapState(["categories", "token"])
  },
  methods: {
    ...mapActions(["refreshData"]),
    goToDetail(id) {
      this.$router.push({
        name: "TransactionsDetail",
        params: { id }
      });
    },
    confirmDeleting(id) {
      const params = {
        title: "Smazání transakce",
        message: "Tato akce nenávratně smaže transakci. Přejete si pokračovat?",
        showConfirmButton: true,
        onConfirm: () => this.deleteTransaction(id)
      };

      this.$modal.show(params);
    },
    deleteTransaction(id) {
      const url = `/transactions/${id}/`;

      this.$axios
        .delete(url, { headers: { Authorization: `JWT ${this.token}` } })
        .then(() => {
          this.refreshData();
        });
    }
  },
  components: { AppButton }
};
</script>

<style lang="stylus" scoped>
@import '../styles/variables'

$height = 3.5em
$padding-top-bottom = 0.625em
$border-color = #D9D9D9

.transaction
    @media screen and (min-width: 768px)
        font-size: 20px

    position: relative
    width: 100%
    max-width: 43.750em
    height: $height
    padding-left: 13px
    padding-right: 10px
    padding-top: $padding-top-bottom
    padding-bottom: $padding-top-bottom
    display: flex
    justify-content: space-between
    align-items: center

    border-bottom: 1px solid $border-color

.transaction-category-bar
    position: absolute
    width: 3px
    height: calc(100% - 10px)
    top: 5px
    left: 0

.transaction-right, .transaction-options, .transaction-left
    height: $height - $padding-top-bottom * 2
    width: 50%
    display: flex
    justify-content: flex-end
    align-items: center

.transaction-left
    flex-flow: column
    justify-content: space-between
    align-items: unset

.transaction-right
    font-weight: 500

.transaction-small-text
    font-size: 0.750em
    font-weight: 400

.transaction-big-text
    font-size: 0.875em
    font-weight: 500

.transaction-options
    width: 8.750em
    display: flex
    justify-content: space-around
    align-items: center

.transaction-option
    width: 1.875em
    height: 1.875em
    display: flex
    justify-content: center
    align-items: center

    color: #FFFFFF
    border-radius: 50%

.is-positive
    color: $SUCCESS-COLOR

.is-negative
    color: $DANGER-COLOR

</style>
