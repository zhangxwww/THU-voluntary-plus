import json
import math
import traceback

from django.shortcuts import render, redirect
from django.utils import timezone
from django.shortcuts import HttpResponse
from django.http import JsonResponse

from . import models as showactivity_models
import mysite.models as mysite_models
from .models import Message, MessageReadOrNot, Activity, ActivityPic, ENROLL_STATE_CONST, Membership, checkin
from mysite.views import checkSessionValid, LOGGED_IN_CONST
from mysite.models import VOLUNTEER

import datetime 
from django.utils.timezone import utc
import requests

ranking_last_update_time = datetime.datetime.utcnow() # 排行榜上次更新的时间
ranking_top_100_list = []

PERMISSION_CONST = {
    'TEACHER': 233,
    'ORGANIZATION': 255,
    'VOLUNTEER': 258,
    'UNAUTHENTICATED': 266
}

BAIDU_MAP_AK = "H5LGjLHfy731eaPCZAUKfAnZH6eiql9M"

def checkUserType(request):
    try:
        if request.user.is_authenticated: # 先检查是否为老师或公益团体账号
            print("authenticated")
            if mysite_models.UserIdentity(request.user).isTeacher:
                return PERMISSION_CONST['TEACHER']
            else:
                return PERMISSION_CONST['ORGANIZATION']
        else:
            res = checkSessionValid(request)[1]
            if res is not None:
                return PERMISSION_CONST['VOLUNTEER']
            else:
                return PERMISSION_CONST['UNAUTHENTICATED']
    except:
        return PERMISSION_CONST['UNAUTHENTICATED']
            

# Create your views here.
#检查登录
"""
def check_login(request):
    is_login = request.session.get('is_login', None)
    if is_login :
        client_type = request.session.get('MicroMessenger')
        if client_type == '':
            #id = request.session.get('sessionid')
            user = WX_OPENID_TO_THUID.objects.get(pk=request.session.get('THUID'))
            if not request.session.get('THUID'):
                request.session.flush()
                return redirect('/login/')
        else :
            #TODO
            user = WX_OPENID_TO_THUID.objects.get(pk=request.session.get('OPENID'))
            if not request.session.get('OPENID'):
                request.session.flush()
                return redirect('/login/')
    return user
"""

# 发布活动
def post_activity(request): # name, place, date, time, tag, description, amount
    print(request.COOKIES)
    print(checkUserType(request))
    if checkUserType(request) in [PERMISSION_CONST['TEACHER'], PERMISSION_CONST['ORGANIZATION']]:
        name = json.loads(request.body)["name"]
        city = json.loads(request.body)["city"]
        location = json.loads(request.body)["location"]
        totalNum = json.loads(request.body)["totalNum"]
        startDate = json.loads(request.body)["startdate"]
        startTime = json.loads(request.body)["starttime"]
        endDate = json.loads(request.body)["enddate"]
        endTime = json.loads(request.body)["endtime"]
        startDateTime = startDate.split('T')[0] + " " + startTime.split('T')[1][:5]
        endDateTime = endDate.split('T')[0] + " " + endTime.split('T')[1][:5]
        tag = json.loads(request.body)["tag"]
        description = json.loads(request.body)["desc"]

        try:
            organizer = mysite_models.User.objects.get(username = request.user.username)
        except:
            organizer = None
        activity = Activity(ActivityName = name, ActivityCity = city, ActivityLocation = location, ActivityStartDate = startDateTime, \
            ActivityEndDate = endDateTime, Tag = tag, ActivityIntro = description, ActivityTotalAmount = totalNum, \
            ActivityRemain = totalNum, ActivityOrganizer = organizer)
        activity.save()
        print("POST ACTIVITY SUCCESS")
        return HttpResponse("POST ACTIVITY SUCCESS", status=200)
    else:
        return HttpResponse("NOT AUTHENTICATED", status=401)
   

