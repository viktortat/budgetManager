<template>
    <div class="section">
        <h1>Trn det</h1>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    data() {
        return {
            transaction: {}
        }
    },
    created() {
        const transactionID = this.$route.params.id;
        const url = "/api/transactions/" + transactionID + "/";
        axios.get(url, { headers: { Authorization: 'JWT ' + this.$store.state.token }}).then(res => {
            console.log(res);
            this.transaction = res.data;
        }).catch(err => {
            console.log(err);
        });
    }
}
</script>

