<template>
    <div ref="chart" class="ct-chart" :class="[ratio]"></div>
</template>

<script>
import Chartist from 'chartist'
import 'chartist/dist/chartist.min.css'

export default {
  props: {
    type: {
      type: String,
      default: 'Line',
      validator (value) {
        return ['Pie', 'Line', 'Bar'].indexOf(value) !== -1
      }
    },
    data: {
      type: Object,
      required: true
    },
    options: {
      type: Object
    },
    ratio: {
      type: String
    },
    responsiveOptions: {
      type: Array
    }
  },
  data () {
    return {
      chartist: undefined
    }
  },
  watch: {
    data: {
      handler: 'renderChart',
      deep: true
    },
    options: {
      handler: 'renderChart',
      deep: true
    },
    responsiveOptions: {
      handler: 'renderChart',
      deep: true
    }
  },
  methods: {
    renderChart () {
      const data = this.data
      const options = this.options ? this.options : {}
      const responsiveOptions = this.responsiveOptions ? this.responsiveOptions : []

      if (this.chartist) {
        this.chartist.update(data, options, responsiveOptions)
      } else {
        this.chartist = new Chartist[this.type](this.$refs.chart, data, options, responsiveOptions)
      }
    }
  },
  mounted () {
    this.renderChart()
  },
  destroyed () {
    if (this.chartist) {
      this.chartist.detach()
    }
  }
}
</script>
