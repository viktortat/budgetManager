<template>
    <div class="section transaction-detail-wrapper">
        <div class="transaction">
            <form>
                <p>
                    <label for="transaction-amount" class="label">
                        <p>Částka</p>                     
                    </label>
                    <input id="transaction-amount" type="number" class="input input-100" v-model="transaction.amount">
                </p>
                <p>
                    <label for="transaction-category" class="label">
                        <p>Kategorie</p>                     
                    </label>
                    <select id="transaction-category" class="input input-100" v-model="transaction.category">
                        <option v-for="category in categories" :key="category.id" :value="category.id">{{ category.name }}</option>
                    </select>
                </p>
                <p>
                    <label for="transaction-date" class="label">
                        <p>Datum</p>                     
                    </label>
                    <flat-pickr id="transaction-date" v-model="transaction.date" class="input input-100"></flat-pickr>
                </p>
                <p>
                    <label for="transaction-notes" class="label">
                        <p>Poznámka</p>                     
                    </label>
                    <input id="transaction-notes" type="text" class="input input-100" v-model="transaction.notes">
                </p>
                <p>
                    <label for="transaction-type" class="label">
                        <p>Typ transakce</p>                     
                    </label>
                    <select id="transaction-type" class="input input-100" v-model="transaction.transaction_type">
                        <option value="income">Příjem</option>
                        <option value="expense">Výdej</option>
                    </select>
                </p>
                <button class="button is-success" @click.prevent="sendTransaction()">Přidat</button>
            </form>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

import { mapState, mapActions } from 'vuex'

import flatPickr from 'vue-flatpickr-component'
import 'flatpickr/dist/flatpickr.css'

export default {
    data() {
        return {
            transaction: {
                'amount': '',
                'transaction_type': '',
                'notes': '',
                'date': '',
                'category': ''
            }
        }
    },
    methods: {
        ...mapActions([
            'loadData'
        ]),
        sendTransaction() {
            const data = {
                'category': this.transaction.category,
                'amount': this.transaction.amount,
                'transaction_type': this.transaction.transaction_type,
                'notes': this.transaction.notes,
                'date': this.transaction.date
            };

        }
    },
    computed: {
        ...mapState([
            'wallet',
            'transactions',
            'categories'
        ])
    },
    components: {
        flatPickr
    },
    created() {
        if("id" in this.$route.params) {
            const transactionID = this.$route.params.id;
            if(this.$store.state.transactions.length == 0) {
                const url = "/api/transactions/" + transactionID + "/";
                axios.get(url, { headers: { Authorization: 'JWT ' + this.$store.state.token }}).then(res => {
                    this.transaction = res.data;
                }).catch(err => {});
            } else {
                const transaction = this.$store.state.transactions.find(x => x.id === transactionID);
                this.transaction = Object.assign({}, transaction);
            }
        }
        this.loadData();
    }
}
</script>

<style lang="stylus" scoped>
@import "../styles/variables.styl"

.transaction-detail-wrapper
    min-height: 100.06vh

    background-color: $background-color-primary

.transaction-edit
    width: 320px
    padding-left: 20px
    padding-right: 20px
    padding-top: 20px
    padding-bottom: 20px

    background-color: #FFFFFF
    border-radius: $border-radius
</style>
