<template>
  <transition name="slide-right">
    <section
      v-if="isFilterActive"
      class="filter-wrapper">
      <div>
        <app-label
          class="label"
          for="filter-date-from">Datum od</app-label>
        <app-date-input
          id="filter-date-from"
          v-model="dateFrom"
          class="input"/>
      </div>
      <div>
        <app-label
          class="label"
          for="filter-date-to">Datum do</app-label>
        <app-date-input
          id="filter-date-to"
          v-model="dateTo"
          class="input"/>
      </div>
      <div>
        <app-button
          class="button is-link divider"
          @click="setFilterDate('thisMonth')">současný měsíc</app-button>
        <app-button
          class="button is-link"
          @click="setFilterDate('lastMonth')">minulý měsíc</app-button>
      </div>
      <div>
        <app-button
          class="button is-link divider"
          @click="setFilterDate('thisYear')">současný rok</app-button>
        <app-button
          class="button is-link"
          @click="setFilterDate('lastYear')">minulý rok</app-button>
      </div>
      <div>
        <app-label
          class="label"
          for="filter-amount-from">Částka od</app-label>
        <app-input
          id="filter-amount-from"
          v-model="amountFrom"
          class="input"/>
      </div>
      <div>
        <app-label
          class="label"
          for="filter-amount-to">Částka do</app-label>
        <app-input
          id="filter-amount-to"
          v-model="amountTo"
          class="input"/>
      </div>
      <div>
        <app-label
          class="label"
          for="filter-type">Typ transakce</app-label>
        <app-select
          id="filter-type"
          v-model="type"
          class="input">
          <option value="expense">Výdej</option>
          <option value="income">Příjem</option>
        </app-select>
      </div>
      <div>
        <app-label
          class="label"
          for="filter-category">Kategorie</app-label>
        <app-select
          id="filter-category"
          v-model="category"
          class="input">
          <option
            v-for="category in categories"
            :key="category.id"
            :value="category.id">{{ category.name }}</option>
        </app-select>
      </div>
      <div>
        <app-button
          class="button is-danger"
          @click="resetFilter()">Reset</app-button>
        <app-button
          class="button is-success"
          @click="setIsFilterActive(false)">Zavřít</app-button>
      </div>
    </section>
  </transition>
</template>

<script>
import { mapMutations, mapState } from "vuex";

import AppDateInput from "@/components/AppDateInput.vue";
import AppButton from "@/components/AppButton.vue";
import AppInput from "@/components/AppInput.vue";
import AppLabel from "@/components/AppLabel.vue";
import AppSelect from "@/components/AppSelect.vue";

export default {
  computed: {
    ...mapState(["isFilterActive", "categories"]),
    dateFrom: {
      get() {
        return this.$store.state.filter.dateFrom;
      },
      set(value) {
        this.updateDateFrom(value);
      }
    },
    dateTo: {
      get() {
        return this.$store.state.filter.dateTo;
      },
      set(value) {
        this.updateDateTo(value);
      }
    },
    amountFrom: {
      get() {
        return this.$store.state.filter.amountFrom;
      },
      set(value) {
        this.updateAmountFrom(value);
      }
    },
    amountTo: {
      get() {
        return this.$store.state.filter.amountTo;
      },
      set(value) {
        this.updateAmountTo(value);
      }
    },
    type: {
      get() {
        return this.$store.state.filter.type;
      },
      set(value) {
        this.updateType(value);
      }
    },
    category: {
      get() {
        return this.$store.state.filter.category;
      },
      set(value) {
        this.updateCategory(value);
      }
    }
  },
  methods: {
    ...mapMutations([
      "setIsFilterActive",
      "updateDateTo",
      "updateDateFrom",
      "updateType",
      "updateCategory",
      "updateAmountFrom",
      "updateAmountTo",
      "resetFilter"
    ]),
    setFilterDate(value) {
      switch (value) {
        case "thisMonth":
          this.updateDateFrom(
            this.$moment()
              .startOf("month")
              .format("YYYY-MM-DD")
          );
          this.updateDateTo(
            this.$moment()
              .endOf("month")
              .format("YYYY-MM-DD")
          );
          break;
        case "lastMonth":
          this.updateDateFrom(
            this.$moment()
              .subtract(1, "months")
              .startOf("month")
              .format("YYYY-MM-DD")
          );
          this.updateDateTo(
            this.$moment()
              .subtract(1, "months")
              .endOf("month")
              .format("YYYY-MM-DD")
          );
          break;
        case "thisYear":
          this.updateDateFrom(
            this.$moment()
              .startOf("year")
              .format("YYYY-MM-DD")
          );
          this.updateDateTo(
            this.$moment()
              .endOf("year")
              .format("YYYY-MM-DD")
          );
          break;
        case "lastYear":
          this.updateDateFrom(
            this.$moment()
              .subtract(1, "years")
              .startOf("year")
              .format("YYYY-MM-DD")
          );
          this.updateDateTo(
            this.$moment()
              .subtract(1, "years")
              .endOf("year")
              .format("YYYY-MM-DD")
          );
          break;
      }
    }
  },
  components: {
    AppButton,
    AppInput,
    AppLabel,
    AppDateInput,
    AppSelect
  }
};
</script>

<style lang="stylus" scoped>
@import '../styles/variables'

$height = 3.5em
$padding-top-bottom = 0.625em
$border-color = #D9D9D9

.filter-wrapper
    @media screen and (min-width: 768px)
        top: 60px
        left: unset
        bottom: unset
        right: 4px
        padding: 15px

        border: 1px solid $border-color
        border-radius: $BORDER-RADIUS

        & > *
            padding-bottom: 15px
        & > *:last-child
            padding-bottom: 0px

    position: fixed
    z-index: 100
    top: 0
    bottom: 0
    left: 0
    right: 0
    display: flex
    flex-flow: column
    align-items: center
    justify-content: space-around

    background-color: white

.divider
    padding-right: 1em

</style>
