<template>
 <div ref='wordcloud2' class='wordcloud2'>
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
       const { data } = await axios.get('static/data/result.json')
       this.List = data
       this.initchart()
     },
     initchart () {
       const myChart = echarts.init(this.$refs.wordcloud2)
       myChart.on('click', eConsole)
       function eConsole (param) {
     if (typeof param.seriesIndex !== 'undefined') {
        switch (param.name) {
            case '《自然》：新冠疫苗加强针为何对奥密克戎仍有效':
                window.open('https://news.sciencenet.cn/htmlnews/2022/4/477767.shtm', '_blank')
                     break
            case '以色列卫生部宣布发现新型新冠病毒变异毒株':
                window.open('https://news.sciencenet.cn/htmlnews/2022/3/475745.shtm', '_blank')
                     break
            case '新冠感染或致脑部退行性病变':
                window.open('https://news.sciencenet.cn/htmlnews/2022/3/475650.shtm', '_blank')
                     break
            case '双毒合一！“德尔塔克戎”变体首次证实':
                window.open('https://news.sciencenet.cn/htmlnews/2022/3/475606.shtm', '_blank')
                     break
            case '传播能力为何这么强？奥密克戎四大谜团揭秘':
                window.open('https://news.sciencenet.cn/htmlnews/2022/3/475605.shtm', '_blank')
                     break
            case '吉林市本轮疫情病毒基因序列为奥密克戎进化分支':
                window.open('https://news.sciencenet.cn/htmlnews/2022/3/475405.shtm', '_blank')
                     break
            case '连云港疫情病毒测序为奥密克戎变异株进化分支':
                window.open('https://news.sciencenet.cn/htmlnews/2022/3/475390.shtm', '_blank')
                     break
            case '《自然》：一单克隆抗体可中和奥密克戎全部亚型':
                window.open('https://news.sciencenet.cn/htmlnews/2022/3/475024.shtm', '_blank')
                     break
            case '加拿大或现首个“鹿传人”新冠病例':
                window.open('https://news.sciencenet.cn/htmlnews/2022/3/474939.shtm', '_blank')
                     break
            case '保持社交距离能防新冠演化出抗疫苗变异株':
                window.open('https://news.sciencenet.cn/htmlnews/2022/2/474554.shtm', '_blank')
                     break
             case '我国学者发现可有效抑制新冠病毒感染药物':
                window.open('https://news.sciencenet.cn/htmlnews/2022/2/474325.shtm', '_blank')
                     break
            default:
                break
        }
      }
    }
       myChart.setOption({
         title: {
           text: '关于疫情的相关研究'
         },
         series: [
           {
             textRotation: [0, 0],
             type: 'wordCloud',
             gridSize: 0.1,
             sizeRange: [10, 40],
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
.wordcloud2{
  overflow: hidden;
  width:90%;
  height:100%;
  margin:auto;
}
</style>
