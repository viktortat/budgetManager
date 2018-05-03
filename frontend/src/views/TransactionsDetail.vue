<template>
    <main class="section">
        {{ transaction }}
    </main>
</template>


<script>
import { mapActions, mapState } from "vuex";

import AppButton from '@/components/AppButton.vue'
import AppInput from '@/components/AppInput.vue'
import AppLabel from '@/components/AppLabel.vue'

export default {
    data() {
        return {
            transaction: {
                'amount': '',
                'transaction_type': '',
                'notes': '',
                'date': this.$moment().format('YYYY-MM-DD'),
                'category': ''
            }
        }
    },
    computed: {
        ...mapState([

        ])
    },
    methods: {
        ...mapActions([
            'loadData'
        ])
    },
    components: {
        AppButton,
        AppInput,
        AppLabel
    },
    created() {
        this.loadData()
        const transactionID = this.$route.params.id
        if (!transactionID) console.log("new")
        else if (Number(transactionID)) {
            const transaction = this.$store.state.transactions.find(x => x.id == transactionID)
            this.transaction = Object.assign({}, transaction)
        } else this.$router.push("/")
    }
}
</script>
