<template>
    <view class="cu-modal" :class="modalName=='Modal'?'show':''">
        <view class="cu-dialog">
            <view class="cu-bar bg-white justify-end">
                <view class="content">{{ title }}</view>
                <view class="action" @tap="hideModal">
                    <text class="cuIcon-close text-red"></text>
                </view>
            </view>
            <view class="padding-xl">
                {{ content }}
            </view>
        </view>
    </view>
</template>

<script>
    export default {
        props: {
            title: {
                type: String,
                required: true
            },
            content: {
                type: String,
                required: true
            }
        },
        data() {
            return {
                modalName: null
            }
        },
        methods: {
            hideModal() {
                this.modalName = null
            }
        }
    }
</script>