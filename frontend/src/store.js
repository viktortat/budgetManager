import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

import { test, getApiCategories, getApiTransactions } from './utils.js'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    token: "",
    isUserLoggedIn: false,
    wallet: null,
    categories: [],
    transactions: []
  },
  mutations: {
    setToken: (state, payload) => {
      state.token = payload;
    },
    setIsUserLoggedIn: (state, payload) => {
      state.isUserLoggedIn = payload;
    },
    setWallet: (state, payload) => {
      state.wallet = payload;
    },
    setCategories: (state, payload) => {
      state.categories = payload;
    },
    setTransactions: (state, payload) => {
      state.transactions = payload;
    }
  },
  actions: {
    logUserIn: ({ commit }, payload) => {
      commit("setToken", payload);
      commit("setIsUserLoggedIn", true);
    },
    logUserOut: ({ commit }, payload) => {
      commit("setToken", "");
      commit("setIsUserLoggedIn", false);
    },
    pickWallet: ({ commit }, payload) => {
      commit("setWallet", payload);
    },
    loadData: (context, payload) => {
      const walletID = context.state.wallet.id;
      const token = context.state.token;
      axios.all([getApiCategories(walletID, token), getApiTransactions(walletID, token)]).then(
        axios.spread((cat, tran) => {
          context.commit("setTransactions", tran.data);
          context.commit("setCategories", cat.data);
        })
      );
    }
  },
  getters: {

  }
})
