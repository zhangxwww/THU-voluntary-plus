<template>
  <el-tabs v-model="activeName"
           type="border-card"
           @tab-click="handleClick">
    <el-tab-pane label="工时分配"
                 name="alloc">
      <allocation />
    </el-tab-pane>
    <el-tab-pane label="发布通知"
                 name="announce">
      <announce />
    </el-tab-pane>
    <el-tab-pane label="查看反馈"
                 name="feedback">
      <feedback />
    </el-tab-pane>
  </el-tabs>
</template>

<script>
import Allocation from './Allocation'
import Announce from "./Announce"
import Feedback from "./Feedback"

export default {
  components: {
    Allocation,
    Announce,
    Feedback
  },
  data () {
    return {
      activeName: 'alloc',
    }
  },
  computed: {},
  methods: {
    handleClick (tab, event) {
      window.console.log(event)
    }
  }
}
</script>

<style scope>
</style>