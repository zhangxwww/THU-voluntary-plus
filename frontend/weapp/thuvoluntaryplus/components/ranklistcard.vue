<template>
    <view class="cu-list menu card-menu margin-top line-mauve">
        <view class="cu-item noneBottom">
            <view class="content grid justify-around">
                <view class="basis-xs">
                    <rank-list-medal :rank="rankitem.rank"></rank-list-medal>
                </view>
                <view class="basis-lg">   
                    <text class="basis-lg text-black text-xl">{{ rankitem.name}} </text>
                </view>
                <view class="basis-xs">
                    <text class="basis-lg text-black text-xl">{{ rankitem.totalTime}}h </text>
                </view>
            </view>
        </view>
    </view>
</template>

<script>
    import RankListMedal from '@/components/ranklistmedal.vue'
	export default {
        name: 'RankListCard',
        components: {
            'rank-list-medal': RankListMedal
        },
        props: {
            rankitem: {
                type: Object,
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
