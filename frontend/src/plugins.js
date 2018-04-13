import Notification from '@/components/Notification.vue'

const testPlugin = {
    install(Vue, options) {
        Vue.component('notifications', Notification)
    }
}

export default testPlugin
