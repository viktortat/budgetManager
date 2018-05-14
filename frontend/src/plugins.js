import Vue from 'vue'
import Notifications from 'vue-notification'

Vue.use(Notifications)


// my custom Modal plugin
import AppModal from '@/components/AppModal.vue'

export const Modal = {
    install(Vue) {
        this.EventBus = new Vue()

        Vue.component('app-modal', AppModal)

        Vue.prototype.$modal = {
            show(params) {
                Modal.EventBus.$emit('show', params)
            },
            hide() {
                Modal.EventBus.$emit('hide')
            }
        }
    }
}

Vue.use(Modal)
