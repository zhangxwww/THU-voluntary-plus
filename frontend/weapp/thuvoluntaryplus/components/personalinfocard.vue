<template>
  <view class="cu-card article">
    <view class="cu-item">
      <view class="content">
        <image :src="avatarurl"
               mode="aspectFill"></image>
        <view class="desc">
          <view class="text-content lg text-gray"> {{personalinfo.name}}</view>
          <view>
            <view class="cu-tag bg-red light round">{{personalinfo.subject}}</view>
          </view>
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
  name: 'PersonalInfoCard',
  data () {
    return {
      avatarurl: 'https://overwatch.nosdn.127.net/1/assets/img/pages/heroes/list/roadhog.png'
    };
  },
  computed: {
    ...mapState(['personalinfo'])
  },
  methods: {
  }
}
</script>

<style>
</style>
