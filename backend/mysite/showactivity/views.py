import json
import math
import traceback

from django.shortcuts import render, redirect
from django.utils import timezone
from django.shortcuts import HttpResponse

from . import models as showactivity_models
import mysite.models as mysite_models
from .models import Message, MessageReadOrNot, Activity, ActivityPic
from mysite.views import checkSessionValid, LOGGED_IN_CONST

PERMISSION_CONST = {
    'TEACHER': 233,
    'ORGANIZATION': 255,
    'VOLUNTEER': 258,
    'UNAUTHENTICATED': 266
}

def checkUserType(request):
    try:
        if request.user.is_authenticated: # 先检查是否为老师或公益团体账号
            print("authenticated")
            if mysite_models.UserIdentity(request.user).isTeacher:
                return PERMISSION_CONST['TEACHER']
            else:
                return PERMISSION_CONST['ORGANIZATION']
        else:
            return PERMISSION_CONST['UNAUTHENTICATED']
    except:
        traceback.print_exc()
        res = checkSessionValid(request)[1]
        if res is not None:
            return PERMISSION_CONST['VOLUNTEER']
        else:
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
        region = json.loads(request.body)["region"]
        totalNum = json.loads(request.body)["totalNum"]
        startDate = json.loads(request.body)["date1"]
        endDate = json.loads(request.body)["date2"]
        tag = json.loads(request.body)["tag"]
        description = json.loads(request.body)["desc"]

        try:
            organizer = mysite_models.User.objects.get(username = request.user.username)
        except:
            organizer = None 
        activity = Activity(ActivityName = name, ActivityPlace = region, ActivityStartDate = startDate, \
            ActivityEndDate = endDate, Tag = tag, ActivityIntro = description, ActivityRemain = totalNum, \
            ActivityOrganizer = organizer)
        activity.save()
        print("POST ACTIVITY SUCCESS")
        return HttpResponse("POST ACTIVITY SUCCESS", status=200)
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

    if checkUserType(request) == PERMISSION_CONST['UNAUTHENTICATED']:
        return HttpResponse("You need to login or bind wxID to THUID!", status = 401)

    rtn_list = showactivity_models.Activity.objects.all()

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
        rtn["location"] = rtn_list[i].ActivityPlace
        rtn["tag"] = rtn_list[i].Tag
        rtn["status"] = rtn_list[i].ActivityStatus
        rtn["time1"] = rtn_list[i].ActivityStartDate
        rtn["time2"] = rtn_list[i].ActivityEndDate
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
    return JsonResponse(result)

# 查看活动详细信息
def activity_detail(request):
    if checkUserType(request) == PERMISSION_CONST['UNAUTHENTICATED']:
        return HttpResponse("You need to login or bind wxID to THUID!", status = 401)
    try:
        activity_id = request.POST.get(activity_id)
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
        rtn["id"] = rtn_list[i].id
        rtn["title"] = rtn_list[i].ActivityName
        rtn["location"] = rtn_list[i].ActivityPlace
        rtn["tag"] = rtn_list[i].Tag
        rtn["status"] = rtn_list[i].ActivityStatus
        rtn["time1"] = rtn_list[i].ActivityStartDate
        rtn["time2"] = rtn_list[i].ActivityEndDate
        try:
            rtn["organizer"] = rtn_list[i].ActivityOrganizer.username
        except:
            rtn["organizer"] = "Unable to get"


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
        return HttpResponse("INVALID ACTIVITY ID", status=404)

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
            rtn["organizer"] = rtn_list[i].ActivityOrganizer.username
        except:
            rtn["organizer"] = "Unable to get"
        rtn_list.append(rtn)
        #rtn_list.append(Activity(rtn_activity, showactivity_models.ActivityPic.objects.filter(ActivityNumber=rtn_activity.ActivityNumber)[0], rtn_activity.ActivityTime))
    #return render(request, "showactivity/search.html", locals())
    return JsonResponse(rtn_list)

