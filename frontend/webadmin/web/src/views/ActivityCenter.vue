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
          { text: '未开始', value: '未开始' },
          { text: '进行中', value: '进行中' },
          { text: '已结束', value: '已结束' }
        ]"
                       :filter-method="filterStatus"
                       filter-placement="bottom-end">
        <template slot-scope="scope">
          <el-tag :type="scope.row.status | statusMapper">{{ scope.row.status }}
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
                     @click="handleDetail(scope.$index, scope.row)">管理
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
    <el-dialog title="编辑活动"
               :visible.sync="editVisible">
      <el-form :model="editForm"
               :rules="rules"
               ref="editForm"
               label-width="100px"
               class="demo-editForm">
        <el-form-item label="活动名称"
                      prop="name">
          <el-input v-model="editForm.name"></el-input>
        </el-form-item>
        <el-form-item label="所在省份"
                      prop="city">
          <el-select v-model="editForm.city"
                     placeholder="请选择所在省份">
            <el-option v-for="pro in provinces"
                       :label="pro.label"
                       :value="pro.value"
                       :key="pro.id"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="具体地点"
                      prop="location">
          <el-input v-model="editForm.location"></el-input>
        </el-form-item>
        <el-form-item label="活动人数"
                      prop="totalNum">
          <el-input-number v-model="editForm.totalNum"
                           :min="1"
                           :max="50"
                           label="活动人数"></el-input-number>
        </el-form-item>
        <el-form-item label="开始时间"
                      required>
          <el-row :gutter="20">
            <el-col :span="11">
              <el-form-item prop="startdate">
                <el-date-picker type="date"
                                placeholder="选择日期"
                                v-model="editForm.startdate"
                                style="width: 100%;"></el-date-picker>
              </el-form-item>
            </el-col>
            <el-col :span="11">
              <el-form-item prop="starttime">
                <el-time-picker placeholder="选择时间"
                                v-model="editForm.starttime"
                                style="width: 100%;"></el-time-picker>
              </el-form-item>
            </el-col>
          </el-row>
        </el-form-item>
        <el-form-item label="结束时间"
                      required>
          <el-row :gutter="20">
            <el-col :span="11">
              <el-form-item prop="enddate">
                <el-date-picker type="date"
                                placeholder="选择日期"
                                v-model="editForm.enddate"
                                style="width: 100%;"></el-date-picker>
              </el-form-item>
            </el-col>
            <el-col :span="11">
              <el-form-item prop="endtime">
                <el-time-picker placeholder="选择时间"
                                v-model="editForm.endtime"
                                style="width: 100%;"></el-time-picker>
              </el-form-item>
            </el-col>
          </el-row>
        </el-form-item>
        <el-form-item label="活动标签"
                      prop="tag">
          <el-input class="input-new-tag"
                    v-model="inputValue"
                    v-if="inputVisible"
                    size="small"
                    @keyup.enter.native="handleInputConfirm"
                    @blur="handleInputConfirm">
          </el-input>
          <el-button v-else
                     plain
                     type="primary"
                     class="button-new-tag"
                     size="small"
                     @click="showInput">
            {{ editForm.tag }}
          </el-button>
        </el-form-item>
        <el-form-item label="活动简介"
                      prop="desc">
          <el-input type="textarea"
                    v-model="editForm.desc"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="success"
                     @click="submitEdit">确认
          </el-button>
          <el-button type="info"
                     @click="cancelEdit">取消</el-button>
        </el-form-item>
      </el-form>
    </el-dialog>
    <div class="pagination">
      <el-pagination background
                     @size-change="handleSizeChange"
                     @current-change="handleCurrentChange"
                     :current-page="1"
                     :page-sizes="[10, 20, 30]"
                     :page-size="10"
                     layout="total, sizes, prev, pager, next, jumper"
                     :total="total">
      </el-pagination>
    </div>
  </div>
</template>

<script>
import { getActivity, deleteActivity, editActivity } from '../script/index'

