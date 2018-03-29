import Vue from 'vue'
import Router from 'vue-router'
import Dashboard from './views/Dashboard.vue'
import Transactions from './views/Transactions.vue'

Vue.use(Router)

export default new Router({
  routes: [
    { path: '/', name: 'Dashboard', component: Dashboard },
    { path: '/transactions', name: 'Transactions', component: Transactions }
  ],
  mode: 'history'
})
