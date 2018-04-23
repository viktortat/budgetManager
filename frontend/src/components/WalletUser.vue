<template>
    <div class="user-wrapper">
        <div>{{ user.email }}</div>
        <div v-if="!isOwner">
            <button class="button is-danger" @click="deleteCheck = !deleteCheck" v-if="!deleteCheck">Smazat</button>
            <button class="button is-danger" @click="removeUser()" v-else>Opravdu?</button>
        </div>
        <div v-else>
            Vlastník peněženky
        </div>
    </div>
</template>


<script>
import axios from 'axios'
import { mapState, mapActions } from 'vuex'

export default {
    props: ['user'],
    data() {
        return {
            deleteCheck: false,
        }
    },
    methods: {
        ...mapActions([
            'pickWallet'
        ]),
        removeUser() {
            let data = {
                'users_id': []
            }
            for(let user of this.wallet.users) {
                if(user.id !== this.user.id) data.users_id.push(user.id)
            }
            const url = '/api/wallets/' + this.wallet.id + '/'
            axios.patch(url, data, { headers: { Authorization: 'JWT ' + this.$store.state.token }}).then(res => {
                this.pickWallet(res.data)
                this.$notify({
                    text: 'Uživatel odebrán.',
                    type: 'success'
                })
            }).catch(err => {
                this.$notify({
                    text: 'Vyskytl se problém, zkuste to prosím později.',
                    type: 'error'
                })
            })
            this.deleteCheck = false
        }
    },
    computed: {
        ...mapState([
            'wallet'
        ]),
        isOwner() {
            return this.user.id === this.wallet.owner
        },
    },
}
</script>


<style lang="stylus" scoped>

.user-wrapper
    display: flex
    justify-content: space-between
    align-items: center
    padding: 10px
    margin-bottom: 10px
    height: 65px    

</style>
