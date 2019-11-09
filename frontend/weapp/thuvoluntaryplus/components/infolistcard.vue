<template>
	<view class="cu-list menu border bar-menu" :class="itemprop.separate?'margin-bottom':'solids-top'">
		<view class="cu-item" :class="itemprop.menuarrow?'arrow':''">
			<text v-if="itemprop.hasIcon" class="padding-right" :class="itemprop.icon"></text>
			<view class="content">
				<text class="text-black">{{ itemprop.infokey}}</text>
			</view>
			<view class="action" @tap="bindToken">
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
            bindToken: () => {
                console.log('navigate to mini')
                uni.navigateToMiniProgram({
                    appId: "wx1ebe3b2266f4afe0",
                    path: "pages/index/index",
                    envVersion: "trial",
                    extraData: {
                        "origin": "miniapp",
                        "type": "id.tsinghua"
                    },
                    success: (res) => {
                        console.log(res)
                        let token = res.token
                        // TODO POST token
                    }, 
                    fail: (res) => {
                        console.log("navi to mini failed", res)
                    }
                }) 
            }
        }
	}
</script>

<style>

</style>
