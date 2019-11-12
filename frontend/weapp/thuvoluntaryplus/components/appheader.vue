<template>
	<view :class="{'cu-bar':needSearch?true:false}">
		<view v-if="needSearch" class="cu-bar bg-mauve search fixed" :style="[{top:CustomBar + 'px'}]">
			<view class="search-form round">
				<text class="cuIcon-search"></text>
				<input type="text" placeholder="输入搜索的关键词" confirm-type="search"></input>
			</view>
			<view class="action">
				<button class="cu-btn lines-white text-center round">搜索</button>
			</view>
		</view>
	</view>
</template>

<script>
	export default {
		Name: 'AppHeader',
		props: {
			needSearch: {
				type: Boolean,
				required: true
			},
			title: {
				type: String,
				required: true
			},
		},
		data() {
			return {
				
			};
		}
	}
</script>

<style>
</style>
