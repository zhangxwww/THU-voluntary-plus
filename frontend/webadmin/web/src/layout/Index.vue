<template>
    <div id="app">
        <el-container class="app-wrapper">
            <el-header class="header-container">
                <nav-bar></nav-bar>
            </el-header>
            <el-container>
                <el-aside class="side-container">
                    <side-bar></side-bar>
                </el-aside>
                <el-container class="app-container">
                    <el-main class="app-main">
                        <router-view :key="this.$route.path"></router-view>
                    </el-main>
                </el-container>
            </el-container>
        </el-container>
    </div>
</template>

<script>
    import NavBar from '@/layout/NavBar'
    import SideBar from '@/layout/SideBar'

    export default {
        name: 'Layout',
        components: {
            NavBar,
            SideBar
        },
        data() {
            return {}
        },
        computed: {}
    }
</script>

<style type="scss" scoped>
    .side-container {
        transition: width 0.28s;
        width: 200px;
        position: fixed;
        font-size: 0px;
        top: 0;
        left: 0;
        height: 100%;
        z-index: 1001;
        overflow: hidden;
        border-radius: 4px;
        border-color: rgba(116, 52, 129, 0.04);
        border: 1px solid blur;
        box-shadow: 0 2px 4px rgba(66, 2, 79, .12), 0 0 6px rgba(66, 2, 79, .04);
    }

    .app-container {
        min-height: 100%;
        transition: margin-left .28s;
        margin-left: $sideBarWidth;
        position: relative;
    }

    .app-main {
        min-height: calc(100vh - 50px);
        width: 100%;
        position: relative;
        margin-left: 300px;
        margin-top: 30px;
        padding-top: 20px;
        padding-left: 20px;
        width: 50%;
        max-width: 1100px;
        overflow: hidden;
    }

    .app-wrapper {
        @include clearfix;
        position: relative;
        height: 100%;
        width: 100%;

        &.mobile.openSidebar {
            position: fixed;
            top: 0;
        }
    }

    .drawer-bg {
        background: #000;
        opacity: 0.3;
        width: 100%;
        top: 0;
        height: 100%;
        position: absolute;
        z-index: 999;
    }
</style>
