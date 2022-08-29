<template>
  <div id = 'main'></div>
</template>

<script>
import * as echarts from 'echarts'
import axios from 'axios'
import $ from 'jquery'
// import SH from '@/puclic/static/data/上海市.json'
export default {

  data () {
    return {
      List: []
    }
  },
  created () {
    this.get_data()
  },
  mounted () {
    // this.init()
    // this.get_data()
  },
  methods: {
    async get_data () {
     const { data } = await axios.get('http://localhost:8888/api/sh_map')
     this.List = data
     console.log(data)
     this.init()
    },
    init () {
      var chartDom = document.getElementById('main')
      var myChart = echarts.init(chartDom)
      var option

      myChart.showLoading()
      $.get('static/data/上海市.json', function (geoJson) {
        console.log(geoJson)
        myChart.hideLoading()
        echarts.registerMap(
          'SH', geoJson
        )
      myChart.setOption(
      (option = {
        title: {
          text: '上海新增确诊分布',
          left: 'center',
          subtext: ''
        },
      tooltip: {
      },
      toolbox: {
        show: true,
        orient: 'vertical',
        left: 'right',
        top: 'center',
        feature: {
          dataView: { readOnly: false },
          restore: {},
          saveAsImage: {}
        }
      },
      visualMap: {
        type: 'piecewise',
        pieces: [
            { min: 39, max: 1000000, label: '大于等于40人', color: '#00CED1' },
            { min: 30, max: 39, label: '确诊30-39人', color: 'red' },
            { min: 20, max: 29, label: '确诊20-29人', color: '#006400' },
            { min: 10, max: 19, label: '确诊10-19人', color: '#ee7263' },
            { min: 1, max: 9, label: '确诊1-9人', color: '#f5bba7' },
             { min: 0, max: 0, label: '清零', color: '#EEB4B4' }
        ],
        color: ['#E0022B', '#E09107', '#A3E00B']
      },
      series: [
        {
          type: 'map',
          mapType: 'SH',
          zoom: 1.4,
          label: {
            show: true
          },
            roam: true,
            scaleLimit: {
            min: 1,
            max: 2
            // 自定义名称映射
          },
          data: [
                  { name: '浦东新区', value: 49 },
                  { name: '黄浦区', value: 27 },
                  { name: '徐汇区', value: 26 },
                  { name: '闵行区', value: 15 },
                  { name: '虹口区', value: 11 },
                  { name: '静安区', value: 17 },
                  { name: '宝山区', value: 34 },
                  { name: '长宁区', value: 6 },
                  { name: '杨浦区', value: 27 },
                  { name: '普陀区', value: 8 },
                  { name: '青浦区', value: 2 },
                  { name: '嘉定区', value: 4 },
                  { name: '松江区', value: 34 },
                  { name: '崇明区', value: 0 },
                  { name: '奉贤区', value: 0 },
                  { name: '金山区', value: 0 }
                ]

        }
      ]

    })
  )
})
       option && myChart.setOption(option)
    }
  }
}
</script>

<style lang='less' scoped>
  #main{
    width: 100%;
    height: 100%;
  }
</style>
