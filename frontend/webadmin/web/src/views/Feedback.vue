<template>
  <div>
    <el-table :data="updateList.filter(data => !search || data.title.toLowerCase().includes(search.toLowerCase()))">
      <el-table-column type="expand">
        <template slot-scope="props">
          <el-form label-position="left"
                   inline
                   class="demo-table-expand">
            <el-form-item label="详情">
              <span>{{ props.row.detail }}</span>
            </el-form-item>
          </el-form>
        </template>
      </el-table-column>
      <el-table-column prop="id"
                       label="#"
                       width="50"></el-table-column>
      <el-table-column prop="title"
                       label="标题"
                       width="180"></el-table-column>
      <el-table-column prop="author"
                       label="发布者"
                       width="120"></el-table-column>
      <el-table-column prop="time"
                       label="发布时间"
                       width="180">
        <template slot-scope="scope">
          <i class="el-icon-time" />
          <span>{{ scope.row.time }}</span>
        </template>
      </el-table-column>
      <el-table-column prop="status"
                       class-name="status-col"
                       label="状态"
                       width="80"
                       align="center"
                       :filters="[{ text: '已读', value: '已读' }, { text: '未读', value: '未读' }]"
                       :filter-method="filterStatus"
                       filter-placement="bottom-end">
        <template slot-scope="scope">
          <el-tag :type="scope.row.status | statusMapper">{{ scope.row.status }}</el-tag>
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
          <hidable-button icon="el-icon-check"
                          size="mini"
                          type="success"
                          text="标记为已读"
                          @click="handleCheck(scope.row)">
          </hidable-button>
        </template>
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
import HidableButton from "../components/HidableButton"
import { getFeedback, checkFeedback } from '../script/index'
import { mapState } from 'vuex'

export default {
  components: {
    // eslint-disable-next-line vue/no-unused-components
    HidableButton
  },
  name: "Feedback",
  filters: {
    statusMapper (status) {
      const statusMap = {
        '已读': 'success',
        '未读': 'warning',
      };
      return statusMap[status]
    }
  },
  data () {
    return {
      rawlist: [{
        id: 1,
        title: '垃圾微沙龙',
        detail: '垃圾微沙龙不能喝咖啡垃圾微沙龙不能喝咖啡垃圾微沙龙不能喝咖啡垃圾微沙龙不能喝咖啡垃圾微沙龙不能喝咖啡垃圾微沙龙不能喝咖啡垃圾微沙龙不能喝咖啡垃圾微沙龙不能喝咖啡',
        time: '2019-10-1',
        status: '已读',
        author: '张大头'
      }, {
        id: 2,
        title: '注意口臭',
        detail: '大家一定要管好自己的嘴，不要随便口吐莲花，不要嘴臭臭哦！大家一定要管好自己的嘴，不要随便口吐莲花，不要嘴臭臭哦！大家一定要管好自己的嘴，不要随便口吐莲花，不要嘴臭臭哦！大家一定要管好自己的嘴，不要随便口吐莲花，不要嘴臭臭哦！大家一定要管好自己的嘴，不要随便口吐莲花，不要嘴臭臭哦！大家一定要管好自己的嘴，不要随便口吐莲花，不要嘴臭臭哦！',
        time: '2019-10-1',
        author: '张大头',
        status: '未读'
      }, {
        id: 3,
        title: '注意口臭',
        detail: '大家一定要管好自己的嘴，不要随便口吐莲花，不要嘴臭臭哦！大家一定要管好自己的嘴，不要随便口吐莲花，不要嘴臭臭哦！大家一定要管好自己的嘴，不要随便口吐莲花，不要嘴臭臭哦！大家一定要管好自己的嘴，不要随便口吐莲花，不要嘴臭臭哦！大家一定要管好自己的嘴，不要随便口吐莲花，不要嘴臭臭哦！大家一定要管好自己的嘴，不要随便口吐莲花，不要嘴臭臭哦！大家一定要管好自己的嘴，不要随便口吐莲花，不要嘴臭臭哦！',
        time: '2019-10-1',
        author: '张大头',
        status: '未读'
      }, {
        id: 4,
        title: '注意口臭',
        detail: '大家一定要管好自己的嘴，不要随便口吐莲花，不要嘴臭臭哦！大家一定要管好自己的嘴，不要随便口吐莲花，不要嘴臭臭哦！大家一定要管好自己的嘴，不要随便口吐莲花，不要嘴臭臭哦！大家一定要管好自己的嘴，不要随便口吐莲花，不要嘴臭臭哦！大家一定要管好自己的嘴，不要随便口吐莲花，不要嘴臭臭哦！大家一定要管好自己的嘴，不要随便口吐莲花，不要嘴臭臭哦！大家一定要管好自己的嘴，不要随便口吐莲花，不要嘴臭臭哦！大家一定要管好自己的嘴，不要随便口吐莲花，不要嘴臭臭哦！',
        time: '2019-10-1',
        author: '张大头',
        status: '已读'
      },
      ],
      hover: false,
      search: '',
      pagesize: 10,
      list: [],
      page: 1
    }
  },
  computed: {
    ...mapState(['modifyActivityId']),
    total: function () {
      return this.rawlist.length
    },
    updateList: function () {
      this.getList()
      return this.list
    }
  },
  methods: {
    updateFeedback () {
      getFeedback(this.modifyActivityId, list => {
        this.rawlist.splice(0, this.rawlist.length)
        for (let li of list) {
          let new_item = {
            id: li.id,
            title: li.title,
            detail: li.detail,
            time: li.time,
            author: li.author,
            status: li.status
          }
          this.rawlist.push(new_item)
          this.getList()
        }
      }, () => {
        alert('fail')
      })
    },
    handleSizeChange: function (val) {
      this.pagesize = val;
      this.getList()
    },
    handleCurrentChange: function (val) {
      this.page = val;
      this.getList()
    },
    handleCheck: function (row) {
      checkFeedback(row.id, () => {
        this.getFeedback()
      }, () => {
        alert('fail')
      })
    },
    filterStatus (value, row) {
      return row.status === value;
    },
    getList: function () {
      this.list = this.rawlist.slice((this.page - 1) * this.pagesize, this.page * this.pagesize)
    }
  },
  created () {
    this.getFeedback()
    this.list = this.rawlist.slice(0, this.pagesize)
  }
}
</script>

<style scoped>
</style>