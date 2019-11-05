<template>
<NavBar :curpage="curpage"></NavBar>
</template>

<script>
	import NavBar from '../../components/navbar.vue'
	export default {
		components: {
			NavBar
		},
		data() {
			return {
				title: 'Hello',
				currentUser: {
					name: '汪大头'
				},
				curpage: 'userCenter'
			}
		},
		computed: {
		},
		onLoad() {

		},
		methods: {

		}
	}
</script>

<style>
	.box {
		margin: 20upx 0;
	}
	
	.box view.cu-bar {
		margin-top: 20upx;
	}
</style>
