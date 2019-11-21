<template>
	<view class="cu-list menu border bar-menu" :class="itemprop.separate?'margin-bottom':'solids-top'">
		<view class="cu-item" :class="itemprop.menuarrow?'arrow':''">
			<text v-if="itemprop.hasIcon" class="padding-right" :class="itemprop.icon"></text>
			<view class="content">
				<text class="text-black">{{ itemprop.infokey}}</text>
			</view>
			<view class="action">
				<text class="text-gray sm text">{{ itemprop.infovalue }}</text>
			</view>
		</view>
	</view>
</template>

<script>
    import mapState from 'vuex'
	export default {
		name: 'InfoListCard',
		props: {
			itemprop: {
				type: Object,
				required: true
			}
		},
		data() {
			return {
				
			};
		},
        computed: {
        },
        methods: {
            
        }
	}
</script>

<style>

</style>
