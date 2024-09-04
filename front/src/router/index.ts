import Vue from 'vue'
import VueRouter from 'vue-router'

import MainWindow from '@/views/MainWindow.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'MainWindow',
    component: MainWindow
  }
]

const router = new VueRouter({
  routes
})

export default router
