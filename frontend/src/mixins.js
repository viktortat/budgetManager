import axios from 'axios'
import store from '@/store/store'

export const tokenCheck = {
    beforeRouteEnter(to, from, next) {
        const data = {
            token: store.state.token
        }
        const url = '/api/auth/verify/'
        axios.post(url, data).catch(err => {
            store.dispatch("logUserOut")
        })
        next()
    },
}