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
        <a href="http://127.0.0.1:8080/#/" class="tag_aa">全国整体情况</a></div></div>
        <div class="tabbar"><div class="tabbar_">
        <span class="iconfont" style="font-size: 25px;">&#xe6c7;</span>
        <a href="http://127.0.0.1:8080/#/screen1" class="tag_aa" style="color:red">上海疫情</a></div></div>
        <div class="tabbar"><div class="tabbar_">
        <span class="iconfont" style="font-size: 25px;">&#xe504;</span>
        <a href="http://127.0.0.1:8080/#/screen2" class="tag_aa">各省抗疫</a></div></div>
      </div>
    </div>
  </div>
  <div class="screen-body">
    <div class="body-left">
      <div id="left-top">
        <Policy></Policy>
      </div>
      <div id="left-bottom">
        <tips></tips>
      </div>
    </div>
    <div class="body-middle">
      <div id="middle-top">
       <map2></map2>
      </div>
      <div id="middle-bottom">
        <increse1></increse1>
      </div>
    </div>
    <div class="body-right">
      <div id="right-top">
        <OverSeas1></OverSeas1>
      </div>
      <div id="right-bottom">
        <help1 ref = "help1" :help_list = 'Help_List'></help1>
      </div>
    </div>
  </div>
</div>
</template>

<script>
import Map2 from '@/components/map2'
import Help1 from '@/components/help'
import OverSeas from '@/components/overseas'
import Increse1 from '@/components/new_increase'
import Policy1 from '@/components/policy'
import Tip from '@/components/tip'
import axios from 'axios'

export default {
  components: {
    map2: Map2,
    OverSeas1: OverSeas,
    help1: Help1,
    increse1: Increse1,
    Policy: Policy1,
    tips: Tip
  },
  data () {
    return {
      Help_List: []
    }
  },
  created () {
    this.get_help()
  },
  mounted () {
  },
  methods: {
  async get_help () {
    const { data } = await axios.get('static/data/help.json')
    this.Help_List = data
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
  width: 40%;
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
  width: 30%;
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
  overflow: hidden;
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
