<template>
  <div class="app-container">
    <el-row>
      <el-button icon="el-icon-plus"
                 @click="getVerificationCode"
                 style="margin-bottom: 30px">生成邀请码
      </el-button>
      <el-input v-model="verificationCode"
                class="verificationinput"></el-input>
    </el-row>
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
      <el-table-column type="expand">
        <template slot-scope="props">
          <el-form label-position="left"
                   inline
                   class="demo-table-expand">
            <el-form-item label="成立时间">
              <span>{{ props.row.setuptime }}</span>
            </el-form-item>
            <el-form-item label="联系电话">
              <span>{{ props.row.phone }}</span>
            </el-form-item>
            <el-form-item label="电子邮箱">
              <span> {{ props.row.email }}</span>
            </el-form-item>
            <el-form-item label="组织成员">
              <div v-for="member in props.row.members"
                   :key="member.id">
                <span>{{ member.name }}</span>
                <el-divider direction="vertical"></el-divider>
                <span>{{ member.subject }}</span>
              </div>
            </el-form-item>
            <el-form-item label="简介">
              <span> {{ props.row.about }}</span>
            </el-form-item>
          </el-form>
        </template>
      </el-table-column>
      <el-table-column prop="id"
                       sortable
                       align="center"
                       label="#"
                       width="80">
      </el-table-column>
      <el-table-column prop="name"
                       width="200"
                       sortable
                       label="团体名称">
      </el-table-column>
      <el-table-column prop="setuptime"
                       align="center"
                       label="建立时间"
                       width="120">
        <template slot-scope="scope">
          <i class="el-icon-time" />
          <span>{{ scope.row.setuptime }}</span>
        </template>
      </el-table-column>
      <el-table-column prop="status"
                       class-name="status-col"
                       label="状态"
                       width="80"
                       align="center"
                       :filters="[
          { text: '已通过', value: '已通过' },
          { text: '待审核', value: '待审核' }
        ]"
                       :filter-method="filterStatus"
                       filter-placement="bottom-end">
        <template slot-scope="scope">
          <el-tag :type="scope.row.status | statusMapper">{{ scope.row.status }}
          </el-tag>
        </template>
      </el-table-column>
      <el-table-column align="right"
                       width="230">
        <template slot="header"
                  slot-scope="scope">
          <el-input v-model="search"
                    size="mini"
                    placeholder="搜索名称">
          </el-input>
          <span style="display:none">{{ scope.$index }}</span>
        </template>
        <!--
        <template slot-scope="scope">
          <el-button size="mini"
                     type="success"
                     @click="handlePass(scope.$index, scope.row)">通过
          </el-button>
          <el-button size="mini"
                     type="info"
                     @click="handleCancel(scope.$index, scope.row)">拒绝
          </el-button>
          <el-button size="mini"
                     type="danger"
                     @click="handleDelete(scope.$index, scope.row)">删除
          </el-button>
        </template>
        -->
      </el-table-column>
    </el-table>
    <div class="pagination">
      <el-pagination background
                     @size-change="handleSizeChange"
                     @current-change="handleCurrentChange"
                     :current-page="1"
                     :page-sizes="[10, 20, 30]"
                     :page-size="3"
                     layout="total, sizes, prev, pager, next, jumper"
                     :total="total">
      </el-pagination>
    </div>
  </div>
</template>

<script>
import { generateVerificationCode, getCheckingGroupList } from '../script/index'
export default {
  filters: {
    statusMapper (status) {
      const statusMap = {
        已通过: 'success',
        待审核: 'warning',
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
      pagesize: 10,
      list: [],
      verificationCode: ''
    }
  },
  computed: {
    total: function () {
      return this.list.length
    },
    updateList: function () {
      this.getList()
      return this.list
    }
  },
  created () {
    this.getRawList()
  },

  methods: {
    getRawList () {
      getCheckingGroupList(
        list => {
          this.rawlist.splice(0, this.rawlist.length)
          if (list === undefined) {
            return
          }
          for (let li of list) {
            let new_item = li
            new_item.name = li.groupname
            new_item.status = '已通过'
            this.rawlist.push(new_item)
          }
          this.getList()
        },
        () => {
          alert('fail')
        }
      )
    },
    // eslint-disable-next-line no-unused-vars
    handlePass (index, row) { },
    // eslint-disable-next-line no-unused-vars
    handleDelete (index, row) { },
    // eslint-disable-next-line no-unused-vars
    handleCancel (index, row) { },
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
    },
    getVerificationCode () {
      generateVerificationCode(
        code => {
          this.verificationCode = code
          alert('success')
        },
        () => {
          alert('fail')
        }
      )
    }
  }
}
</script>

<style scoped>
.pagination {
  margin-top: 30px;
}

.demo-table-expand {
  font-size: 0;
}

.demo-table-expand label {
  width: 90px;
  color: #99a9bf;
}

.demo-table-expand .el-form-item {
  margin-right: 0;
  margin-bottom: 0;
  width: 100%;
}

.verificationinput {
  width: 200px;
  margin-left: 20px;
}
</style>
