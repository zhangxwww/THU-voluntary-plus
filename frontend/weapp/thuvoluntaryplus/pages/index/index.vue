<template>
<view>
	<Header :needSearch="needSearch" :title="title"></Header>
	<NavBar :curpage="curpage"></NavBar>
</view>
</template>

<script>
	import NavBar from '@/components/navbar.vue'
	import Header from '@/components/header.vue'
	export default {
		components: {
			NavBar,
			Header
		},
		data() {
			return {
				title: '志愿广场',
				needSearch: true,
				currentUser: {
					name: '汪大头'
				},
				curpage: 'index',
			}
		},
		computed: {
			
		},
		
		onLoad() {
			uni.setNavigationBarTitle({
				title: this.title
			})
            login()
		},
		
		methods: {
            
		}
	}
    
    function login() {
        uni.checkSession({
            success: (res) => {
                console.log("check", res)
                // TODO
                /*
                if (!res) {
                    uni.login({
                        provider:"weixin",
                        success: (res) => {
                            console.log("login", res)
                        }
                    })
                }
                */
            },
            fail: (res) => {
                console.log("check fail", res)
            }
        })
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
