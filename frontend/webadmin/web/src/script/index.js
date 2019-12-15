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

export function newAnnounce(announce, success, fail) {
    axios.post('api/messages/post', {
        activity_id: announce.activity_id,
        title: announce.title,
        content: announce.content
    }).then(res => {
        if (res.status === 200) {
            success()
        } else {
            fail()
        }
    }).catch(e => {
        alert(e)
        fail()
    })
}

export function editAnnounce(announce, success, fail) {
    axios.post('/api/messages/edit', {
        id: announce.id,
        title: announce.title,
        content: announce.content
    }).then(res => {
        if (res.status === 200) {
            success()
        } else {
            fail()
        }
    }).catch(e => {
        alert(e)
        fail()
    })
}

export function getAnnounceList(id, success, fail) {
    axios.post('/api/messages/list', {
        activity_id: id
    }).then(res => {
        if (res.status === 200) {
            let list = res.data.messages
            success(list)
        } else {
            fail()
        }
    }).catch(e => {
        alert(e)
        fail()
    })
}

export function deleteAnnounce(id_, success, fail) {
    axios.post('/api/messages/delete', {
        id: id_
    }).then(res => {
        if (res.status === 200) {
            success()
        } else {
            fail()
        }
    }).catch(e => {
        alert(e)
        fail()
    })
}

export function getParticipant(id_, success, fail) {
    axios.post('/api/activities/participants', {
        id: id_
    }).then(res => {
        if (res.status === 200) {
            let list = res.data.list
            success(list)
        } else {
            fail()
        }
    }).catch(e => {
        alert(e)
        fail()
    })
}

export function allocateTime(aid, pid, time, success, fail) {
    axios.post('/api/activities/allocate', {
        activity_id: aid,
        list: [{
            student_id: pid,
            time: time
        }]
    }).then(res => {
        if (res.status === 200) {
            success()
        } else {
            fail()
        }
    }).catch(e => {
        alert(e)
        fail()
    })
}

export function generateVerificationCode(success, fail) {
    axios.get('/api/code/generate', {

    }).then(res => {
        if (res.status === 200) {
            success(res.data.code)
        } else {
            fail()
        }
    }).catch(e => {
        alert(e)
        fail()
    })
}

export function signupGroup(form, success, fail) {
    axios.post('/api/users/create', {
        username: form.username,
        password: form.password,
        code: form.invitationcode
    }).then(res => {
        if (res.status === 200) {
            success()
        } else {
            fail()
        }
    }).catch(e => {
        alert(e)
        fail()
    })
}

export function setupGroup(form, success, fail) {
    axios.post('/api/group/create', form).then(res => {
        if (res.status === 200) {
            success()
        } else {
            fail()
        }
    }).catch(e => {
        alert(e)
        fail(e)
    })
}

export function getCheckingGroupList(success, fail) {
    axios.get('/api/group/selectfrom').then(res => {
        if (res.status === 200) {
            let list = res.data.groups
            success(list)
        } else {
            fail()
        }
    }).catch(e => {
        alert(e)
        fail()
    })
}

export function checkGroupSetup(gid, check, success, fail) {
    axios.post('', {
        id: gid,
        check: check
    }).then(res => {
        if (res.status === 200) {
            success()
        } else {
            fail()
        }
    }).catch(e => {
        alert(e)
        fail()
    })
}

export function getGroupInfo(success, fail) {
    axios.get('/api/group/info').then(res => {
        if (res.status === 200) {
            let data = res.data
            success(data)
        } else {
            fail()
        }
    }).catch(e => {
        alert(e)
        fail()
    })
}

export function editGroupInfo(form, success, fail) {
    axios.post('/api/group/edit', {
        phone: form.phone,
        email: form.email,
        about: form.about
    }).then(res => {
        if (res.status === 200) {
            success()
        } else {
            fail()
        }
    }).catch(e => {
        alert(e)
        fail()
    })
}

export function getGroupTimeline(success, fail) {
    axios.get('/api/activities/list').then(res => {
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