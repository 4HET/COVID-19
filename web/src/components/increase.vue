<template>
  <div id="echBox"></div>
</template>

<script>
import axios from 'axios'
export default {
  data () {
    return {
      name: [
      ],
      list2: [
      ]
    }
  },
  created () {
    this.get_data()
  },
  methods: {
   async get_data () {
      const { data } = await axios.get('http://localhost:8888/api/add')
      data.forEach((key) => {
        this.name.push(key.name)
        this.list2.push(key.value)
      })

      this.asda()
    },
    asda () {
      var myChart = this.$echarts.init(document.getElementById('echBox'))

      const option = {

        title: {
            show: true,
            text: '各省新增确诊数量',
            link: '',
            target: null,
            sublink: '',
            subtarget: null,
            x: 'center',
            y: 'top',
            borderColor: '#ccc',
            borderWidth: 0,
            padding: 5,
            itemGap: 10,
            textStyle: {
                fontSize: 20,
                fontStyle: 'italic',
                fontWeight: 200,
                color: '#ccc'
            }
        },
        grid: {
          left: '5%',
          right: '5%',
          bottom: '5%',
          top: '10%',
          containLabel: true
        },
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'none'
          }
        },
        dataZoom: [
          {
            type: 'slider',
            show: true,
            yAxisIndex: [0, 1],
            start: 0,
            end: 30,
            width: '10',
            fillerColor: 'red',
            handleSize: 0,
            borderColor: 'transparent',
            backgroundColor: 'transparent',
            showDataShadow: false,
            showDetail: false
          },
          {
            type: 'inside',
            yAxisIndex: [0, 1],
            zoomOnMouseWheel: false,
            moveOnMouseMove: true
          }
        ],
        backgroundColor: 'white',
        xAxis: {
          show: false,
          type: 'value'
        },
        yAxis: [
          {
            type: 'category',
            inverse: true,
            axisLabel: {
              show: true,
              textStyle: {
                color: 'red'
              }
            },
            splitLine: {
              show: true,
              lineStyle: {
                color: 'rgba(228,228,228,0.2)',
                type: 'dashed'
              }
            },
            boundaryGap: false,
            axisTick: {
              show: false
            },
            axisLine: {
              show: false
            },
            data: this.name
          },
          {
            type: 'category',
            inverse: true,
            axisTick: 'none',
            axisLine: 'none',
            show: true,
            boundaryGap: false,
            axisLabel: {
              textStyle: {
                color: '#orange',
                fontSize: '12'
              }
            },
            data: this.list2
          }
        ],
        series: [
          {
            name: '人数',
            type: 'bar',
            zlevel: 1,
            itemStyle: {
              normal: {
                barBorderRadius: 30,
                color: new this.$echarts.graphic.LinearGradient(0, 0, 1, 0, [
                  {
                    offset: 0,
                    color: 'rgb(57,89,255,1)'
                  },
                  {
                    offset: 1,
                    color: 'rgb(46,200,207,1)'
                  }
                ])
              }
            },
            barWidth: 20,
            data: this.list2
          },
          {
            name: '人数',
            type: 'bar',
            barWidth: 20,
            barGap: '-100%',
            data: this.list2,
            itemStyle: {
              normal: {
                color: 'rgba(24,31,68, 0)'
              }
            }
          }
        ]
      }

      // 使用刚指定的配置项和数据显示图表。
      myChart.setOption(option)

      var timeOut = ''
      autoMove()
      document.getElementById('echBox').onmouseenter = () => {
        stop()
      }
      document.getElementById('echBox').onmouseleave = e => {
        autoMove()
        const myChartOption = myChart.getOption()
        endVal = myChartOption.dataZoom[0].end
        startVal = myChartOption.dataZoom[0].start
      }

      // eslint-disable-next-line no-unused-vars
        var endVal = 30
        var startVal = 0
      function autoMove () {
        timeOut = setInterval(() => {
          if (endVal === 100) {
            endVal = 30
            startVal = 0
          } else {
            endVal = endVal + 1
            startVal = startVal + 1
          }
          myChart.dispatchAction({
            type: 'dataZoom',
            dataZoomIndex: [0, 1],
            start: startVal,
            end: endVal
          })
        }, 300)
      }
      function stop () {
        clearInterval(timeOut)
      }
    }
  }
}
</script>

<style scoped>
#echBox {
  padding: 20px;
  width: 100%;
  height: 480px;
}
</style>
