import axios from 'axios'

export function getActivity(success, fail) {
    axios.get('/api/activities/list', {

    }).then(res => {
        if (res.status === 200) {
            let list = res.data.ActivityList
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
    axios.post('/api/activities/postactivity', {
        name: form.name,
        location: form.location,
        city: form.city,
        totalNum: form.totalNum,
        startdate: form.startdate,
        starttime: form.starttime,
        enddate: form.enddate,
        endtime: form.endtime,
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
    axios.post('/api/manager/login', {
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