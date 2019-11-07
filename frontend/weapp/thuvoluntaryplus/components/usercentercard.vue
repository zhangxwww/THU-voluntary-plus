<template>
	<view class="cu-card case">
		<view class="cu-item shadow">
			<cu-list menu-avatar>
				<view class="cu-bar bg-white solid-bottom">
					<view class="action">
						<text class="cuIcon-messagefill text-mauve"></text> 消息中心
					</view>
				</view>
			</cu-list>	
			<cu-list menu-avatar>
				<view class="cu-bar bg-white solid-bottom">
					<view class="action">
						<text class="cuIcon-infofill text-mauve"></text> 个人信息
					</view>
				</view>
			</cu-list>
			<cu-list menu-avatar>
				<view class="cu-bar bg-white solid-bottom">
					<view class="action">
						<text class="cuIcon-timefill text-mauve"></text> 工时统计
					</view>
				</view>
			</cu-list>
			<cu-list menu-avatar>
				<view class="cu-bar bg-white solid-bottom">
					<view class="action">
						<text class="cuIcon-selectionfill text-mauve"></text> 志愿历史
					</view>
				</view>
			</cu-list>
			<cu-list menu-avatar>
				<view class="cu-bar bg-white solid-bottom">
					<view class="action">
						<text class="cuIcon-sort text-mauve"></text> 志愿排行
					</view>
				</view>
			</cu-list>
		</view>
	</view>
</template>

<script>
	export default {
		name: 'UserCenterCard',
		data() {
			return {
				
			};
		}
	}
</script>

<style>

</style>