export default {
  filters: {
    statusMapper (status) {
      const statusMap = {
        未开始: 'success',
        进行中: 'warning',
        已结束: 'danger'
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
      inputVisible: false,
      inputValue: '',
      editVisible: false,
      currentEditRow: null,
      editForm: {
        name: '',
        city: '',
        location: '',
        totalNum: '',
        startdate: '',
        starttime: '',
        enddate: '',
        endtime: '',
        tag: '',
        desc: '',
      },
      provinces: [
        {
          id: 0,
          label: '北京',
          value: '北京'
        },
        {
          id: 1,
          label: '上海',
          value: '上海'
        }
      ],
      ruleForm: {
        name: '',
        region: '',
        totalNum: 1,
        startdate: '',
        starttime: '',
        enddate: '',
        endtime: '',
        delivery: false,
        tag: '',
        desc: ''
      },
      rules: {
        name: [
          { required: true, message: '请输入活动名称', trigger: 'blur' },
          { min: 3, max: 20, message: '长度在 3 到 20 个字符', trigger: 'blur' }
        ],
        city: [
          { required: true, message: '请选择所在省份', trigger: 'change' }
        ],
        location: [
          { required: true, message: '请输入具体地点', trigger: 'change' }
        ],
        totalNum: [{ required: true }],
        startdate: [
          {
            type: 'date',
            required: true,
            message: '请选择日期',
            trigger: 'change'
          }
        ],
        starttime: [
          {
            type: 'date',
            required: true,
            message: '请选择时间',
            trigger: 'change'
          }
        ],
        enddate: [
          {
            type: 'date',
            required: true,
            message: '请选择日期',
            trigger: 'change'
          }
        ],
        endtime: [
          {
            type: 'date',
            required: true,
            message: '请选择时间',
            trigger: 'change'
          }
        ],
        desc: [{ required: true, message: '请填写活动简介诶', trigger: 'blur' }]
      }
    }
  },
  computed: {
    total: function () {
      return this.rawlist.length
    },
    updateList: function () {
      this.getList()
      return this.list
    }
  },
  created () {
    this.updateActivities()
  },

  methods: {
    handleDelete (index, row) {
      deleteActivity(row.id, () => {
        this.$message({
          message: '删除成功',
          type: 'success'
        });
        this.updateActivities()
      }, () => {
        this.$message.error('删除失败，请稍后再试')
      })
    },
    updateActivities () {
      getActivity(
        li => {
          this.rawlist.splice(0, this.rawlist.length)
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
            this.rawlist.push(new_item)
            this.getList()
          }
        },
        () => {
          this.$message.error('获取列表失败，请稍后再试')
        }
      )
    },
    // eslint-disable-next-line no-unused-vars
    handleEdit (index, row) {
      this.editVisible = true
      this.currentEditRow = row
      this.editForm.name = row.title
      this.editForm.location = row.location
      this.editForm.tag = row.tag
      this.editForm.desc = row.desc
    },
    handleDetail (index, row) {
      //alert(row.id)
      this.$store.commit('setModifyAcitvityId', row.id)
      this.$router.push('/dashboard/config/')
    },
    filterStatus (value, row) {
      return row.status === value
    },
    getList: function () {
      this.list.splice(0, this.list.length, ...this.rawlist.slice((this.page - 1) * this.pagesize, this.page * this.pagesize))
    },
    handleSizeChange (val) {
      this.pagesize = val
      this.getList()
    },
    handleCurrentChange (val) {
      this.page = val
      this.getList()
    },
    submitEdit () {
      editActivity(this.currentEditRow.id, this.editForm, () => {
        this.editVisible = false
        this.updateActivities()
        this.clearEditForm()
        this.$message({
          message: '编辑成功',
          type: 'success'
        });
      }, () => {
        this.$message.error('错了哦，这是一条错误消息');
      })
    },
    cancelEdit () {
      this.editVisible = false
    },
    handleClose (tag) {
      this.dynamicTags.splice(this.dynamicTags.indexOf(tag), 1)
    },
    showInput () {
      this.inputVisible = true
      this.$nextTick(function () {
        this.$refs.saveTagInput.$refs.input.focus()
      })
    },
    clearEditForm () {
      this.editForm.name = ''
      this.editForm.location = ''
      this.editForm.city = ''
      this.editForm.totalNum = ''
      this.editForm.startdate = ''
      this.editForm.starttime = ''
      this.editForm.enddate = ''
      this.editForm.endtime = ''
      this.editForm.tag = ''
      this.editForm.desc = ''
    }
  }
}
</script>

<style scope>
.pagination {
  margin-top: 30px;
}
</style>
