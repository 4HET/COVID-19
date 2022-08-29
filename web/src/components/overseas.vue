<template>
  <div class="com-container">
    <div class="com-chart" ref="mn_ref">
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  created () {
    this.get_data()
  },
  data () {
    return {
      chartInstance: null,
      List: [],
      Number: []
    }
  },
  destroyed () {
    window.removeEventListener('resize', this.updataChart)
  },
  mounted () {
    this.initChart()
    this.updataChart()
    window.addEventListener('resize', this.updataChart)
    this.updataChart()
  },
  methods: {
    async get_data () {
      const { data } = await axios.get('https://api.inews.qq.com/newsqa/v1/query/pubished/daily/list?province=%E4%B8%8A%E6%B5%B7')
      this.List = data.data
      this.List = this.List.filter(function (d) {
        return d.year === 2022 && d.date >= '04.01' && d.date <= '04.30'
      })

     this.List.filter((d) => {
       this.Number.push(d.confirm)
      })

      this.Number = this.Number.filter((d, index) => {
        if (index < 30) {
          return d
        }
      })
    },
    initChart () {
      this.chartInstance = this.$echarts.init(this.$refs.mn_ref)
    },
    updataChart () {
      const option = {
        backgroundColor: '#F5F5F5',
        title: {
          text: '四月份确诊人数变化',
          itemGap: 5,
          x: 'center',
          y: '1%',
          textStyle: {
            fontFamily: 'sans-serif',
            fontSize: 21,
            fontWeight: 'normal'
          },
          subtextStyle: {
            color: '#646464',
            fontFamily: 'sans-serif',
            fontSize: 15,
            fontWeight: 'normal'
          }
        },
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'line'
          }
        },
        xAxis: {
          type: 'category',
          axisLine: {
            show: false
          },
          axisTick: {
            show: false
          },
          axisLabel: {
            fontSize: 15
          },
          boundaryGap: true,
          data: ['一号', '二号', '三号', '四号', '五号', '六号', '七号', '八号', '九号', '十号', '十一号', '十二号', '十三号',
            '十四号', '十五号', '十六号', '十七号', '十八号', '十九号', '二十号', '二十一号', '二十二号', '二十三号',
            '二四号', '二五号', '二六号', '二七号', '二八号', '二九号', '三十号'
          ]
        },
        yAxis: [{
          type: 'value',
          axisLine: {
            show: false,
            lineStyle: {
              color: '#000000'
            }
          },
          axisLabel: {
            fontSize: 15
          },
          min: 200,
          splitNumber: 6
        }],
        dataZoom: [{
          type: 'slider',
          filterMode: 'filter',
          show: true,
          height: 15,
          left: '11%',
          right: '10%',
          xAxisIndex: [
            0
          ],
          bottom: '1%',
          start: 0,
          end: 50,
          handleStyle: {
            color: '#40bcf9',
            borderColor: '#1fb2fb'
          },
          backgroundColor: '#e2f3ff',
          dataBackground: {
            lineStyle: {
              color: '#000000'
            },
            areaStyle: {
              color: '#d4d9dd'
            }
          },
          fillerColor: 'rgba(31,178,251,0.2)',
          labelFormatter: function (value, params) {
            var str = ''
            if (params.length > 4) {
              str = params.substring(0, 4) + '人'
            } else {
              str = params
            }
            return str
          }
        }],
        grid: {
          left: '2%',
          right: '2%',
          bottom: '6%',
          top: '14%',
          containLabel: true,
          borderWidth: '0'
        },
        series: [{
          name: '确诊人数',
          type: 'line',
          smooth: true,
          symbol: 'circle',
          symbolSize: 10,
          data: [6714, 7158, 7591, 7862, 8177, 8506, 9334, 10351, 10351, 12283, 12283, 14471, 17044, 20244, 23838, 27078, 29498, 32582, 35077, 37712, 39643, 39643, 39643, 39643, 39643, 42379, 42379, 42379, 42379, 42379
          ],
          itemStyle: {
            normal: {
              color: '#5fbdff',
              lineStyle: {
                width: 2
              }
            }
          }
        }]
      }
      this.chartInstance.setOption(option)
      this.chartInstance.resize()
    }
    }
}
</script>

<style>

</style>
