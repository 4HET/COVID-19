<template>
  <div class="screens">
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
        <a href="http://127.0.0.1:8080/#/screen1" class="tag_aa" >上海疫情</a></div></div>
        <div class="tabbar"><div class="tabbar_">
        <span class="iconfont" style="font-size: 25px;">&#xe504;</span>
        <a href="http://127.0.0.1:8080/#/screen2" class="tag_aa"  style="color:red">各省抗疫</a></div></div>
      </div>
    </div>
  </div>
    <div class="header">
      <Scien1></Scien1>
    </div>
    <div class="content">
      <Province></Province>
    </div>
    <div class="footer">
      <Image1></Image1>
    </div>
  </div>
</template>

<script>
import Scien from '@/components/scien'
import province from '@/components/province'
import Image from '@/components/image'
export default {
  components: {
    Scien1: Scien,
    Province: province,
    Image1: Image
  }
}
</script>

<style lang="less" scoped>
  .screens {
    width: 100%;
    height: 850px;
  }
  .header {
    height: 30%;
    width: 100%;
  }
  .content {
    margin-top: 20px;
    height: 50%;
    width: 100%;
  }
  .footer {
    margin: 0 auto;
    margin-top: 80px;
    height: 30%;
    width: 100%;
    // background-color: orange
  }
</style>
