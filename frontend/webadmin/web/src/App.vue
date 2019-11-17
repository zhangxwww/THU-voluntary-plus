<template>
  <div id="app">
    <el-container>
      <el-header>
        <nav-bar></nav-bar>
      </el-header>
      <el-container>
        <el-aside width="200px">Aside</el-aside>
        <el-container>
          <el-main>
          <router-view />
          </el-main>
          <el-footer>Footer</el-footer>
        </el-container>
      </el-container>
    </el-container>
  </div>
</template>

<script>
import NavBar from '@/layout/NavBar'
export default{
  components: {
    NavBar
  },
  data() {
    return {

    }
  },
  computed: {

  }
}
</script>

<style>
</style>
