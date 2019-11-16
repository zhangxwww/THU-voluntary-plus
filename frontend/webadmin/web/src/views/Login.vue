<template>
	<div class="login-container">
		<el-form :model="loginForm"
		:rules="loginRules" class="login-form" auto-complete="on"
		label-position="left">
			<div class="title-container">
				<h3 class="title">登录到THU志愿+</h3>
			</div>
			
			<el-form-item prop="username">
				<el-input
					ref="username"
					v-model="loginForm.username"
					placeholder="用户名"
					name="username"
					type="text"
					tabindex="1"
					auto-complete="on"
				/>
			</el-form-item>
			
			<el-form-item prop="password">
				<el-input
					:key="passwordType"
					ref="password"
					v-model="loginForm.password"
					placeholder="用户名"
					name="password"
					:type="passwordType"
					tabindex="2"
					auto-complete="on"
					@keyup.enter.native="handleLogin"
				/>
			</el-form-item>
			<el-button :loading="loading"
			type="primary"
			stye="width:100%;margin-bottom:30px"
			@click.native.prevent="handleLogin">登录</el-button>
		</el-form>
	</div>
</template>

<script>
export default {
	name: 'login',
	data: function() {
		return {
			loginForm: {
				username: 'admin',
				password: '111111'
			},
			loginRules: {
				username: [{
					required: true,
					trigger: 'blur'
				}],
				password: [{
					required: true,
					trigger: 'blur'
				}]
			},
			loading: false,
			passwordType: 'password',
			redirect: undefined
		}
	},
	methods: {
		showPassword: function() {
			
		},
		handleLogin: function() {
			
		}
	}
}
</script>

<style>
.login-container .el-input {
    display: inline-block;
    height: 47px;
    width: 85%;
}

.login-container .el-input input {
    background: transparent;
    border: 0px;
    -webkit-appearance: none;
    border-radius: 0px;
    padding: 12px 5px 12px 15px;
    height: 47px;

    &:-webkit-autofill {
        box-shadow: 0 0 0px 1000px #283443 inset !important;
        -webkit-text-fill-color: #fff !important;
    }
}

.login-container .el-form-item {
    border: 1px solid rgba(255, 255, 255, 0.1);
    background: rgba(0, 0, 0, 0.1);
    border-radius: 5px;
    color: #454545;
}
</style>

<style scoped>
.login-container {
  min-height: 100%;
  width: 100%;
  overflow: hidden;
}

.login-container .login-form {
    position: relative;
    width: 520px;
    max-width: 100%;
    padding: 160px 35px 0;
    margin: 0 auto;
    overflow: hidden;
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
    font-size: 24px;
    color: $fff;
    margin: 0px auto 40px auto;
    text-align: ledt;
    font-weight: bold;
}

.login-container .show-pwd {
    position: absolute;
    right: 10px;
    top: 7px;
    font-size: 16px;
    color: fff;
    cursor: pointer;
    user-select: none;
}
</style>
