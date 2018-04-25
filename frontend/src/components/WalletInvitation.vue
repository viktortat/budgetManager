<template>
    <div class="user-wrapper">
        <div>{{ invitation.invited.email }}</div>
        <button class="button is-danger is-square" @click="cancelInvitation()"><i class="fas fa-times"></i></button>
    </div>
</template>


<script>
import { mapState, mapActions } from 'vuex'
import axios from 'axios'

export default {
    props: ['invitation'],
    methods: {
        cancelInvitation() {
            const data = {
                'id': this.invitation.id
            }
            const url = '/api/invitations/resolve/'
            axios.patch(url, data, { headers: { Authorization: 'JWT ' + this.$store.state.token }}).then(res => {
                this.$notify({
                    text: 'Pozvánka zrušena.',
                    type: 'success'
                })
                this.$emit('reloadInvitations')
            })
        }
    },
    computed: {
        ...mapState([
            'wallet'
        ]),
    },
}
</script>
