<template>
    <div class="category" v-if="!editMode" @click="editMode = !editMode">
        <aside class="category-color" :style="{backgroundColor: category.color }"></aside>
        <h3 class="is-bold">{{ category.name }}</h3>
        <p>Transakcí: {{ category.transactions.length }}</p>
        <p class="is-bold" :class="{'is-success': Number(category.balance) > 0, 'is-danger': Number(category.balance) < 0 }">{{ category.balance | formatCurrency }}</p>
    </div>
    <div class="category" v-else-if="!menuMode">
        <button class="button" @click="close(false, false, false)">Zavřít</button>
        <button class="button is-success" @click="menuMode = !menuMode">Upravit</button>
        <div>
            <button class="button is-danger is-100" @click="deleteCheck = !deleteCheck" v-if="!deleteCheck">Smazat</button>
            <button class="button is-danger is-100" @click="deleteCategory()" v-else >Doopravdy?</button>
        </div>
    </div>
    <div class="category category-create" v-else>
        <p> 
            <label :for="'category-name-' + category.id" class="label">
                <p>Jméno kategorie</p>
            </label>
            <input type="text" :id="'category-name-' + category.id" class="input input-100" v-model="name">
        </p>
        <p>
            <label :for="'category-color-' + category.id" class="label">
                <p>Barva kategorie</p>
            </label>
            <input type="text" :id="'category-color-' + category.id" class="input input-100" v-model="color">
        </p>
        <div class="category-edit">
            <button class="button" @click="close(false, false, false)">Zavřít</button>
            <button class="button is-success" @click="editCategory()">Uložit</button>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

import { mapState, mapActions } from 'vuex';

export default {
    props: ['category'],
    data() {
        return {
            editMode: false,
            menuMode: false,
            deleteCheck: false,
            name: '',
            color: ''
        }
    },
    computed: {
        ...mapState([
            'wallet'
        ])
    },
    methods: {
        ...mapActions([
            'refreshData'
        ]),
        close(editMode, menuMode, deleteCheck) {
            this.editMode = editMode
            this.menuMode = menuMode
            this.deleteCheck = deleteCheck
            this.name = this.category.name
            this.color = this.category.color
        },
        deleteCategory() {
            const url = "/api/categories/" + this.category.id + "/"
            axios.delete(url, { headers: { Authorization: 'JWT ' + this.$store.state.token }}).then(res => {
                this.refreshData()
                this.close(false, false, false)
                this.$notify({
                    text: 'Kategorie byla smazána.',
                    type: 'success'
                });
            }).catch(err => {
                this.$notify({
                    text: 'Vyskytl se problém, zkuste to prosím později.',
                    type: 'error'
                });
            });      
        },
        editCategory() {
            const data = {
                'name': this.name,
                'color': this.color
            }
            const url = "/api/categories/" + this.category.id + "/"
            axios.patch(url, data, { headers: { Authorization: 'JWT ' + this.$store.state.token }}).then(res => {
                this.refreshData()
                this.close(false, false, false)
                this.$notify({
                    text: 'Kategorie byla upravena.',
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
    created() {
        this.name = this.category.name
        this.color = this.category.color
    }
}
</script>

<style lang="stylus" scoped>

.category-edit
    width: 100%
    display: flex
    justify-content: space-between

.category-color
    position: absolute
    left: 0
    top: 0
    width: 100%
    height: 4px

</style>
