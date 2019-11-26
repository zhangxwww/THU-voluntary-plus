import axios from 'axios'

export function addNewActivity(form, success, fail) {
    alert(form.name)
    alert(form.region)
    alert(form.date1)
    alert(form.date2)
    alert(form.tag)
    alert(form.desc)

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
    })
}