<template>
	<view>
		<view class="cu-list menu shadow-lg card-menu margin-top">
			<view class="cu-item shadow solids-bottom">
				<view class="cu-tag round" :class="color">
					<text class="text-white">{{label}}</text>
				</view>
				<view class="content">
					<text class="text-black text-sm text-bold margin-left">{{curmsg.title}}</text>
				</view>
				<view class="action">
					<view class="text-grey text-xs">{{curmsg.time}}</view>
				</view>
			</view>
			<view class="cu-list cu-item shadow">
				<view class="content">
					<text class="text-gray text-sm">{{curmsg.content}}</text>
				</view>
			</view>
		</view>
	</view>
</template>

<script>
	import {
		mapState,
		mapMutations
	} from 'vuex'
	export default {
		data() {
			return {
				
			}
		},
		computed: {
			...mapState(['curmsg']),
			color: function() {
				if (this.curmsg.read) {
					return 'bg-green'
				} else {
					return 'bg-red'
				}
			},
			label: function() {
				if (this.curmsg.read) {
					return '已读'
				} else {
					return '未读'
				}
			}
		},
		methods: {
			
		}
	}
</script>

<style>

</style>