# 编辑活动
def edit_activity(request): # name, place, date, time, tag, description, amount
    # print(request.COOKIES)
    # print(checkUserType(request))
    if checkUserType(request) in [PERMISSION_CONST['TEACHER'], PERMISSION_CONST['ORGANIZATION']]:
        activity_id = json.loads(request.body)["id"]
        activity = showactivity_models.Message.objects.get(id = activity_id)
        if activity.ActivityOrganizer != request.user:
            return HttpResponse("Not your activity!", status=401)

        activity.ActivityName = json.loads(request.body)["name"]
        activity.AcitivityCity = json.loads(request.body)["city"]
        activity.ActivityLocation = json.loads(request.body)["location"]
        activity.ActivityTotalAmount = json.loads(request.body)["totalNum"]
        startDate = json.loads(request.body)["startdate"]
        endDate = json.loads(request.body)["enddate"]
        activity.ActivityStartDate = startDate.split('T')[0] + " " + startTime.split('T')[1][:5]
        activity.ActivityEndDate = endDate.split('T')[0] + " " + endTime.split('T')[1][:5]
        activity.Tag = json.loads(request.body)["tag"]
        activity.ActivityIntro = json.loads(request.body)["desc"]

        activity.save()
        print("POST ACTIVITY SUCCESS")
        return HttpResponse("EDIT ACTIVITY SUCCESS", status=200)
    else:
        return HttpResponse("NOT AUTHENTICATED", status=401)

#显示活动列表
def catalog_grid(request):
    #is_login = request.session.get('is_login', None)
    #if is_login:
    #    user = WX_OPENID_TO_THUID.objects.get(pk=request.session.get('THUID'))
    #if not request.session.get('studentID'):
    #    request.session.flush()
    #   return redirect('/login/')
    # user = check_login(request)
    usertype = checkUserType(request)
    if usertype == PERMISSION_CONST['UNAUTHENTICATED']:
        return HttpResponse("You need to login or bind wxID to THUID!", status = 401)

    if usertype == PERMISSION_CONST['VOLUNTEER']:
        rtn_list = showactivity_models.Activity.objects.all()
    else:
        rtn_list = showactivity_models.Activity.objects.filter(ActivityOrganizer = request.user)

    rtn_pic = []
    result = []
    #page_str = request.GET.get('page')
    #if page_str is None:
    #    page = 1
    #else:
    #    page = int(page_str)
    for i in range(len(rtn_list)):
        rtn = {}
        #ActivityID = rtn_list[i].ActivityNumber
        rtn["id"] = rtn_list[i].id
        rtn["title"] = rtn_list[i].ActivityName
        rtn["city"] = rtn_list[i].ActivityCity
        rtn["location"] = rtn_list[i].ActivityLocation
        rtn["tag"] = rtn_list[i].Tag
        rtn["status"] = rtn_list[i].ActivityStatus
        rtn["startdate"] = rtn_list[i].ActivityStartDate.split(" ")[0]
        rtn["starttime"] = rtn_list[i].ActivityStartDate.split(" ")[1]
        rtn["enddate"] = rtn_list[i].ActivityEndDate.split(" ")[0]
        rtn["endtime"] = rtn_list[i].ActivityEndDate.split(" ")[1]
        rtn["totalAmount"] = rtn_list[i].ActivityTotalAmount
        rtn["remainAmount"] = rtn_list[i].ActivityRemain
        rtn["desc"] = rtn_list[i].ActivityIntro
        try:
            rtn["organizer"] = rtn_list[i].ActivityOrganizer.username
        except:
            rtn["organizer"] = "Unable to get"
        #pic_tmp = showactivity_models.ActivityPic.objects.filter(ActivityNumber=ActivityID)
        #rtn_pic.append(pic_tmp[0])
        #rtn["pic"] = pic_tmp[0]
        result.append(rtn)
    #rtn_dic = dict(map(lambda x, y: [x, y], rtn_pic, rtn_listt))
    #return render(request, "showactivity/catalog_grid.html", locals())
    return JsonResponse({"ActivityList": result}, safe=False)

