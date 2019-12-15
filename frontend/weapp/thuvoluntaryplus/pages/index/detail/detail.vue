<template>
  <view>
    <active-info :itemprop="activitydata"
                 :hasJoin="activitydata.hasJoin"
                 :hasCheckedIn="activitydata.hasCheckedIn"
                 :hasFeedback="activitydata.hasFeedback"
                 :status="activitydata.status"></active-info>
  </view>
</template>

<script>
import ActiveInfo from '@/components/activeinfo.vue'
import {
  mapState,
  mapMutations
} from 'vuex'

export default {
  components: {
    'active-info': ActiveInfo
  },
  data () {
    return {

    }
  },
  onload: function () {
    uni.setNavigationBarTitle({
      title: '活动详情'
    })
  },
  computed: {
    ...mapState(['activitydata']),
  },
  methods: {
    ...mapMutations(['setTitle'])
  },
  beforeMount () {
    uni.setNavigationBarTitle({
      title: '活动详情'
    })
  }
}
</script>

<style>
</style>
