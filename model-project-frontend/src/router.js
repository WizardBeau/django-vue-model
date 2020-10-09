import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

const routers = [
  {
    path: '/',
    component: () => import('./components/HelloWorld.vue')
  }
]

var router = new Router({
  'mode': 'history',
  routers
})
export default router
