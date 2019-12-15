import Vue from 'vue'
import Vuex from 'vuex'
Vue.use(Vuex)

const store = new Vuex.Store({
  state: {
    bind: false,
    curpage: 'index',
    title: '志愿广场',
    personalinfo: {
      name: '张欣炜',
      nickname: '张大头',
      subject: '黑魔法防御术',
      avatarurl: 'https://ossweb-img.qq.com/images/lol/web201310/skin/big10001.jpg',
      studentId: 2001010101,
      phone: 18811111111,
      signature: '如果这个世界亏待你，你就杀了张欣炜'
    },
    activitydata: null,
    sessionid: '',
    curmsg: {
      id: 0,
      sender: '特奖得主金昕祺',
      avatar: 'https://ossweb-img.qq.com/images/lol/web201310/skin/big81020.jpg',
      title: '特奖得主邀您加入清华首家线上赌场',
      time: '22:20',
      read: false,
      content: '特奖得主金昕祺邀请您加入清华首家线上赌场，同花顺，扎金花，24点，统统赚大钱，美元澳元港元带回家！'
    },
    currentModified: null,
    hasSendFeedback: false
  },
  mutations: {
    setBind (state, bind) {
      state.bind = bind
    },
    changePageTo (state, page) {
      state.curpage = page
    },
    setTitle (state, title) {
      state.title = title
      uni.setNavigationBarTitle({
        title: title
      })
    },
    setPersonalInfo (state, info) {
      state.personalinfo = info
    },
    setActivityData (state, data) {
      state.activitydata = data
    },
    setSessionId (state, sessionid) {
      state.sessionid = sessionid
    },
    setCurmsg (state, msg) {
      state.curmsg = msg
    },
    modifyInfo (state, obj) {
      state.personalinfo[obj.key] = obj.value
      console.log(state.personalinfo)
    },
    setCurrentModified (state, obj) {
      state.currentModified = obj
    },
    setFeedback (state, s) {
      state.hasSendFeedback = s
    }
  }
})
export default store
