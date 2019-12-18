<template>
  <view>
    <app-header :needSearch="needSearch"
                :title="title"></app-header>
    <user-center v-if="title==='个人中心'"></user-center>
    <active-card-list v-if="title==='志愿广场'"></active-card-list>
    <nav-bar></nav-bar>
  </view>
</template>

<script>
import NavBar from '@/components/navbar.vue'
import AppHeader from '@/components/appheader.vue'
import ActiveCardList from '@/components/activecardlist.vue'
import UserCenter from '@/pages/usercenter/usercenter.vue'
import {
  mapState,
  mapMutations
} from 'vuex'

export default {
  components: {
    'nav-bar': NavBar,
    'app-header': AppHeader,
    'user-center': UserCenter,
    'active-card-list': ActiveCardList,
  },
  data () {
    return {
      currentUser: {
        name: ''
      },
      activitydetail: null,
    }
  },
  computed: {
    ...mapState(['curpage', 'title', 'sessionid']),
    needSearch: function () {
      return (this.curpage === 'index')
    },
  },

  mounted () {
    uni.setNavigationBarTitle({
      title: this.title
    })
  },


  methods: {
    ...mapMutations(['setTitle', 'setActivityData', 'setSessionId', 'setPersonalInfo', 'setBind']),

  }
}



</script>

<style>
.box {
  margin: 20upx 0;
}

.box view.cu-bar {
  margin-top: 20upx;
}
</style>