# 消息列表
def message_catalog_grid(request):
    
    # user = User.objects.get(pk = request.session.get('THUID'))
    # message = showactivity_models.Message.objects.get(MessageId=messaage_id)
    message_list = showactivity_models.MessageReadOrNot.objects.filter(THUID=request.session.get('THUID'))
    rtn_list = []
    for i in range(len(message_list)):
        message_id = message_list[i].MessageId
        message = showactivity_models.Message.objects.get(id=messaage_id)
        rtn = {}
        rtn["ReadOrNot"] = message_list[i].ReadOrNot
        rtn["Title"] = message.MessageTitle
        rtn["BriefContent"] = message.MessageBriefContent
        rtn_list.append(rtn)    
    return JsonResponse({"message_list":rtn_list})

# 读消息
'''
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
    if not checkSessionValid(request):
        return HttpResponse("You need to login!", status = 401)
    THUID = getStudentID(request)
    if THUID == False:
        return HttpResponse("Fail to get THUID!", status = 404)
    message_id = request.POST.get(message_id)
    # THUID = 
    message = showactivity_models.Message.objects.get(id=messaage_id)
    message_ReadOrNot = showactivity_models.MessageReadOrNot.objects.filter(THUId=THUID)
    message_ReadOrNot = showactivity_models.MessageReadOrNot.objects.get(MessageId=message_id)
    message_ReadOrNot.update(ReadOrNot = 1)
    message_ReadOrNot.save()
    return HttpResponse("Succeed to mark as read already", status = 200)

# 删除一条消息
def delete_message(request):
    if not checkSessionValid(request):
        return HttpResponse("You need to login!", status = 401)
    THUID = getStudentID(request)
    if THUID == False:
        return HttpResponse("Fail to get THUID!", status = 404)
    message_id = request.POST.get(message_id)
    # THUID = 
    # message = showactivity_models.Message.objects.get(MessageId=messaage_id)
    message_ReadOrNot = showactivity_models.MessageReadOrNot.objects.filter(THUId=THUID)
    message_ReadOrNot = showactivity_models.MessageReadOrNot.objects.get(MessageId=message_id)
    message_ReadOrNot.delete()
    # message_ReadOrNot.update(ReadOrNot = 1)
    # message_ReadOrNot.save()

    return HttpResponse("Succeed to delete message", status = 200)
'''
# 报名活动
def register_activity(request):
    if not checkSessionValid(request):
        return HttpResponse("You need to login!", status = 401)
    THUID = getStudentID(request)
    if THUID == False:
        return HttpResponse("Fail to get THUID!", status = 404)
    activity_id = request.POST.get(activity_id)

    user = User.objects.get(pk = THUID)
    activity = Activity.objects.get(id = activity_id)

    user.Activities.add(activity)
    user.save()

    activity.Participants.add(user)
    activity.save()

    amount = activity.ActivityRemain - 1
    activity.update(ActivityRemain=amount)
    activity.save()

# 取消报名
def cancel_registration(request):
    if not checkSessionValid(request):
        return HttpResponse("You need to login!", status = 401)
    THUID = getStudentID(request)
    if THUID == False:
        return HttpResponse("Fail to get THUID!", status = 404)
    activity_id = request.POST.get(activity_id)

    user = User.objects.get(pk = THUID)
    activity = Activity.objects.get(id = activity_id)

    user.Activities.remove(activity)
    user.save()

    activity.Participants.remove(user)
    activity.save()

    amount = activity.ActivityRemain + 1
    activity.update(ActivityRemain=amount)
    activity.save()
'''

def post_message(request):
    if checkUserType(request) in [PERMISSION_CONST['TEACHER'], PERMISSION_CONST['ORGANIZATION']]:
        activity_id = request.POST.get(id)
        activity = showactivity_models.Activity.objects.get(id=activity_id)
        volunteers = activity.Participants

        title = json.loads(request.body)["title"]
        content = json.loads(request.body)["content"]
        

        message = Message(MessageTitle = title, MessageDetailContent = content,ActivityNumber = activity_id, volunteers = volunteers)
        message.save()

        message_ReadOrNot = MessageReadOrNot(MessageID = message.id, VolunteerID = volunteers, ReadOrNot = 0)
        message_ReadOrNot.save()
        
        return HttpResponse("Post messages successful", status = 200)
    else:
        return HttpResponse("You have no access", status = 401)
