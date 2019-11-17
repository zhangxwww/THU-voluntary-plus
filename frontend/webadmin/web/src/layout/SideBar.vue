<template>
  <div class="showLogo">
    <sidebar-logo collapse=false />
    <el-scrollbar wrap-class="scrollbar-wrapper">
      <el-menu
        :collapse="false"
        :background-color="variables.menuBg"
        :text-color="variables.menuText"
        :unique-opened="false"
        :active-text-color="variables.menuActiveText"
        :collapse-transition="false"
        mode="vertical"
      >
        <sidebar-item v-for="route in routes" :key="route.path" :item="route" :base-path="route.path" />
      </el-menu>
    </el-scrollbar>
  </div>
</template>

<script>
import SidebarLogo from '@/components/SidebarLogo'
import SidebarItem from '@/components/SidebarItem'
import variables from '@/styles/variables.scss'

export default {
  components: { SidebarItem, SidebarLogo },
  computed: {
    routes() {
      return this.$router.options.routes
    },
    variables() {
      return variables
    }
  }
}
</script>
