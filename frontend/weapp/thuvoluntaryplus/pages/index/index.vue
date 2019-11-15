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
		}
	}
    
    function login() {
		/*
		uni.checkSession({
		    success: (res) => {
		        // TODO
		        
		        if (!res) {
		            uni.login({
		                provider:"weixin",
		                success: (res) => {
		                    console.log("login", res)
		                }
		            })
		        }
		        
		    //},
		
		    fail: (res) => {
		        console.log("check fail", res)
		    }
		})*/
		uni.login({
		  provider: 'weixin',
		  success: function (loginRes) {
		    code = loginRes.code;
		  }
		});
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
