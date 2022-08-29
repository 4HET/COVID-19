<template>
<div>
<div class="box">
<ul class="ullist" @mouseleave="clearTimeout" @mouseenter="beginTimeout">
<li><img src="static/img/yiqing/01.jpg" alt="vue实现匀速轮播效果" class="Liwidth"></li>
<li><img src="static/img/yiqing/11.jpg" alt="vue实现匀速轮播效果" class="Liwidth"></li>
<li><img src="static/img/yiqing/03.jpg" alt="vue实现匀速轮播效果" class="Liwidth"></li>
<li><img src="static/img/yiqing/04.jpg" alt="vue实现匀速轮播效果" class="Liwidth"></li>
<li><img src="static/img/yiqing/05.jpg" alt="vue实现匀速轮播效果" class="Liwidth"></li>
<li><img src="static/img/yiqing/06.jpg" alt="vue实现匀速轮播效果" class="Liwidth"></li>
<li><img src="static/img/yiqing/07.jpg" alt="vue实现匀速轮播效果" class="Liwidth"></li>
<li><img src="static/img/yiqing/08.jpg" alt="vue实现匀速轮播效果" class="Liwidth"></li>
<li><img src="static/img/yiqing/09.jpg" alt="vue实现匀速轮播效果" class="Liwidth"></li>
<li><img src="static/img/yiqing/10.jpg" alt="vue实现匀速轮播效果" class="Liwidth"></li>
</ul>
</div>
</div>
</template>
<script>
export default {
      data () {
        return {
        screenWidth: '',
        boxWidth: 0,
        isClear: 0,
        timer: null,
        left: 0,
        timerRun: false
        }
        },
    methods: {
    getListLeng() {
    this.boxWidth = document.getElementsByClassName('box')[0].offsetWidth
    var ul = document.getElementsByClassName('ullist')[0]
    var length = ul.children.length
    ul.style.width = length * 230 + 'px'
    this.runTimeout(ul, this.boxWidth, length)
    },
runTimeout(ul, boxWidth, length) {
const that = this
this.timer = setInterval(function() {
// move();
that.move(ul, boxWidth, length)
}, 50)
},
move(ul, boxWidth, length) {
var num = this.left--
var allWidth = length * 230 - boxWidth
if (Math.abs(num) > allWidth) {
ul.style.left = 0 + 'px'
this.left = 0
}
ul.style.left = num + 'px'
},
beginTimeout() {
clearInterval(this.timer)
},
clearTimeout() {
clearInterval(this.timer)
this.timer = null
this.boxWidth = document.getElementsByClassName('box')[0].offsetWidth
const ul = document.getElementsByClassName('ullist')[0]
const length = ul.children.length
ul.style.width = length * 230 + 'px'
this.runTimeout(ul, this.boxWidth, length)
}
},
      mounted() {
      this.getListLeng()
        window.onresize = () => {
            return (() => {
            this.boxWidth = document.getElementsByClassName('box')[0].offsetWidth
            })()
        }
      // eslint-disable-next-line no-undef
      getSwiperList().then(res => {
      this.bannerList = res.data
      })
      },
destroyed () {
clearInterval(this.timer)
}
}
</script>
<style lang="less" scped>
      .box{
      height:230px;
      width:80%;
      margin: 200px auto;
      position: relative;
      overflow: hidden;
      ul{
      position: absolute;
      }
      li{
      list-style: none;
      float: left;
      height:230px;
      width:230px;
      img{
      height:200px;
      width:200px;
    }
  }
}
</style>
