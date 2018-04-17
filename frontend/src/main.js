import Vue from 'vue'
import App from '@/App.vue'
import router from '@/router/router'
import store from '@/store/store'
import axios from 'axios'
import '@/registerServiceWorker'
import Notifications from 'vue-notification'
import moment from 'moment'

Vue.use(Notifications)

moment.locale('cs')

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')

Vue.filter('formatCurrency', value => {
  return value.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ' ').replace('.', ',') + ' Kč'
})

axios.interceptors.response.use(response => {
  return response
}, error => {
  console.log(error)
  if(error.response.status === 401) {
    store.dispatch("logUserOut")
  }
  return Promise.reject(error)
});