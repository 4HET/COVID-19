<template>
  <div class="Increase" ref="Increase"></div>
</template>

<script>

export default {
   mounted () {
    this.initChart()
    this.updataChart()
  },
  methods: {
    initChart () {
    this.chartInstance = this.$echarts.init(document.querySelector('.Increase'))
  },
  updataChart () {
	const textfontsize = this.$refs.Increase.offsetWidth / 600
	// console.log(textfontsize)
    var years = ['周一', '周二', '周三', '周四', '周五', '周六', '周天'
    ]

    var jdData = [
  ['加拿大', '美国', '丹麦', '日本', '香港特别行政区'],
  ['加拿大', '美国', '丹麦', '日本', '法国', '香港特别行政区'],
  ['加拿大', '法国', '乌干达', '香港特别行政区'],
  ['加拿大', '法国', '乌干达', '香港特别行政区'],
  ['加拿大', '科特迪瓦', '法国', '乌干达', '香港特别行政区'],
  ['加拿大', '科特迪瓦', '法国', '乌干达'],
  ['加拿大', '科特迪瓦', '法国', '乌干达']
]
 var data = [
        [2, 1, 1, 1, 1],
        [3, 1, 1, 1, 1, 1],
        [2, 1, 1, 1],
        [2, 1, 1, 1],
        [3, 1, 1, 1, 1],
        [3, 1, 1, 1],
        [6, 1, 1, 1]
]

    const option = {
        baseOption: {
        backgroundColor: '#F5F5F5',
            timeline: {
                data: years,
                axisType: 'category',
                autoPlay: true,
                playInterval: 2200,
                left: 'center',
                right: '15%',
                bottom: textfontsize + 2,
                width: '95%',
                label: {
                    normal: {
                        textStyle: {
                            color: '#FFA500'
                        }
                    }
                },
                symbolSize: 6,
                lineStyle: {
                    color: '#555'
                },
                checkpointStyle: {
                    borderColor: '#777',
                    borderWidth: 2
                },
                controlStyle: {
                    itemSize: 19,
                    itemGap: 3,
                    normal: {
                        color: '#FFA500',
                        borderColor: '#FFA500'
                    },
                    emphasis: {
                        color: '#FFA500',
                        borderColor: '#FFA500'
                    }
                }
            },
            title: [{
                text: '',
                right: '5%',
                bottom: '15%',
                textStyle: {
                    fontSize: 25,
                    color: '#696969'
                }
            }, {
                text: '境外输入情况',
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
            }],
            tooltip: {
                trigger: 'axis'
            },
            calculable: true,
            grid: {
                left: '2%',
                right: '3%',
                bottom: '12%',
                top: '10%',
                containLabel: true
            },
            label: {
                normal: {
                    textStyle: {
                        color: '#fff'
                    }
                }
            },
            yAxis: [{
                offset: '10',
                type: 'category',
                data: '',
                nameTextStyle: {
                    color: ''
                },
                axisLine: {
                    show: false
                },
                axisTick: {
                    show: false
                },
                axisLabel: {
                    textStyle: {
                        fontSize: 14 + textfontsize
                    }
                }
            }],
            xAxis: [{
                type: 'value',
                splitNumber: 8,
                axisLabel: {
                    formatter: '{value} '
                },
                splitLine: {
                    lineStyle: {
                        color: '#ccc'
                    }
                }
            }],
            series: [{
                type: 'bar',
                barWidth: '50%',
                barBorderRadius: [0, 20, 20, 0],
                label: {
                    normal: {
                        show: true,
                        position: 'inside',
                        formatter: '{c}'
                    }
                },
                itemStyle: {
                    normal: {
                        color: function (params) {
                            var colorList = [
                                '#efbbcf', '#eea2a4', '#f5b971', '#649d66', '#aacfcf', '#d291bc', '#ffa5b0',
                                '#fedd8b', '#7fec9d', '#a6dcef', '#c3bed4', '#495a80',
                                '#9966cc', '#bdb76a', '#eee8ab', '#a35015',
                                '#04dd98', '#d9b3e6', '#b6c3fc', '#315dbc'
                            ]
                            return colorList[params.dataIndex]
                        }
                    }
                }
            }],
            animationDurationUpdate: 2000,
            animationEasingUpdate: 'quinticInOut'
        },
        options: []
    }
    for (var n = 0; n < years.length; n++) {
        var res = []
        for (var j = 0; j < data[n].length; j++) {
            res.push({
                name: jdData[n][j],
                value: data[n][j]
            })
        }
        res.sort(function (a, b) {
            return b.value - a.value
        }).slice(0, 6)
        res.sort(function (a, b) {
            return a.value - b.value
        })
        var res1 = []
        var res2 = []
        for (var t = 0; t < res.length; t++) {
            res1[t] = res[t].name
            res2[t] = res[t].value
        }
        option.options.push({
            title: {
                text: years[n]
            },
            yAxis: {
                data: res1
            },
            series: [{
                data: res2
            }]
        })
      }
    this.chartInstance.setOption(option)
    this.chartInstance.resize()
  }
      // option && myChart.setOption(option)
  }

}
</script>

<style lang="less" scoped>
  .Increase{
    margin: 10px auto;
    border-radius: 20px;
    width: 95%;
    height: 95%;
  }
</style>
