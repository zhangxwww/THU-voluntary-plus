<!--活动详情组件-->
<template>
	<scroll-view>
		<view class="cu-card case">
			<view class="cu-item shadow">
				<!--location and title-->
				<view class="cu-bar bg-white solid-top solid-bottom mygrid">
					<view class="action mygridcol1">
						<text :class="[textColor, titleIcon]">{{city}}</text>
					</view>
					<text class="mygridcol2">{{title}}</text>
				</view>
				<!--time-->
				<view class="cu-bar bg-white solid-top solid-bottom mygrid">
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
				<view class="cu-bar bg-white solid-top solid-bottom mygrid">
					<view class="action mygridcol1">
						<text :class="[textColor, locationIcon]" class="mygridcol1">地点</text>
					</view>
					<text class="mygridcol2">{{location}}</text>
				</view>
			</view>
		</view>
		
		<view class="cu-card case">
			<view class="cu-item shadow">
				<!--详情-->
				<view class="cu-bar bg-white solid-top ">
					<view class="action">
						<text :class="[textColor, titleIcon]">详情</text>
					</view>
				</view>
				<view class="cu-bar bg-white solid-top ">
					<view class="action">
						{{detail}}
					</view>
				</view>
			</view>
		</view>
		<view class="cu-card case">
			<view class="cu-item shadow">
				<!--详情-->
				<view class="cu-bar bg-white solid-top ">
					<view class="action">
						<text :class="[textColor, titleIcon]">参与人员</text>
					</view>
				</view>
				<view class="cu-bar bg-white solid-top ">
					<view class="action">
						<ul id="example-1">
						  <li v-for="item in participantList" :key=item.studentID>
						    {{ item["username"] }}
						  </li>
						</ul>
					</view>
				</view>
			</view>
		</view>
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
		data() {
			return {
				textColor: 'text-mauve',
				locationIcon: 'cuIcon-locationfill',
				timeIcon: 'cuIcon-timefill',
				peopleIcon: 'cuIcon-peoplefill',
				tagIcon: 'cuIcon-tagfill',
				titleIcon: 'cuIcon-formfill'
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
</style>
