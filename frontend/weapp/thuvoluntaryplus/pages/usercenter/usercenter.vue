<template>
  <view>
    <personal-info-card></personal-info-card>
    <view class="cu-card case">
      <view class="cu-item shadow">
        <user-center-card v-for="functionCard in functionCardList"
                          :key="functionCard.id"
                          :icon="functionCard.icon"
                          :description="functionCard.description"
                          :menuarrow="functionCard.menuarrow">
        </user-center-card>
      </view>
    </view>
  </view>
</template>

<script>
import UserCenterCard from '@/components/usercentercard.vue'
import PersonalInfoCard from '@/components/personalinfocard.vue'
import {
  mapState,
  mapMutations
} from 'vuex'

export default {
  Name: "UserCenter",
  components: {
    'user-center-card': UserCenterCard,
    'personal-info-card': PersonalInfoCard
  },
  data () {
    return {
      functionCardList: [{
        id: 0,
        description: '消息中心',
        icon: 'cuIcon-messagefill',
        menuarrow: true
      }, {
        id: 1,
        description: '个人信息',
        icon: 'cuIcon-infofill',
        menuarrow: true
      }, {
        id: 2,
        description: '志愿历史',
        icon: 'cuIcon-selectionfill',
        menuarrow: true
      }, {
        id: 3,
        description: '志愿排行',
        icon: 'cuIcon-sort',
        menuarrow: true
      }, {
        id: 4,
        description: '注销用户',
        icon: 'cuIcon-deletefill',
        menuarrow: false
      }
      ]
    }
  },
  computed: {
  },
  methods: {
    ...mapMutations(['setTitle']),
  },
}
</script>

<style>
.box {
  margin: 20upx 0;
}

.box view.cu-bar {
  margin-top: 20upx;
}
</style>
