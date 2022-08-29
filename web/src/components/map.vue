<template>
  <div class="main-map-chart">
    </div>
</template>
<script>
import axios from 'axios'
let chart = null
export default {

  props: {
    list: Array
  },
  data () {
    return {
      List: [],
      config: {},
      title: '中国疫情分布图'
    }
  },
  created () {
    this.get_data()
  },

  methods: {
    async get_data () {
      const { data } = await axios.get('http://localhost:8888/api/map')
      this.List = data
      console.log(this.List)
      this.initChart()
    },
    initChart () {
      if (chart != null && undefined !== chart) {
        chart.dispose()
      }
      const mychart = document.querySelector('.main-map-chart')
      chart = this.$echarts.init(mychart)
      this.setOptions()
    },
    setOptions () {
    const option = {
    title: {
        text: '中国疫情图',
        left: 'center'
    },
    tooltip: {
        trigger: 'item'
    },
    legend: {
        orient: 'vertical',
        left: 'left',
        data: ['中国疫情图']
    },
    visualMap: {
        type: 'piecewise',
        pieces: [
            { min: 1000, max: 1000000, label: '大于等于1000人', color: '#372a28' },
            { min: 500, max: 999, label: '确诊500-999人', color: '#4e160f' },
            { min: 100, max: 499, label: '确诊100-499人', color: '#974236' },
            { min: 10, max: 99, label: '确诊10-99人', color: '#ee7263' },
            { min: 1, max: 9, label: '确诊1-9人', color: '#f5bba7' },
            { min: 0, max: 0, label: '清零', color: '#ccc' }
        ],
        color: ['#E0022B', '#E09107', '#A3E00B']
    },
    toolbox: {
        show: true,
        orient: 'vertical',
        left: 'right',
        top: 'center',
        feature: {
            mark: { show: true },
            dataView: { show: true, readOnly: false },
            restore: { show: true },
            saveAsImage: { show: true }
        }
    },
    roamController: {
        show: true,
        left: 'right',
        mapTypeControl: {
            china: true
        }
    },
    series: [
        {
                    zoom: 1.2,
                    roam: true,
                    itemStyle: {
                        normal: {
                            label: {
                                show: true,
                                textStyle: { color: 'rgb(249, 249, 249)' }
                            }
                        },
                        emphasis: {
                            label: { show: true }
                        }
                    },
            name: '确诊数',
            type: 'map',
            // eslint-disable-next-line no-dupe-keys
            mapType: 'china',
            // eslint-disable-next-line no-dupe-keys
            roam: true,
            label: {
                show: true,
                color: 'rgb(249, 249, 249)'
            },
            data: this.List
        }]
        }
       chart.setOption(option)
      }
  },
  watch: {
  List: {
      handler (newValue, oldValue) {
        if (oldValue !== newValue) {
          this.setOptions()
        }
      },
      deep: true
    }
  }
}
</script>

<style scoped>
  .main-map-chart{
    width: 100%;
    height: 100%;
  }
</style>
