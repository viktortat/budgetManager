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

new Vue({
    router,
    store,
    render: h => h(App)
}).$mount('#app')