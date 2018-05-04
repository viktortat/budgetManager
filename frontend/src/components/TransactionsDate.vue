<template>
    <section class="transactions-date-wrapper">
        <div class="transactions-date-arrow" @click="subtractDate()">
            <icon name="chevron-left" />
        </div>
        <div>
            <span v-if="isMonth()">
                {{ this.$moment(filter.dateFrom).format('MMMM') }}
            </span>
            <span v-else-if="isYear()">
                {{ this.$moment(filter.dateFrom).format('YYYY') }}
            </span>
            <span v-else>
                {{ this.$moment(filter.dateFrom).format('DD.MM.YYYY') }} - {{ this.$moment(filter.dateTo).format('DD.MM.YYYY') }}
            </span>
        </div>
        <div class="transactions-date-arrow" @click="addDate()">
            <icon name="chevron-right" />
        </div>
    </section>
</template>


<script>
import { mapState, mapMutations } from 'vuex'

export default {
    computed: {
        ...mapState([
            'filter'
        ])
    },
    methods: {
        ...mapMutations([
            'updateDateFrom',
            'updateDateTo'
        ]),
        updateDates(dateFrom, dateTo) {
            this.updateDateFrom(dateFrom)
            this.updateDateTo(dateTo)
        },
        subtractDate() {
            let dateFrom = this.$store.state.filter.dateFrom
            let dateTo = this.$store.state.filter.dateTo

            if(this.isMonth()) {
                dateTo = this.$moment(dateTo).subtract(1, 'months').endOf('month').format('YYYY-MM-DD')
                dateFrom = this.$moment(dateFrom).subtract(1, 'months').startOf('month').format('YYYY-MM-DD')
            } else if (this.isYear()) {
                dateTo = this.$moment(dateTo).subtract(1, 'years').endOf('year').format('YYYY-MM-DD')
                dateFrom = this.$moment(dateFrom).subtract(1, 'years').startOf('year').format('YYYY-MM-DD')
            } else {
                let difference = this.$moment.duration(this.$moment(dateTo).diff(this.$moment(dateFrom))).asDays()
                if (difference === 0) difference = 1
                dateTo = this.$moment(dateTo).subtract(difference, 'days').format('YYYY-MM-DD')
                dateFrom = this.$moment(dateFrom).subtract(difference, 'days').format('YYYY-MM-DD')
            }

            this.updateDates(dateFrom, dateTo)
        },
        addDate() {
            let dateFrom = this.$store.state.filter.dateFrom
            let dateTo = this.$store.state.filter.dateTo

            if(this.isMonth()) {
                dateTo = this.$moment(dateTo).add(1, 'months').endOf('month').format('YYYY-MM-DD')
                dateFrom = this.$moment(dateFrom).add(1, 'months').startOf('month').format('YYYY-MM-DD')
            } else if (this.isYear()) {
                dateTo = this.$moment(dateTo).add(1, 'years').endOf('year').format('YYYY-MM-DD')
                dateFrom = this.$moment(dateFrom).add(1, 'years').startOf('year').format('YYYY-MM-DD')
            } else {
                let difference = this.$moment.duration(this.$moment(dateTo).diff(this.$moment(dateFrom))).asDays()
                if (difference === 0) difference = 1
                dateTo = this.$moment(dateTo).add(difference, 'days').format('YYYY-MM-DD')
                dateFrom = this.$moment(dateFrom).add(difference, 'days').format('YYYY-MM-DD')
            }        
            
            this.updateDates(dateFrom, dateTo)
        },
        isMonth() {
            const dateFrom = this.$store.state.filter.dateFrom
            const dateTo = this.$store.state.filter.dateTo

            const startOfPeriod = this.$moment(dateFrom).startOf('month').format('YYYY-MM-DD')
            const endtOfPeriod = this.$moment(dateTo).endOf('month').format('YYYY-MM-DD')
            const diference = this.$moment.duration(this.$moment(endtOfPeriod).diff(this.$moment(startOfPeriod))).asDays()

            return this.$moment(startOfPeriod).isSame(this.$moment(dateFrom)) && this.$moment(endtOfPeriod).isSame(this.$moment(dateTo)) && diference > 26 && diference < 32
        },
        isYear() {
            const dateFrom = this.$store.state.filter.dateFrom
            const dateTo = this.$store.state.filter.dateTo

            const startOfPeriod = this.$moment(dateFrom).startOf('year').format('YYYY-MM-DD')
            const endtOfPeriod = this.$moment(dateTo).endOf('year').format('YYYY-MM-DD')
            const diference = this.$moment.duration(this.$moment(endtOfPeriod).diff(this.$moment(startOfPeriod))).asDays()

            return this.$moment(startOfPeriod).isSame(this.$moment(dateFrom)) && this.$moment(endtOfPeriod).isSame(this.$moment(dateTo)) && diference > 360 && diference < 370
        },
    }
}
</script>


<style lang="stylus" scoped>
@import '../styles/variables'

$border-color = #D9D9D9

.transactions-date-wrapper
    @media screen and (min-width: 768px)
        font-size: 20px
        width: calc(100% - 208px)

    position: fixed
    top: 56px
    height: 2em
    width: 100%
    display: flex
    justify-content: space-between
    align-items: center
    z-index: 50

    border-bottom: 1px solid $border-color
    background-color: #FFFFFF

.transactions-date-arrow
    @media screen and (min-width: 768px)
        cursor: pointer

    height: 2em
    width: 2em
    display: flex
    justify-content: center
    align-items: center    

</style>
