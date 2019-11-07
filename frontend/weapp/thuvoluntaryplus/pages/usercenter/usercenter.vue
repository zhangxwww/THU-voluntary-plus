<template>
	<view>
		<!--
		<view>
			<view class="cu-card case">
				<view class="cu-item shadow">
					<UserCenterCard v-for="functionCard in functionCardList" 
					:key="functionCard.id" :icon="functionCard.icon" :description="functionCard.description">
					</UserCenterCard>
				</view>
			</view>
		</view>
		-->
		<ActivityInfo :location="ActivityPropList.location" :title="ActivityPropList.title" 
		:time="ActivityPropList.time" :organizer="ActivityPropList.organizer" :tag="ActivityPropList.tag"
		:city="ActivityPropList.city" :detail="ActivityPropList.detail"
		v-bind:participantList="ActivityPropList.participantList"></ActivityInfo>
		<NavBar :curpage="curpage"></NavBar>
	</view>
</template>

<script>
	import NavBar from '@/components/navbar.vue'
	import UserCenterCard from '@/components/usercentercard.vue'
	import Header from '@/components/header.vue'
	import ActivityInfo from '@/components/ActivityInfo.vue'
	export default {
		components: {
			NavBar,
			UserCenterCard,
			ActivityInfo,
			Header
		},
		data() {
			return {
				title: '个人中心',
				needSearch: true,
				currentUser: {
					name: '汪大头'
				},
				ActivityPropList:{
					location: 'Beijing',
					title: 'eee',
					time: '2019.10.1-2019.10.4',
					organizer: "zxw",
					tag: "coding",
					city:"北京",
					detail:"大家一起来桃李敲代码。。。",
					participantList:[
						{
							username:"wyb",
							studentID:"2016010022"
						},{
							username:'zxw',
							studentID:"2016010023"
						}
					]
				},
				curpage: 'userCenter',
				functionCardList: [ {
						id: 0,
						description: '消息中心',
						icon: 'cuIcon-messagefill'
					}, {
						id: 1,
						description: '个人信息',
						icon: 'cuIcon-infofill'
					}, {
						id: 2,
						description: '工时统计',
						icon: 'cuIcon-timefill'
					}, {
						id: 3,
						description: '志愿历史',
						icon: 'cuIcon-selectionfill'
					}, {
						id: 4,
						description: '志愿排行',
						icon: 'cuIcon-sort'
					}
				]
			}
		},
		computed: {
		},
		onLoad() {
            uni.setNavigationBarTitle({
            	title: this.title
            })
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
