import Vue from 'vue'
import Router from 'vue-router'

const Dashboard = () => import('@/views/Dashboard.vue')
const Transactions = () => import('@/views/Transactions.vue')
const TransactionsDetail = () => import('@/views/TransactionsDetail.vue')
const Categories = () => import('@/views/Categories.vue')
const CategoriesDetail = () => import('@/views/CategoriesDetail.vue')
const Budgets = () => import('@/views/Budgets.vue')
const BudgetsDetail = () => import('@/views/BudgetsDetail.vue')
const Settings = () => import('@/views/Settings.vue')
const Login = () => import('@/views/Login.vue')
const Wallets = () => import('@/views/Wallets.vue')
const WalletsDetail = () => import('@/views/WalletsDetail.vue')

import Header from '@/components/TheHeader.vue'
import Navbar from '@/components/TheNavbar.vue'

import store from '@/store/store.js'

Vue.use(Router)

const router = new Router({
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
                if (!store.state.token) {
                    next({ name: 'Login', query: {redirect: to.fullPath} })
                } 
                else if (store.state.wallet == null) {
                    next({ name: 'Wallets', query: {redirect: to.fullPath} })
                } 
                else {
                    next()
                }
            }
        },
        { 
            path: '/transakce',
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
                if (!store.state.token) {
                    next({ name: 'Login', query: {redirect: to.fullPath} })
                } 
                else if (store.state.wallet == null) {
                    next({ name: 'Wallets', query: {redirect: to.fullPath} })
                } 
                else {
                    next()
                }
            }
        },
        { 
            path: '/transakce/new',
            name: 'TransactionsNew',
            components: {
                default: TransactionsDetail,
                header: Header,
                navbar: Navbar
            },
            meta: {
                'name': 'Transakce'
            },
            beforeEnter: (to, from, next) => {
                if (!store.state.token) {
                    next({ name: 'Login', query: {redirect: to.fullPath} })
                } 
                else if (store.state.wallet == null) {
                    next({ name: 'Wallets', query: {redirect: to.fullPath} })
                } 
                else {
                    next()
                }
            }
        },
        { 
            path: '/transakce/:id',
            name: 'TransactionsDetail',
            components: {
                default: TransactionsDetail,
                header: Header,
                navbar: Navbar
            },
            meta: {
                'name': 'Transakce'
            },
            beforeEnter: (to, from, next) => {
                if (!store.state.token) {
                    next({ name: 'Login', query: {redirect: to.fullPath} })
                } 
                else if (store.state.wallet == null) {
                    next({ name: 'Wallets', query: {redirect: to.fullPath} })
                } 
                else {
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
                if (!store.state.token) {
                    next({ name: 'Login', query: {redirect: to.fullPath} })
                } 
                else if (store.state.wallet == null) {
                    next({ name: 'Wallets', query: {redirect: to.fullPath} })
                } 
                else {
                    next()
                }
            }
        },
        { 
            path: '/kategorie/new',
            name: 'CategoriesNew',
            components: {
                default: CategoriesDetail,
                header: Header,
                navbar: Navbar
            },
            meta: {
                'name': 'Kategorie'
            },
            beforeEnter: (to, from, next) => {
                if (!store.state.token) {
                    next({ name: 'Login', query: {redirect: to.fullPath} })
                } 
                else if (store.state.wallet == null) {
                    next({ name: 'Wallets', query: {redirect: to.fullPath} })
                } 
                else {
                    next()
                }
            }
        },
        { 
            path: '/kategorie/:id',
            name: 'CategoriesDetail',
            components: {
                default: CategoriesDetail,
                header: Header,
                navbar: Navbar
            },
            meta: {
                'name': 'Kategorie'
            },
            beforeEnter: (to, from, next) => {
                if (!store.state.token) {
                    next({ name: 'Login', query: {redirect: to.fullPath} })
                } 
                else if (store.state.wallet == null) {
                    next({ name: 'Wallets', query: {redirect: to.fullPath} })
                } 
                else {
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
                if (!store.state.token) {
                    next({ name: 'Login', query: {redirect: to.fullPath} })
                } 
                else if (store.state.wallet == null) {
                    next({ name: 'Wallets', query: {redirect: to.fullPath} })
                } 
                else {
                    next()
                }
            }
        },
        { 
            path: '/rozpocty/new',
            name: 'BudgetsNew',
            components: {
                default: BudgetsDetail,
                header: Header,
                navbar: Navbar
            },
            meta: {
                'name': 'Rozpočty'
            },
            beforeEnter: (to, from, next) => {
                if (!store.state.token) {
                    next({ name: 'Login', query: {redirect: to.fullPath} })
                } 
                else if (store.state.wallet == null) {
                    next({ name: 'Wallets', query: {redirect: to.fullPath} })
                } 
                else {
                    next()
                }
            }
        },
        { 
            path: '/rozpocty/:id',
            name: 'BudgetsDetail',
            components: {
                default: BudgetsDetail,
                header: Header,
                navbar: Navbar
            },
            meta: {
                'name': 'Rozpočty'
            },
            beforeEnter: (to, from, next) => {
                if (!store.state.token) {
                    next({ name: 'Login', query: {redirect: to.fullPath} })
                } 
                else if (store.state.wallet == null) {
                    next({ name: 'Wallets', query: {redirect: to.fullPath} })
                } 
                else {
                    next()
                }
            }
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
                if (!store.state.token) {
                    next({ name: 'Login', query: {redirect: to.fullPath} })
                } 
                else if (store.state.wallet == null) {
                    next({ name: 'Wallets', query: {redirect: to.fullPath} })
                } 
                else {
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
            beforeEnter: (to, from, next) => {
                if (!store.state.token) {
                    next({ name: 'Login', query: {redirect: to.fullPath} })
                } else {
                    next()
                }
            }
        },
        {
            path: '/penezenky/new',
            name: 'WalletsNew',
            components: {
                default: WalletsDetail,
                header: Header
            },
            beforeEnter: (to, from, next) => {
                if (!store.state.token) {
                    next({ name: 'Login', query: {redirect: to.fullPath} })
                } else {
                    next()
                }
            }
        },
        {
            path: '/penezenky/:id',
            name: 'WalletsDetail',
            components: {
                default: WalletsDetail,
                header: Header
            },
            beforeEnter: (to, from, next) => {
                if (!store.state.token) {
                    next({ name: 'Login', query: {redirect: to.fullPath} })
                } else {
                    next()
                }
            }
        },
        { 
            path: '/', 
            name: 'Home', 
            redirect: { name: 'Dashboard' }
        },
        {
            path: '/login',
            name: 'Login',
            component: Login
        }
    ],
    mode: 'history'
})

router.beforeEach((to, from, next) => {
    store.dispatch("toggleMenu", false)
    next()
})

export default router