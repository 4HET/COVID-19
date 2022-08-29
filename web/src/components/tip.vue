<template>
 <div ref='wordcloud1' class='wordcloud1'>
 </div>
</template>
<script>
import * as echarts from 'echarts'
import 'echarts-wordcloud/dist/echarts-wordcloud'
import 'echarts-wordcloud/dist/echarts-wordcloud.min'
import axios from 'axios'
 export default {
   data () {
     return {
       List: [],
        wordList: [
                ]
     }
   },
   created () {
     this.get_data()
   },
   mounted () {
   },
   methods: {
    async get_data () {
       const { data } = await axios.get('static/data/attention.json')
       this.List = data
       console.log(data)
       this.initchart()
     },
     initchart () {
       const myChart = echarts.init(this.$refs.wordcloud1)
       myChart.on('click', eConsole)
       function eConsole (param) {
     if (typeof param.seriesIndex !== 'undefined') {
        switch (param.name) {
            case '个人防护要注意这些':
                window.open('https://www.thepaper.cn/newsDetail_forward_15869303', '_blank')
                     break
            case '个人防护注意事项':
                window.open('https://www.htu.edu.cn/history/2020/0709/c943a170358/page.htm', '_blank')
                     break
            case '坚持防疫的“三件套”':
                window.open('https://new.qq.com/omn/20220317/20220317A07V4O00.html', '_blank')
                     break
            case '【疫情防控不松劲】':
                window.open('https://new.qq.com/omn/20220311/20220311A094IX00.html', '_blank')
                     break
            case '怎样预防新冠疫情！':
                window.open('https://www.sohu.com/a/485691184_121124716', '_blank')
                     break
            case '疫情防控小知识':
                window.open('https://m.thepaper.cn/baijiahao_10707654', '_blank')
                     break
            case '八大注意事项是什么？':
                window.open('https://zhidao.baidu.com/question/1740709635615510827.html', '_blank')
                     break
            case '个人防护，一篇搞定！':
                window.open('https://www.sohu.com/a/539967883_121124032', '_blank')
                     break
            case '外出有哪些注意事项？':
                window.open('http://health.hebnews.cn/2021-01/29/content_8346997.htm', '_blank')
                     break
            case '个人防护':
                window.open('https://m.gmw.cn/2022-05/03/content_1302929348.htm', '_blank')
                     break
            default:
                break
        }
      }
    }
       myChart.setOption({
         title: {
           text: '关于疫情的小常识'
         },
         series: [
           {
             textRotation: [0, 0],
             type: 'wordCloud',
             gridSize: 0.1,
             sizeRange: [10, 30],
             rotationRange: [0, 0],
             textStyle: {
                 color: function () {
                   return (
                     'rgb(' +
                     Math.round(Math.random() * 255) +
                     ', ' +
                     Math.round(Math.random() * 255) +
                     ', ' +
                     Math.round(Math.random() * 255) +
                     ')'
                   )
               }
             },
             left: 'center',
             top: 'center',
             right: null,
             bottom: null,
             width: '200%',
             height: '200%',
             data: this.List
           }
         ]
       })
     }
   }
 }
</script>
<style scoped>
.wordcloud1{
  overflow: hidden;
  width:90%;
  height:100%;
  margin:auto;
}
</style>
