<template>
<div class="screen-container">
<div class="screen-head">
    <div class="head-middle">
      <div class="title">
       <div class="title_">
         <div class="title_">
          疫情下的中国 团结抗疫
         </div>
       </div>
      </div>
      <div class="tag_a">
        <div class="tabbar"><div class="tabbar_">
        <span class="iconfont" style="font-size: 25px;">&#xe70d;</span>
        <a href="http://127.0.0.1:8080/#/" class="tag_aa" style="color:red">全国整体情况</a></div></div>
        <div class="tabbar"><div class="tabbar_">
        <span class="iconfont" style="font-size: 25px;">&#xe6c7;</span>
        <a href="http://127.0.0.1:8080/#/screen1" class="tag_aa">上海疫情</a></div></div>
        <div class="tabbar"><div class="tabbar_">
        <span class="iconfont" style="font-size: 25px;">&#xe504;</span>
        <a href="http://127.0.0.1:8080/#/screen2" class="tag_aa">各省抗疫</a></div></div>
      </div>
    </div>
  </div>
  <div class="screen-body">
    <div class="body-left">
      <div id="left-top">
        <Mapciyuntu></Mapciyuntu>
      </div>
      <div id="left-bottom">
        <area1></area1>
      </div>
    </div>
    <div class="body-middle">
      <div id="middle-top">
        <!-- 使用路由进行传输数据 -->
        <map1 ref="map1" :list = "List"></map1>
      </div>
      <div id="middle-bottom">
          <news></news>
      </div>
    </div>
    <div class="body-right">
      <div id="right-top">
        <Inc1></Inc1>
      </div>
      <div id="right-bottom">
        <!-- <news></news> -->
          <Move1></Move1>

      </div>
    </div>
  </div>
</div>
</template>

<script>
import Map from '@/components/map'
import Move from '@/components/move'
import Inc from '@/components/increase'
import cyt from '@/components/ciyuntu'
import New from '@/components/news'
import Area from '@/components/area'
import axios from 'axios'
export default {
  components: {
    map1: Map,
    Move1: Move,
    Inc1: Inc,
    Mapciyuntu: cyt,
    news: New,
    area1: Area
  },
  data () {
    return {
      year: '',
      month: '',
      day: '',
      sum_h: '',
      hiddle: 0,
      List: []
    }
  },
  created () {
    this.get_data()
  },
  mounted () {
    this.countTime()
  },
  methods: {
    get_data: async function () {
      const { data: ans } = await axios.get('static/data/coj.json')
      this.List = ans.data
    },
    countTime () {
      // 定义当前时间戳
      // const now = Date.now()
     var d = new Date()

     const year = d.getFullYear()

     const month = d.getMonth()

     const day = d.getDate()

     this.year = year

     this.month = month + 1

     this.day = day

      // //  定义this指向
      const that = this
      //  使用定时器 然后使用递归 让每一次函数能调用自己达到倒计时效果
      setTimeout(function () {
        that.countTime()
      }, 1000)
    }
  }
}
</script>

<style>
*{
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
@font-face {
  font-family: 'iconfont';
  src: url('../assets/font3/iconfont.ttf');
}
body {
  margin: 0;
  padding: 0;
}
html {
  height: 1100px;
  width: 100%;
}
#app {
  height: 1100px;
  width: 100%;
}
.screen-container {
  width: 100%;
  height: 100%;
  margin: 0;
  padding: 0;
}
/* 头顶中间 */
.screen-head {
  width: 100%;
  height: 130px;
  margin-bottom: 10px;
  position: relative;
  display:flex;
  justify-content: space-between;
}

