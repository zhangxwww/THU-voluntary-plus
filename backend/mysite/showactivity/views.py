import json
import math

from django.shortcuts import render, redirect
from django.utils import timezone
from django.shortcuts import HttpResponse

import showactivity.models as showactivity_models
import mysite.models as mysite_models

# Create your views here.
#检查登录
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
    

#显示活动列表
def catalog_grid(request):
    #is_login = request.session.get('is_login', None)
    #if is_login:
    #    user = WX_OPENID_TO_THUID.objects.get(pk=request.session.get('THUID'))
    #if not request.session.get('studentID'):
    #    request.session.flush()
    #   return redirect('/login/')
    user = check_login(request)
        
    type = request.GET.get('type')
    if type is None:
        rtn_list = showactivity_models.Activity.objects.all()
    else:
        rtn_list = showactivity_models.Activity.objects.filter(Category=type)
    rtn_pic = []
    rtn_listt = []
    #page_str = request.GET.get('page')
    #if page_str is None:
    #    page = 1
    #else:
    #    page = int(page_str)
    for i in range(len(rtn_list)):
        rtn = {}
        ActivityID = rtn_list[i].ActivityNumber
        rtn["id"] = ActivityID
        rtn["name"] = rtn_list[i].ActivityName
        rtn["date"] = rtn_list[i].ActivityTime
        pic_tmp = showactivity_models.ActivityPic.objects.filter(ActivityNumber=ActivityID)
        #rtn_pic.append(pic_tmp[0])
        rtn["pic"] = pic_tmp[0]
        rtn_listt.append(rtn)
    #rtn_dic = dict(map(lambda x, y: [x, y], rtn_pic, rtn_listt))
    #return render(request, "showactivity/catalog_grid.html", locals())
    return JsonResponse({"activity_list":rtn_listt})

# 查看活动详细信息
def activity_detail(request,activity_id):
    #is_login = request.session.get('is_login', None)
    #if is_login:
    #    user = User.objects.get(pk=request.session.get('studentID'))
    user = check_login(request)
    #Activity_Number = request.GET.get('Number')
    activity = showactivity_models.Activity.objects.get(ActivityNumber=activity_id)
    pic = showactivity_models.ActivityPic.objects.filter(ActivityNumber=activity_id)
    class Recommend:
        def __init__(self, activity, pic):
            self.activity = activity
            self.pic = pic
    activity_rtn = Recommend(activity,pic)

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
    return JsonResponse({"activity_detail":activity_rtn})

def search(request):
    #is_login = request.session.get('is_login', None)
    #if is_login:
    #    user = User.objects.get(pk=request.session.get('studentID'))
    user = check_login(request)
    keyword = request.GET.get('search')
    rtn_set = set()
    rtn_list = []
    name_key = showactivity_models.Activity.objects.filter(ActivityName__contains=keyword)
    content_key = showactivity_models.Activity.objects.filter(ActivityIntro__contains=keyword)
    organizer_key = showactivity_models.Activity.objects.filter(ActivityOrganizer__contains=keyword)
    num_key = showactivity_models.Activity.objects.filter(ActivityNumber__contains=keyword)

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
    for num in num_key:
        rtn_set.add(num)
    rtn_listt = []
    for rtn_activity in rtn_set:
        rtn = {}
        ActivityID = rtn_activity.ActivityNumber
        rtn["id"] = ActivityID
        rtn["name"] = rtn_activity.ActivityName
        rtn["date"] = rtn_activity.ActivityTime
        pic_tmp = showactivity_models.ActivityPic.objects.filter(ActivityNumber=ActivityID)
        #rtn_pic.append(pic_tmp[0])
        rtn["pic"] = pic_tmp[0]
        rtn_listt.append(rtn)
        #rtn_list.append(Activity(rtn_activity, showactivity_models.ActivityPic.objects.filter(ActivityNumber=rtn_activity.ActivityNumber)[0], rtn_activity.ActivityTime))
    #return render(request, "showactivity/search.html", locals())
    return JsonResponse({"search_result":rtn_listt})

def read_message(request):
    