import { Line, mixins } from 'vue-chartjs'
const { reactiveProp } = mixins

export default {
    mixins: [reactiveProp],
    extends: Line,
    props: ['options'],
    mounted() {
        this.renderChart(this.chartData, this.options)
    }
}