<template>
    <main class="section">
        <section class="transaction-detail-wrapper">
            <div class="transaction-detail-form">
                <div class="transcation-detail-form-item">
                    <app-label class="label" for="transaction-amount">Částka</app-label>
                    <app-input v-model="transaction.amount" class="input" id="transaction-amount" type="number" />
                </div>
                <div class="transcation-detail-form-item">
                    <app-label class="label" for="transaction-category">Kategorie</app-label>
                    <app-select class="input" v-model="transaction.category" id="transaction-category" :empty="false">
                        <option v-for="category in categories" :key="category.id" :value="category.id">{{ category.name | shortenString(20) }}</option>
                    </app-select>
                </div>
                <div class="transcation-detail-form-item">
                    <app-label class="label" for="transaction-date">Datum</app-label>
                    <app-date-input id="transaction-date" class="input" v-model="transaction.date"></app-date-input>
                </div>
                <div class="transcation-detail-form-item">
                    <app-label class="label" for="transaction-notes">Poznámka</app-label>
                    <app-input v-model="transaction.notes" class="input" id="transaction-notes" />
                </div>
                <div class="transcation-detail-form-item">
                    <app-label class="label" for="transaction-type">Typ transakce</app-label>
                    <app-select class="input" v-model="transaction.transaction_type" id="transaction-type" :empty="false">
                        <option value="expense">Výdej</option>
                        <option value="income">Příjem</option>
                    </app-select>
                </div>
                <app-button class="button is-success" @click="createOrUpdateTransaction" >
                    <span v-if="isNew">Přidat</span>
                    <span v-else>Upravit</span>
                </app-button>
            </div>
        </section>
    </main>
</template>

<script>
import { mapActions, mapState, mapMutations } from "vuex";

import AppDateInput from "@/components/AppDateInput.vue";
import AppButton from "@/components/AppButton.vue";
import AppInput from "@/components/AppInput.vue";
import AppLabel from "@/components/AppLabel.vue";
import AppSelect from "@/components/AppSelect.vue";

export default {
  data() {
    return {
      transaction: {
        amount: "",
        transaction_type: "expense",
        notes: "",
        date: this.$moment().format("YYYY-MM-DD"),
        category: ""
      },
      isNew: false
    };
  },
  computed: {
    ...mapState(["categories", "token"])
  },
  methods: {
    ...mapMutations(["addTransaction"]),
    ...mapActions(["loadData", "refreshData"]),
    createOrUpdateTransaction() {
      const data = {
        category: this.transaction.category,
        amount: this.transaction.amount,
        transaction_type: this.transaction.transaction_type,
        notes: this.transaction.notes,
        date: this.transaction.date
      };
      if (this.isNew) {
        const url = "/transactions/";
        this.$axios
          .post(url, data, { headers: { Authorization: "JWT " + this.token } })
          .then(() => {
            this.refreshData();
            this.resetTransaction();
          });
      } else {
        const url = "/transactions/" + this.transaction.id + "/";
        this.$axios
          .patch(url, data, { headers: { Authorization: "JWT " + this.token } })
          .then(() => {
            this.refreshData();
            this.$router.push({ name: "Transactions" });
          });
      }
    },
    resetTransaction() {
      this.transaction.amount = "";
      this.transaction.transaction_type = "expense";
      this.transaction.notes = "";
      this.transaction.date = this.$moment().format("YYYY-MM-DD");
      this.transaction.category = "";
    }
  },
  watch: {
    $route() {
      this.isNew = true;
      this.resetTransaction();
    }
  },
  components: {
    AppButton,
    AppInput,
    AppLabel,
    AppDateInput,
    AppSelect
  },
  created() {
    this.loadData();
    const transactionID = this.$route.params.id;
    if (!transactionID) this.isNew = true;
    else if (Number(transactionID)) {
      const transaction = this.$store.state.transactions.find(
        x => x.id == transactionID
      );
      this.transaction = Object.assign({}, transaction);
    } else this.$router.push("/");
  }
};
</script>

<style lang="stylus" scoped>

.transaction-detail-wrapper
    @media screen and (min-width: 768px)
        font-size: 20px

    display: flex
    flex-flow: column
    justify-content: center
    align-items: center
    width: 100%
    height: 100%
    padding-top: 20px

    & .button
        align-self: flex-end

.transaction-detail-form
    display: flex
    flex-flow: column

.transcation-detail-form-item
    margin-bottom: 20px

</style>
