import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '@/views/Login'
import AddActivity from '@/views/AddActivity'
import ActivityCenter from '@/views/ActivityCenter'
import ConfigActivity from '@/views/ConfigActivity'
import GroupCenter from "@/views/GroupCenter"
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
        redirect: '/dashboard'
    },

    {
        path: '/dashboard',
        redirect: '/dashboard/activity',
        component: Layout,
        name: 'Dashboard',
        meta: {
            title: '活动管理'
        },
        children: [{
            path: 'add',
            name: 'AddActivity',
            component: AddActivity,
            meta: {
                title: '发布活动'
            }
        }, {
            path: 'activity',
            name: 'ActivityCenter',
            component: ActivityCenter,
            meta: {
                title: '查看活动'
            }
        }, {
            path: 'config',
            name: 'ConfigActivity',
            component: ConfigActivity
        }]
    },
    {
        path: '/group',
        component: Layout,
        redirect: '/group/groupcenter',
        name: 'Group',
        meta: {
            title: '团体中心'
        },
        children: [
            {
                path: 'groupcenter',
                name: 'GroupCenter',
                component: GroupCenter,
                meta: {
                    title: '团体信息'
                }
            }
        ]
    }
]

const router = new VueRouter({
    routes
})

export default router