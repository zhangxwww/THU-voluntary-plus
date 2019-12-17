<!--活动详情组件-->
<template>
  <view>
    <!--活动信息-->
    <view class="cu-list menu shadow-lg card-menu margin-top">
      <view class="cu-item shadow solids-bottom">
        <!--城市和标题-->
        <view class="cu-tag bg-mauve round">
          <text class="cuIcon-locationfill text-white"></text>
          <text class="text-white">{{ itemprop.city }}</text>
        </view>
        <view class="content">
          <text class="text-black text-lg text-bold margin-left">{{ itemprop.name }}</text>

        </view>
        <view class="action"><text class="text-sm margin-left">{{itemprop.status}}</text></view>
      </view>
      <view class="cu-item shadow">
        <!--时间-->
        <view class="content">
          <text class="cuIcon-timefill text-gray"></text>
          <text class="text-gray">时间</text>
          <text class="text-black margin-left">{{ itemprop.time }}</text>
        </view>
      </view>
      <view class="cu-item shadow">
        <!--发起人-->
        <view class="content">
          <text class="cuIcon-peoplefill text-gray"></text>
          <text class="text-gray">发起人</text>
          <text class="text-black margin-left">{{ itemprop.organizer}}</text>
        </view>
      </view>
      <view class="cu-item shadow">
        <!--标签-->
        <view class="content">
          <text class="cuIcon-tagfill text-gray"></text>
          <text class="text-gray">标签</text>
          <text class="text-black margin-left">{{ itemprop.tag }}</text>
        </view>
      </view>
      <view class="cu-item shadow">
        <!--地点-->
        <view class="content">
          <text class="cuIcon-locationfill text-gray"></text>
          <text class="text-gray">地点</text>
          <text class="text-black margin-left">{{ itemprop.location }}</text>
        </view>
      </view>
    </view>

    <!--详情-->
    <view class="cu-list menu shadow-lg card-menu margin-top">
      <view class="cu-item shadow solids-bottom">
        <!--标题栏-->
        <view class="cu-tag bg-mauve round">
          <text class="cuIcon-formfill text-white"></text>
          <text class="text-white">详情</text>
        </view>
        <view class="content"></view>
      </view>
      <view class="cu-list cu-item shadow">
        <view class="content">
          <text class="text-gray text-sm">{{ itemprop.detail }}</text>
        </view>
      </view>
    </view>

    <!--参与人员-->
    <view class="cu-list menu shadow-lg card-menu margin-top">
      <view class="cu-item shadow solids-bottom">
        <!--标题栏-->
        <view class="cu-tag bg-mauve round">
          <text class="cuIcon-peoplefill text-white"></text>
          <text class="text-white">参与人员</text>
        </view>
        <view class="content"></view>
      </view>
      <!--头像列表-->
      <view v-for="person in itemprop.participantList"
            :key="person.id"
            class="cu-item arrow">
        <view class="content">
          <text v-if="person.gender==='male'"
                class="cuIcon-peoplefill text-sm text-blue"></text>
          <text v-if="person.gender==='female'"
                class="cuIcon-peoplefill text-sm text-pink"></text>
          <text v-if="person.gender==='unknown'"
                class="cuIcon-peoplefill text-sm text-gray"></text>
          <text class="text-grey text-sm">{{ person.username }}</text>
        </view>
        <view class="action cu-avatar round sm"
              :style="{'background-image' : person.avatarUrl}">
        </view>
      </view>
    </view>
    <!--按钮-->
    <view class="cu-list menu shadow-lg card-menu margin-top solid-bottom margin-bottom">
      <view class="cu-item sm">
        <view class="content">
          <text class="cuIcon-roundcheck"
                :class="hasJoinFunc?'text-green':'text-gray'"></text>
          <text class="text-grey text-sm">{{ joinInstructionText }}</text>
        </view>
        <view class="action">
          <button v-if="hasFeedbackFunc"
                  class="cu-btn sm shadow bg-gray margin-right">
            <text class="cuIcon-edit"></text>提交反馈</button>
          <button v-else-if="hasCheckedFunc"
                  @tap="feedback"
                  class="cu-btn sm shadow bg-blue margin-right">
            <text class="cuIcon-edit"></text>提交反馈</button>
          <button v-else-if="hasJoinFunc"
                  @tap="signin"
                  class="cu-btn sm shadow bg-blue margin-right">
            <text class="cuIcon-location"></text>定位打卡</button>
          <button class="cu-btn sm shadow"
                  :class="hasJoinFunc?'bg-gray':'bg-green'"
                  @tap="join">
            <text class="cuIcon-write"></text>{{ joinButtonText }}</button>
        </view>
      </view>
    </view>
  </view>
