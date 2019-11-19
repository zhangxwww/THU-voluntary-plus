<template>
	<view>
		<text v-if="rank===1" class="icon-xl text-gold cuIcon-upstagefill"></text>
        <text v-else-if="rank===2" class="icon-xl text-silver cuIcon-upstagefill"></text>
        <text v-else-if="rank===3" class="icon-xl text-bronze cuIcon-upstagefill"></text>
        <view v-else class="cu-tag round bg-grey padding-lr-sm">{{ rank }}</view>
	</view>
</template>

<script>
	export default {
        name: 'RankListMedal',
        props: {
            rank: {
                type: Number,
                required: true
            }
        },
		data() {
			return {
				
			};
		}
	}
</script>

<style>

</style>
