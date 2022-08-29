<template>
  <div class="pro">
    <div v-for="item in List" :key="item.id" class="add">
      <!-- {{item.img}} -->
      <a :href="item.url">{{item.name}}</a>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  data () {
    return {
      List: []
    }
  },
  created () {
    this.get_data()
  },
  mounted () {
    this.change()
      // this.timer = setInterval(this.change, 1000)
    },
    beforeDestroy () {
      clearInterval(this.timer)
    },
  methods: {
   async get_data () {
     const { data } = await axios.get('static/data/province.json')
     this.List = data
    },
    change () {
      // const dom = document.querySelectorAll('div')
      // console.log(dom[5])
    }
  }
}
</script>

<style lang="less" scoped>
  .pro{
    display: flex;
    justify-content: space-around;
    flex-wrap: wrap;
  }
  .pro div{
    margin: 10px;
    text-align: center;
    line-height:100px;
    width: 100px;
    height: 100px;
    box-shadow: 0 0 12px #009dfd;
    // animation: move 5s linear infinite;
    // background-color:orange;
  }
  a{
    text-decoration: none;
    color: #ccc;
  }
   @keyframes move {
            0% {}
            70% {
                width: 200px;
                height: 200px;
            }
        }
</style>
