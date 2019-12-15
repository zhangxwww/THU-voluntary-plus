<template>
  <view>
    <view class="cu-form-group margin-top">
      <textarea maxlength="-1"
                :disabled="modalName!=null"
                @input="textareaAInput"
                placeholder="多行文本输入框"></textarea>
    </view>
    <view style="margin-top: 20upx; margin-right: 20upx; float: right">
      <button class="cu-btn shadow bg-green"
              @tap="join">
        <text class="text-sm">提交反馈</text>{{ joinButtonText }}</button>
    </view>
  </view>
</template>

<script>
export default {
  data () {
    return {

    }
  },
  methods: {

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
