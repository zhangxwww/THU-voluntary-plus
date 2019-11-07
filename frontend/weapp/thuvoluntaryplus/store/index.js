import Vue from 'vue'
import Vuex from 'vuex'
Vue.use(Vuex)

const store = new Vuex.Store({
	state: {
		curpage: 'index',
		title: '志愿广场'
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
		}
	}
})
export default store