</template>

<script>
import {
  mapState,
  mapMutations
} from 'vuex'

export default {
  Name: 'ActiveInfo',
  props: {
    itemprop: {
      type: Object,
      required: true
    },
    hasJoin: {
      type: Boolean,
      required: true
    },
    hasCheckedIn: {
      type: Boolean,
      required: true
    },
    hasFeedback: {
      type: Boolean,
      required: true
    },
    status: {
      type: String,
      required: true
    }
  },
  data () {
    return {
      created: false,
      //hasJoin: false
    }
  },
  created () {
    this.$store.commit('setFeedback', true)
  },
  computed: {
    ...mapState(['sessionid', 'hasSendFeedback']),
    statusClass: function () {
      if (this.status === '进行中') {
        return "cuIcon-hot bg-mauve text-sm"
      }
      if (this.status === '未开始') {
        return "cuIcon-warn bg-orange text-sm"
      }
      if (this.status === '已完成') {
        return "cuIcon-check bg-green text-sm"
      }
    },
    joinInstructionText: function () {
      if (this.hasJoin) {
        return '您已报名参加此活动'
      } else {
        return '您尚未报名此活动，点击按钮报名'
      }
    },
    joinButtonText: function () {
      if (this.hasJoin) {
        return '取消'
      } else {
        return '加入'
      }
    },
    hasJoinFunc: function () {
      return this.hasJoin
    },
    currentState: function () {
      if (this.hasJoin && !this.hasCheckedIn) {
        return 'join'
      } else if (this.hasCheckedIn && !this.hasFeedback) {
        return 'checked'
      } else if (this.hasFeedback) {
        return 'feedback'
      }
    },
    hasCheckedFunc: function () {
      return this.hasCheckedIn && !this.hasFeedback
    },
    hasFeedbackFunc: function () {
      return this.hasFeedback
    }
  },

  methods: {
    join: function () {
      if (this.hasJoin) {
        uni.request({
          url: 'https://thuvplus.iterator-traits.com/api/activities/cancelregistration',
          method: 'POST',
          header: {
            'Content-Type': 'application/json',
            "Set-Cookie": "sessionid=" + this.sessionid
          },
          data: {
            id: this.itemprop.id
          },
          success: (res) => {
            if (res.statusCode === 200) {
              if (res.data.success) {
                this.hasJoin = false
                this.hasCheckedIn = false
                this.hasFeedback = false
              } else {
                console.log(res.data.failinfo)
              }
            } else {
              console.log(res)
            }
          },
          fail: (res) => {
            console.log(res)
          }
        })
      } else {
        uni.request({
          url: 'https://thuvplus.iterator-traits.com/api/activities/register',
          method: 'POST',
          header: {
            'Content-Type': 'application/json',
            "Set-Cookie": "sessionid=" + this.sessionid
          },
          data: {
            id: this.itemprop.id
          },
          success: (res) => {
            if (res.statusCode === 200) {
              if (res.data.success) {
                this.hasJoin = true
              } else {
                console.log(res.data.failinfo)
              }
            } else {
              console.log(res)
            }
          },
          fail: (res) => {
            console.log(res)
          }
        })
      }
    },
    signin: function () {
      uni.authorize({
        scope: 'scope.userLocation',
        success: () => {
          uni.getLocation({
            success: (res) => {
              console.log(res)
              uni.request({
                url: 'https://thuvplus.iterator-traits.com/api/activities/checkin',
                method: 'POST',
                header: {
                  'Content-Type': 'application/json',
                  "Set-Cookie": "sessionid=" + this.sessionid
                },
                data: {
                  id: this.itemprop.id,
                  latitude: res.latitude,
                  longitude: res.longitude,
                  address: res.address
                },
                success: (res) => {
                  if (res.statusCode === 200) {
                    if (res.data.success) {
                      this.hasCheckedIn = true
                    } else {
                      console.log(res.data.failinfo)
                    }
                  } else {
                    console.log(res)
                  }
                },
                fail: (res) => {
                  console.log(res)
                }
              })
            },
            fail: (res) => {
              console.log(res)
            }
          })
        },
        fail: (res) => {
          console.log(res)
        }
      })
    },
    feedback () {
      uni.navigateTo({
        url: '../../../pages/index/feedback/feedback?id=' + this.itemprop.id,
        success: () => {
          if (this.hasSendFeedback) {
            this.hasFeedback = true
          }
        }
      })
    }
  }
}
</script>

<style>
</style>
