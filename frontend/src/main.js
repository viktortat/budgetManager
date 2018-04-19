import Vue from 'vue'
import App from '@/App.vue'
import router from '@/router/router'
import store from '@/store/store'
import '@/registerServiceWorker'
import Notifications from 'vue-notification'
import axios from 'axios'
import moment from 'moment'

Vue.use(Notifications)

moment.locale('cs')

Vue.filter('formatCurrency', value => {
  return value.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ' ').replace('.', ',') + ' Kč'
})

axios.interceptors.response.use(response => {
  return response
}, error => {
  if(error.response.status === 401) {
    store.dispatch("logUserOut")
  }
  return Promise.reject(error)
});

router.beforeEach((to, from, next) => {
  store.dispatch("toggleMenu", 'false')
  next()
})

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')