import Vue from 'vue'
import App from '@/App.vue'
import router from '@/router/router'
import store from '@/store/store'
import axios from 'axios'
import '@/registerServiceWorker'
import Notifications from 'vue-notification'
import VueSweetalert2 from 'vue-sweetalert2';

Vue.use(Notifications)
Vue.use(VueSweetalert2)

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')

Vue.filter('formatCurrency', value => {
  return value.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ' ').replace('.', ',') + ' Kč'
})
