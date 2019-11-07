<template>
	<view class="cu-list menu card-menu margin-top">
	    <view class="cu-item noneBottom" @tap="showDetail" :id="'active' + item.id">
	        <view class="content grid justify-around">
	            <view class="basis-xs">
	                <view class='cu-tag bg-mauve round'>
	                    <text class="text-white cuIcon-locationfill"></text>
	                    <text class="text-white">{{ item.location }}</text>
	                </view>
	            </view>
	            <text class="basis-lg text-gray text-lg">{{ item.name }} </text>
	            <text class="basis-xs text-grey text-right">({{ item.curnum }}/{{ item.totalnum }})</text> 
	        </view>
	    </view>
	    <view class="cu-item noneBottom">
	        <view class="content grid justify-around">
	            <view class="basis-xs"></view>
	            <view class="basis-xl">
	                <text class="lg text-gray cuIcon-time"></text>
	                <text class="text-grey text-df">{{ item.startTime }} 至 {{ item.endTime }}</text>
	            </view>
	        </view>
	    </view>
	    <view class="cu-item noneBottom">
	        <view class="content grid justify-around">
	            <view class="basis-xs">
	                <text class="lg text-gray cuIcon-peoplefill"></text>
	                <text class="text-grey">{{ item.leader }}</text>
	            </view>
	            <view class="basis-df text-left">    
	                <text class="lg text-gray cuIcon-tagfill"></text>
	                <text class="text-grey">{{ item.type }}</text>
	            </view>
	            <view class="basis-xs text-right" @tap="like" :id="'like' + item.id">    
	                <text class="lg text-mauve" :class="'cuIcon-like' + (item.liked?'fill':'')"></text>
	                <text class="text-grey">{{ item.likes }}</text>
	            </view>
	        </view>
	    </view>
	</view>
</template>

<script>
	export default {
		name: 'ActiveCard',
		props: {
			item: {
				type: Object,
				required: true
			},
		},
		data() {
			return {
				
			};
		},
		computed: {
		},
		methods: {
			showDetail(e) {
			    let activeId = parseInt(e.currentTarget.id.substring(6))
			    // TODO POST
			    console.log(activeId)
			},
			like(e) {
			    let activeId = parseInt(e.currentTarget.id.substring(4))
			    // TODO POST
			    console.log(activeId)
			    if (this.activeList[activeId].liked) {
			        let likes = this.activeList[activeId].likes
			        this.$set(this.activeList[activeId], "liked", false)
			        this.$set(this.activeList[activeId], "likes", likes - 1)
			    } else {
			        let likes = this.activeList[activeId].likes
			        this.$set(this.activeList[activeId], "liked", true)
			        this.$set(this.activeList[activeId], "likes", likes + 1)
			    }
			}
		}
	}
</script>

<style>

</style>
