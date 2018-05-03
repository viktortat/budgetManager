<template>
    <section class="filter-wrapper" v-if="isFilterActive">
        <div>
            <app-label class="label" for="filter-date-from">DateFrom</app-label>
            <app-date-input class="input" id="filter-date-from" v-model="dateFrom"></app-date-input>
        </div>
        <div>
            <app-label class="label" for="filter-date-to">DateTo</app-label>
            <app-date-input class="input" id="filter-date-to" v-model="dateTo"></app-date-input>
        </div>
        <app-button class="button is-link" @click="setFilterDate('thisMonth')">tento měsíc</app-button>
        <app-button class="button is-link" @click="setFilterDate('lastMonth')">minulý měsíc</app-button>
        <app-button class="button is-link" @click="setFilterDate('thisYear')">současný rok</app-button>
        <app-button class="button is-link" @click="setFilterDate('lastYear')">minulý rok</app-button>
        <div>
            <app-label class="label" for="filter-date-type">Type</app-label>
            <app-select class="input" id="filter-date-type" v-model="type">
                <option value="expense">Výdej</option>
                <option value="income">Příjem</option>
            </app-select>
        </div>
        <app-button class="button is-danger" @click="resetFilter()">Reset</app-button>
        <app-button class="button is-success" @click="setIsFilterActive(false)">Zavřít</app-button>
    </section>
</template>


<script>
import { mapState, mapMutations } from 'vuex'

import AppDateInput from '@/components/AppDateInput.vue'
import AppButton from '@/components/AppButton.vue'
import AppInput from '@/components/AppInput.vue'
import AppLabel from '@/components/AppLabel.vue'
import AppSelect from '@/components/AppSelect.vue'

export default {
    computed: {
        ...mapState([
            'isFilterActive'
        ]),
        dateFrom: {
            get() {
                return this.$store.state.filter.dateFrom
            },
            set(value) {
                this.updateDateFrom(value)
            }
        },
        dateTo: {
            get() {
                return this.$store.state.filter.dateTo
            },
            set(value) {
                this.updateDateTo(value)
            }            
        },
        type: {
            get() {
                return this.$store.state.filter.type
            },
            set(value) {
                this.updateType(value)
            }               
        }
    },
    methods: {
        ...mapMutations([
            'setIsFilterActive',
            'updateDateTo',
            'updateDateFrom',
            'updateType',
            'resetFilter'
        ]),
        setFilterDate(value) {
            switch(value) {
                case 'thisMonth':
                    this.updateDateFrom(this.$moment().startOf('month').format('YYYY-MM-DD'))
                    this.updateDateTo(this.$moment().endOf('month').format('YYYY-MM-DD'))
                    break
                case 'lastMonth':
                    this.updateDateFrom(this.$moment().subtract(1, 'months').startOf('month').format('YYYY-MM-DD'))
                    this.updateDateTo(this.$moment().subtract(1, 'months').endOf('month').format('YYYY-MM-DD'))
                    break
                case 'thisYear':
                    this.updateDateFrom(this.$moment().startOf('year').format('YYYY-MM-DD'))
                    this.updateDateTo(this.$moment().endOf('year').format('YYYY-MM-DD'))
                    break
                case 'lastYear':
                    this.updateDateFrom(this.$moment().subtract(1, 'years').startOf('year').format('YYYY-MM-DD'))
                    this.updateDateTo(this.$moment().subtract(1, 'years').endOf('year').format('YYYY-MM-DD'))
                    break
            }
        }
    },
    components: {
        AppButton,
        AppInput,
        AppLabel,
        AppDateInput,
        AppSelect
    },
}
</script>


<style lang="stylus" scoped>

.filter-wrapper
    position: fixed
    z-index: 100
    top: 0
    bottom: 0
    left: 0
    right: 0
    display: flex
    flex-flow: column
    align-items: center
    justify-content: space-around

    background-color: white

</style>