# 查看活动详细信息
def activity_detail(request):
    if checkUserType(request) == PERMISSION_CONST['UNAUTHENTICATED']:
        return HttpResponse("You need to login or bind wxID to THUID!", status = 401)
    try:
        THUID = checkSessionValid(request)[1]
        if THUID is None:
            return HttpResponse("Failed to get THUID!", status = 401)
        user = VOLUNTEER.objects.get(pk=THUID)
        activity_id = json.loads(request.body)["activity_id"]
        activity = showactivity_models.Activity.objects.get(id=activity_id)
        #pic = showactivity_models.ActivityPic.objects.filter(ActivityId=activity_id
   # '''
   # class Recommend:
   #     def __init__(self, activity, pic):
   #         self.activity = activity
   #         self.pic = pic
   # activity_rtn = Recommend(activity,pic)
   # '''
        rtn = {}
        rtn["id"] = activity.id
        rtn["title"] = activity.ActivityName
        rtn["city"] = activity.ActivityCity
        rtn["location"] = activity.ActivityLocation
        rtn["tag"] = activity.Tag
        rtn["status"] = activity.ActivityStatus
        rtn["startdate"] = activity.ActivityStartDate.split(" ")[0]
        rtn["starttime"] = activity.ActivityStartDate.split(" ")[1]
        rtn["enddate"] = activity.ActivityEndDate.split(" ")[0]
        rtn["endtime"] = activity.ActivityEndDate.split(" ")[1]
        rtn["totalAmount"] = activity.ActivityTotalAmount
        rtn["remainAmount"] = activity.ActivityRemain
        rtn["desc"] = activity.ActivityIntro
        try:
            rtn["organizer"] = activity.ActivityOrganizer.username
        except:
            rtn["organizer"] = "Unable to get"
        rtn["participants"] = []
        try:
            Membership.objects.get(activity=activity, volunteer=user)
            rtn["registered"] = True
        except:
            rtn["registered"] = False
        for m in Membership.objects.filter(activity=activity):
            if m.state == ENROLL_STATE_CONST['ACCEPTED']:
                volunteer = m.volunteer
                info = {
                    "THUID".lower(): volunteer.THUID,
                    "NAME".lower(): volunteer.NAME,
                    "DEPARTMENT".lower(): volunteer.DEPARTMENT,
                    "NICKNAME".lower(): volunteer.NICKNAME,
                    "SIGNATURE".lower(): volunteer.SIGNATURE,
                    "PHONE".lower(): volunteer.PHONE,
                    "VOLUNTEER_TIME".lower(): volunteer.VOLUNTEER_TIME,
                    "EMAIL".lower(): volunteer.EMAIL
                }
                rtn["participants"].append(info)

    #Activity_recommend = showactivity_models.Activity.objects.filter(IsOverDeadline=0)
    #Number_set = set()
    #for gr in Activity_recommend:
    #    Number_set.add(gr.ActivityNumber)
    #Activity_recommend_rtn = []
    #for num in Number_set:
    #        ojb = showactivity_models.Activity.objects.get(ActivityNumber=num)
    #        pic = showactivity_models.ActivityPic.objects.filter(ActivityNumber=num)[0]
    #        Activity_recommend_rtn.append(Recommend(ojb, pic))
    #Activity = showactivity_models.Activity.objects.get(ActivityNumber=Activity_Number)
    #Activity_pic_list = showactivity_models.ActivityPic.objects.filter(ActivityNumber=Activity_Number)
    #studentID = request.session['studentID']
    #user = User.objects.get(studentID=studentID)
    #request.session['number'] = Activity.ActivityNumber
    #return render(request, "showactivity/activity_detail_page.html", locals())
        return JsonResponse(rtn)
    except:
        traceback.print_exc()
        return HttpResponse("INVALID ACTIVITY ID", status=404)

def compareTime(year1, month1, day1, hour1, minute1, year2, month2, day2, hour2, minute2):
    '''
    若(year1, month1, day1, hour1, minute1)<=(year2, month2, day2, hour2, minute2), 返回True，否则返回False
    '''
    if year1!=year2:
        return year1<year2
    if month1!=month2:
        return month1<month2
    if day1!=day2:
        return day1<day2
    if hour1!=hour2:
        return hour1<hour2
    if minute1!=minute2:
        return minute1<minute2
    return True

