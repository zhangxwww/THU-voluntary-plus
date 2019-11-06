<template>
<NavBar :curpage="curpage"></NavBar>
</template>

<script>
	import NavBar from '../../components/navbar.vue'
	export default {
		components: {
			"NavBar": NavBar
		},
		data() {
			return {
				title: 'Hello',
				currentUser: {
					name: '汪大头'
				},
				curpage: 'index'
			}
		},
		computed: {
			
		},
		
		onLoad() {
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
