<template>
  <el-form :model="ruleForm"
           :rules="rules"
           ref="ruleForm"
           label-width="100px"
           class="demo-ruleForm">
    <el-form-item label="活动名称"
                  prop="name">
      <el-input v-model="ruleForm.name"></el-input>
    </el-form-item>
    <el-form-item label="所在省份"
                  prop="city">
      <el-select v-model="ruleForm.city"
                 placeholder="请选择所在省份">
        <el-option v-for="pro in provinces"
                   :label="pro.label"
                   :value="pro.value"
                   :key="pro.id"></el-option>
      </el-select>
    </el-form-item>
    <el-form-item label="具体地点"
                  prop="location">
      <el-input v-model="ruleForm.location"></el-input>
    </el-form-item>
    <el-form-item label="活动人数"
                  prop="totalNum">
      <el-input-number v-model="ruleForm.totalNum"
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
                            v-model="ruleForm.startdate"
                            style="width: 100%;"></el-date-picker>
          </el-form-item>
        </el-col>
        <el-col :span="11">
          <el-form-item prop="starttime">
            <el-time-picker placeholder="选择时间"
                            v-model="ruleForm.starttime"
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
                            v-model="ruleForm.enddate"
                            style="width: 100%;"></el-date-picker>
          </el-form-item>
        </el-col>
        <el-col :span="11">
          <el-form-item prop="endtime">
            <el-time-picker placeholder="选择时间"
                            v-model="ruleForm.endtime"
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
        {{ ruleForm.tag }}
      </el-button>
    </el-form-item>
    <el-form-item label="活动简介"
                  prop="desc">
      <el-input type="textarea"
                v-model="ruleForm.desc"></el-input>
    </el-form-item>
    <el-form-item>
      <el-button type="primary"
                 @click="submitForm">立即创建
      </el-button>
      <el-button @click="resetForm">重置</el-button>
    </el-form-item>
  </el-form>
</template>

<script>
import { addNewActivity } from '../script/index'

export default {
  name: 'AddActivity',

  data () {
    return {
      inputVisible: false,
      inputValue: '',
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
        tag: '志愿活动',
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
  methods: {
    submitForm () {
      this.$refs['ruleForm'].validate(valid => {
        if (valid) {
          addNewActivity(
            this.ruleForm,
            () => {
              this.resetForm()
              this.$message({
                message: '发布成功',
                type: 'success'
              });
              this.$router.push('/dashboard/activity')
            },
            () => {
              this.$message.error('发布失败')
            }
          )
        } else {
          this.$message.error('发布失败')
          return false
        }
      })
    },
    resetForm () {
      this.$refs['ruleForm'].resetFields()
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

    handleInputConfirm () {
      let inputValue = this.inputValue
      if (inputValue) {
        this.ruleForm.tag = inputValue
      }
      this.inputVisible = false
      this.inputValue = ''
    }
  }
}
</script>

<style>
.el-tag + .el-tag {
  margin-left: 10px;
}

.button-new-tag {
  margin-left: 10px;
  height: 32px;
  line-height: 30px;
  padding-top: 0;
  padding-bottom: 0;
}

.input-new-tag {
  width: 90px;
  margin-left: 10px;
  vertical-align: bottom;
}
</style>
