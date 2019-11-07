<template>
	<view>
		<UserCenterCard></UserCenterCard>
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
				title: 'Hello',
				currentUser: {
					name: '汪大头'
				},
				curpage: 'userCenter'
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
