<template>
    <view>
        <ActiveCardList :activeList="activeList"></ActiveCardList>
        <NavBar :curpage="curpage"></NavBar>
    </view>
</template>

<script>
	import NavBar from '@/components/navbar.vue'
    import ActiveCardList from "@/components/activecardlist.vue"
	export default {
		components: {
			NavBar,
            ActiveCardList
		},
		data() {
			return {
				title: 'Hello',
				currentUser: {
					name: '汪大头'
				},
				curpage: 'index',
                activeList: [{
                        id: 0,
                        name: "wyb",
                        shortDiscription: "short",
                        longDiscription: "long",
                        startTime: "2019.10.1"
                    }, {
                        id: 1,
                        name: "jxq",
                        shortDiscription: "shorthahha",
                        longDiscription: "longhhaha",
                        startTime: "2019.10.2"
                    }
                ]
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
