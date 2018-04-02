import Vue from 'vue'
import Router from 'vue-router'
import Dashboard from './views/Dashboard.vue'
import Transactions from './views/Transactions.vue'
import Settings from './views/Settings.vue'
import Categories from './views/Categories.vue'
import Login from './views/Login.vue'

import Header from '@/components/Header.vue';
import Navbar from '@/components/Navbar.vue';

Vue.use(Router)

export default new Router({ 
  routes: [
    { path: '/', name: 'Dashboard', components: {
      default: Dashboard,
      header: Header,
      navbar: Navbar
    }},
    { path: '/transakce', name: 'Transactions', components: {
      default: Transactions,
      header: Header,
      navbar: Navbar
    }},
    { path: '/nastaveni', name: 'Settings', components: {
      default: Settings,
      header: Header,
      navbar: Navbar
    }},
    { path: '/kategorie', name: 'Categories', components: {
      default: Categories,
      header: Header,
      navbar: Navbar
    }},
    { path: '/login', name: 'Login', component: Login }
  ],
  mode: 'history'
})
