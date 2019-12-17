<template>
  <el-button :icon="icon"
             :size="size"
             :type="type"
             :circle="isCircle"
             :round="isRound"
             @mouseenter.native="onHover"
             @mouseleave.native="onLeave">{{ buttontext }}
  </el-button>
</template>

<script>
export default {
  props: {
    icon: {
      type: String,
      default: ''
    },
    size: {
      type: String,
      default: 'mini'
    },
    text: {
      type: String,
      default: ''
    },
    type: {
      type: String,
      default: "primary"
    },
    shape: {
      type: String,
      default: ""
    },
    clickHandler: {
      default: null
    }
  },
  name: "HidableButton",
  data () {
    return {
      hover: false
    }
  },
  computed: {
    buttontext: function () {
      if (this.hover) {
        return this.text
      } else {
        return ''
      }
    },
    isRound: function () {
      return this.shape === 'round'
    },
    isCircle: function () {
      return this.shape === 'circle'
    }
  },
  methods: {
    onHover: function () {
      this.hover = true
    },
    onLeave: function () {
      this.hover = false
    }
  }
}
</script>

<style scoped>
</style>