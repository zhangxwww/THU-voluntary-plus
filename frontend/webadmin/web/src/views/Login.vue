<template>
  <div class="login-container bg-purple">
    <el-form :model="loginForm"
             :rules="loginRules"
             class="login-form"
             auto-complete="on"
             label-position="left">
      <div class="title-container">
        <h3 class="title">登录到THU志愿+</h3>
      </div>

      <el-form-item prop="username">
        <el-input placeholder="用户名"
                  v-model="loginForm.username">
          <i slot="prefix"
             class="el-input__icon el-icon-user"></i>
        </el-input>
      </el-form-item>

      <el-form-item prop="password">
        <el-input placeholder="密码"
                  v-model="loginForm.password"
                  show-password>
          <i slot="prefix"
             class="el-input__icon el-icon-lock"></i>
        </el-input>
      </el-form-item>
      <el-button :loading="loading"
                 type="primary"
                 @click.native.prevent="handleLogin">登录
      </el-button>
    </el-form>
  </div>
</template>

<script>
import { login } from '../script/index'

export default {
  name: 'login',
  components: {},
  data: function () {
    return {
      loginForm: {
        username: 'admin',
        password: '111111'
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
        ]
      },
      loading: false,
      passwordType: 'password',
      redirect: undefined
    }
  },
  methods: {
    showPassword: function () {
    },
    handleLogin: function () {
      login(
        this.loginForm,
        () => {
          this.$router.push('/dashboard/activity')
        },
        () => {
          alert('登录失败，请稍后重试')
        }
      )
    }
  }
}
</script>

<style>
.page-title {
  color: #fff;
  font-size: 32px;
  font-weight: heavy;
  position: fixed;
  left: 80px;
  top: 20px;
}

.login-container .el-input {
  display: inline-block;
  border: 0px;
  height: 47px;
  width: 85%;
}

.login-container .el-input input {
  background: transparent;
  border: 0px;
  -webkit-appearance: none;
  border-radius: 0px;
  padding: 12px 5px 12px 15px;
  margin-left: 20px;
  height: 47px;

  & :-webkit-autofill {
    box-shadow: 0 0 0px 1000px #283443 inset !important;
    -webkit-text-fill-color: #fff !important;
  }
}

.login-container .el-form-item {
  border: 1px solid;
  background: rgba(0, 0, 0, 0.01);
  box-shadow: 0 2px 12px 0 rgba(116, 52, 129, 0.1);
  border-color: rgba(116, 52, 129, 0.1);
  border-radius: 5px;
  color: #454545;
}

.login-container .el-form-item:hover {
  border: 1px solid;
  background: rgba(0, 0, 0, 0.01);
  box-shadow: 0 2px 12px 0 rgba(116, 52, 129, 0.1);
  border-color: rgba(116, 52, 129, 0.6);
  border-radius: 5px;
  color: #454545;
}
</style>

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
