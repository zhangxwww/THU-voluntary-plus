<template>
  <view class="cu-card article">
    <view class="cu-item">
      <view class="content">
        <image :src="personalinfo.avatarurl"
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
