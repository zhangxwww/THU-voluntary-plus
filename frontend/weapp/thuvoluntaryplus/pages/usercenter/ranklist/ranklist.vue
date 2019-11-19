<template>
    <view class="cu-list menu card-menu margin-top line-mauve">
        <view class="cu-item noneBottom" :key="item.id" v-for="item in ranklist">
            <view class="content grid justify-around">
                <view class="margin-right">
                    <rank-list-medal :rank="item.rank"></rank-list-medal>
                </view>
                <view class="content">   
                    <text class="basis-lg text-black">{{ item.name}} </text>
                </view>
                <view class="action">
                    <text class="basis-lg text-grey text-sm">{{ item.totalTime}}h </text>
                </view>
            </view>
        </view>
    </view>
</template>

<script>
    import RankListMedal from '@/components/ranklistmedal.vue'
    export default {
        name: "RankList",
        components: {
            'rank-list-medal': RankListMedal
        },
        data() {
            return {
                ranklist: [{
                        id: 0,
                        rank: 1,
                        name: '汪大头',
                        totalTime: 1000
                    }, {
                        id: 1,
                        rank: 2,
                        name: '汪二头',
                        totalTime: 233
                    }, {
                        id: 2,
                        rank: 3,
                        name: '汪三头',
                        totalTime: 222
                    }, {
                        id: 3,
                        rank: 4,
                        name: '汪四头',
                        totalTime: 99
                    }, {
                        id: 4,
                        rank: 5,
                        name: '汪小头',
                        totalTime: 1
                    }
                ]
            }
        }
    }
</script>