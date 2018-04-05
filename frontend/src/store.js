import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    token: "",
    isUserLoggedIn: false
  },
  mutations: {
    setToken: (state, payload) => {
      state.token = payload;
    },
    setIsUserLoggedIn: (state, payload) => {
      state.isUserLoggedIn = payload;
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
    }
  },
  getters: {
    getToken: state => {
      return state.token;
    },
    getIsUserLoggedIn: state => {
      return state.isUserLoggedIn;
    }
  }
})
