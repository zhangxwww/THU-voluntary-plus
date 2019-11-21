import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '@/views/Login'
import AddActivity from '@/views/AddActivity'
import ActivityCenter from '@/views/ActivityCenter'
import Layout from '@/layout/Index.vue'
//import Layout from '@/layout/index'
Vue.use(VueRouter)

const routes = [{
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
        meta: {
            title: '例子',
            icon: 'index'
        },
        children: [{
                path: 'table',
                name: 'Table',
                component: Login,
                meta: {
                    title: '表格',
                    icon: 'table'
                }
            },
            {
                path: 'tree',
                name: 'Tree',
                component: Login,
                meta: {
                    title: '树状图',
                    icon: 'tree'
                }
            }
        ]
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
        }]
    }
]

const router = new VueRouter({
    routes
})

export default router