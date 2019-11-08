<template>
	<cu-list menu-avatar>
		<view class="cu-bar bg-white solid-top solid-bottom" :class="menuarrow?'arrow':''" @click="redirectToPage">
			<view class="action">
				<text :class="[textColor, icon]"></text> {{ description }}
			</view>
		</view>
	</cu-list>		
</template>

<script>
	export default {
		name: 'UserCenterCard',
		props: {
			icon: {
				type: String,
				required: true
			},
			description: {
				type: String,
				required: true
			},
			menuarrow: {
				type: Boolean,
				required: true
			}
		},
		
		data() {
			return {
				textColor: 'text-mauve',
			};
		},
		methods: {
			redirectToPage: function() {
				if (this.description === '个人信息') {
					uni.navigateTo({
						url: '/pages/usercenter/account/account'
					})
				}
			}
		}
	} 
</script>

<style>

</style>
