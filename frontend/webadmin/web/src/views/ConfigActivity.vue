<template>
    <el-tabs v-model="activeName" type="border-card" @tab-click="handleClick">
        <el-tab-pane label="工时分配" name="alloc"><allocation /></el-tab-pane>
        <el-tab-pane label="发布通知" name="announce">发布通知</el-tab-pane>
        <el-tab-pane label="查看反馈" name="feedback">查看反馈</el-tab-pane>
    </el-tabs>
</template>

<script>
import Allocation from './Allocation'
export default {
    components: {
        Allocation
    },
    data() {
        return {
            activeName: 'alloc'
        }
    },
    computed: {

    },
    methods: {
        handleClick(tab, event) {
            window.console.log(event)
        }
    }
}
</script>

<style scope>
</style>