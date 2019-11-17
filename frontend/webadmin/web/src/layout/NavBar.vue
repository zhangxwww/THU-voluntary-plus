<template>
  <div class="navbar">
    <div class="left-menu">
      <img src="@/assets/logo.jpg" width="80" class="left-menu-item">
      <div class="left-menu-item">
        <span class="logo-text">THU志愿+管理后台</span>
      </div>
    </div>
    <div class="right-menu">
      <el-menu 
      :default-active="activeIndex" 
      class="el-menu-demo right-menu-item" 
      mode="horizontal" 
      active-text-color="#5c307d">
        <el-menu-item index="1">活动中心</el-menu-item>
        <el-menu-item index="2">管理面板</el-menu-item>
        <el-menu-item index="3">个人信息</el-menu-item>
      </el-menu>
      <el-dropdown class="avatar-container" trigger="click">
        <div class="avatar-wrapper">
          <img :src="avatar+'?imageView2/1/w/80/h/80'" class="user-avatar">
          <i class="el-icon-caret-bottom" />
        </div>
        <el-dropdown-menu slot="dropdown" class="user-dropdown">
          <el-dropdown-item>
            <span style="display:block;" @click="logout">登出</span>
          </el-dropdown-item>
        </el-dropdown-menu>
      </el-dropdown>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      activeIndex: '1',
      activeIndex2: '1'
    }
  },
  components: {
  },
  computed: {
    avatar: function() {
      return 'https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif'
    },
  },
  methods: {
  }
}
</script>

<style lang="scss" scoped>
.navbar {
  border-bottom:1px solid rgba(116, 52, 129, .12);
  padding-left: 30px;
  margin-left: 50px;
  height: 80px;
  width: 90%;
  overflow: hidden;
  position: relative;
  //box-shadow: 0 1px 4px rgba(0,21,41,.08);
  .left-menu-item {
    display: inline-block;
    padding: 0 8px;
    height: 100%;
    font-size: 24px;
    font-weight: bold;
    color: #5a5e66;
    vertical-align: middle;
  }
  .left-menu {
    float: left;

    .logo-container {
      margin-right: 30px;

      .logo-wrapper {
        margin-top: 5px;
        position: relative;

        .logo {
          cursor: pointer;
          width: 80px;
          height: 80px;
          border-radius: 10px;
        }

        .el-icon-caret-bottom {
          cursor: pointer;
          position: absolute;
          right: -20px;
          top: 25px;
          font-size: 12px;
        }
      }
    }
  }
  .right-menu {
    float: right;
    height: 100%;
    line-height: 70px;
    .right-menu-item {
      display: inline-block;
      padding: 0 8px;
      height: 100%;
      font-size: 18px;
      color: #5a5e66;
      vertical-align: middle;
    }

    .avatar-container {
      margin-right: 30px;

      .avatar-wrapper {
        margin-top: 5px;
        position: relative;

        .user-avatar {
          cursor: pointer;
          width: 50px;
          height: 50px;
          border-radius: 10px;
        }

        .el-icon-caret-bottom {
          cursor: pointer;
          position: absolute;
          right: -20px;
          top: 25px;
          font-size: 12px;
        }
      }
    }
  }
}
</style>