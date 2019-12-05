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
      activelist: [/* {
        id: 0,
        location: "北京",
        name: "十一期间参观志愿者",
        leader: "汪元标",
        startTime: "2019.10.1",
        endTime: "2019.10.1",
        curnum: 5,
        totalnum: 10,
        type: "校内志愿活动",
        likes: 3,
        liked: true
      }, {
        id: 1,
        location: "河北",
        name: "廊坊志愿小学支教",
        leader: "金昕琪",
        startTime: "2019.10.1",
        endTime: "2019.10.1",
        curnum: 5,
        totalnum: 10,
        type: "支教",
        likes: 5,
        liked: false
      }, {
        id: 3,
        location: "河北",
        name: "廊坊志愿小学支教",
        leader: "金昕琪",
        startTime: "2019.10.1",
        endTime: "2019.10.1",
        curnum: 5,
        totalnum: 10,
        type: "支教",
        likes: 5,
        liked: false
      }, {
        id: 4,
        location: "河北",
        name: "廊坊志愿小学支教",
        leader: "金昕琪",
        startTime: "2019.10.1",
        endTime: "2019.10.1",
        curnum: 5,
        totalnum: 10,
        type: "支教",
        likes: 5,
        liked: false
      } */
      ]
    };
  },

  computed: {
    ...mapState(['sessionid']),
    updateList: function () {
      return this.activelist
    }
  },

  created: function () {
    this.getActivityList()
  },
  
  onShow() {
      this.getActivityList()
  },

  methods: {
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
                location: item.location,
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
