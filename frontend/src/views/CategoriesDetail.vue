<template>
    <main class="section">
        <section class="category-detail-wrapper">
            <div class="category-detail-form">
                <div class="category-detail-form-item">
                    <app-label class="label" for="category-name">Jméno</app-label>
                    <app-input v-model="category.name" class="input" id="category-name" type="text" />
                </div>
                <div class="category-detail-form-item">
                    <app-label class="label" for="category-color">Barva</app-label>
                    <app-colorpicker v-model="category.color" id="category-color"></app-colorpicker>
                </div>
                <app-button class="button is-success" @click="createOrUpdateCategory" >
                    <span v-if="isNew">Přidat</span>
                    <span v-else>Upravit</span>
                </app-button>
            </div>
        </section>
    </main>
</template>


<script>
import { mapActions, mapState, mapMutations } from "vuex";

import AppDateInput from '@/components/AppDateInput.vue'
import AppButton from '@/components/AppButton.vue'
import AppInput from '@/components/AppInput.vue'
import AppLabel from '@/components/AppLabel.vue'
import AppSelect from '@/components/AppSelect.vue'
import AppColorpicker from '@/components/AppColorpicker.vue'

export default {
    data() {
        return {
            category: {
                name: '',
                color: ''
            },
            isNew: false
        }
    },
    computed: {
        ...mapState([
            'categories',
            'token',
            'wallet'
        ])
    },
    methods: {
        ...mapMutations([
            'addCategory'
        ]),
        ...mapActions([
            'loadData',
            'refreshData'
        ]),
        createOrUpdateCategory() {
            const data = {
                name: this.category.name,
                color: this.category.color,
                wallet: this.wallet.id
            }
            if(this.isNew) {
                const url = '/categories/'
                this.$axios.post(url, data, { headers: { Authorization: 'JWT ' + this.token }}).then(response => {
                    this.refreshData()
                    this.resetCategory()
                })
            } else {
                const url = '/categories/' + this.category.id + '/'
                this.$axios.patch(url, data, { headers: { Authorization: 'JWT ' + this.token }}).then(response => {
                    this.refreshData()
                    this.$router.push({name: 'Categories'})
                }).catch(error => {
                    console.log(error.response)
                })
            }
        },
        resetCategory() {
            this.category.name = ''
            this.category.color = ''
        }
    },
    components: {
        AppButton,
        AppInput,
        AppLabel,
        AppDateInput,
        AppSelect,
        AppColorpicker
    },
    created() {
        this.loadData()
        const categoryID = this.$route.params.id
        if (!categoryID) this.isNew = true
        else if (Number(categoryID)) {
            const category = this.$store.state.categories.find(x => x.id == categoryID)
            this.category = Object.assign({}, category)
        } else this.$router.push("/")
    }
}
</script>


<style lang="stylus" scoped>

.category-detail-wrapper
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

.category-detail-form
    display: flex
    flex-flow: column
    
.category-detail-form-item
    margin-bottom: 20px

</style>
