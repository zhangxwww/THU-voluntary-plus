<template>
  <div>
    <el-steps
      :space="300"
      :active="step"
      finish-status="success"
      label-width="80px"
    >
      <el-step title="填写基本信息"></el-step>
      <el-step title="添加团队简介"></el-step>
      <el-step title="添加团队成员"></el-step>
      <el-step title="提交申请"></el-step>
    </el-steps>

    <el-form
      v-if="step === 0"
      style="margin-top: 20px; width: 50%"
      label-position="top"
    >
      <el-form-item label="团体名称">
        <el-input v-model="descriptions.name"></el-input>
      </el-form-item>
      <el-form-item label="成立时间">
        <el-col :span="11">
          <el-date-picker
            type="date"
            placeholder="选择日期"
            v-model="descriptions.setuptime"
            style="width: 100%;"
          ></el-date-picker>
        </el-col>
      </el-form-item>
      <el-form-item label="电话/手机">
        <el-input v-model="descriptions.phone"></el-input>
      </el-form-item>
      <el-form-item label="电子邮箱">
        <el-input v-model="descriptions.email"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="handleSubmit(1)">下一步</el-button>
      </el-form-item>
    </el-form>

    <el-form
      v-if="step === 1"
      autosize
      style="margin-top: 20px; width: 50%"
      label-position="top"
    >
      <el-form-item label="团体简介">
        <el-input
          rows="10"
          type="textarea"
          v-model="descriptions.about"
        ></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="handleSubmit(2)">下一步</el-button>
      </el-form-item>
    </el-form>

    <el-form v-if="step === 2" style="margin-top: 20px" label-position="top">
      <h1 style="font-size: 20px">团队成员</h1>
      <el-row
        style="margin-bottom: 20px;"
        v-for="member in descriptions.members"
        :key="member.name"
      >
        <el-tag
          block
          closable
          type="info"
          :disable-transitions="false"
          size="large"
          @close="handleClose(member)"
        >
          <span>{{ member.name }}</span>
          <el-divider direction="vertical"></el-divider>
          <span>{{ member.subject }}</span>
        </el-tag>
      </el-row>
      <el-row style="margin-top:30px">
        <el-input
          style="width: 120px;margin-right: 30px;"
          v-if="inputVisible"
          v-model="newMember.name"
          placeholder="输入姓名"
          @keyup.enter.native="handleInputConfirm"
        >
        </el-input>
        <el-input
          style="width: 120px; margin-right: 30px"
          v-if="inputVisible"
          v-model="newMember.subject"
          placeholder="输入专业"
          @keyup.enter.native="handleInputConfirm"
        >
        </el-input>
        <div v-else>
          <el-button type="primary" @click="showInput">+ 新成员</el-button>
          <el-button type="success" @click="handleSubmit(3)">下一步</el-button>
        </div>
      </el-row>
    </el-form>
  </div>
</template>

<script>
import { setupGroup } from '../script/index'
export default {
  name: 'Setup',
  data() {
    return {
      step: 0,
      descriptions: {
        name: '',
        setuptime: '',
        members: [],
        phone: '',
        email: '',
        about: ''
      },
      inputValue: '',
      inputVisible: false,
      newMember: {
        name: '',
        subject: ''
      }
    }
  },
  methods: {
    handleSubmit: function(nextstep) {
      this.step = nextstep
      if (this.step === 3) {
        setupGroup(
          this.descriptions,
          () => {
            alert('success')
          },
          () => {
            alert('fail')
          }
        )
      }
    },
    showInput: function() {
      this.inputVisible = true
    },
    handleInputConfirm: function() {
      this.descriptions.members.push(this.newMember)
      this.newMember = {
        name: '',
        subject: ''
      }
      this.inputVisible = false
    },
    handleClose: function(member) {
      this.descriptions.members.splice(
        this.descriptions.members.indexOf(member),
        1
      )
    }
  }
}
</script>

<style scoped></style>
