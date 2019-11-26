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
			...mapState(['currentModified']),
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
				/* todo: 与服务器同步 */
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
