import Vue from "vue"

Vue.filter('formatCurrency', value => {
    return value.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ' ').replace('.', ',') + ' Kč'
})
  
Vue.filter('shortenString', (value, lng) => {
    if (value.length > lng) return value.substring(0, lng).trim() + '...'
    else return value
})