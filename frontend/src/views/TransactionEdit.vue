<template>
    <div class="section transaction-detail-wrapper">
        <form class="transaction">
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
            <footer class="transaction-footer">
                <button class="button is-danger" @click.prevent="deleteCheck = !deleteCheck" v-if="!deleteCheck">Smazat</button>
                <button class="button is-danger" @click.prevent="deleteTransaction()" v-else>Opravdu?</button>
                <button class="button is-success" @click.prevent="editTransaction()">Uložit</button>
            </footer>
        </form>
    </div>
</template>

<script>
import axios from 'axios'

import { mapState, mapActions } from 'vuex'
import { tokenCheck } from '@/mixins.js'

import flatPickr from 'vue-flatpickr-component'
import 'flatpickr/dist/flatpickr.css'

export default {
    data() {
        return {
            transaction: {},
            deleteCheck: false
        }
    },
    methods: {
        ...mapActions([
            'loadData',
            'refreshData'
        ]),
        editTransaction() {
            const data = {
                'category': this.transaction.category,
                'amount': this.transaction.amount,
                'transaction_type': this.transaction.transaction_type,
                'notes': this.transaction.notes,
                'date': this.transaction.date
            }
            if (true) {
                const url = "/api/transactions/" + this.transaction.id + "/"
                axios.put(url, data, { headers: { Authorization: 'JWT ' + this.$store.state.token }}).then(res => {
                    this.refreshData()
                    this.$router.push({name: 'Transactions'})
                    this.$notify({
                        text: 'Transakce byla upravena.',
                        type: 'success'
                    });
                }).catch(err => {
                    this.$notify({
                        text: 'Vyskytl se problém, zkuste to prosím později.',
                        type: 'error'
                    });
                }); 
            }
            this.deleteCheck = false
        },
        deleteTransaction() {
            const url = "/api/transactions/" + this.transaction.id + "/"
            axios.delete(url, { headers: { Authorization: 'JWT ' + this.$store.state.token }}).then(res => {
                this.refreshData()
                this.$router.push({name: 'Transactions'})
                this.$notify({
                    text: 'Transakce byla smazána.',
                    type: 'success'
                });
            }).catch(err => {
                this.$notify({
                    text: 'Vyskytl se problém, zkuste to prosím později.',
                    type: 'error'
                });
            });          
        }
    },
    mixins: [tokenCheck],
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
        this.loadData();
    }
}
</script>

<style lang="stylus" scoped>
@import "../styles/variables.styl"

.transaction-detail-wrapper
    @media screen and (max-width: 767px)
        min-height: 100vh
        
    min-height: 100.06vh

    background-color: $background-color-primary

.transaction
    position: relative
    display: grid
    grid-template-columns: repeat(auto-fit, minmax(260px, 1fr))
    grid-gap: 10px
    padding-left: 20px
    padding-right: 20px
    padding-top: 20px
    padding-bottom: 75px
    margin-left: 10px
    margin-top: 10px
    margin-bottom: 10px
    margin-right: 10px

    background-color: #FFFFFF
    border-radius: $border-radius

.transaction-footer
    position: absolute
    bottom: 0
    left: 0
    width: 100%
    padding: 20px
    display: flex
    justify-content: space-between
    align-items: center

</style>
