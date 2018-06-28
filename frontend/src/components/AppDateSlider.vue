<template>
    <section class="transactions-date-wrapper">
        <div class="transactions-date-arrow" @click="editDates(false)">
            <icon name="chevron-left" />
        </div>
        <div>
            <span v-if="renderMonth">
                {{ this.$moment(filter.dateFrom).format('MMMM') }}
            </span>
            <span v-else-if="renderYear">
                {{ this.$moment(filter.dateFrom).format('YYYY') }}
            </span>
            <span v-else>
                {{ this.$moment(filter.dateFrom).format('DD.MM.YYYY') }} - {{ this.$moment(filter.dateTo).format('DD.MM.YYYY') }}
            </span>
        </div>
        <div class="transactions-date-arrow" @click="editDates(true)">
            <icon name="chevron-right" />
        </div>
    </section>
</template>

<script>
import { mapState, mapMutations } from "vuex";

import { dateMixin } from "@/mixins";

export default {
  mixins: [dateMixin],
  computed: {
    ...mapState(["filter"]),
    renderMonth() {
      return this.isMonth(
        this.$store.state.filter.dateFrom,
        this.$store.state.filter.dateTo
      );
    },
    renderYear() {
      return this.isYear(
        this.$store.state.filter.dateFrom,
        this.$store.state.filter.dateTo
      );
    }
  },
  methods: {
    ...mapMutations(["updateDateFrom", "updateDateTo"]),
    updateDates(dateObj) {
      this.updateDateFrom(dateObj.dateFrom);
      this.updateDateTo(dateObj.dateTo);
    },
    editDates(add) {
      let dateObj = {};
      let dateFrom = this.$store.state.filter.dateFrom;
      let dateTo = this.$store.state.filter.dateTo;

      if (add) dateObj = this.addDate(dateFrom, dateTo);
      else dateObj = this.subtractDate(dateFrom, dateTo);

      this.updateDates(dateObj);
    }
  }
};
</script>

<style lang="stylus" scoped>
@import '../styles/variables'

$border-color = #D9D9D9

.transactions-date-wrapper
    @media screen and (min-width: 768px)
        font-size: 20px
        width: calc(100% - 208px)

    position: fixed
    top: 56px
    height: 2em
    width: 100%
    display: flex
    justify-content: space-between
    align-items: center
    z-index: 50

    border-bottom: 1px solid $border-color
    background-color: #FFFFFF

.transactions-date-arrow
    @media screen and (min-width: 768px)
        cursor: pointer

    height: 2em
    width: 2em
    display: flex
    justify-content: center
    align-items: center

</style>
