import createPersistedState from 'vuex-persistedstate'

export const plugins = [
    createPersistedState({
        paths: ['token', 'isUserLoggedIn', 'user'],
    })
]
