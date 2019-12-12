<template>
  <div class="app-container">
    <el-table v-loading="listLoading"
              :data="
        updateList.filter(
          data =>
            !search || data.title.toLowerCase().includes(search.toLowerCase())
        )
      "
              element-loading-text="Loading"
              fit
              highlight-current-row>
      <el-table-column type="selection"
                       width="55"></el-table-column>
      <el-table-column prop="id"
                       sortable
                       align="center"
                       label="#"
                       width="80">
      </el-table-column>
      <el-table-column prop="title"
                       width="200"
                       sortable
                       label="活动名称">
      </el-table-column>
      <el-table-column prop="assembler"
                       label="发起人"
                       width="110"
                       align="center">
      </el-table-column>
      <el-table-column prop="location"
                       sortable
                       label="活动地点"
                       width="120"
                       align="center">
      </el-table-column>
      <el-table-column prop="status"
                       class-name="status-col"
                       label="状态"
                       width="80"
                       align="center"
                       :filters="[
          { text: '已发布', value: '已发布' },
          { text: '审核中', value: '审核中' },
          { text: '已删除', value: '已删除' }
        ]"
                       :filter-method="filterStatus"
                       filter-placement="bottom-end">
        <template slot-scope="scope">
          <el-tag :type="scope.row.status | statusMapper">{{
                        scope.row.status
                        }}
          </el-tag>
        </template>
      </el-table-column>
      <el-table-column prop="time"
                       align="center"
                       label="活动时间"
                       width="120">
        <template slot-scope="scope">
          <i class="el-icon-time" />
          <span>{{ scope.row.time }}</span>
        </template>
      </el-table-column>
      <el-table-column align="right"
                       width="230">
        <template slot="header"
                  slot-scope="scope">
          <el-input v-model="search"
                    size="mini"
                    placeholder="搜索标题">
          </el-input>
          <span style="display:none">{{ scope.$index }}</span>
        </template>
        <template slot-scope="scope">
          <el-button size="mini"
                     type="info"
                     @click="handleDetail(scope.$index, scope.row)">设置
          </el-button>
          <el-button size="mini"
                     @click="handleEdit(scope.$index, scope.row)">编辑
          </el-button>
          <el-button size="mini"
                     type="danger"
                     @click="handleDelete(scope.$index, scope.row)">删除
          </el-button>
        </template>
      </el-table-column>
    </el-table>
    <div class="pagination">
      <el-pagination background
                     @size-change="handleSizeChange"
                     @current-change="handleCurrentChange"
                     :current-page="1"
                     :page-sizes="[3, 5, 10]"
                     :page-size="3"
                     layout="total, sizes, prev, pager, next, jumper"
                     :total="total">
      </el-pagination>
    </div>
  </div>
</template>

<script>
import { getActivity } from '../script/index'

export default {
  filters: {
    statusMapper (status) {
      const statusMap = {
        已发布: 'success',
        审核中: 'warning',
        已删除: 'danger'
      }
      return statusMap[status]
    }
  },
  data () {
    return {
      page: 1,
      rawlist: [],
      listLoading: false,
      search: '',
      pagesize: 3,
      list: []
    }
  },
  computed: {
    total: function () {
      return this.list.length
    },
    updateList: function () {
      return this.list
    }
  },
  created () {
    getActivity(
      (li) => {
        this.list.splice(0, this.list.length)
        for (let item of li) {
          let new_item = {
            id: item.id,
            title: item.title,
            assembler: item.organizer,
            location: item.location,
            tag: item.tag,
            status: item.status,
            time: item.startdate
          }
          this.list.push(new_item)
        }
      },
      () => {
        alert('Fail to get activity list')
        //this.list = this.rawlist.slice(0, this.pagesize)
      }
    )
  },

  methods: {
    handleEdit (index, row) {
      alert(index, row)
    },
    handleDelete (index, row) {
      alert(index, row)
    },
    handleDetail (index, row) {
      alert(index, row)
      this.$store.commit('setModifyAcitvityId', row.id)
      this.$router.push('/dashboard/config/')
    },
    filterStatus (value, row) {
      return row.status === value
    },
    getList: function () {
      this.list = this.rawlist.slice(
        (this.page - 1) * this.pagesize,
        this.page * this.pagesize
      )
    },
    handleSizeChange (val) {
      this.pagesize = val
      this.getList()
    },
    handleCurrentChange (val) {
      this.page = val
      this.getList()
    }
  }
}

</script>

<style scope>
.pagination {
  margin-top: 30px;
}
</style>
