import moment from "moment";

export const state = {
  user: {},
  token: "",
  wallet: null,

  wallets: [],
  transactions: [],
  categories: [],
  budgets: [],

  isMenuActive: false,
  isFilterActive: false,

  // filter
  filter: {
    dateFrom: moment()
      .startOf("month")
      .format("YYYY-MM-DD"),
    dateTo: moment()
      .endOf("month")
      .format("YYYY-MM-DD"),
    type: "",
    category: "",
    amountFrom: "",
    amountTo: ""
  }
};
