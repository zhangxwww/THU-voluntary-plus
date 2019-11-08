<template>
<view>
	<Header :needSearch="needSearch" :title="title"></Header>
	<ActivityInfo :location="ActivityPropList.location" :title="ActivityPropList.title"
	:time="ActivityPropList.time" :organizer="ActivityPropList.organizer" :tag="ActivityPropList.tag"
	:city="ActivityPropList.city" :detail="ActivityPropList.detail"
	v-bind:participantList="ActivityPropList.participantList"></ActivityInfo>
	<NavBar :curpage="curpage"></NavBar>
</view>
</template>

<script>
	import NavBar from '@/components/navbar.vue'
	import Header from '@/components/header.vue'
	import ActivityInfo from '@/components/ActivityInfo.vue'
	export default {
		components: {
			NavBar,
			Header,
			ActivityInfo
		},
		data() {
			return {
				title: '志愿广场',
				needSearch: true,
				currentUser: {
					name: '汪大头'
				},
				curpage: 'index',
				ActivityPropList:{
					location: 'Beijing',
					title: 'eee',
					time: '2019.10.1-2019.10.4',
					organizer: "zxw",
					tag: "coding",
					city:"北京",
					detail:"大家一起来桃李敲代码。。。",
					participantList:[
						{
							username:"wyb",
							studentID:"2016010022",
							avatarUrl:'url(https://ossweb-img.qq.com/images/lol/web201310/skin/big10001.jpg)'
						},{
							username:'zxw',
							studentID:"2016010023",
							avatarUrl:'url(https://ossweb-img.qq.com/images/lol/web201310/skin/big10001.jpg)'
						},{
							username:'sjz',
							studentID:"2016010023",
							avatarUrl:'url(https://ossweb-img.qq.com/images/lol/web201310/skin/big10001.jpg)'
						},{
							username:'jxq',
							studentID:"2016010023",
							avatarUrl:'url(https://ossweb-img.qq.com/images/lol/web201310/skin/big10001.jpg)'
						},{
							username:'..',
							studentID:"2016010023",
							avatarUrl:'url(https://ossweb-img.qq.com/images/lol/web201310/skin/big10001.jpg)'
						},{
							username:'.,,.',
							studentID:"2016010023",
							avatarUrl:'url(https://ossweb-img.qq.com/images/lol/web201310/skin/big10001.jpg)'
						}
					]
				},
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
