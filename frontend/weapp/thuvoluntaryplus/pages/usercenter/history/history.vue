<template>
  <view class="cu-list menu card-menu margin-top">
    <view v-for="item in historyList"
          :key="item.id"
          @click="handleClick($event)"
          :id="'active' + item.id"
          class="cu-item noneBottom arrow">
      <view class="content grid justify-around">
        <view>
          <view class="cu-tag bg-mauve round margin-right">
            <text class="text-white cuIcon-locationfill"></text>
            <text class="text-white">{{ item.location }}</text>
          </view>
        </view>
        <text class="content margin-right">{{ item.name }} </text>
      </view>
    </view>
  </view>
</template>

<script>
import { mapState } from 'vuex'
export default {
  data () {
    return {
      list: [
        {
          id: 0,
          location: '北京',
          name: '十一期间参观志愿者',
          workingTime: 5
        },
        {
          id: 1,
          location: '河北',
          name: '廊坊志愿小学支教',
          workingTime: 1.5
        },
        {
          id: 3,
          location: '河北',
          name: '廊坊志愿小学支教',
          workingTime: 99
        },
        {
          id: 4,
          location: '河北',
          name: '廊坊志愿小学支教',
          workingTime: 8.1
        }
      ]
    }
  },
  computed: {
    ...mapState(['sessionid']),
    historyList: function () {
      return this.list
    }
  },
  beforeMount () {
    uni.setNavigationBarTitle({
      title: '志愿历史'
    })
  },
  onShow () {
    this.getHistoryList()
  },
  methods: {
    getHistoryList () {
      uni.request({
        url: 'https://thuvplus.iterator-traits.com/api/volunteer/history',
        method: 'GET',
        header: {
          'Content-Type': 'application/json',
          'Set-Cookie': 'sessionid=' + this.sessionid
        },
        success: res => {
          if (res.statusCode === 200) {
            let list = res.data.history
            this.list.splice(0, this.list.length)
            for (let it of list) {
              let new_item = {
                id: it.id,
                location: it.city,
                name: it.title,
                status: it.state
              }
              this.list.push(new_item)
            }
          } else {
            console.log(res)
          }
        },
        fail: e => {
          console.log(e)
        }
      })
    },
    handleClick (e) {
      uni.request({
        url: 'https://thuvplus.iterator-traits.com/api/activities/detail',
        method: 'POST',
        header: {
          'Content-Type': 'application/json',
          "Set-Cookie": "sessionid=" + this.sessionid
        },
        data: {
          activity_id: e.currentTarget.id.substring(6)
        },
        success: (res) => {
          if (res.statusCode === 200) {
            let data = res.data
            this.activitydata = {
              id: data.id,
              location: data.location,
              time: data.startdate + '-' + data.enddate,
              organizer: data.organizer,
              tag: data.tag,
              city: data.city,
              location: data.location,
              detail: data.desc,
              participantList: [],
              hasJoin: data.registered
            }
            for (let part of data.participants) {
              this.activitydata.participantList.push({
                id: part.thuid,
                username: part.name,
                studentID: part.thuid,
                gender: 'male',
                avatarUrl: 'url(https://ossweb-img.qq.com/images/lol/web201310/skin/big10001.jpg)'
              })
            }
            this.$store.commit('setActivityData', this.activitydata)
            uni.navigateTo({
              url: '/pages/index/detail/detail'
            })
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

<style></style>
