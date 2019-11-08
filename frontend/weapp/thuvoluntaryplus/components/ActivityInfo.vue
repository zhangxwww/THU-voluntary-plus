<!--活动详情组件-->
<template>
	<div>
		<view class="cu-card case">
			<view class="cu-item shadow">
				<!--location and title-->
				<view class="cu-bar bg-white solid-top solid-bottom">
					<view class="action">
						<text :class="[textColor, titleIcon]" min-width=30% max-width=30% display="block">{{city}}</text>
							{{title}}
					</view>
				</view>
				<!--time-->
				<view class="cu-bar bg-white solid-top solid-bottom">
					<view class="action">
						<text :class="[textColor, timeIcon]">时间</text>
						    {{time}}	
					</view>
				</view>
				<!--发起人-->
				<view class="cu-bar bg-white solid-top solid-bottom">
					<view class="action">
						<text :class="[textColor, peopleIcon]">发起人</text>
						   {{organizer}}	
					</view>
				</view>
				<!--标签-->
				<view class="cu-bar bg-white solid-top solid-bottom">
					<view class="action">
						<text :class="[textColor, tagIcon]">标签</text>
						<text>{{tag}}</text>
					</view>
				</view>
				<!--地点-->
				<view class="cu-bar bg-white solid-top solid-bottom">
					<view class="action">
						<text :class="[textColor, locationIcon]">地点</text>
						    {{location}}	
					</view>
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
						  <li v-for="item in participantList">
						    {{ item["username"] }}
						  </li>
						</ul>
					</view>
				</view>
			</view>
		</view>
	</div>
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
</style>
