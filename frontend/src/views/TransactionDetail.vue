<template>
    <div class="section">
        <h1>Trn det</h1>
        <form class="form">
            <p><input type="text" class="input" v-model="transaction.id"></p>
            <p><input type="text" class="input" v-model="transaction.amount"></p>
            <p><input type="text" class="input" v-model="transaction.category"></p>
            <p><input type="text" class="input" v-model="transaction.date"></p>
            <p><input type="text" class="input" v-model="transaction.notes"></p>
            <p><input type="text" class="input" v-model="transaction.transaction_type"></p>
        </form>
    </div>
</template>

<script>
import axios from 'axios'

import { mapState, mapActions } from 'vuex'

export default {
    data() {
        return {
            transaction: {}
        }
    },
    computed: {
        ...mapState([
            'wallet',
            'transactions',
            'categories'
        ])
    },
    created() {
        if("id" in this.$route.params) {
            const transactionID = this.$route.params.id;
            if(this.$store.state.transactions.length == 0) {
                const url = "/api/transactions/" + transactionID + "/";
                axios.get(url, { headers: { Authorization: 'JWT ' + this.$store.state.token }}).then(res => {
                    this.transaction = res.data;
                }).catch(err => {
                    console.log(err);
                });
            } else {
                this.transaction = this.$store.state.transactions.find(x => x.id === transactionID)
            }
        }
    }
}
</script>

