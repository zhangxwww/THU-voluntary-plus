<template>
	<view class="cu-list menu-avatar sm-border card-menu margin-top">
		<view v-for="msg in messagelist" :key="msg.id" class="cu-item cur" @tap='viewmessage(msg)'>
			<view class="cu-avatar radius lg" :style="{'background-image':'url('+msg.avatar+')'}">
				<view v-if="!msg.read" class="cu-tag badge"></view>
			</view>
			<view class="content">
				<view>
					<view class="text-cut">{{msg.sender}}</view>
				</view>
				<view class="text-gray text-sm flex">
					<view class="text-cut">{{msg.title}}</view>
				</view>
			</view>
			<view class="action">
				<view class="text-grey text-xs">{{msg.time}}</view>
				<view v-if="!msg.read" class="cu-tag round bg-red sm">未读</view>
				<view v-if="msg.read" class="cu-tag round bg-green sm">已读</view>
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
			messagelist: function() {
				return [
					{
						id: 0,
						sender: '特奖得主张欣炜',
						avatar: 'https://ossweb-img.qq.com/images/lol/web201310/skin/big81020.jpg',
						title: '特奖得主邀您加入清华首家线上赌场',
						time: '22:20',
						read: false,
						content: '特奖得主张欣炜邀请您加入清华首家线上赌，同花顺，扎金花，24点，统统赚大钱，美元澳元港元带回家，不用学习，明年直接特奖！'
					},
					{
						id: 1,
						sender: '特奖得主张欣炜',
						avatar: 'https://ossweb-img.qq.com/images/lol/web201310/skin/big81020.jpg',
						title: '特奖得主邀您加入清华首家线上赌场',
						time: '22:20',
						read: false,
						content: '特奖得主张欣炜邀请您加入清华首家线上赌，同花顺，扎金花，24点，统统赚大钱，美元澳元港元带回家，不用学习，明年直接特奖！'
					},
					{
						id: 2,
						sender: '特奖得主张欣炜',
						avatar: 'https://ossweb-img.qq.com/images/lol/web201310/skin/big81020.jpg',
						title: '特奖得主邀您加入清华首家线上赌场',
						time: '22:20',
						read: true,
						content: '特奖得主张欣炜邀请您加入清华首家线上赌，同花顺，扎金花，24点，统统赚大钱，美元澳元港元带回家，不用学习，明年直接特奖！'
					},
					{
						id: 3,
						sender: '特奖得主张欣炜',
						avatar: 'https://ossweb-img.qq.com/images/lol/web201310/skin/big81020.jpg',
						title: '特奖得主邀您加入清华首家线上赌场',
						time: '22:20',
						read: true,
						content: '特奖得主张欣炜邀请您加入清华首家线上赌，同花顺，扎金花，24点，统统赚大钱，美元澳元港元带回家，不用学习，明年直接特奖！'
					}
				]
			}
		},
		onload() {
			uni.setNavigationBarTitle({
				title: '消息中心'
			})
		},
		methods: {
			...mapMutations(['setCurmsg']),
			viewmessage: function(msg) {
				this.setCurmsg(msg)
				uni.navigateTo({
					url: '/pages/usercenter/messages/messagedetail/messagedetail'
				})
				/* todo: 向服务器请求更改此消息位已读 */
			}
		}
	}
</script>

<style>

</style>
