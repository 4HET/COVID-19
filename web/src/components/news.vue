<template>
  <div>
    <div class='scroll-wrap'>
      <ul
        class='scroll-content'
        :style='{ top }'
        @mouseenter='Stop()'
        @mouseleave='Up()'
      >
        <li v-for='item in prizeList' v-bind:key='item.id'>
          <a :href='item.url' target="_blank">{{ item.news }}</a>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'complexTable',
  data () {
    return {
      prizeList: [],
      activeIndex: 0,
      intnum: undefined
    }
  },
  computed: {
    top () {
      return -this.activeIndex * 20 + 'px'
    }
  },
  mounted () {
    this.get()
  },
  created () {
    this.ScrollUp()
  },
  methods: {
    ScrollUp () {
      // eslint-disable-next-line no-unused-vars
      this.intnum = setInterval((_) => {
        if (this.activeIndex < this.prizeList.length) {
          this.activeIndex += 1
        } else {
          this.activeIndex = 0
        }
      }, 1000)
    },

    Stop () {
      clearInterval(this.intnum)
    },
    Up () {
      this.ScrollUp()
    },
  async  get () {
    const { data: ans } = await axios.get('http://localhost:8888/api/news')

        this.prizeList = ans
    }
  }
}
</script>
<style scoped>
.scroll-wrap {
  padding: 15px;
  height:100%;
  overflow: hidden;
}

.scroll-content {
  position: relative;
  transition: top 0.5s;
}
li{
  line-height:50px;
}
a {
  color: black;
  width: 100%;
  height: 50px;
  display: inline-block;
  text-decoration: none;
  text-align: center;
}
li{
  list-style: none;
}
a:hover{
  background-color: orange;
}
li:nth-child(even){
  background-color:#ccc;
}
</style>
