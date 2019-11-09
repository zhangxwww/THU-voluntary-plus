<template>
    <view>
        <app-header :needSearch="needSearch" :title="title"></app-header>
        <user-center v-if="title==='个人中心'"></user-center>
		<active-card-list v-if="title==='志愿广场'"></active-card-list>
        <nav-bar></nav-bar>
    </view>
</template>

<script>
	import NavBar from '@/components/navbar.vue'
	import AppHeader from '@/components/appheader.vue'
	import ActiveCardList from '@/components/activecardlist.vue'
	import ActivityInfo from '@/components/activityinfo.vue'
	import UserCenter from '@/pages/usercenter/usercenter.vue'
	import {
	    mapState,  
	    mapMutations
	} from 'vuex'
	export default {
		components: {
			'nav-bar': NavBar,
			'app-header': AppHeader,
			'user-center': UserCenter,
			'active-card-list': ActiveCardList,
			'activity-info': ActivityInfo
		},
		data() {
			return {
				currentUser: {
					name: '汪大头'
				},
				activitydetail: null,
                activeList: [{
                        id: 0,
                        location: "北京",
                        name: "十一期间参观志愿者",
                        leader: "汪元标",
                        startTime: "2019.10.1",
                        endTime: "2019.10.1",
                        curnum: 5,
                        totalnum: 10,
                        type: "校内志愿活动",
                        likes: 3,
                        liked: true
                    }, {
                        id: 1,
                        location: "河北",
                        name: "廊坊志愿小学支教",
                        leader: "金昕琪",
                        startTime: "2019.10.1",
                        endTime: "2019.10.1",
                        curnum: 5,
                        totalnum: 10,
                        type: "支教",
                        likes: 5,
                        liked: false
                    }
                ]
			}
		},
		computed: {
			...mapState(['curpage', 'title']),
			needSearch: function() {
				//console.log(this.curpage === 'index')
				return (this.curpage === 'index')
			},
		},
		
		onLoad() {
			uni.setNavigationBarTitle({
				title: this.title
			})
            login()
		},
		
		methods: {
			...mapMutations(['setTitle', 'setActivityData']),
            indexShowActivityInfo(id){
				this.getActivityInfo(id)
				this.setActivityData(this.activitydetail)
				uni.navigateTo({
					url: '/pages/index/detail/detail'
				})
			},
			getActivityInfo(id){
				//TODO: download activity info data from backend server
				this.activitydetail={
					location: '北京紫荆餐厅地下',
					title: '集体编程开发活动',
					time: '2019.10.1-2019.10.4',
					organizer: "张大头",
					tag: "集体开发",
					city:"北京",
					detail:"周二下午在逃离餐厅地下进行集体敲代码。周二下午在逃离餐厅地下进行集体敲代码。周二下午在逃离餐厅地下进行集体敲代码。周二下午在逃离餐厅地下进行集体敲代码。周二下午在逃离餐厅地下进行集体敲代码。周二下午在逃离餐厅地下进行集体敲代码。",
					participantList:[
						{
							id: 0,
							username:"汪元标",
							gender: 'male',
							studentID:"2016010022",
							avatarUrl:'url(https://ossweb-img.qq.com/images/lol/web201310/skin/big10001.jpg)'
						},{
							id: 1,
							gender: 'male',
							username:'张欣炜',
							studentID:"2016010023",
							avatarUrl:'url(https://ossweb-img.qq.com/images/lol/web201310/skin/big10001.jpg)'
						},{
							id: 2,
							gender: 'female',
							username:'邵璟之',
							studentID:"2016010023",
							avatarUrl:'url(https://ossweb-img.qq.com/images/lol/web201310/skin/big10001.jpg)'
						}
					]
				}
			}
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
