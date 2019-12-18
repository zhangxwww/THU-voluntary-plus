<template>
  <div class="container">
    <el-card style="margin-bottom: 20px"
             v-for="person in getPerson"
             :key="person.id"
             shadow="hover">
      <div slot="header">
        <el-row style="padding-right: 0px">
          <el-col :span="4">
            <el-badge :value="person.checked ? '已打卡' : '未打卡'"
                      :type="person.checked ? 'success' : 'danger'">
              <el-tag>{{ person.name }}</el-tag>
            </el-badge>
          </el-col>
          <el-col :span="14"
                  v-if="person.checked">
            <el-tag style="margin-left: 20px"
                    type="info"
                    class="el-icon-location">{{ person.checkpos }}</el-tag>
          </el-col>

          <el-col :span="6"
                  style="float: right">
            <el-button type="primary"
                       size="small"
                       @click="submitForm($event)"
                       :id="person.id">确认</el-button>
            <el-button size="small"
                       @click="resetForm($event)"
                       :id="person.id">重置</el-button>
          </el-col>
        </el-row>
      </div>
      <el-slider style="width:95%"
                 v-model="person.time"
                 show-input></el-slider>
    </el-card>
  </div>
</template>

<script>
import { getParticipant, allocateTime } from '../script/index'
import { mapState } from 'vuex'

export default {
  name: 'Allocation',
  data () {
    return {
      persons: [
        /*
      {
        id: 0,
        name: '张大头',
        avatar:
          'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg',
        department: '魔药学院',
        checked: true,
        checkpos: '桃李地下'
      },
      */
      ]
    }
  },
  computed: {
    ...mapState(['modifyActivityId']),

    getPerson () {
      return this.persons
    }
  },
  created () {
    this.updateList()
  },

  methods: {
    submitForm (e) {
      let t = e.target
      if (t.localName === 'span') {
        t = t.parentElement
      }
      let person
      for (let p of this.persons) {
        if (p.id + '' === t.id) {
          person = p
          break
        }
      }
      allocateTime(
        this.modifyActivityId,
        person.id,
        person.time,
        () => {
          this.$message({
            message: '分配成功',
            type: 'success'
          });
          this.persons.splice(this.persons.indexOf(person), 1)
        },
        () => {
          this.$message.error('分配失败，请稍后重试')
        }
      )
    },

    resetForm (e) {
      let t = e.target
      if (t.localName === 'span') {
        t = t.parentElement
      }
      for (let p of this.persons) {
        if (p.id + '' === t.id) {
          p.time = 0
          break
        }
      }
    },

    updateList () {
      getParticipant(
        this.modifyActivityId,
        list => {
          this.persons.splice(0, this.persons.length)
          for (let li of list) {
            let new_item = {
              id: li.thuid,
              name: li.name,
              checked: li.checked,
              checkpos: null,
              avatar:
                'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg'
            }
            new_item.checkpos = li.checked ? li.checkin_record.address : null
            this.persons.push(new_item)
          }
        },
        () => {
          this.$message.error('更新列表失败')
        }
      )
    }
  }
}
</script>

<style scope>
.container {
  margin-top: 20px;
  margin-left: 20px;
  width: 80%;
}

el-row {
  margin-top: 20px;
}
</style>