.head-left{
  flex: 1;
  height: 100%;
  width: 23%;
  position: relative;
}
.head-middle{
  flex:2;
  height: 100%;
  width: 50%;
  border: 1px solid;
  border-image-slice: 51 38 20 132;
  border-image-width: 51px 38px 20px 132px;
  border-image-source: url(../../public/static/img/border.png);
}
/* 头部右边 */
.head-right{
  flex:1;
  position: relative;
  height: 100%;
  width: 20%;
  top: 10px;
  border: 1px solid;
  border-image-slice: 51 38 20 132;
  border-image-width: 51px 38px 20px 132px;
  border-image-source: url(../../public/static/img/border.png);
  background-repeat: no-repeat;
}
.head-right-top{
  width: 100%;
  height: 20%;
  font-size: 20px;
  text-align: center;
  color: rgb(25, 185, 206);
  margin-bottom: 10px;
}
.head-right-middle{
  display:flex;
  justify-content: space-around;
  width: 100%;
  height: 100%;
}
.day{
  width: 38%;
  height: 100%;
  float: left;
}
.time{
  width: 19%;
  height: 100%;
  float: left;
}
.time1{
  width: 19%;
  height: 100%;
  float: left;
}
.time-top{
  height: 25%;
  width: 100%;
  text-align: center;
  font-size: 20px;
  color: #4169E1;
}
.time-bottom{
  height: 75%;
  width: 100%;
  text-align: center;
  font-size: 35px;
  margin-top: 10px;
  color: #4169E1;
}
.title{
  width: 100%;
  height: 45%;
}
.title_{
  width: 100%;
  height: 100%;
  margin-top: 15px;
  font-size: 30px;
  font-family: electronicFont;
  text-align: center;
  color: #4169E1;
}
.tag_a{
  width: 100%;
  height: 50%;
  position: relative;
  color: #4169E1;
}
.tag_aa{
  color: black;
  font-size: 25px;
  text-decoration:none;
  color: #4169E1;
}
.tag_aa:hover{
  color: hotpink;
  text-decoration:none;
}
.tabbar{
  width: 30%;
  height: 80%;
  float: left;
  margin-left: 10px;
}
.tabbar_{
  width: 100%;
  height: 100%;
  margin-top: 15px;
  text-align: center;
  position: relative;
}
.screen-body{
  display:flex;
  justify-content: space-between;
  width: 100%;
  margin-top: 15px;
  height: 650px;
}
.body-left{
  flex: 1;
  width: 100%;
  height: 890px;
  float: left;
  margin-left: 10px;
}
.body-middle{
  flex: 2;
  width: 100%;
  height: 650px;
  float: left;
  margin-left: 10px;
  margin-right: 10px;
}
.body-right{
  flex: 1;
  width: 100%;
  height: 825px;
  float: left;
  margin-right: 10px;
}
/* 头部 左边 */
/* .log-bg{
   background: url(../../public/static/img/Time-bg.jpg);
} */
/* 做顶上一张 */
#left-top{
  width: 100%;
  height: 480px;
  margin-bottom: 25px;
  position: relative;
  border: 1px solid;
  border-image-slice: 51 38 20 132;
  border-image-width: 51px 38px 20px 132px;
  border-image-source: url(../../public/static/img/border.png);

}
/* 走下面一张 */
#left-bottom{
  width: 100%;
  height: 440px;
  position: relative;
  border: 1px solid;
  border-image-slice: 51 38 20 132;
  border-image-width: 51px 38px 20px 132px;
  border-image-source: url(../../public/static/img/border.png);
}
/* 右顶上一张 */
#right-top{
  width: 100%;
  height: 480px;
  position: relative;
  border: 1px solid;
  border-image-slice: 51 38 20 132;
  border-image-width: 51px 38px 20px 132px;
  border-image-source: url(../../public/static/img/border.png);
}
/* 有下面一张 */
#right-bottom{
  width: 100%;
  height: 440px;
  margin-top: 25px;
  position: relative;
  border: 1px solid;
  border-image-slice: 51 38 20 132;
  border-image-width: 51px 38px 20px 132px;
  border-image-source: url(../../public/static/img/border.png);
}
/* 中间一张 */
#middle-top{
  padding-top:10px;
  padding-bottom:20px;
  padding-left:10px;
  padding-right:10px;
  width: 100%;
  height: 605px;
  margin-bottom: 15px;
  position: relative;
  border: 1px solid;
  border-image-slice: 51 38 20 132;
  border-image-width: 51px 38px 20px 132px;
  border-image-source: url(../../public/static/img/border.png);
  /* background-color: #060612; */
  background-color: white;
}
/* 最下面一张 */
#middle-bottom{
  overflow: hidden;
  /* background-color: orange; */
  width: 100%;
  height: 325px;
  /* display: flex; */
  position: relative;
  border: 1px solid;
  border-image-slice: 51 38 20 132;
  border-image-width: 51px 38px 20px 132px;
  border-image-source: url(../../public/static/img/border.png);
}
</style>
