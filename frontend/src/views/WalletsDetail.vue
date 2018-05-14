<template>
    <main class="section top">
        <section class="wallet-detail-wrapper">
            <div class="wallet-detail-form">
                <div class="wallet-detail-form-item">
                    <app-label class="label" for="wallet-name">Jméno</app-label>
                    <app-input v-model="wallet.name" class="input" id="wallet-name" type="text" />
                </div>
                <app-button class="button is-success" @click="createOrUpdateWallet" >
                    <span v-if="isNew">Přidat</span>
                    <span v-else>Upravit</span>
                </app-button>
            </div>
        </section>
    </main>
</template>


<script>
import { mapActions, mapState } from "vuex";

import AppDateInput from '@/components/AppDateInput.vue'
import AppButton from '@/components/AppButton.vue'
import AppInput from '@/components/AppInput.vue'
import AppLabel from '@/components/AppLabel.vue'
import AppSelect from '@/components/AppSelect.vue'

export default {
    data() {
        return {
            wallet: {
                name: ''
            },
            isNew: false
        }
    },
    computed: {
        ...mapState([
            'token',
            'wallets'
        ])
    },
    methods: {
        ...mapActions([
            'loadData',
            'refreshData'
        ]),
        createOrUpdateWallet() {
            const data = {
                name: this.wallet.name
            }
            if(this.isNew) {
                const url = '/wallets/'
                this.$axios.post(url, data, { headers: { Authorization: 'JWT ' + this.token }}).then(response => {
                    this.getWallets()
                    this.$router.push({name: 'Wallets'})
                })
            } else {
                const url = '/wallets/' + this.wallet.id + '/'
                this.$axios.patch(url, data, { headers: { Authorization: 'JWT ' + this.token }}).then(response => {
                    this.getWallets()
                    this.$router.push({name: 'Wallets'})
                })
            }
        },
        getWallets() {
            const url = '/wallets/'
            this.$axios.get(url, { headers: { Authorization: 'JWT ' + this.token }}).then(response => {
                this.setWallets(response.data)
            }).catch(error => {})
        },
    },
    components: {
        AppInput,
        AppLabel,
        AppSelect,
        AppButton
    },
    created() {
        const walletID = this.$route.params.id
        if (!walletID) this.isNew = true
        else if (Number(walletID)) {
            const wallet = this.wallets.find(x => x.id == walletID)
            this.wallet = Object.assign({}, wallet)
        } else this.$router.push("/")
    }
}
</script>


<style lang="stylus" scoped>

.wallet-detail-wrapper
    @media screen and (min-width: 768px)
        font-size: 20px
    
    display: flex
    flex-flow: column
    justify-content: center
    align-items: center
    width: 100%
    height: 100%
    padding-top: 20px
    
    & .button
        align-self: flex-end

.wallet-detail-form
    display: flex
    flex-flow: column
    
.wallet-detail-form-item
    margin-bottom: 20px

</style>
