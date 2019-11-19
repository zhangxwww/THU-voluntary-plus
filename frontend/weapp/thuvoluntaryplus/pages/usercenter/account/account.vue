<template>
	<view>
		<info-list-card :itemprop="bindprop" @tap="bindStudentId"></info-list-card>
		<info-list-card v-for="itemprop in itemproplist" :key="itemprop.id" :itemprop="itemprop"></info-list-card>
	</view>
</template>

<script>
	import {
		mapState,
		mapMutations
	} from 'vuex'
	import InfoListCard from '@/components/infolistcard.vue'
	
	export default {
		components: {
			'info-list-card': InfoListCard
		},
		data() {
			return {
				bind: false,
				BindOperationFinished: false,
				itemproplist: [
					{
						id: 0,
						menuarrow: false,
						infokey: '昵称',
						infotype: 'text',
						infovalue: '张大头',
						hasIcon: false,
						separate: false
					},
					{
						id: 1,
						menuarrow: false,
						infokey: '姓名',
						infotype: 'text',
						infovalue: '张欣炜',
						hasIcon: false,
						separate: false
					},
					{
						id: 2,
						menuarrow: false,
						infokey: '学号',
						infotype: 'text',
						infovalue: '2016111111',
						hasIcon: false,
						separate: false
					}
				],
			}
		},
		watch: {
			BindOperationFinished(newValue, oldValue) {
				if(newValue === true){
					wx.onAppShow(function(res){
						console.log("No!")
					})
				}
			}
		},
		
		computed: {
			...mapState(['personalinfo', 'sessionid']),
			bindprop: function() {
				if (this.bind) {
					return {
						menuarrow: false,
						infokey: '您已成功绑定清华账号！',
						infovalue: '',
						hasIcon: true,
						icon: 'cuIcon-roundcheckfill text-green',
						separate: true
					}
				} else {
					return {
						menuarrow: true,
						infokey: '您尚未绑定清华账号！',
						infovalue: '绑定',
						hasIcon: true,
						icon: 'cuIcon-warnfill text-red',
						separate: true
					}
				}
			},
		},
		methods: {
			...mapMutations(['setTitle']),
            bindStudentId: function() {
                wx.navigateToMiniProgram({
                    'appId': 'wx1ebe3b2266f4afe0',
                    'path': 'pages/index/index',
                    'envVersion': 'trial',
                    'extraData': {
                        'origin': 'miniapp',
                        'type': 'id.tsinghua',
                    },
					complete: function(){
						that.$data.BindOperationFinished = false;
					}
                })
				var sessionid = this.sessionid
				var that = this
                wx.onAppShow(function(res) {
					if(that.$data.BindOperationFinished===false){
						console.log(res)
						let extra = res.referrerInfo.extraData
						if (extra !== undefined) {
							that.$data.BindOperationFinished = true;
							let token = res.referrerInfo.extraData.token
							uni.request({
								url: 'https://thuvplus.iterator-traits.com/api/bind',
								header: {
									'Content-Type': 'application/json',
									"Set-Cookie": "sessionid="+sessionid
								},
								data: {
									wx_token: token
								},
								method: 'POST',
								complete: (res) => {
									console.log(res.statusCode)
								}
							})
						}
					}
                })
            }
		},
		onload() {
			this.setTitle('个人信息')
		},
	}
</script>

<style>

</style>
