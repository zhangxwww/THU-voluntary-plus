import axios from 'axios'

export function getActivity(success, fail) {
    axios.get('/api/activities/list', {

    }).then(res => {
        if (res.status === 200) {
            let list = res.activity_list
            success(list)
        } else {
            fail()
        }
    }).catch(e => {
        alert(e)
        fail()
    })
}

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
    axios.post('/api/api/manager/login', {
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