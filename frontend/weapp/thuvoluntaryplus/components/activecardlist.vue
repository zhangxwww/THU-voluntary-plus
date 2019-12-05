<template>
  <view>
    <view v-for="item in updateList"
          :key="item.id">
      <active-card :item="item"></active-card>
    </view>
  </view>
</template>

<script>
import {
  mapState,
  mapMutations
} from 'vuex'
import ActiveCard from '@/components/activecard.vue'
export default {
  name: "ActiveCardList",
  components: {
    'active-card': ActiveCard
  },
  props: {
  },

  data () {
    return {
      activelist: []
    };
  },

  computed: {
    ...mapState(['sessionid']),
    updateList: function () {
      return this.activelist
    }
  },

  mounted: function () {
    this.login()
  },

  created: function () {
    this.getActivityList()
  },

  onShow () {
    this.getActivityList()
  },

  methods: {
    login () {
      var that = this
      uni.login({
        provider: 'weixin',
        success: function (loginRes) {
          uni.request({
            url: 'https://thuvplus.iterator-traits.com/api/login',
            method: 'POST',
            header: {
              'Content-Type': 'application/json'
            },
            data: {
              'wx_code': loginRes.code
            },
            success (res) {
              if (res.statusCode === 200) {
                console.log(res);
                let sessionid = res["header"]["Set-Cookie"].split(";")[0].split("=")[1];
                console.log(sessionid)
                that.$store.commit('setSessionId', sessionid);
                if (res.data.BINDED) {
                  let info = {
                    nickname: res.data.NICKNAME,
                    name: res.data.NAME,
                    subject: res.data.DEPARTMENT,
                    studentId: res.data.THUID,
                    phone: res.data.PHONE,
                    signature: res.data.SIGNATURE
                  }
                  that.$store.commit('setPersonalInfo', info)
                  that.$store.commit('setBind', true)
                }
                that.getActivityList()
              } else {
                print('post login fail')
                print(res)
              }
            },
            fail (res) {
              console.log('post login fail')
              console.log(res)
            }
          })
        },
        fail (res) {
          console.log('weixin login fail')
          console.log(res)
        }
      })
    },
    getActivityList: function () {
      uni.request({
        url: 'https://thuvplus.iterator-traits.com/api/activities/list',
        method: 'GET',
        header: {
          'Content-Type': 'application/json',
          "Set-Cookie": "sessionid=" + this.sessionid
        },
        success: (res) => {
          if (res.statusCode === 200) {
            let li = res.data.ActivityList
            this.activelist.splice(0, this.activelist.length)
            for (let item of li) {
              let new_item = {
                id: item.id,
                location: item.city,
                name: item.title,
                leader: item.organizer,
                startTime: item.startdate,
                endTime: item.enddate,
                curnum: item.remainAmount,
                totalnum: item.totalAmount,
                type: item.tag,
                likes: 0,
                liked: false
              }
              this.activelist.push(new_item)
            }
          }
        },
        fail: (res) => {
          console.log(res)
        }
      })
    }
  }
}
</script>

<style>
</style>
