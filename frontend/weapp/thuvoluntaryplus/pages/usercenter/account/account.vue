<template>
  <view>
    <info-list-card :itemprop="bindprop"
                    @tap="bindStudentId"></info-list-card>
    <info-list-card v-for="itemprop in itemproplist"
                    :key="itemprop.id"
                    :itemprop="itemprop"
                    @tap="onTapInfo(itemprop)"></info-list-card>
  </view>
</template>

<script>
import {
  mapState,
  mapMutations
} from 'vuex'
import InfoListCard from '@/components/infolistcard.vue'

export default {
  components: {
    'info-list-card': InfoListCard
  },
  data () {
    return {
      // bind: false,
    }
  },
  computed: {
    ...mapState(['personalinfo', 'sessionid', 'currentModified', 'bind']),
    itemproplist: function () {
      return [
        {
          id: 0,
          menuarrow: false,
          key: 'nickname',
          infokey: '昵称',
          infotype: 'text',
          infovalue: this.personalinfo.nickname,
          hasIcon: false,
          separate: false
        },
        {
          id: 1,
          menuarrow: false,
          infokey: '姓名',
          key: 'name',
          infotype: 'text',
          infovalue: this.personalinfo.name,
          hasIcon: false,
          separate: false
        },
        {
          id: 2,
          menuarrow: false,
          infokey: '学号',
          key: 'studentId',
          infotype: 'text',
          infovalue: this.personalinfo.studentId,
          hasIcon: false,
          separate: false
        },
        {
          id: 3,
          menuarrow: true,
          infokey: '电话',
          key: 'phone',
          infotype: 'text',
          infovalue: this.personalinfo.phone,
          hasIcon: false,
          separate: false
        },
        {
          id: 4,
          menuarrow: true,
          infokey: '签名',
          key: 'signature',
          infotype: 'text',
          infovalue: this.personalinfo.signature,
          hasIcon: false,
          separate: false
        }
      ]
    },
    bindprop: function () {
      if (this.bind) {
        console.log('bind!')
        return {
          menuarrow: false,
          infokey: '您已成功绑定清华账号！',
          infovalue: '',
          hasIcon: true,
          icon: 'cuIcon-roundcheckfill text-green',
          separate: true
        }
      } else {
        return {
          menuarrow: true,
          infokey: '您尚未绑定清华账号！',
          infovalue: '绑定',
          hasIcon: true,
          icon: 'cuIcon-warnfill text-red',
          separate: true
        }
      }
    },
  },
  methods: {
    ...mapMutations(['setCurrentModified', 'setPersonalInfo', 'setBind']),
    onTapInfo: function (itemprop) {
      if (itemprop.menuarrow) {
        this.setCurrentModified(itemprop)
        console.log(this.currentModified)
        uni.navigateTo({
          url: '/pages/usercenter/account/modify/modify'
        })
      }
    },
    bindStudentId: function () {
      wx.navigateToMiniProgram({
        'appId': 'wx1ebe3b2266f4afe0',
        'path': 'pages/index/index',
        'envVersion': 'trial',
        'extraData': {
          'origin': 'miniapp',
          'type': 'id.tsinghua',
        },
        complete: function () {
          that.$data.BindOperationFinished = false;
        }
      })
      var sessionid = this.sessionid
      var that = this
      wx.onAppShow(function (res) {
        if (that.$data.BindOperationFinished === false) {
          let extra = res.referrerInfo.extraData
          if (extra !== undefined) {
            that.$data.BindOperationFinished = true;
            let token = res.referrerInfo.extraData.token
            uni.request({
              url: 'https://thuvplus.iterator-traits.com/api/bind',
              header: {
                'Content-Type': 'application/json',
                "Set-Cookie": "sessionid=" + sessionid
              },
              data: {
                wx_token: token
              },
              method: 'POST',
              success: (res) => {
                if (res.statusCode === 200) {
                  that.$store.commit('setBind', true)
                  let info = {
                    nickname: res.data.NICKNAME,
                    name: res.data.NAME,
                    subject: res.data.DEPARTMENT,
                    studentId: res.data.THUID,
                    phone: res.data.PHONE,
                    signature: res.data.SIGNATURE
                  }
                  that.$store.commit('setPersonalInfo', info)
                }
              },
              complete: (res) => {
                console.log(res.statusCode)
              }
            })
          }
        }
      })
    }
  },
  beforeMount () {
    uni.setNavigationBarTitle({
      title: '个人信息'
    })
  },
}
</script>

<style>
</style>
