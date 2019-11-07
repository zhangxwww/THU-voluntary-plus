<template>
	<view class = "footer">
		<view class="cu-bar tabbar shadow bg-white foot">
			<view :class="{action: true, 'text-mauve': isIndex, 'text-gray': !isIndex}" @click="redirectTo('index', '/pages/index/index')">
				<view class="cuIcon-homefill"></view> 志愿广场
			</view>
			<view class="action text-gray add-action">
				<view class="cu-avatar round shadow add" style="background-image: url(https://ossweb-img.qq.com/images/lol/web201310/skin/big10001.jpg)"></view>
				{{currentUser.name}}
			</view>
			<view :class="{action: true, 'text-mauve': isUserCenter, 'text-gray': !isUserCenter}">
				<view class="cuIcon-my" @click="redirectTo('usercenter', '/pages/usercenter/usercenter')">
					<view class="cu-tag badge"></view>
				</view>
				个人中心
			</view>
		</view>
	</view>
</template>

<script>
	export default {
		name: 'NavBar',
		
		props: {
			curpage: {
				type: String,
				required: true
			}
		},
		
		data() {
			return {
				title: 'Hello',
				currentUser: {
					name: '汪大头'
				},
			}
		},
		computed: {
			isIndex: function() {
				return (this.curpage === 'index')
			},
			isUserCenter: function() {
				return (this.curpage === 'userCenter')
			}
		},
		methods: {
			redirectTo: function(curpage, url) {
				console.log('navTo called at ' + url)
				uni.redirectTo({url})
			}
		},
		onLoad() {

		}
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
