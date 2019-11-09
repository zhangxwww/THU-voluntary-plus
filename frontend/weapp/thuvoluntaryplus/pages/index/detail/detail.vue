<template>
	<view>
		<activity-info :itemprop="activitydata"></activity-info>
	</view>
</template>

<script>
	import ActivityInfo from '@/components/activityinfo.vue'
	import {
		mapState,
		mapMutations
	} from 'vuex'
	export default {
		components: {
			'activity-info': ActivityInfo
		},
		data() {
			return {
				
			}
		},
		onload: function() {
			uni.setNavigationBarTitle({
				title: '活动详情'
			})
		},
		computed: {
			...mapState(['activitydata']),
		},
		methods: {
			...mapMutations(['setTitle'])
		}
	}
</script>

<style>

</style>
