<template>
    <div>
        <sidebar-logo :collapse="false"/>
        <el-scrollbar wrap-class="scrollbar-wrapper">
            <el-menu
                    :collapse="false"
                    :unique-opened="false"
                    :collapse-transition="false"
                    mode="vertical"
            >
                <sidebar-item v-for="route in routes" :key="route.path" :item="route" :base-path="route.path"/>
            </el-menu>
        </el-scrollbar>
    </div>
</template>

<script>
    import SidebarItem from '@/components/SidebarItem'
    import variables from '@/styles/variables.scss'

    export default {
        components: {SidebarItem},
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
