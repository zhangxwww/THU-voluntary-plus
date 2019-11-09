import Vue from 'vue'
import Vuex from 'vuex'
Vue.use(Vuex)

const store = new Vuex.Store({
	state: {
		curpage: 'index',
		title: '志愿广场',
		personalinfo: {
			name: '张大头',
			subject: '黑魔法防御术',
			avatarurl: 'https://ossweb-img.qq.com/images/lol/web201310/skin/big10001.jpg'
		},
		activitydata: null
	},
	mutations: {
		changePageTo(state, page) {
			state.curpage = page
		},
		setTitle(state, title) {
			state.title = title
			uni.setNavigationBarTitle({
				title: title
			})
		},
		setPersonalInfo(state, info) {
			state.personalinfo = info
		},
		setActivityData(state, data) {
			state.activitydata = data
		}
	}
})
export default store