<template>
  <main class="section">
    <app-date-slider />
    <section class="dashboard">
      <app-balance />
      <div class="graph">
        <vue-chartist
          :data="balanceDataset"
          :options="{fullWidth: true, chartPadding: 20}"
          :ratio="'ct-golden-section'"
          type="Line" />
      </div>
      <dashboard-income-and-expense />
      <div class="graph">
        <vue-chartist
          :data="categoriesDataset"
          :options="{fullWidth: true, chartPadding: 20}"
          :ratio="'ct-perfect-fifth'"
          type="Pie" />
      </div>
      <categories-category
        v-for="category in biggestCategories"
        :key="category.id"
        :category="category" />
    </section>
  </main>
</template>

<script>
import { mapActions, mapState } from "vuex";

import AppDateSlider from "@/components/AppDateSlider.vue";
import AppBalance from "@/components/AppBalance.vue";
import DashboardIncomeAndExpense from "@/components/DashboardIncomeAndExpense.vue";
import VueChartist from "@/components/VueChartist.vue";
import CategoriesCategory from "@/components/CategoriesCategory.vue";

import { balanceMixin, dateMixin, filterMixin } from "@/mixins";

export default {
  mixins: [filterMixin, dateMixin, balanceMixin],
  computed: {
    ...mapState(["transactions", "categories", "budgets", "filter"]),
    balanceDataset() {
      const data = {
        series: [[]],
        labels: []
      };

      let dateFrom = this.filter.dateFrom;
      let dateTo = this.filter.dateTo;

      for (let i = 0; i < 6; i++) {
        const transactions = this.filterTransactionsByDate(
          this.transactions,
          dateFrom,
          dateTo
        );

        data.series[0].unshift(this.calculateBalance(transactions));

        if (this.isMonth(dateFrom, dateTo)) {
          data.labels.unshift(this.$moment(dateFrom).format("MMMM"));
        } else if (this.isYear(dateFrom, dateTo)) {
          data.labels.unshift(this.$moment(dateFrom).format("YYYY"));
        }

        const dateObj = this.subtractDate(dateFrom, dateTo);

        dateFrom = dateObj.dateFrom;
        dateTo = dateObj.dateTo;
      }

      return data;
    },
    categoriesDataset() {
      const data = {
        series: [],
        labels: []
      };

      const categories = this.sortedCategories();
      let iterations = 0;
      let balance = 0;

      for (const cat of categories) {
        if (iterations < 5) {
          cat.dateExpenses === 0
            ? data.labels.push("")
            : data.labels.push(cat.name);
          data.series.push(cat.dateExpenses);
        } else {
          balance += cat.dateExpenses;
        }
        iterations++;
      }
      balance === 0 ? data.labels.push("") : data.labels.push("Zbytek");
      data.series.push(balance);

      return data;
    },
    biggestCategories() {
      return this.sortedCategories().splice(0, 5);
    }
  },
  methods: {
    ...mapActions(["loadData"]),
    sortedCategories() {
      const transactions = this.filterTransactionsByDate(
        this.transactions,
        this.filter.dateFrom,
        this.filter.dateTo
      );
      const categories = this.categories.slice();

      for (const cat of categories) {
        let expenses = 0;

        for (let i = 0; i < cat.transactions.length; i++) {
          const trn = transactions.find(x => x.id === cat.transactions[i]);

          if (trn) {
            if (trn.transaction_type === "expense") {
              expenses += Number(trn.amount);
            }
          }
        }
        cat.dateExpenses = expenses;
      }

      return categories.sort((a, b) => b.dateExpenses - a.dateExpenses);
    }
  },
  components: {
    AppDateSlider,
    AppBalance,
    DashboardIncomeAndExpense,
    VueChartist,
    CategoriesCategory
  },
  created() {
    this.loadData();
  }
};
</script>

<style lang="stylus" scoped>

.section
    @media screen and (min-width: 768px)
        font-size: 20px

    padding-top: calc(2em + 56px)

.dashboard
    display: flex
    flex-flow: column
    align-items: center

.graph
    width: 100%
    max-width: 43.75em
</style>
