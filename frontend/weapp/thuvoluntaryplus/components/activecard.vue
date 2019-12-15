<template>
  <view class="cu-list menu card-menu margin-top">
    <view class="cu-item noneBottom"
          @tap="showDetail"
          :id="'active' + item.id">
      <view class="content grid justify-around">
        <view class="basis-xs">
          <view class='cu-tag bg-mauve round'>
            <text class="text-white cuIcon-locationfill"></text>
            <text class="text-white">{{ item.location }}</text>
          </view>
        </view>
        <text class="basis-lg text-black text-lg">{{ item.name }} </text>
        <text class="basis-xs text-grey text-right">({{ item.curnum }}/{{ item.totalnum }})</text>
      </view>
    </view>
    <view class="cu-item noneBottom">
      <view class="content grid justify-around">
        <view class="basis-xs"></view>
        <view class="basis-xl">
          <text class="lg text-gray cuIcon-time"></text>
          <text class="text-grey text-df">{{ item.startTime }} 至 {{ item.endTime }}</text>
        </view>
      </view>
    </view>
    <view class="cu-item noneBottom">
      <view class="content grid justify-around">
        <view class="basis-xs">
          <text class="lg text-gray cuIcon-peoplefill"></text>
          <text class="text-grey">{{ item.leader }}</text>
        </view>
        <view class="basis-df text-left">
          <text class="lg text-gray cuIcon-tagfill"></text>
          <text class="text-grey">{{ item.type }}</text>
        </view>
        <view class="basis-xs text-right"
              @tap="like"
              :id="'like' + item.id">
          <text class="lg text-mauve"
                :class="'cuIcon-like' + (item.liked?'fill':'')"></text>
          <text class="text-grey">{{ item.likes }}</text>
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
  name: 'ActiveCard',
  props: {
    item: {
      type: Object,
      required: true
    },
  },
  data () {
    return {
      activitydata: {
        location: '北京紫荆餐厅地下',
        title: '集体编程开发活动',
        time: '2019.10.1-2019.10.4',
        organizer: "张大头",
        tag: "集体开发",
        city: "北京",
        detail: "周二下午在逃离餐厅地下进行集体敲代码。周二下午在逃离餐厅地下进行集体敲代码。周二下午在逃离餐厅地下进行集体敲代码。周二下午在逃离餐厅地下进行集体敲代码。周二下午在逃离餐厅地下进行集体敲代码。周二下午在逃离餐厅地下进行集体敲代码。",
        participantList: [
          {
            id: 0,
            username: "汪元标",
            gender: 'male',
            studentID: "2016010022",
            avatarUrl: 'url(https://ossweb-img.qq.com/images/lol/web201310/skin/big10001.jpg)'
          }, {
            id: 1,
            gender: 'male',
            username: '张欣炜',
            studentID: "2016010023",
            avatarUrl: 'url(https://ossweb-img.qq.com/images/lol/web201310/skin/big10001.jpg)'
          }, {
            id: 2,
            gender: 'female',
            username: '邵璟之',
            studentID: "2016010023",
            avatarUrl: 'url(https://ossweb-img.qq.com/images/lol/web201310/skin/big10001.jpg)'
          }
        ]
      }
    };
  },
  computed: {
    ...mapState(['sessionid']),
  },
  methods: {
    showDetail: function (e) {
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
              name: data.title,
              time: data.startdate + '-' + data.enddate,
              organizer: data.organizer,
              tag: data.tag,
              city: data.city,
              location: data.location,
              detail: data.desc,
              participantList: [],
              hasJoin: data.registered,
              status: data.status
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
    },

    like (e) {
      let activeId = parseInt(e.currentTarget.id.substring(4))
      // TODO POST
      console.log(activeId)
      /*
if (this.activeList[activeId].liked) {
    let likes = this.activeList[activeId].likes
    this.$set(this.activeList[activeId], "liked", false)
    this.$set(this.activeList[activeId], "likes", likes - 1)
} else {
    let likes = this.activeList[activeId].likes
    this.$set(this.activeList[activeId], "liked", true)
    this.$set(this.activeList[activeId], "likes", likes + 1)
}
      */
    }
  }
}
</script>

<style>
</style>
