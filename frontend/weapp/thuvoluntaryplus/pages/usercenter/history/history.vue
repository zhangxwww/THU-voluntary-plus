<template>
    <view class="cu-list menu card-menu margin-top">
        <view v-for="item in historylist" :key="item.id" class="cu-item noneBottom arrow">
            <view class="content grid justify-around">
                <view>
                    <view class='cu-tag bg-mauve round margin-right'>
                        <text class="text-white cuIcon-locationfill"></text>
                        <text class="text-white">{{ item.location }}</text>
                    </view>
                </view>
                <text class="content margin-right">{{ item.name }} </text>
                <text class="action text-grey">{{ item.workingTime }}h</text> 
            </view>
        </view>
    </view>
</template>

<script>
    export default {
        data() {
        	return {
        		historylist: [{
        		        id: 0,
        		        location: "北京",
        		        name: "十一期间参观志愿者",
        		        workingTime: 5
        		    }, {
        		        id: 1,
        		        location: "河北",
        		        name: "廊坊志愿小学支教",
        		        workingTime: 1.5
        		    }, {
        		        id: 3,
        		        location: "河北",
        		        name: "廊坊志愿小学支教",
        		        workingTime: 99
        		    }, {
        		        id: 4,
        		        location: "河北",
        		        name: "廊坊志愿小学支教",
        		        workingTime: 8.1
        		    }
        		]
        	};
        },
    }
</script>

<style>
</style>
