import moment from "moment";

export const mutations = {
  setUser: (state, payload) => {
    state.user = payload;
  },
  setToken: (state, payload) => {
    state.token = payload;
  },
  setWallet: (state, payload) => {
    state.wallet = payload;
  },

  setWallets: (state, payload) => {
    state.wallets = payload;
  },
  setCategories: (state, payload) => {
    state.categories = payload;
  },
  setTransactions: (state, payload) => {
    state.transactions = payload;
  },
  setBudgets: (state, payload) => {
    state.budgets = payload;
  },

  setIsMenuActive: (state, payload) => {
    state.isMenuActive = payload;
  },
  setIsFilterActive: (state, payload) => {
    state.isFilterActive = payload;
  },

  // Filter
  updateDateFrom: (state, payload) => {
    state.filter.dateFrom = payload;
  },
  updateDateTo: (state, payload) => {
    state.filter.dateTo = payload;
  },
  updateAmountFrom: (state, payload) => {
    state.filter.amountFrom = payload;
  },
  updateAmountTo: (state, payload) => {
    state.filter.amountTo = payload;
  },
  updateType: (state, payload) => {
    state.filter.type = payload;
  },
  updateCategory: (state, payload) => {
    state.filter.category = payload;
  },
  resetFilter: state => {
    state.filter = {
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
    };
  }
};
