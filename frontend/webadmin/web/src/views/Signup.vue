<template>
  <div class="login-container bg-purple">
    <el-form :model="signupForm"
             :rules="loginRules"
             class="login-form"
             auto-complete="on"
             label-position="left">
      <div class="title-container">
        <h3 class="title">注册</h3>
      </div>

      <el-form-item prop="username">
        <el-input placeholder="用户名"
                  v-model="signupForm.username">
          <i slot="prefix"
             class="el-input__icon el-icon-user"></i>
        </el-input>
      </el-form-item>

      <el-form-item prop="password">
        <el-input placeholder="密码"
                  v-model="signupForm.password"
                  show-password>
          <i slot="prefix"
             class="el-input__icon el-icon-lock"></i>
        </el-input>
      </el-form-item>
      <el-form-item prop="invitationcode">
        <el-input placeholder="邀请码"
                  v-model="signupForm.invitationcode">
          <i slot="prefix"
             class="el-input__icon el-icon-warning-outline"></i>
        </el-input>
      </el-form-item>
      <el-button :loading="loading"
                 type="primary"
                 @click.native.prevent="handleSignup">注册
      </el-button>
    </el-form>
  </div>
</template>

<script>
import { signupGroup } from '../script/index'

export default {
  name: 'Signup',
  data: function () {
    return {
      signupForm: {
        username: '',
        password: '',
        invitationcode: ''
      },
      loginRules: {
        username: [
          {
            required: true,
            trigger: 'blur'
          }
        ],
        password: [
          {
            required: true,
            trigger: 'blur'
          }
        ],
        invitationcode: [
          {
            required: true,
            trigger: 'blur'
          }
        ]
      },
      loading: false,
      passwordType: 'password',
      redirect: undefined
    }
  },
  methods: {
    handleSignup () {
      signupGroup(
        this.signupForm,
        () => {
          this.$router.push('/group/setup')
        },
        () => {
          alert('注册失败，请稍后重试')
        }
      )
    }
  }
}
</script>

<style type="scss" scoped>
.login-container {
  position: fixed;
  left: 0;
  top: 0;
  height: 100%;
  width: 100%;
  background: #50296b;
  overflow: hidden;
}

.login-container .login-form {
  position: relative;
  width: 520px;
  max-width: 100%;
  top: 200px;
  padding: 35px 35px 0;
  margin: 0 auto;
  border-radius: 4px;
  box-shadow: 0 2px 4px rgba(116, 52, 129, 0.12),
    0 0 6px rgba(116, 52, 129, 0.04);
  overflow: hidden;
  background-color: #fff;
}

.login-container .tips {
  font-size: 14px;
  color: #fff;
  margin-bottom: 10px;
}

.login-container .tips span {
  &:first-of-type {
    margin-right: 16px;
  }
}

.login-container .svg-container {
  padding: 6px 5px 6px 15px;
  color: $fff;
  vertical-align: middle;
  width: 30px;
  display: inline-block;
}

.login-container .title-container {
  position: relative;
}

.login-container .title-container .title {
  font-size: 28px;
  color: $fff;
  margin: 0px auto 40px auto;
  text-align: ledt;
  font-weight: heavy;
}

.login-container .show-pwd {
  position: absolute;
  right: 10px;
  top: 7px;
  font-size: 16px;
  color: #fff;
  cursor: pointer;
  user-select: none;
}

.login-container .icon-container {
  padding: 6px 5px 6px 15px;
  color: $dark_gray;
  vertical-align: middle;
  width: 30px;
  display: inline-block;
}

.login-container .el-button {
  width: 100%;
  margin-bottom: 30px;
}
</style>
