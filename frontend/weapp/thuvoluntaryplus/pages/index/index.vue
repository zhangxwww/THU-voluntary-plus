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
			}
		},
		computed: {
			...mapState(['curpage', 'title', 'sessionid']),
			needSearch: function() {
				//console.log(this.curpage === 'index')
				return (this.curpage === 'index')
			},
		},
		
		onLoad() {
			uni.setNavigationBarTitle({
				title: this.title
			})
            this.login()
		},
		
		methods: {
			...mapMutations(['setTitle', 'setActivityData', 'setSessionId']),
            login: function() {
                uni.login({
                    provider:"weixin",
                    success: (res) => {
                        console.log("login", res)
                        uni.request({
                            url: "/api/login",
                            data: {
                                code: res.code
                            },
                            method: "POST",
                            success: function(res) {
                                let sessionid = res.header.sessionid
                                console.log(sessionid)
                                this.setSessionId(sessionid)
                            }
                        })
                    }
                })
            }
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
			console.log(loginRes)
			uni.request({
				url: 'https://62.234.31.126/api/login',
				method: 'POST',
				header: {
					'Content-Type': 'application/json'
				},
				data: {
				    'wx_code': loginRes.code
				},
				success(res) {
					console.log(res.data)
				},
				fail(res) {
					console.log(res)
				}
			})
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
