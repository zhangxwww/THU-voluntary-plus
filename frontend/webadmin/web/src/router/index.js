import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

import Login from '@/views/Login'

const routes = [
    {
        path: '/',
        name: 'index',
        redirect: '/login'
    },
    {
        path: '/login',
        name: 'login',
        component: Login
    }
]

const router = new VueRouter({
	routes: routes
})

export default router