def checkinApi(request):
    FAIL_INFO_KEY = "failinfo"
    if checkUserType(request) != PERMISSION_CONST['VOLUNTEER']:
        JsonResponse({"success": False, FAIL_INFO_KEY: "Only logged-in volunteer can checkin!"})
    THUID = checkSessionValid(request)[1]
    if THUID is None:
        return JsonResponse({"success": False, FAIL_INFO_KEY: "Fail to get THUID!"})
    jsonBody = json.loads(request.body)
    volunteer = VOLUNTEER.objects.get(THUID=THUID)
    activity = Activity.objects.get(id=jsonBody["id"])
    utcnow = datetime.datetime.utcnow().replace(tzinfo=utc)
    year = utcnow.year
    month = utcnow.month
    day = utcnow.day
    hour = utcnow.hour
    minute = utcnow.minute
    time1 = activity.ActivityStartDate
    time2 = activity.ActivityEndDate
    year1 = int(time1.split(" ")[0].split("-")[0])
    month1 = int(time1.split(" ")[0].split("-")[1])
    day1 = int(time1.split(" ")[0].split("-")[2])
    hour1 = int(time1.split(" ")[1].split(":")[0])
    minute1 = int(time1.split(" ")[1].split(":")[1])
    year2 = int(time2.split(" ")[0].split("-")[0])
    month2 = int(time2.split(" ")[0].split("-")[1])
    day2 = int(time2.split(" ")[0].split("-")[2])
    hour2 = int(time2.split(" ")[1].split(":")[0])
    minute2 = int(time2.split(" ")[1].split(":")[1])
    if not compareTime(year1, month1, day1, hour1, minute1, year, month, day, hour, minute):
        return JsonResponse({"success": False, FAIL_INFO_KEY: "You cannot check in before the activity start date!"})
    if not compareTime(year, month, day, hour, minute, year2, month2, day2, hour2, minute2):
        return JsonResponse({"success": False, FAIL_INFO_KEY: "You cannot check in after the activity end date!"})
    try:
        utcnow = "{}-{}-{} {}:{}".format(year, month, day, hour, minute)
        membership = Membership.objects.get(volunteer=volunteer, activity=activity, state=ENROLL_STATE_CONST['ACCEPTED'])
        latitude = jsonBody["latitude"]
        longitude = jsonBody["longitude"]
        try:
            print(jsonBody)
            address = json.loads(requests.get("http://api.map.baidu.com/reverse_geocoding/v3/?ak={}&output=json&coordtype=wgs84ll&location={},{}".format(BAIDU_MAP_AK, latitude, longitude)).text)
            print(address["status"])
            if address["status"] == 0:
                address = address["result"]["formatted_address"]
            else:
                address = "UNKNOWN"
        except:
            traceback.print_exc()
            address = "UNKNOWN"
        checkin(membership=membership, latitude=jsonBody["latitude"], longtitude=jsonBody["longitude"], checkinTime=utcnow, address=address).save()
        return JsonResponse({"success": True})
    except:
        traceback.print_exc()
        return JsonResponse({"success": False, FAIL_INFO_KEY: "You have not been accepted by the activity organizer"})


def search(request):
    if checkUserType(request) == PERMISSION_CONST['UNAUTHENTICATED']:
        return HttpResponse("You need to login or bind wxID to THUID!", status = 401)
    #user = check_login(request)
    keyword = request.GET.get('search')
    rtn_set = set()
    rtn_list = []
    name_key = showactivity_models.Activity.objects.filter(ActivityName__contains=keyword)
    content_key = showactivity_models.Activity.objects.filter(ActivityIntro__contains=keyword)
    organizer_key = showactivity_models.Activity.objects.filter(ActivityOrganizer__contains=keyword)
    #num_key = showactivity_models.Activity.objects.filter(id__contains=keyword)

    #class Activity:
    #    def __init__(self, id,name,date, pic):
    #        self.id = id
    #        self.pic = pic

    for name in name_key:
        rtn_set.add(name)
    for content in content_key:
        rtn_set.add(content)
    for organizer in organizer_key:
        rtn_set.add(organizer)
    #for num in num_key:
        #rtn_set.add(num)
    rtn_list = []
    for rtn_activity in rtn_set:
        rtn = {}
        rtn["id"] = rtn_activity.id
        rtn["title"] = rtn_activity.ActivityName
        rtn["location"] = rtn_activity.ActivityPlace
        rtn["tag"] = rtn_activity.Tag
        rtn["status"] = rtn_activity.ActivityStatus
        rtn["time1"] = rtn_activity.ActivityStartDate
        rtn["time2"] = rtn_activity.ActivityEndDate
        try:
            rtn["organizer"] = rtn_activity.ActivityOrganizer.username
        except:
            rtn["organizer"] = "Unable to get"
        rtn_list.append(rtn)
        #rtn_list.append(Activity(rtn_activity, showactivity_models.ActivityPic.objects.filter(ActivityNumber=rtn_activity.ActivityNumber)[0], rtn_activity.ActivityTime))
    #return render(request, "showactivity/search.html", locals())
    return JsonResponse(rtn_list)

