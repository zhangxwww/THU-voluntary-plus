<template>
  <div>
    <el-row :gutter="20">
      <el-col :span="14">
        <el-card class="box-card">
          <div slot="header"
               class="clearfix">
            <span style="font-weight: bolder">{{ descriptions.name }}</span>
          </div>
          <el-form label-position="left">
            <el-form-item label="成立时间">
              <span>{{ descriptions.setuptime }}</span>
            </el-form-item>
            <el-form-item label="联系电话">
              <span v-if="!isEdit">{{ descriptions.phone }}</span>
              <el-input v-if="isEdit"
                        v-model="descriptions.phone"></el-input>
            </el-form-item>
            <el-form-item label="电子邮箱">
              <span v-if="!isEdit"> {{ descriptions.email }}</span>
              <el-input v-if="isEdit"
                        v-model="descriptions.email"></el-input>
            </el-form-item>
            <el-form-item label="组织成员">
              <div v-for="member in descriptions.members"
                   :key="member.id"
                   :style="{ 'padding-left': '70px' }">
                <span>{{ member.name }}</span>
                <el-divider direction="vertical"></el-divider>
                <span>{{ member.subject }}</span>
              </div>
            </el-form-item>
          </el-form>
          <el-divider direction="horizontal"></el-divider>
          <el-form label-position="top">
            <el-form-item label="团体简介">
              <span v-if="!isEdit">
                {{ descriptions.about }}
              </span>
              <el-input v-if="isEdit"
                        type="textarea"
                        autosize
                        v-model="descriptions.about"></el-input>
            </el-form-item>
          </el-form>
          <el-row type="flex"
                  justify="end space-between">
            <el-col v-if="!isEdit"
                    :span="5">
              <el-button icon="el-icon-edit"
                         size="small"
                         @click="handleEdit">编辑</el-button>
            </el-col>
            <el-col v-if="isEdit"
                    :span="3">
              <el-button size="small"
                         type="success"
                         @click="handleConfirm">确认</el-button>
            </el-col>
            <el-col v-if="isEdit"
                    :span="3">
              <el-button size="small"
                         type="danger"
                         @click="handleCancel">取消</el-button>
            </el-col>
          </el-row>
        </el-card>
      </el-col>
      <el-col :span="10">
        <el-card class="box-card">
          <div slot="header"
               class="clearfix">
            <span style="font-weight: bolder">时间线</span>
          </div>
          <div class="block">
            <el-timeline>
              <el-timeline-item v-for="activity in timelines"
                                :key="activity.id"
                                :timestamp="activity.timestamp"
                                :color="activity.finished ? '#0bbd87' : 'primary'"
                                placement="top">
                <el-card>
                  <h4>{{ activity.title }}</h4>
                </el-card>
              </el-timeline-item>
            </el-timeline>
          </div>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import { getGroupInfo, getGroupTimeline, editGroupInfo } from '../script/index'
export default {
  name: 'GroupCenter',
  data () {
    return {
      isEdit: false,
      descriptions: {
        name: '霍格沃茨微志愿',
        setuptime: '2019-2-10',
        members: [
          {
            id: 0,
            name: '张大头',
            subject: '黑魔法防御术'
          },
          {
            id: 1,
            name: '汪大头',
            subject: '魔草药学'
          },
          {
            id: 2,
            name: '金大头',
            subject: '神奇动物驯养学'
          }
        ],
        phone: '11178901234',
        email: 'hogwarts@vol.thu.edu',
        about:
          '霍格沃茨微志愿团体成立于清华3/4站台，由四位热心的团员组成，他们勤奋工作，为清华大学霍格沃茨学院的志愿事业献出一份力'
      },
      timelines: [
        {
          id: 0,
          title: '北京地区交通引导',
          settler: '张大头',
          timestamp: '2019/12/10',
          finished: false
        },
        {
          id: 0,
          title: '十一期间导游',
          settler: '张大头',
          timestamp: '2019/10/1',
          finished: true
        },
        {
          id: 0,
          title: '十一期间导游',
          settler: '张大头',
          timestamp: '2019/10/1',
          finished: true
        }
      ]
    }
  },
  methods: {
    handleEdit: function () {
      this.isEdit = true
    },
    handleConfirm: function () {
      editGroupInfo(this.descriptions, () => {
        this.isEdit = false
        this.updateDescriptions()
      }, () => {
        alert('fail')
      })
    },
    handleCancel: function () {
      this.isEdit = false
    },
    updateDescriptions () {
      getGroupInfo(
        data => {
          this.descriptions.name = data.groupname
          this.descriptions.setuptime = data.setuptime
          this.descriptions.members = data.members
          this.descriptions.phone = data.phone
          this.descriptions.email = data.email
          this.descriptions.about = data.about
          window.console.log(this.descriptions)
        },
        () => {
          alert('fail')
        }
      )
    },
    updateTimeline () {
      getGroupTimeline(
        list => {
          this.timelines.splice(0, this.timelines.length)
          for (let li of list) {
            let new_item = {
              id: li.id,
              title: li.title,
              timestamp: li.startdate,
              finished: li.finished
            }
            this.timelines.push(new_item)
          }
        },
        () => {
          alert('fail')
        }
      )
    }
  },
  computed: {
    getDescriptions () {
      return this.descriptions
    },
    getTimeline () {
      return this.timelines
    }
  },
  created () {
    this.updateDescriptions()
    this.updateTimeline()
  }
}
</script>

<style scoped></style>
