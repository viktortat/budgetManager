import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import './registerServiceWorker'

import Chart from 'chart.js'

Chart.defaults.global.defaultFontColor = '#4D4D4D'
Chart.defaults.global.defaultFontFamily = "'Montserrat', sans-serif"

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')

Vue.filter('formatCurrency', value => {
  return value.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ' ').replace('.', ',') + ' Kč'
})
