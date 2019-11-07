<template>
	<cu-list menu-avatar>
		<view class="cu-bar bg-white solid-bottom">
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
			}
		},
		
		data() {
			return {
				textColor: 'text-mauve',
			};
		}
	}
</script>

<style>

</style>
