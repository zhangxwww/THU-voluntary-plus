<template>
  <view>
    <view class="cu-form-group margin-top">
      <input placeholder="标题"
             name="input"
             v-model="title">
      </input>
    </view>
    <view class="cu-form-group margin-top">

      <textarea maxlength="-1"
                @input="textAreaInput($event)"
                placeholder="详细信息"></textarea>
    </view>
    <view style="margin-top: 20upx; margin-right: 20upx; float: right">
      <button class="cu-btn shadow bg-green"
              @tap="post">
        <text class="text-sm">提交反馈</text></button>
    </view>
  </view>
</template>

<script>
import { mapState } from 'vuex'
export default {
  data () {
    return {
      id: -1,
      title: '',
      detail: ''
    }
  },
  computed: {
    ...mapState(['sessionid']),
  },
  onLoad (param) {
    this.id = param.id
  },
  methods: {
    post () {
      this.feedback(this.id, this.title, this.detail)
    },
    feedback (id, title, detail) {
      console.log(id)
      console.log(title)
      console.log(detail)
      uni.request({
        url: 'https://thuvplus.iterator-traits.com/api/feedback/post',
        method: 'POST',
        header: {
          'Content-Type': 'application/json',
          "Set-Cookie": "sessionid=" + this.sessionid
        },
        data: {
          id: id,
          title: title,
          detail: detail
        },
        success: res => {
          if (res.statusCode === 200) {
            this.$store.commit('setFeedback', true)
            uni.navigateBack({})
          } else {
            console.log(res)
          }
        },
        fail: e => {
          console.log(e)
        }
      })
    },
    textAreaInput (e) {
      this.detail = e.detail.value
    }
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