# 获取消息列表
def message_catalog_grid(request):
    
    # user = User.objects.get(pk = request.session.get('THUID'))
    # message = showactivity_models.Message.objects.get(MessageId=messaage_id)
    usertype = checkUserType(request)
    if usertype == PERMISSION_CONST["VOLUNTEER"]:
        THUID = checkSessionValid(request)[1]
        volunteer = VOLUNTEER(THUID = THUID)
        res = []
        for info in MessageReadOrNot.objects.filter(VolunteerID=volunteer):
              msgInfo = {}
              msg = info.MessageID
              msgInfo["id"] = msg.id
              msgInfo["content"] = msg.MessageDetailContent
              msgInfo["title"] = msg.MessageTitle
              msgInfo["time"] = msg.PostTime
              msgInfo["sender"] = msg.ActivityNumber.ActivityOrganizer.username
              msgInfo["read"] = info.ReadOrNot
              res.append(msgInfo)
        return JsonResponse({"messages":res})
    elif usertype in [PERMISSION_CONST['TEACHER'], PERMISSION_CONST['ORGANIZATION']]:
        activity_id = json.loads(request.body)["activity_id"]
        activity = Activity.objects.get(id=activity_id)
        res = []
        for msg in Message.objects.filter(ActivityNumber=activity):
            msgInfo = {}
            msgInfo["id"] = msg.id
            msgInfo["title"] = msg.MessageTitle
            msgInfo["content"] = msg.MessageDetailContent
            msgInfo['time'] = msg.PostTime
            res.append(msgInfo)
        return JsonResponse({"messages": res}, safe=False)
    else:
        return HttpResponse("NOT AUTHENTICATED", status=401)
'''
# 读消息
def read_message(request):
    if not checkSessionValid(request):
        return HttpResponse("You need to login!", status = 401)
    THUID = getStudentID(request)
    if THUID == False:
        return HttpResponse("Fail to get THUID!", status = 404)
    # message_id = request.POST.get(message_id)
    user = 
    .objects.get(pk = THUID)
    message_id = request.POST.get(message_id)
    message = showactivity_models.Message.objects.get(id=messaage_id)
    message_ReadOrNot = showactivity_models.MessageReadOrNot.objects.get(MessageId=message_id)
    rtn = {}
    rtn["Title"] = message.MessageTitle
    rtn["DetailContent"] = message.MessageDetailContent
    message_ReadOrNot.update(ReadOrNot = 1)
    message_ReadOrNot.save()
    return JsonResponse({"message_detail":rtn})
'''
# 将消息标记为已读
def mark_read(request):
    if checkUserType(request) == PERMISSION_CONST["VOLUNTEER"]:
        THUID = checkSessionValid(request)[1]
        volunteer = VOLUNTEER(THUID=THUID)
        messaage_id = json.loads(request.body)["id"]
        message = Message.objects.get(id=messaage_id)
        info = MessageReadOrNot.objects.get(VolunteerID=volunteer, MessageID=message)
        info.ReadOrNot = True
        info.save()
        return HttpResponse("SUCCESS", status = 200)
    else:
        return HttpResponse("Only volunteer can read the message", status = 401)

# 删除一条消息
def delete_message(request):
    usertype = checkUserType(request)
    if usertype in [PERMISSION_CONST['TEACHER'], PERMISSION_CONST['ORGANIZATION']]:
        message_id = json.loads(request.body)["id"]
        message = showactivity_models.Message.objects.get(id = message_id)
        activity = message.ActivityNumber
        if activity.ActivityOrganizer != request.user:
            return HttpResponse("Not your message!", status=401)
        message.delete()
        return HttpResponse("SUCCESS", status=200)
    elif usertype == PERMISSION_CONST["VOLUNTEER"]:
        messaage_id = json.loads(request.body)["id"]
        THUID = checkSessionValid(request)[1]
        volunteer = VOLUNTEER(THUID=THUID)
        message = Message(id=messaage_id)
        MessageReadOrNot.objects.get(VolunteerID=volunteer, MessageID=message).delete()
        return HttpResponse("SUCCESS", status=200)
    else:
        return HttpResponse("Failed to delete message", status = 401)

