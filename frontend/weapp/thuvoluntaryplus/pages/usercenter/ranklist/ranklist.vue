<template>
  <view class="cu-list menu card-menu margin-top line-mauve">
    <view class="cu-item noneBottom" :key="item.id" v-for="item in ranklist">
      <view class="content grid justify-around">
        <view class="margin-right">
          <rank-list-medal :rank="item.rank"></rank-list-medal>
        </view>
        <view class="content">
          <text class="basis-lg text-black">{{ item.name }} </text>
        </view>
        <view class="action">
          <text class="basis-lg text-grey text-sm">{{ item.totalTime }}h </text>
        </view>
      </view>
    </view>
  </view>
</template>

<script>
import RankListMedal from '@/components/ranklistmedal.vue'
import { mapState } from 'vuex'
export default {
  name: 'RankList',
  components: {
    'rank-list-medal': RankListMedal
  },
  computed: {
    ...mapState(['sessionid']),
    ranklist() {
      return this.list
    }
  },
  data() {
    return {
      last_update: 0,
      list: [
        {
          id: 0,
          rank: 1,
          name: '汪大头',
          totalTime: 1000
        },
        {
          id: 1,
          rank: 2,
          name: '汪二头',
          totalTime: 233
        },
        {
          id: 2,
          rank: 3,
          name: '汪三头',
          totalTime: 222
        },
        {
          id: 3,
          rank: 4,
          name: '汪四头',
          totalTime: 99
        },
        {
          id: 4,
          rank: 5,
          name: '汪小头',
          totalTime: 1
        }
      ]
    }
  },
  beforeMount() {
    uni.setNavigationBarTitle({
      title: '志愿排行'
    })
    this.getRankList()
  },
  methods: {
    getRankList() {
      uni.request({
        url: 'https://thuvplus.iterator-traits.com/api/volunteerhours/rank',
        method: 'GET',
        header: {
          'Content-Type': 'application/json',
          'Set-Cookie': 'sessionid=' + this.sessionid
        },
        success: res => {
          this.list.splice(0, this.list.length)
          if (res.statusCode === 200) {
            let list = res.data.list
            this.last_update = res.data.last_update_time
            for (let it of list) {
              let new_item = {
                id: it.thuid,
                rank: it.rank,
                name: it.name,
                totalTime: it.volunteer_time
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
    }
  }
}
</script>
