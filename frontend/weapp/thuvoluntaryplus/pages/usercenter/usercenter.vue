<template>
	<view>
		<personal-info-card></personal-info-card>
		<view class="cu-card case">
			<view class="cu-item shadow">
				<user-center-card v-for="functionCard in functionCardList" 
				:key="functionCard.id" :icon="functionCard.icon" :description="functionCard.description"
				:menuarrow="functionCard.menuarrow">
				</user-center-card>
			</view>
		</view>
	</view>	
</template>

<script>
	import UserCenterCard from '@/components/usercentercard.vue'
	import PersonalInfoCard from '@/components/personalinfocard.vue'
	export default {
		Name: "UserCenter",
		components: {
			'user-center-card': UserCenterCard,
			'personal-info-card': PersonalInfoCard
		},
		data() {
			return {
				functionCardList: [ {
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
						description: '工时统计',
						icon: 'cuIcon-timefill',
						menuarrow: true
					}, {
						id: 3,
						description: '志愿历史',
						icon: 'cuIcon-selectionfill',
						menuarrow: true
					}, {
						id: 4,
						description: '志愿排行',
						icon: 'cuIcon-sort',
						menuarrow: true
					}
				]
			}
		},
		computed: {
		},
		onLoad() {
		},
		methods: {

		}
	}
    
    function bindToken() {
        uni.navigateToMiniProgram({
            appId: "wx1ebe3b2266f4afe0",
            path: "pages/index/index",
            envVersion: "trial",
            extraData: {
                "origin": "miniapp",
                "type": "id.tsinghua"
            },
            success: (res) => {
                console.log(res)
                let token = res.token
                let userInfo = uni.getUserInfo({
                    provider:"weixin",
                    success: (res) => {
                        let openId = res.userInfo.openid
                        console.log("openid: ", openId)
                        // TODO POST {token, openId}
                    }
                })
            }, 
            fail: (res) => {
                console.log("navi to mini failed", res)
            }
        }) 
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
