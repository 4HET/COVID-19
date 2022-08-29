<template>
  <div class="container">
  </div>
</template>

<script>
import axios from 'axios'
let chart = null
export default {
  data () {
    return {
      List: [],
      length: 0,
      list: [],
      data: [],
      confirm: [],
      suspect: [],
      heal: [],
      dead: [],
      suspect_add: [],
      confirm_add: [],
      heal_add: [],
      dead_add: []
    }
  },
  mounted () {
    this.initchart()
  },
  created () {
    this.get()
  },

  methods: {
    async get () {
      const { data } = await axios.get('http://localhost:8888/api/trend')
      this.List = data
      console.log(data)

      for (var it in data) {
        this.length++
        this.data.push(it)
        this.confirm.push(data[it].confirm)
        this.suspect.push(data[it].suspect)
        this.heal.push(data[it].heal)
        this.dead.push(data[it].dead)
        this.suspect_add.push(data[it].suspect_add)
        this.confirm_add.push(data[it].confirm_add)
        this.heal_add.push(data[it].heal_add)
        this.dead_add.push(data[it].dead_add)
      }
      this.data = this.data.filter((value, index) => {
        if (this.length - index <= 7) {
          return value
        }
       })
       this.confirm = this.confirm.filter((value, index) => {
        if (this.length - index <= 7) {
          return value
        }
       })
        this.suspect = this.suspect.filter((value, index) => {
        if (this.length - index <= 7) {
          return value
        }
       })
        this.heal = this.heal.filter((value, index) => {
        if (this.length - index <= 7) {
          return value
        }
       })
        this.dead = this.dead.filter((value, index) => {
        console.log(this.length)
        if (this.length - index <= 7) {
          return value
        }
       })
        this.suspect_add = this.suspect_add.filter((value, index) => {
        console.log(this.length)
        if (this.length - index <= 7) {
          return value
        }
       })
        this.confirm_add = this.confirm_add.filter((value, index) => {
        console.log(this.length)
        if (this.length - index <= 7) {
          return value
        }
       })
        this.heal_add = this.heal_add.filter((value, index) => {
        console.log(this.length)
        if (this.length - index <= 7) {
          return value
        }
       })
        this.dead_add = this.dead_add.filter((value, index) => {
        console.log(this.length)
        if (this.length - index <= 7) {
          return value
        }
       })
       this.initchart()
    },
    initchart () {
      chart = this.$echarts.init(document.querySelector('.container'))
      this.setOptions()
    },
    setOptions () {
      const option = {
        color: ['#80FFA5', '#00DDFF', '#37A2FF', '#FF0087', '#FFBF00'],
        title: {
          // text: '一周内疫情形式变化'
        },
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'cross',
            label: {
              backgroundColor: '#6a7985'
            }
          }
        },
        legend: {
          data: ['确诊', '怀疑', '治愈', '死亡', '怀疑增加', '确诊增加', '治愈增加', '死亡增加']
        },
        toolbox: {
          feature: {
            saveAsImage: {}
          }
        },
        grid: {
          left: '3%',
          right: '4%',
          bottom: '3%',
          containLabel: true
        },
        xAxis: [
          {
            type: 'category',
            boundaryGap: false,
            data: this.data
          }
        ],
        yAxis: [
          {
            type: 'value'
          }
        ],
        series: [
          {
            name: '确诊',
            type: 'line',
            stack: 'Total',
            smooth: true,
            lineStyle: {
              width: 0
            },
            showSymbol: false,
            areaStyle: {
              opacity: 0.8,
              color: new this.$echarts.graphic.LinearGradient(0, 0, 0, 1, [
                {
                  offset: 0,
                  color: 'rgb(128, 255, 165)'
                },
                {
                  offset: 1,
                  color: 'rgb(1, 191, 236)'
                }
              ])
            },
            emphasis: {
              focus: 'series'
            },
            data: this.confirm
          },
          {
            name: '怀疑',
            type: 'line',
            stack: 'Total',
            smooth: true,
            lineStyle: {
              width: 0
            },
            showSymbol: false,
            areaStyle: {
              opacity: 0.8,
              color: new this.$echarts.graphic.LinearGradient(0, 0, 0, 1, [
                {
                  offset: 0,
                  color: 'rgb(0, 221, 255)'
                },
                {
                  offset: 1,
                  color: 'rgb(77, 119, 255)'
                }
              ])
            },
            emphasis: {
              focus: 'series'
            },
            data: [120, 282, 111, 234, 220, 340, 310]
          },
          {
            name: '治愈',
            type: 'line',
            stack: 'Total',
            smooth: true,
            lineStyle: {
              width: 0
            },
            showSymbol: false,
            areaStyle: {
              opacity: 0.8,
              color: new this.$echarts.graphic.LinearGradient(0, 0, 0, 1, [
                {
                  offset: 0,
                  color: 'rgb(55, 162, 255)'
                },
                {
                  offset: 1,
                  color: 'rgb(116, 21, 219)'
                }
              ])
            },
            emphasis: {
              focus: 'series'
            },
            data: [320, 132, 201, 334, 190, 130, 220]
          },
          {
            name: '死亡',
            type: 'line',
            stack: 'Total',
            smooth: true,
            lineStyle: {
              width: 0
            },
            showSymbol: false,
            areaStyle: {
              opacity: 0.8,
              color: new this.$echarts.graphic.LinearGradient(0, 0, 0, 1, [
                {
                  offset: 0,
                  color: 'rgb(255, 0, 135)'
                },
                {
                  offset: 1,
                  color: 'rgb(135, 0, 157)'
                }
              ])
            },
            emphasis: {
              focus: 'series'
            },
            data: [220, 402, 231, 134, 190, 230, 120]
          },
          {
            name: '怀疑增加',
            type: 'line',
            stack: 'Total',
            smooth: true,
            lineStyle: {
              width: 0
            },
            showSymbol: false,
            label: {
              show: true,
              position: 'top'
            },
            areaStyle: {
              opacity: 0.8,
              color: new this.$echarts.graphic.LinearGradient(0, 0, 0, 1, [
                {
                  offset: 0,
                  color: 'rgb(255, 101, 0)'
                },
                {
                  offset: 1,
                  color: 'rgb(24, 62, 76)'
                }
              ])
            },
            emphasis: {
              focus: 'series'
            },
            data: [220, 302, 181, 234, 210, 290, 150]
          },
          {
            name: '确诊增加',
            type: 'line',
            stack: 'Total',
            smooth: true,
            lineStyle: {
              width: 0
            },
            showSymbol: false,
            label: {
              show: true,
              position: 'top'
            },
            areaStyle: {
              opacity: 0.8,
              color: new this.$echarts.graphic.LinearGradient(0, 0, 0, 1, [
                {
                  offset: 0,
                  color: 'rgb(25, 191, 0)'
                },
                {
                  offset: 1,
                  color: 'rgb(24, 62, 76)'
                }
              ])
            },
            emphasis: {
              focus: 'series'
            },
            data: [220, 302, 181, 234, 210, 290, 150]
          },
          {
            name: '治愈增加',
            type: 'line',
            stack: 'Total',
            smooth: true,
            lineStyle: {
              width: 0
            },
            showSymbol: false,
            label: {
              show: true,
              position: 'top'
            },
            areaStyle: {
              opacity: 0.8,
              color: new this.$echarts.graphic.LinearGradient(0, 0, 0, 1, [
                {
                  offset: 0,
                  color: 'rgb(100, 191, 100)'
                },
                {
                  offset: 1,
                  color: 'rgb(204, 90, 76)'
                }
              ])
            },
            emphasis: {
              focus: 'series'
            },
            data: [220, 302, 181, 234, 210, 290, 150]
          },
          {
            name: '死亡增加',
            type: 'line',
            stack: 'Total',
            smooth: true,
            lineStyle: {
              width: 0
            },
            showSymbol: false,
            label: {
              show: true,
              position: 'top'
            },
            areaStyle: {
              opacity: 0.8,
              color: new this.$echarts.graphic.LinearGradient(0, 0, 0, 1, [
                {
                  offset: 0,
                  color: 'rgb(125, 101, 0)'
                },
                {
                  offset: 1,
                  color: 'rgb(124, 62, 76)'
                }
              ])
            },
            emphasis: {
              focus: 'series'
            },
            data: [220, 302, 181, 234, 210, 290, 150]
          }
        ]
      }
      chart.setOption(option)
    }
   }

}
</script>

<style  scoped>
  .container{
    width: 100%;
    height: 100%;
  }
</style>
