<template>
	<view class="cu-card">
		<view class="cu-item">
			<!-- 在map标签绑定经纬度和标记点数组-->
			<map id="maps" :latitude="targetLocation.latitude" :longitude="targetLocation.longitude" :markers="targetLocation.markers" scale="80"></map>
		</view>
	</view>
</template>

<script>
	import {
	    mapState,  
	    mapMutations
	} from 'vuex'
	export default{
		name: "Map",
		props: {
			targetLocation: {
				type: Object,
				required: true
			}
		}
	}
</script>

<style>
</style>