# 报名活动
def register_activity(request):
    FAIL_INFO_KEY = "failinfo"
    if checkUserType(request) != PERMISSION_CONST['VOLUNTEER']:
        return JsonResponse({"success": False, FAIL_INFO_KEY: "Only logged-in volunteer can register activities!"})
    THUID = checkSessionValid(request)[1]
    if THUID is None:
        return JsonResponse({"success": False, FAIL_INFO_KEY: "Fail to get THUID!"})
    activity_id = json.loads(request.body)["id"]

    user = VOLUNTEER.objects.get(pk = THUID)
    activity = Activity.objects.get(id = activity_id)
    for m in Membership.objects.filter(activity=activity):
        if m.volunteer == user:
            return JsonResponse({"success": False, FAIL_INFO_KEY: "No need to register repeatedly"})

    if activity.ActivityRemain == 0:
        return JsonResponse({"success": False, FAIL_INFO_KEY: "No remain amount!"})

    Membership(volunteer=user, activity = activity, state=ENROLL_STATE_CONST["ACCEPTED"]).save()
    activity.ActivityRemain = activity.ActivityRemain - 1
    activity.save()
    return JsonResponse({"success": True})
    

# 取消报名
def cancel_registration(request):
    if checkUserType(request) != PERMISSION_CONST['VOLUNTEER']:
        return JsonResponse({"success": False, FAIL_INFO_KEY: "Only logged-in volunteer can register activities!"})
    THUID = checkSessionValid(request)[1]
    if THUID is None:
        return JsonResponse({"success": False, FAIL_INFO_KEY: "Fail to get THUID!"})
    activity_id = json.loads(request.body)["id"]

    user = VOLUNTEER.objects.get(pk = THUID)
    activity = Activity.objects.get(id = activity_id)

    already_registered = False
    for m in Membership.objects.filter(activity=activity):
        if m.volunteer == user:
            already_registered = True

    if not already_registered:
        return JsonResponse({"success": False, FAIL_INFO_KEY: "You need to register before cancelling it"})

    activity.members.remove(user)
    activity.ActivityRemain = activity.ActivityRemain + 1
    activity.save()
    return JsonResponse({"success": True})

# 发布消息
def post_message(request):
    if checkUserType(request) in [PERMISSION_CONST['TEACHER'], PERMISSION_CONST['ORGANIZATION']]:
        print(json.loads(request.body))
        activity_id = json.loads(request.body)["activity_id"]
        activity = showactivity_models.Activity.objects.get(id=activity_id)
        title = json.loads(request.body)["title"]
        content = json.loads(request.body)["content"]
        date = datetime.datetime.utcnow().replace(tzinfo=utc)
        date = "{}-{}-{}".format(date.year, date.month, date.day)
        message = Message(MessageTitle = title, MessageDetailContent = content,ActivityNumber = activity, PostTime = date)
        message.save()
        volunteers = activity.members
        for volunteer in volunteers.all():
            membership = Membership.objects.get(volunteer = volunteer, activity = activity)
            if membership.state == ENROLL_STATE_CONST['ACCEPTED']:
                message.volunteers.add(volunteer)
        message.save()
        return HttpResponse("Post messages successful", status = 200)
    else:
        return HttpResponse("You have no access", status = 401)

# 编辑消息
def edit_message(request):
    if checkUserType(request) in [PERMISSION_CONST['TEACHER'], PERMISSION_CONST['ORGANIZATION']]:
        message_id = json.loads(request.body)["id"]
        message = showactivity_models.Message.objects.get(id = message_id)
        activity = message.ActivityNumber
        if activity.ActivityOrganizer != request.user:
            return HttpResponse("Not your message!", status=401)
        message.MessageTitle = json.loads(request.body)["title"]
        message.MessageDetailContent = json.loads(request.body)["content"]
        date = datetime.datetime.utcnow().replace(tzinfo=utc)
        date = "{}-{}-{}".format(date.year, date.month, date.day)
        message.PostTime = date
        message.save()
        return HttpResponse("SUCCESS", status=200)
    else:
        return HttpResponse("Not authenticated!", status=401)    

