<template>
    <view>
        <view v-for="item in activelist" :key="item.id">
            <active-card :item="item"></active-card>
        </view>
    </view>
</template>

<script>
	import ActiveCard from '@/components/activecard.vue'
	export default {
        name: "ActiveCardList",
        components: {
			'active-card': ActiveCard
		},
        props: {
        },
        
		data() {
			return {
				activelist: [{
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
				    }, {
				        id: 3,
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
				    }, {
				        id: 4,
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
			};
		},
        
        computed: {
        },
        
        methods: {
        },
        
        methods: {
        }
	}
</script>

<style>

</style>
