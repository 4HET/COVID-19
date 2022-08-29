import Vue from 'vue'
import VueRouter from 'vue-router'
import screenpage1 from '@/views/ScreenPage1'
import screenpage2 from '@/views/ScreenPage2'
import screenpage3 from '@/views/ScreenPage3'
// import map from '@/views/map'

Vue.use(VueRouter)

const routes = [
  // 第一个页面 声明 路径 和 路由名称
  {
    path: '/',
    component: screenpage1
  },
  {
    path: '/screen1',
    component: screenpage2
  },
  {
    path: '/screen2',
    component: screenpage3
  }

]

const router = new VueRouter({
  routes
})

export default router