# 获取用户参加活动的历史
def get_volunteer_history(request):
    usertype = checkUserType(request)
    if usertype == PERMISSION_CONST['VOLUNTEER']:
        THUID = checkSessionValid(request)[1]
        volunteer = VOLUNTEER(THUID=THUID)
        resList = []
        for record in Membership.objects.filter(volunteer=volunteer):
            activity = record.activity
            rtn = {}
            rtn["id"] = activity.id
            rtn["title"] = activity.ActivityName
            rtn["city"] = activity.ActivityCity
            rtn["location"] = activity.ActivityLocation
            rtn["tag"] = activity.Tag
            rtn["status"] = activity.ActivityStatus
            rtn["startdate"] = activity.ActivityStartDate.split(" ")[0]
            rtn["starttime"] = activity.ActivityStartDate.split(" ")[1]
            rtn["enddate"] = activity.ActivityEndDate.split(" ")[0]
            rtn["endtime"] = activity.ActivityEndDate.split(" ")[1]
            rtn["totalAmount"] = activity.ActivityTotalAmount
            rtn["remainAmount"] = activity.ActivityRemain
            rtn["desc"] = activity.ActivityIntro
            try:
                rtn["organizer"] = activity.ActivityOrganizer.username
            except:
                rtn["organizer"] = "Unable to get"
            state = record.state
            rtn["state"] = 'UNCENSORED'
            for state_key in ['ACCEPTED', 'UNCENSORED', 'REJECTED']:
                if state == ENROLL_STATE_CONST[state_key]:
                    rtn["state"] = state_key
                    break
            resList.append(rtn)
        return JsonResponse({"res": resList}, safe=False)
    else:
        return HttpResponse("NOT A VOLUNTEER!", status=401)

# 排名
def get_ranking():
    usertype = checkUserType(request)
    if usertype == PERMISSION_CONST["UNAUTHENTICATED"]:
        return HttpResponse("UNAUTHENTICATED", status=401)
    outdated =  (datetime.datetime.utcnow()-ranking_last_update_time).total_seconds() > (24*3600) # 每24小时更新一次排行榜
    if outdated or (len(ranking_top_100_list) == 0):
        new_top_100_list = []
        for volunteer in VOLUNTEER.objects.all().order_by('-VOLUNTEER_TIME'):
            info = {}
            info["THUID"] = volunteer.THUID
            info["NAME"] = volunteer.NAME
            info["DEPARTMENT"] = volunteer.DEPARTMENT
            info["NICKNAME"] = volunteer.NICKNAME
            info["SIGNATURE"] = volunteer.SIGNATURE
            info["PHONE"] = volunteer.PHONE
            info["VOLUNTEER_TIME"] = volunteer.VOLUNTEER_TIME
            info["EMAIL"] = volunteer.EMAIL
            new_top_100_list.append(info)
        ranking_top_100_list = new_top_100_list
        ranking_last_update_time = datetime.datetime.utcnow()
    return JsonResponse({"ranking_top_100":ranking_top_100_list, "last_update_time":str(ranking_last_update_time)}, safe=False)

# 分配志愿工时（志愿中心/志愿团体）
def allocate_volunteerhours(request):
    # raiseNotImplementedError("Not implemented!")
    if checkUserType(request) in [PERMISSION_CONST['TEACHER'], PERMISSION_CONST['ORGANIZATION']]:
        # hours = json.loads(request.body)["hours"]
        activity_id = json.loads(request.body)["activity_id"]
        # volunteer_id = json.loads(request.body)["volunteer_id"]
        info = json.loads(request.body)["info"]
        activity = showactivity_models.Activity.objects.get(id = activity_id)
        for obj in info:
            student_id = obj["student_id"]
            student = VOLUNTEER.objects.get(id = student_id)  # 不确定传过来的是id还是THUID，先这样写吧orz
            if showactivity_models.Activity.objects.get(members=student) != null:
                time = obj["time"]
                totalTime = student.VOLUNTEER_TIME + time
                student.update(VOLUNTEER_TIME=totalTime)
                student.save()
                return HttpResponse("Allocate volunteer hours successful!", status=200)
            else:
                return HttpResponse("Can't allocate to this student!", status=401)   
    else:
        return HttpResponse("Not authenticated!", status=401)    
        
