<template>
  <view class="cu-list menu-avatar sm-border card-menu margin-top">
    <view v-for="(msg, index) in messagelist"
          :key="msg.id"
          :index="index"
          class="cu-item cur"
          :class="modalName == 'move-box-' + index ? 'move-cur' : ''"
          @touchstart="ListTouchStart"
          @touchmove="ListTouchMove"
          @touchend="ListTouchEnd"
          :data-target="'move-box-' + index"
          @tap="ViewMessage(msg, $event)">
      <view class="cu-avatar radius lg"
            :style="{ 'background-image': 'url(' + msg.avatar + ')' }">
        <view v-if="!msg.read"
              class="cu-tag badge"></view>
      </view>
      <view class="content">
        <view>
          <view class="text-cut">{{ msg.sender }}</view>
        </view>
        <view class="text-gray text-sm flex">
          <view class="text-cut">{{ msg.title }}</view>
        </view>
      </view>
      <view class="action">
        <view class="text-grey text-xs">{{ msg.time }}</view>
        <view v-if="!msg.read"
              class="cu-tag round bg-red sm">未读</view>
        <view v-if="msg.read"
              class="cu-tag round bg-green sm">已读</view>
      </view>
      <view class="move"
            @tap.native.stop="DeleteMessage(msg.id)">
        <view class="bg-red">删除</view>
      </view>
    </view>
  </view>
</template>

<script>
import { mapState, mapMutations } from 'vuex'

export default {
  data () {
    return {
      listTouchStart: 0,
      listTouchDirection: null,
      modalName: null,
      rawlist: []
    }
  },
  computed: {
    ...mapState(['curmsg', 'sessionid']),
    messagelist: function () {
      return this.rawlist
    }
  },
  onload () {
    uni.setNavigationBarTitle({
      title: '消息中心'
    })
  },
  methods: {
    ...mapMutations(['setCurmsg']),
    UpdateList: function () {
      uni.request({
        url: 'https://thuvplus.iterator-traits.com/api/messages/list',
        method: 'POST',
        header: {
          'Content-Type': 'application/json',
          'Set-Cookie': 'sessionid=' + this.sessionid
        },
        success: res => {
          if (res.statusCode === 200) {
            let list = res.data.messages
            this.rawlist.splice(0, this.rawlist.length)
            for (let it of list) {
              let new_item = {
                id: it.id,
                sender: it.sender,
                title: it.title,
                time: it.time,
                read: it.read,
                content: it.content,
                avatar:
                  'https://ossweb-img.qq.com/images/lol/web201310/skin/big81020.jpg'
              }
              this.rawlist.push(new_item)
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
    ViewMessage: function (msg, e) {
      this.setCurmsg(msg)
      uni.request({
        url: 'https://thuvplus.iterator-traits.com/api/messages/read',
        method: 'POST',
        header: {
          'Content-Type': 'application/json',
          'Set-Cookie': 'sessionid=' + this.sessionid
        },
        data: {
          id: msg.id
        },
        success: res => {
          if (res.statusCode === 200) {
            msg.read = true
            uni.navigateTo({
              url: '/pages/usercenter/messages/messagedetail/messagedetail'
            })
          } else {
            console.log(res)
          }
        },
        fail: e => {
          console.log(e)
        }
      })
    },
    DeleteMessage: function (id) {
      console.log(id)
      uni.request({
        url: 'https://thuvplus.iterator-traits.com/api/messages/delete',
        method: 'POST',
        header: {
          'Content-Type': 'application/json',
          'Set-Cookie': 'sessionid=' + this.sessionid
        },
        data: {
          id: id
        },
        success: res => {
          if (res.statusCode === 200) {
            this.UpdateList()
          } else {
            console.log(res)
          }
        },
        fail: e => {
          console.log(e)
        }
      })
    },
    // ListTouch触摸开始
    ListTouchStart: function (e) {
      this.listTouchStart = e.touches[0].pageX
    },

    // ListTouch计算方向
    ListTouchMove: function (e) {
      this.listTouchDirection =
        e.touches[0].pageX - this.listTouchStart > 0 ? 'right' : 'left'
    },

    // ListTouch计算滚动
    ListTouchEnd: function (e) {
      if (this.listTouchDirection == 'left') {
        this.modalName = e.currentTarget.dataset.target
      } else {
        this.modalName = null
      }
      this.listTouchDirection = null
    }
  },
  beforeMount () {
    uni.setNavigationBarTitle({
      title: '消息中心'
    })
    this.UpdateList()
  },
  onShow () {
    this.UpdateList()
  }
}
</script>

<style></style>
