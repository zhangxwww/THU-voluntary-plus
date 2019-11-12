<template>
    <view>
        <template v-for="item in ranklist">
            <rank-list-card :rankitem="item" :key="item.id"></rank-list-card>
        </template>
    </view>
</template>

<script>
    import RankListCard from '@/components/ranklistcard.vue'
    export default {
        name: "RankList",
        components: {
            'rank-list-card': RankListCard
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