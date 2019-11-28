import axios from 'axios'

export function addNewActivity(form, success, fail) {
    axios.post('/api/api/activities/postactivity', {
        name: form.name,
        region: form.region,
        totalNum: form.totalNum,
        date1: form.date1,
        date2: form.date2,
        tag: form.tag,
        desc: form.desc
    }).then(res => {
        if (res.status === 200) {
            success()
        } else {
            fail()
        }
    }).catch(function (e) {
        alert(e)
        fail()
    })
}

export function login(form, success, fail) {
    axios.post('/api/login', {
        username: form.username,
        password: form.password
    }).then(res => {
        if (res.status === 200) {
            success()
        } else {
            fail()
        }
    }).catch(function (e) {
        alert(e)
        fail()
    })
}