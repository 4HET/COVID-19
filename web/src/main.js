import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'
import './assets/css/css.less'
import './assets/font/iconfont.css'
import './assets/font1/iconfont.css'
import './assets/font2/iconfont.css'
import '../public/static/map/china.js'

Vue.config.productionTip = false

// 将全局echarts对象挂载到Vue的原型对象上
// 使用 echarts 时候 只需要调用 this.$echarts  就可以

Vue.prototype.$echarts = window.echarts

// 配置 axios 并且挂载到Vue的原型对象上

// 使用 axios 时候 只需要调用 this.$http 就可以

Vue.prototype.$http = axios

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
