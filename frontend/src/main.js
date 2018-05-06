import Vue from 'vue'
import App from '@/App.vue'
import router from '@/router/router'
import store from '@/store/store'
import '@/filters'
import '@/registerServiceWorker'

import Notifications from 'vue-notification'
import axios from 'axios'
import moment from 'moment'

Vue.use(Notifications)

axios.defaults.baseURL = '/api/';
Vue.prototype.$axios = axios

axios.interceptors.response.use(response => {
        return response
    }, 
    error => {
        if(error.response.status === 401) {
            store.dispatch("logUserOut")
        }
        return Promise.reject(error)
    }
)

moment.locale('cs')
Vue.prototype.$moment = moment

router.beforeEach((to, from, next) => {
    store.dispatch("toggleMenu", false)
    next()
})

// Font awesome
import 'vue-awesome/icons/trash'
import 'vue-awesome/icons/chevron-left'
import 'vue-awesome/icons/chevron-right'
import 'vue-awesome/icons/pencil-alt'
import 'vue-awesome/icons/times'
import 'vue-awesome/icons/bars'
import 'vue-awesome/icons/filter'
import 'vue-awesome/icons/chart-area'
import 'vue-awesome/icons/credit-card'
import 'vue-awesome/icons/list'
import 'vue-awesome/icons/cogs'
import 'vue-awesome/icons/sign-out-alt'
import 'vue-awesome/icons/archive'
import 'vue-awesome/icons/dollar-sign'
import 'vue-awesome/icons/ellipsis-v'
import Icon from 'vue-awesome/components/Icon'
Vue.component('icon', Icon)

new Vue({
    router,
    store,
    render: h => h(App)
}).$mount('#app')