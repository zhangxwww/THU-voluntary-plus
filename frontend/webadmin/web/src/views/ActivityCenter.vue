<template>
  <div class="app-container">
    <el-table
      v-loading="listLoading"
      :data="list"
      element-loading-text="Loading"
      border
      fit
      highlight-current-row
    >
      <el-table-column align="center" label="ID" width="95">
        <template slot-scope="scope">
          {{ scope.$index }}
        </template>
      </el-table-column>
      <el-table-column label="活动名称">
        <template slot-scope="scope">
          {{ scope.row.title }} <span><el-tag :type="scope.row.tag" effect="plain">{{ scope.row.tag }}</el-tag></span>
        </template>
      </el-table-column>
      <el-table-column label="发起人" width="110" align="center">
        <template slot-scope="scope">
          <span>{{ scope.row.assembler }}</span>
        </template>
      </el-table-column>
      <el-table-column label="活动地点" width="110" align="center">
        <template slot-scope="scope">
          {{ scope.row.location }}
        </template>
      </el-table-column>
      <el-table-column class-name="status-col" label="状态" width="110" align="center">
        <template slot-scope="scope">
          <el-tag :type="scope.row.status | statusFilter">{{ scope.row.status }}</el-tag>
        </template>
      </el-table-column>
      <el-table-column align="center" prop="created_at" label="活动时间" width="200">
        <template slot-scope="scope">
          <i class="el-icon-time" />
          <span>{{ scope.row.time }}</span>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
export default {
  filters: {
    statusFilter(status) {
      const statusMap = {
        '已发布': 'success',
        '草稿': 'gray',
        '已删除': 'danger'
      }
      return statusMap[status]
    }
  },
  data() {
    return {
      list: [{
        title: '国庆期间参观志愿者',
        assembler: '张大头',
        location: '二校门',
        tag: '参观志愿者',
        status: '已发布',
        time: '2019-10-1'
      }, {
        title: '国庆期间参观志愿者',
        assembler: '张大头',
        location: '二校门',
        tag: '参观志愿者',
        status: '已发布',
        time: '2019-10-1'
      }, {
        title: '国庆期间参观志愿者',
        assembler: '张大头',
        location: '二校门',
        tag: '参观志愿者',
        status: '已发布',
        time: '2019-10-1'
      }, {
        title: '国庆期间参观志愿者',
        assembler: '张大头',
        location: '二校门',
        tag: '参观志愿者',
        status: '已发布',
        time: '2019-10-1'
      }, {
        title: '国庆期间参观志愿者',
        assembler: '张大头',
        location: '二校门',
        tag: '参观志愿者',
        status: '已发布',
        time: '2019-10-1'
      }, {
        title: '国庆期间参观志愿者',
        assembler: '张大头',
        location: '二校门',
        tag: '参观志愿者',
        status: '已发布',
        time: '2019-10-1'
      },
      ],
      listLoading: false
    }
  },
  created() {
  },
  methods: {
  }
}
</script>
