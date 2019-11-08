<!--活动详情组件-->
<template>
	<scroll-view>
		<view class="cu-card case font40">
			<view class="cu-item shadow" style="border: 0.5upx solid black">
				<!--location and title-->
				<view class="cu-bar bg-white mygrid">
					<view class="action mygridcol1">
						<text :class="[textColor, titleIcon]">{{city}}</text>
					</view>
					<text class="mygridcol2" style="font-size: 43upx;font-weight:bold;">{{title}}</text>
				</view>
				<!--time-->
				<view class="cu-bar bg-white mygrid">
					<view class="action mygridcol1">
						<text :class="[textColor, timeIcon]">时间</text>
					</view>
					<text class="mygridcol2">{{time}}</text>
				</view>
				<!--发起人-->
				<view class="cu-bar bg-white mygrid">
					<view class="action mygridcol1">
						<text :class="[textColor, peopleIcon]" class="mygridcol1">发起人</text>
					</view>
					<text class="mygridcol2">{{organizer}}</text>
				</view>
				<!--标签-->
				<view class="cu-bar bg-white mygrid">
					<view class="action mygridcol1">
						<text :class="[textColor, tagIcon]" class="mygridcol1">标签</text>
					</view>
					<text class="mygridcol2">{{tag}}</text>
				</view>
				<!--地点-->
				<view class="cu-bar bg-white mygrid">
					<view class="action mygridcol1">
						<text :class="[textColor, locationIcon]" class="mygridcol1">地点</text>
					</view>
					<text class="mygridcol2">{{location}}</text>
				</view>
			</view>
		</view>
		
		<view class="cu-card case font40">
			<view class="cu-item shadow" style="margin-top: 0upx;border: 0.5upx solid black">
				<!--详情-->
				<view class="cu-bar bg-white ">
					<view class="action">
						<text :class="[textColor, titleIcon]">详情</text>
					</view>
				</view>
				<view class="cu-bar bg-white ">
					<view class="action" style="font-size: 40upx;">
						{{detail}}
					</view>
				</view>
			</view>
		</view>
		
		<view class="cu-card case">
			<view class="cu-item shadow" style="margin-top: 0upx; margin-bottom: 0upx; border: 0.5upx solid black">
				<!--参会人员-->
				<view class="cu-bar bg-white">
					<view class="action">
						<text :class="[textColor, titleIcon]">参与人员</text>
					</view>
				</view>
				<view v-for="item in participantDisplayList" :key=item.studentID>
					<view class="cu-bar bg-white">
						<view class="action text-gray add-action" style="width: 100%">
							<view style="width: 50%;">
								<view style="flex-wrap: nowrap; display: flex;align-items: center;">
									<view class="cu-avatar shadow add" :style="{'background-image': item[0].avatarUrl}"></view>
									<view style="width:20%"></view>
									<view class="font40">{{item[0].username}}</view>
								</view>
							</view>
							<view style="width: 50%;" v-if="item.length>1">
								<view style="flex-wrap: nowrap; display: flex;align-items: center;">
									<view class="cu-avatar shadow add" :style="{'background-image': item[1].avatarUrl}"></view>
									<view style="width:20%"></view>
									<view class="font40">{{item[1].username}}</view>
								</view>
							</view>
						</view>
					</view>
				</view>
			</view>
		</view>
		
		<view class="cu-bar btngrid" >
			<view class="mybtncol1"></view>
			<view class="action">
				<button class="cu-btn bg-white mybtncol2" style="border: 0.5upx solid black">加入</button>
			</view>
			<view class="action">
				<button class="cu-btn bg-white mybtncol3" style="border: 0.5upx solid black">签到</button>
			</view>
		</view>
		<view class="infoComponentFooter" style="height: 50upx;"></view>
	</scroll-view>
</template>

<script>
	export default {
		Name: 'ActivityInfo',
		props: {
			city:{
				type: String,
				required: true
			},
			location:{
				type: String,
				required: true
			},
			title: {
				type: String,
				required: true
			},
			time: {
				type: String,
				required: true
			},
			organizer:{
				type: String,
				required: true
			},
			tag:{
				type: String,
				required: true
			},
			detail:{
				type: String,
				required: true
			},
			participantList:{
				type: Array,
				required: true
			}
		},
		computed:{
			participantDisplayList(){
				var newlist = []
				console.log(Math.floor(this.participantList.length/2))
				for(let i =0;i<Math.floor(this.participantList.length/2);i++){
					newlist.push([this.participantList[2*i],this.participantList[2*i+1]]);
				}
				if(this.participantList.length%2!==0){
					newlist.push([this.participantList[this.participantList.length-1]]);
				}
				console.log(newlist)
				return newlist;
			}
		},
		data() {
			return {
				textColor: 'text-mauve',
				locationIcon: 'cuIcon-locationfill',
				timeIcon: 'cuIcon-timefill',
				peopleIcon: 'cuIcon-peoplefill',
				tagIcon: 'cuIcon-tagfill',
				titleIcon: 'cuIcon-formfill',
				created: false
			};
		},
	}
</script>

<style>
	.mygrid{
		display: grid; 
		grid-auto-flow: row; 
		grid-template-columns: 30% 70%;
		grid-template-rows: 100%;
		grid-template-areas: "col1 col2";
		width: 100%
	}
	.mygridcol1{
		grid-area: col1;
	}
	.mygridcol2{
		grid-area: col2;
	}
	.peoplegrid{
		display: grid; 
		grid-auto-flow: row; 
		grid-template-columns: 50% 50%;
		grid-template-rows: 100%;
		grid-template-areas: "peoplegridcol1 peoplegridcol2";
		width: 100%
	}
	.peoplegridcol1{
		grid-area: peoplegridcol1;
	}
	.peoplegridcol2{
		grid-area: peoplegridcol2;
	}
	.btngrid{
		display: grid; 
		grid-auto-flow: row; 
		grid-template-columns: 60% 20% 20%;
		grid-template-rows: 100%;
		grid-template-areas: "btncol1 btncol2 btncol3";
		width: 100%
	}
	.mybtncol1{
		grid-area: btncol1;
	}
	.mybtncol2{
		grid-area: btncol2;
	}
	.mybtncol3{
		grid-area: btncol3;
	}
	.font40{
		font-size: 40upx;
	}
</style>
