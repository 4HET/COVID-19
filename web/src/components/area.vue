<template>
  <div id="area">
  </div>
</template>

<script>
import axios from 'axios'
export default {
  data () {
    return {
      time: '',
      mid: [],
      high: []
    }
  },
  created () {
  },
  mounted () {
    this.initchart()
  },
  methods: {

   async initchart () {
      const { data: ans } = await axios.get('https://diqu.gezhong.vip/api.php')

      this.time = ans.data.end_update_time
      this.mid = ans.data.middlelist
      this.high = ans.data.highlist
      var data = [
  {
    name: '高风险地区',
    children: [
      {
        name: this.high[0].county,
        value: Math.random() * 100
      },
      {
        name: this.high[1].county,
        value: Math.random() * 110
      },
      {
        name: this.high[2].county,
        value: Math.random() * 120
      },
      {
        name: this.high[3].county,
        value: Math.random() * 130
      },
      {
        name: this.high[4].county,
        value: Math.random() * 140
      }
    ]
  },
    {
    name: '中高风险地区',
    children: [
      {
        name: this.mid[0].county,
        value: Math.random() * 150
      },
      {
        name: this.mid[1].county,
        value: Math.random() * 160
      },
      {
        name: this.mid[2].county,
        value: Math.random() * 170
      },
      {
        name: this.mid[3].county,
        value: Math.random() * 180
      },
      {
        name: this.mid[4].county,
        value: Math.random() * 190
      },
      {
        name: this.mid[5].county,
        value: Math.random() * 200
      },
      {
        name: this.mid[6].county,
        value: Math.random() * 210
      },
      {
        name: this.mid[7].county,
        value: Math.random() * 220
      },
      {
        name: this.mid[8].county,
        value: Math.random() * 230
      },
      {
        name: this.mid[9].county,
        value: Math.random() * 240
      },
      {
        name: this.mid[10].county,
        value: Math.random() * 250
      },
      {
        name: this.mid[11].county,
        value: Math.random() * 260
      }
    ]
  }
]
const option = {
  title: {
    color: 'red',
    text: '疫情分布',
    subtext: '截止时间' + `${this.time}`,
     subtextStyle: {
            color: 'red',
            fontFamily: 'Arial, Verdana, sans...',
            fontSize: 12,
            fontStyle: 'normal',
            fontWeight: 'normal'
          }
  },
  visualMap: {
    type: 'continuous',
    min: 0,
    max: 260,
    inRange: {
      color: ['#2F93C8', '#AEC48F', '#FFDB5C', '#F98862']
    }
  },
  series: {
    type: 'sunburst',
    data: data,
    radius: [0, '90%'],
    label: {
      rotate: 'radial'
    }
  }
}
     const mychart = this.$echarts.init(document.querySelector('#area'))
     mychart.setOption(option)
    }

  }
}
</script>

<style lang="less" scoped>
  div{
      margin: 10px auto;
      height: 400px;
      width: 400px;
    }
</style>>
