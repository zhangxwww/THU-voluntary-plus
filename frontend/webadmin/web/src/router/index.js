import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '@/views/Login'
import Layout from '@/layout/Index.vue'
//import Layout from '@/layout/index'
Vue.use(VueRouter)

const routes = [
  {
    path: '/login',
    name: 'login',
    component: Login,
    meta: {
      title: '登录'
    }
  },

  {
    path: '/',
    redirect: '/index'
  },

  {
    path: '/index',
    component: Layout,
    redirect: '/index/table',
    name: 'Index',
    meta: { title: '例子', icon: 'index' },
    children: [
      {
        path: 'table',
        name: 'Table',
        component: Login,
        meta: { title: '表格', icon: 'table' }
      },
      {
        path: 'tree',
        name: 'Tree',
        component: Login,
        meta: { title: '树状图', icon: 'tree' }
      }
    ]
  },

  {
    path: '/form',
    component: Login,
    children: [
      {
        path: 'index',
        name: 'Form',
        component: Login,
        meta: { title: '表单', icon: 'form' }
      }
    ]
  },
]

const router = new VueRouter({
  routes
})

export default router
