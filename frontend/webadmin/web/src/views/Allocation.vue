<template>
  <div class="container">
    <el-form label-width="100px">
      <div v-for="person in getPerson"
           :key="person.id">
        <el-form-item :label="person.name">
          <el-slider v-model="person.time"
                     show-input></el-slider>
        </el-form-item>
      </div>
      <el-form-item>
        <el-button type="primary"
                   @click="submitForm">确认</el-button>
        <el-button @click="resetForm">重置</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
import {
  getparticipant
} from '../script/index'
import {
  mapState,
} from 'vuex'

export default {
  name: 'Allocation',
  data () {
    return {
      persons: [
        {
          id: 0,
          name: '张大头',
          avatar: 'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg',
          department: '魔药学院',
          checkin_time: '',
          checkin_address: '',
        },
        {
          id: 1,
          name: '金大头',
          avatar: 'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg',
          department: '魔药学院',
          checkin_time: '',
          checkin_address: '',
        },
        {
          id: 2,
          name: '邵大头',
          avatar: 'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg',
          department: '魔药学院',
          checkin_time: '',
          checkin_address: '',
        },
        {
          id: 3,
          name: '汪大头',
          avatar: 'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg',
          department: '魔药学院',
          checkin_time: '',
          checkin_address: '',
        }
      ]
    }
  },
  computed: {
    ...mapState(['modifyActivityId']),

    getPerson () {
      return this.persons
    },
  },
  onShow () {
    this.updateList()
  },
  methods: {
    submitForm () {
      //
    },

    resetForm () {
      for (let p of this.persons) {
        p.time = 0
      }
    },

    updateList () {
      getparticipant(this.modifyActivityId, (list) => {
        this.persons.splice(0, this.persons.length)
        for (let li of list) {
          let new_item = {
            id: li.id,
            name: li.name,
            department: li.department,
            checkin_time: li.time,
            checkin_address: li.address,
            acatar: 'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg',
          }
          this.persons.push(new_item)
        }
      })
    }

  }
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