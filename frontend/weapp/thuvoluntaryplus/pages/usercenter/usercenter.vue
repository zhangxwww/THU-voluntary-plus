<template>
	<view>
		<cu-list>
			<view class="cu-card case">
				<view class="cu-item shadow">
					<UserCenterCard v-for="functionCard in functionCardList" :icon="functionCard.icon" :description="functionCard.description"></UserCenterCard>
				</view>
			</view>
		</cu-list>
		<NavBar :curpage="curpage"></NavBar>
	</view>
</template>

<script>
	import NavBar from '@/components/navbar.vue'
	import UserCenterCard from '@/components/usercentercard.vue'
	export default {
		components: {
			NavBar,
			UserCenterCard
		},
		data() {
			return {
				title: '个人中心',
				currentUser: {
					name: '汪大头'
				},
				curpage: 'userCenter',
				functionCardList: [ {
						description: '消息中心',
						icon: 'cuIcon-messagefill'
					}, {
						description: '个人信息',
						icon: 'cuIcon-infofill'
					}, {
						description: '工时统计',
						icon: 'cuIcon-timefill'
					}, {
						description: '志愿历史',
						icon: 'cuIcon-selectionfill'
					}, {
						description: '志愿排行',
						icon: 'cuIcon-sort'
					}
				]
			}
		},
		computed: {
		},
		onLoad() {
            // bindToken()
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
