import Vue from 'vue'
import Router from 'vue-router'

import Dashboard from '@/views/Dashboard.vue'
import Transactions from '@/views/Transactions.vue'
import TransactionCreate from '@/views/TransactionCreate.vue'
import TransactionEdit from '@/views/TransactionEdit.vue'
import Settings from '@/views/Settings.vue'
import Categories from '@/views/Categories.vue'
import Login from '@/views/Login.vue'
import Home from '@/views/Home.vue'
import Wallets from '@/views/Wallets.vue'
import Budgets from '@/views/Budgets.vue'

import Header from '@/components/AppHeader.vue'
import Navbar from '@/components/AppNavbar.vue'

import store from '@/store/store.js'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/prehled',
      name: 'Dashboard',
      components: {
        default: Dashboard,
        header: Header,
        navbar: Navbar
      },
      meta: {
        'name': 'Přehled'
      },
      beforeEnter: (to, from, next) => {
        if (!store.state.isUserLoggedIn) {
          next({ name: 'Login', query: {redirect: to.fullPath} })
        } else if (store.state.wallet == null) {
          next({ name: 'Wallets', query: {redirect: to.fullPath} })
        } else {
          next()
        }
      }
    },
    {
      path: '/rozpocty',
      name: 'Budgets',
      components: {
        default: Budgets,
        header: Header,
        navbar: Navbar
      },
      meta: {
        'name': 'Rozpočty'
      },
      beforeEnter: (to, from, next) => {
        if (!store.state.isUserLoggedIn) {
          next({ name: 'Login', query: {redirect: to.fullPath} })
        } else if (store.state.wallet == null) {
          next({ name: 'Wallets', query: {redirect: to.fullPath} })
        } else {
          next()
        }
      }
    },
    {
      path: '/penezenky',
      name: 'Wallets',
      components: {
        default: Wallets,
        header: Header
      },
      meta: {
        'name': ''
      },
      beforeEnter: (to, from, next) => {
        if (!store.state.isUserLoggedIn) {
          next({ name: 'Login', query: {redirect: to.fullPath} })
        } else {
          next()
        }
      }
    },
    { path: '/transakce',
      name: 'Transactions',
      components: {
        default: Transactions,
        header: Header,
        navbar: Navbar
      },
      meta: {
        'name': 'Transakce'
      },
      beforeEnter: (to, from, next) => {
        if (!store.state.isUserLoggedIn) {
          next({ name: 'Login', query: {redirect: to.fullPath} })
        } else if (store.state.wallet == null) {
          next({ name: 'Wallets', query: {redirect: to.fullPath} })
        } else {
          next()
        }
      }
    },
    { path: '/transakce/new',
      name: 'TransactionNew',
      components: {
        default: TransactionCreate,
        header: Header,
        navbar: Navbar
      },
      meta: {
        'name': 'Transakce'
      },
      beforeEnter: (to, from, next) => {
        if (!store.state.isUserLoggedIn) {
          next({ name: 'Login', query: {redirect: to.fullPath} })
        } else if (store.state.wallet == null) {
          next({ name: 'Wallets', query: {redirect: to.fullPath} })
        } else {
          next()
        }
      }
    },
    { path: '/transakce/:id',
      name: 'TransactionDetail',
      components: {
        default: TransactionEdit,
        header: Header,
        navbar: Navbar
      },
      meta: {
        'name': 'Transakce'
      },
      beforeEnter: (to, from, next) => {
        if (!store.state.isUserLoggedIn) {
          next({ name: 'Login', query: {redirect: to.fullPath} })
        } else if (store.state.wallet == null) {
          next({ name: 'Wallets', query: {redirect: to.fullPath} })
        } else {
          next()
        }
      }
    },
    { path: '/',
      name: 'Home', redirect: { name: 'Dashboard' }
    },
    {
      path: '/nastaveni',
      name: 'Settings',
      components: {
        default: Settings,
        header: Header,
        navbar: Navbar
      },
      meta: {
        'name': 'Nastavení'
      },
      beforeEnter: (to, from, next) => {
        if (!store.state.isUserLoggedIn) {
          next({ name: 'Login', query: {redirect: to.fullPath} })
        } else if (store.state.wallet == null) {
          next({ name: 'Wallets', query: {redirect: to.fullPath} })
        } else {
          next()
        }
      }
    },
    {
      path: '/kategorie',
      name: 'Categories',
      components: {
        default: Categories,
        header: Header,
        navbar: Navbar
      },
      meta: {
        'name': 'Kategorie'
      },
      beforeEnter: (to, from, next) => {
        if (!store.state.isUserLoggedIn) {
          next({ name: 'Login', query: {redirect: to.fullPath} })
        } else if (store.state.wallet == null) {
          next({ name: 'Wallets', query: {redirect: to.fullPath} })
        } else {
          next()
        }
      }
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    }
  ],
  mode: 'history'
})
