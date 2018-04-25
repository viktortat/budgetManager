import { Pie, mixins } from 'vue-chartjs'
const { reactiveProp } = mixins

export default {
    mixins: [reactiveProp],
    extends: Pie,
    props: ['options'],
    mounted() {
        this.renderChart(this.chartData, this.options)
    }
}