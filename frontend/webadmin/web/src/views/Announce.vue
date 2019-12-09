<template>
    <div>
        <el-form v-if="isAdding" ref="form" :model="form" label-width="80px">
            <el-form-item label="通知标题">
                <el-input v-model="form.title"></el-input>
            </el-form-item>
            <el-form-item label="通知内容">
                <el-input type="textarea" v-model="form.content"></el-input>
            </el-form-item>
            <el-form-item>
                <el-button type="primary" @click="onSubmit">立即创建</el-button>
                <el-button @click="onCancel">取消</el-button>
            </el-form-item>
        </el-form>
        <el-dialog title="编辑消息" :visible.sync="dialogFormVisible">
            <el-form :model="editform">
                <el-form-item label="通知标题">
                    <el-input v-model="editform.title"></el-input>
                </el-form-item>
                <el-form-item label="通知内容">
                    <el-input type="textarea" v-model="editform.content"></el-input>
                </el-form-item>
            </el-form>
            <div slot="footer" class="dialog-footer">
                <el-button @click="dialogFormVisible=false">取消</el-button>
                <el-button type="success" @click="handleSubmitEdit">编辑</el-button>
            </div>
        </el-dialog>
        <div v-if="!isAdding">
            <el-button type="primary" icon="el-icon-edit"
                       @mouseenter.native="onHoverAddButton"
                       @mouseleave.native="onLeaveAddButton"
                       @click="onClickAddButton"
                       :circle="!hover"> {{ buttontext }}
            </el-button>
            <el-table :data="updateList.filter(data => !search || data.title.toLowerCase().includes(search.toLowerCase()))">
                <el-table-column type="expand">
                    <template slot-scope="props">
                        <el-form label-position="left" inline class="demo-table-expand">
                            <el-form-item label="详情">
                                <span>{{ props.row.detail }}</span>
                            </el-form-item>
                        </el-form>
                    </template>
                </el-table-column>
                <el-table-column prop="id" label="#" width="50"></el-table-column>
                <el-table-column prop="title" label="标题" width="180"></el-table-column>
                <el-table-column prop="time" label="发布时间" width="180">
                    <template slot-scope="scope">
                        <i class="el-icon-time"/>
                        <span>{{ scope.row.time }}</span>
                    </template>
                </el-table-column>
                <el-table-column
                        prop="status"
                        class-name="status-col"
                        label="状态"
                        width="80" align="center"
                        :filters="[{ text: '已发布', value: '已发布' }, { text: '草稿', value: '草稿' }, { text: '已删除', value: '已删除'}]"
                        :filter-method="filterStatus"
                        filter-placement="bottom-end">
                    <template slot-scope="scope">
                        <el-tag :type="scope.row.status | statusMapper">{{ scope.row.status }}</el-tag>
                    </template>
                </el-table-column>
                <el-table-column align="right" width="180">
                    <template slot="header" slot-scope="scope">
                        <el-input
                                v-model="search"
                                size="mini"
                                placeholder="搜索标题">
                        </el-input>
                        <span style="display:none">{{ scope.$index }}</span>
                    </template>
                    <template slot-scope="scope">
                        <el-button
                                size="mini"
                                @click="handleEdit(scope.$index, scope.row)">编辑
                        </el-button>
                        <el-button
                                size="mini"
                                type="danger"
                                @click="handleDelete(scope.$index, scope.row)">删除
                        </el-button>
                    </template>
                </el-table-column>
            </el-table>
            <div class="pagination">
                <el-pagination
                        background
                        @size-change="handleSizeChange"
                        @current-change="handleCurrentChange"
                        :current-page="1"
                        :page-sizes="[10, 20, 30]"
                        :page-size="3"
                        layout="total, sizes, prev, pager, next, jumper"
                        :total="total">
                </el-pagination>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Announce",
        filters: {
            statusMapper(status) {
                const statusMap = {
                    '已发布': 'success',
                    '草稿': 'warning',
                    '已删除': 'danger'
                }
                return statusMap[status]
            }
        },
        data() {
            return {
                form: {
                    title: '',
                    content: ''
                },
                editform: {
                  title: '',
                  content: '',
                    id: 0
                },
                isAdding: false,
                hover: false,
                rawlist: [{
                    id: 1,
                    title: '注意保暖',
                    detail: '全体成员请注意带好自己的衣物，一定要注意保暖。全体成员请注意带好自己的衣物，一定要注意保暖。全体成员请注意带好自己的衣物，一定要注意保暖。全体成员请注意带好自己的衣物，一定要注意保暖。全体成员请注意带好自己的衣物，一定要注意保暖。全体成员请注意带好自己的衣物，一定要注意保暖。全体成员请注意带好自己的衣物，一定要注意保暖。全体成员请注意带好自己的衣物，一定要注意保暖。',
                    time: '2019-10-1',
                    status: '已发布'
                }, {
                    id: 2,
                    title: '注意口臭',
                    detail: '大家一定要管好自己的嘴，不要随便口吐莲花，不要嘴臭臭哦！大家一定要管好自己的嘴，不要随便口吐莲花，不要嘴臭臭哦！大家一定要管好自己的嘴，不要随便口吐莲花，不要嘴臭臭哦！大家一定要管好自己的嘴，不要随便口吐莲花，不要嘴臭臭哦！大家一定要管好自己的嘴，不要随便口吐莲花，不要嘴臭臭哦！大家一定要管好自己的嘴，不要随便口吐莲花，不要嘴臭臭哦！',
                    time: '2019-10-1',
                    status: '草稿'
                }, {
                    id: 3,
                    title: '注意口臭',
                    detail: '大家一定要管好自己的嘴，不要随便口吐莲花，不要嘴臭臭哦！大家一定要管好自己的嘴，不要随便口吐莲花，不要嘴臭臭哦！大家一定要管好自己的嘴，不要随便口吐莲花，不要嘴臭臭哦！大家一定要管好自己的嘴，不要随便口吐莲花，不要嘴臭臭哦！大家一定要管好自己的嘴，不要随便口吐莲花，不要嘴臭臭哦！大家一定要管好自己的嘴，不要随便口吐莲花，不要嘴臭臭哦！大家一定要管好自己的嘴，不要随便口吐莲花，不要嘴臭臭哦！',
                    time: '2019-10-1',
                    status: '已删除'
                }, {
                    id: 4,
                    title: '注意口臭',
                    detail: '大家一定要管好自己的嘴，不要随便口吐莲花，不要嘴臭臭哦！大家一定要管好自己的嘴，不要随便口吐莲花，不要嘴臭臭哦！大家一定要管好自己的嘴，不要随便口吐莲花，不要嘴臭臭哦！大家一定要管好自己的嘴，不要随便口吐莲花，不要嘴臭臭哦！大家一定要管好自己的嘴，不要随便口吐莲花，不要嘴臭臭哦！大家一定要管好自己的嘴，不要随便口吐莲花，不要嘴臭臭哦！大家一定要管好自己的嘴，不要随便口吐莲花，不要嘴臭臭哦！大家一定要管好自己的嘴，不要随便口吐莲花，不要嘴臭臭哦！',
                    time: '2019-10-1',
                    status: '已发布'
                },
                ],
                search: '',
                pagesize: 10,
                list: [],
                page: 1,
                dialogFormVisible: false
            }
        },
        computed: {
            buttontext: function () {
                if (this.hover) {
                    return '添加新活动'
                } else {
                    return ''
                }
            },
            total: function () {
                return this.rawlist.length
            },
            updateList: function () {
                this.getList()
                return this.list
            }
        },
        methods: {
            onHoverAddButton: function () {
                this.hover = true
            },
            onLeaveAddButton: function () {
                this.hover = false
            },
            onClickAddButton: function () {
                this.isAdding = true
            },
            onSubmit: function () {
                this.isAdding = false
                this.hover = false
            },
            onCancel: function () {
                this.isAdding = false
                this.hover = false
            },
            // eslint-disable-next-line no-unused-vars
            handleEdit(index, row) {
                this.dialogFormVisible = true
                this.editform.id = index
            },
            handleDelete(index, row) {
                alert(index, row)
            },
            handleDetail(index, row) {
                alert(index, row)
            },
            filterStatus(value, row) {
                return row.status === value;
            },
            getList: function () {
                this.list = this.rawlist.slice((this.page - 1) * this.pagesize, this.page * this.pagesize)
            },
            handleSizeChange(val) {
                this.pagesize = val
                this.getList()
            },
            handleCurrentChange(val) {
                this.page = val
                this.getList()
            },
            handleSubmitEdit() {
                alert(this.editform.content)
                this.dialogFormVisible = false
            }
        },
        created() {
            this.list = this.rawlist.slice(0, this.pagesize)
        }
    }
</script>

<style scoped>

</style>