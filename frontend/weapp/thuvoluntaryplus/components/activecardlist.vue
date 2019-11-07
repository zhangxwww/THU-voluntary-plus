<template>
    <view class="cu-list menu-avatar comment solids-top">
        <template v-for="(item, index) in activeList">
            <view class="cu-item">
                <view class="content">
                    <view class="flex  p-xs margin-bottom-sm mb-sm">
                        <view class="text-gray flex-sub">location {{ item.location }}</view>
                        <view class="text-grey flex-fifth">{{ item.name }}</view>
                    </view>
                    <view class="text-grey">{{ item.name }}</view>
                    <view class="text-gray text-content text-df">
                        {{ item.startTime }} 至 {{ item.endTime }}
                    </view>
                    <view class="bg-grey padding-sm radius margin-top-sm  text-sm">
                        <view class="flex">
                            <view class="flex-sub">{{ item.longDiscription }}</view>
                        </view>
                    </view>
                    <view class="margin-top-sm flex justify-between">
                        <view class="text-gray text-df">{{ item.startTime }}</view>
                        <view>
                            <text class="cuIcon-appreciate text-gray"></text>
                            <text class="cuIcon-messagefill text-gray margin-left-sm"></text>
                        </view>
                    </view>
                </view>
            </view>
        </template>
	</view>
</template>

<script>
	export default {
        name: "ActiveCardList",
        
        props: {
            activeList: {
                type: Array,
                required: true
            }
        },
        
        components: {
        },
		data() {
			return {
				
			};
		}
	}
</script>

<style>

</style>
