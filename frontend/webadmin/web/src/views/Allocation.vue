<template>
    <div class="container">
        <el-form label-width="100px">
            <div v-for="person in persons" :key="person.id">
                <el-form-item :label="person.name">
                    <el-slider v-model="person.time" show-input></el-slider>
                </el-form-item>
            </div>
            <el-form-item>
                <el-button type="primary" @click="submitForm">立即创建</el-button>
                <el-button @click="resetForm">重置</el-button>
            </el-form-item>
        </el-form>
    </div>
</template>

<script>
    export default {
        name: 'Allocation',
        data() {
            return {
                persons: [
                    {
                        id: 0,
                        name: '张大头',
                        avatar: 'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg',
                        department: '魔药学院'
                    },
                    {
                        id: 1,
                        name: '金大头',
                        avatar: 'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg',
                        department: '魔药学院'
                    },
                    {
                        id: 2,
                        name: '邵大头',
                        avatar: 'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg',
                        department: '魔药学院'
                    },
                    {
                        id: 3,
                        name: '汪大头',
                        avatar: 'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg',
                        department: '魔药学院'
                    }
                ]
            }
        },
        computed: {},
        methods: {}
    }
</script>

<style scope>
    .container {
        margin-top: 20px;
        margin-left: 20px;
        width: 80%;
    }

    el-row {
        margin-top: 20px;
    }

</style>