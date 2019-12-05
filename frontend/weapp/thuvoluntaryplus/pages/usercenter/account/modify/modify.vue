<template>
	<view>
		<form>
			<view class="cu-form-group">
				<view class="title">{{infokey}}</view>
				<input :placeholder="infoval" name="input" v-model="newVal"></input>
				<button class='cu-btn bg-mauve shadow' @tap="confirm">确认</button>
			</view>
		</form>
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
				newVal: ''
			}
		},
		computed: {
			...mapState(['currentModified', 'sessionid']),
			infokey: function() {
				return this.currentModified.infokey
			},
			infoval: function() {
				return '' + this.currentModified.infovalue
			},
			key: function() {
				return this.currentModified.key
			},
		},
		methods: {
			...mapMutations(['modifyInfo']),
			confirm: function() {
                var sessionid = this.sessionid
                var that = this
                var postKey = this.key
                var postValue = this.newVal
				/* todo: 与服务器同步 */
                uni.request({
                    url: 'https://thuvplus.iterator-traits.com/api/volunteer/changeInfo',
                    header: {
                        'Content-Type': 'application/json',
                        'Set-Cookie': 'sessionid=' + sessionid
                    },
                    data: {
                        key: postKey,
                        value: postValue
                    },
                    method: 'POST'
                })
				this.$store.commit('modifyInfo', { key: this.key, value: this.newVal})
				uni.navigateBack()
			}
		},
		onload() {
		},
		beforeMount() {
			uni.setNavigationBarTitle({
				title: '修改信息'
			})
		}
	}
</script>

<style>
.cu-form-group .title {
	min-width: calc(4em + 15px);
}
</style>
