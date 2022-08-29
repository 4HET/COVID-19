<template>
  <div id="help">
  </div>
</template>

<script>
import * as echarts from 'echarts'
import axios from 'axios'
export default {
  props: {
    help_list: Array
  },
  data () {
    return {
      List: []
    }
  },

  created () {
    // this.get()
  },

    mounted () {
    // this.get()
    this.init()
  },

  methods: {
   async get () {
     const { data } = await axios.get('static/data/help.json')
     this.List = data
     console.log(this.List[0].area)
     console.log(this.List[0].data)
    },
    init  () {
      var chartDom = document.getElementById('help')
      var myChart = echarts.init(chartDom)
      const option = {
      legend: {
        top: 'bottom'
      },
      title: {
          text: '支援上海分布',
          left: 'center',
          subtext: '',
          textStyle: {
          color: 'rgb(100,200,55)',
          fontStyle: 'normal',
          fontWeight: 'bold',
          fontFamily: 'sans-serif',
          fontSize: 18
    }
        },
      toolbox: {
        show: true,
        feature: {
          mark: { show: true },
          dataView: { show: true, readOnly: false },
          restore: { show: true },
          saveAsImage: { show: true }
        }
      },
      series: [
        {
          name: 'Nightingale Chart',
          type: 'pie',
          radius: [50, 150],
          center: ['50%', '50%'],
          roseType: 'area',
          itemStyle: {
            borderRadius: 8
          },
          data: [
            { value: 14000, name: '江苏' },
            { value: 11000, name: '浙江' },
            { value: 6000, name: '安徽' },
            { value: 1911, name: '福建' },
            { value: 1871, name: '陕西' },
            { value: 1800, name: '北京' },
            { value: 1771, name: '河南' },
            { value: 1600, name: '重庆' },
            { value: 1590, name: '天津' },
            { value: 1500, name: '甘肃' },
            { value: 1396, name: '湖北' },
            { value: 1333, name: '江西' },
            { value: 1260, name: '广西' },
            { value: 1100, name: '海南' },
            { value: 1040, name: '山东' },
            { value: 979, name: '云南' },
            { value: 712, name: '湖南' },
            { value: 400, name: '贵州' },
            { value: 300, name: '广东' },
            { value: 204, name: '四川' },
            { value: 200, name: '辽宁' },
            { value: 180, name: '河北' },
            { value: 1034, name: '黑龙江' },
            { value: 200, name: '山西' }
          ]
        }
      ]
}
        option && myChart.setOption(option)
        }
  }

}
</script>

<style lang="less" scoped>
  #help {
      margin: 5px auto;
      width: 95%;
      height: 95%;
      border-radius: 20px;
  }
</style>
