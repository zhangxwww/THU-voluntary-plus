from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth import login, logout
from django.contrib.auth import  authenticate
from django.contrib.auth.models import User
from .settings import TICKET_AUTHENTICATION, WX_TOKEN_HEADER, WX_OPENID_HEADER, WX_CODE_HEADER, WX_HTTP_API, \
    WX_APPID, WX_SECRET, REDIRECT_TO_LOGIN
from .models import WX_OPENID_TO_THUID, VOLUNTEER, UserIdentity, VerificationCode, UserIdentity
#User, UserManager
import requests
import json
from django.contrib.sessions.backends.db import SessionStore
import datetime 
from django.utils.timezone import utc
import hashlib
import traceback
import random
import string

from django.db import transaction

from showactivity.models import *
# import mysite.models as mysite_models


import datetime 
from django.utils.timezone import utc
import requests


THUID_CONST="THUID"
TOKEN_CONST="TOKEN"
OPENID_CONST="OPENID"
SUCCESS_CONST="SUCCESS"
LOGGED_IN_CONST="LOGGED_IN"

PERMISSION_CONST = {
    'TEACHER': 233,
    'ORGANIZATION': 255,
    'VOLUNTEER': 258,
    'UNAUTHENTICATED': 266,
    'UNREGISTERED':277
}

def get_hash(s):
    hash = hashlib.sha256()
    hash.update(s.encode('utf-8'))
    return hash.hexdigest()

def redirectToTHUAuthentication(request):
    #TODO: 防止同一客户端未注销后再次发出登录请求
    if False:
        raise NotImplementedError
    return HttpResponseRedirect(REDIRECT_TO_LOGIN)

# 获取客户端的ip地址
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

# 解析清华大学用户电子身份服务系统的返回内容
def parseUserInfoFromTHUAuthentication(text):
    parsed = {}
    for r in text.split(':'):
        prop = r.split('=')[0]
        value = r.split('=')[1]
        parsed[prop] = value
    return parsed

# 检查用户类型
def checkUserType(request):
    try:
        if request.user.is_authenticated: # 先检查是否为老师或公益团体账号
            print("authenticated")
            print(request.user.username)
            print("?????",UserIdentity.objects.select_for_update().get(user=request.user).isTeacher)
            if UserIdentity.objects.select_for_update().get(user=request.user).isTeacher == 1:
                return PERMISSION_CONST['TEACHER']
            elif UserIdentity.objects.select_for_update().get(user=request.user).isTeacher == 2:
                return PERMISSION_CONST['ORGANIZATION']
            else:
                return PERMISSION_CONST['UNREGISTERED']
        else:
            res = checkSessionValid(request)[1]
            if res is not None:
                return PERMISSION_CONST['VOLUNTEER']
            else:
                return PERMISSION_CONST['UNAUTHENTICATED']
    except:
        traceback.print_exc()
        return PERMISSION_CONST['UNAUTHENTICATED']

def checkSessionValid(request):
    '''
    检查学生是否登录、登录是否过期、是否可以获取到学号（小程序端登录时，只有绑定了学号才能获取到学号）。
    若登录且未过期返回(True, THUID/None)（注：若为小程序端且未绑定，才返回None），否则返回(False, None)
    '''
    client_type = request.META['HTTP_USER_AGENT']
    try:
        if "MicroMessenger" in client_type:
            sessionid = request.META["HTTP_SET_COOKIE"].split("=")[1]
        else:
            sessionid = request.session.session_key
        s = SessionStore(session_key=sessionid)
        if s[LOGGED_IN_CONST]!= True:
            return False, None
        expiry_date = s.get_expiry_date()
        print("expiry_date: {}".format(expiry_date))
        utcnow = datetime.datetime.utcnow().replace(tzinfo=utc)
        print("utcnow: {}".format(utcnow))
        if utcnow<expiry_date:
            if "MicroMessenger" in client_type:
                try:
                    record = WX_OPENID_TO_THUID.objects.select_for_update().get(OPENID = s[OPENID_CONST])
                    THUID = record.THUID
                    # return JsonResponse({"THUID":THUID})
                    return True, THUID # 已登录，已绑定
                except:
                    # return JsonResponse({"THUID":"Not binded"})
                    traceback.print_exc()
                    return True, None # 已登录，未绑定
            else:
                return True, int(s[THUID_CONST])
        else:
            s[LOGGED_IN_CONST] = False
            return False, None
    except:
        return False, None

# 志愿者获取个人信息
def volunteerGetInfo(request):
    usertype = checkUserType(request)
    if usertype != PERMISSION_CONST["VOLUNTEER"]:
        return HttpResponse("Not a volunteer!", status=401)
    raise NotImplementedError

'''
def getStudentID(request):
    
    #获取学号，调用此函数前应调用checkSessionValid函数检查登录状态
    #若获取成功则返回学号，否则返回None
    
    client_type = request.META['HTTP_USER_AGENT']
    if "MicroMessenger" in client_type:
        try:
            sessionid = request.META["HTTP_SET_COOKIE"].split("=")[1]
            OPENID = SessionStore(session_key=sessionid)[OPENID_CONST]
            record = WX_OPENID_TO_THUID.objects.select_for_update().get(OPENID = OPENID)
            THUID = record.THUID
            return THUID
        except:
            return None
    else:
        if THUID_CONST in request.session.keys():
            return request.session[THUID_CONST]
        else:
            return None
'''

def loginApi(request):
    '''
    登陆接口
    '''
    client_type = request.META['HTTP_USER_AGENT']
    sessionValidInfo = checkSessionValid(request)
    print(sessionValidInfo)
    if sessionValidInfo[0]:
        return HttpResponse("No need to login repeatedly", status=403)
    if "MicroMessenger" in client_type: # Case 1: 微信端，POST请求
        jsonBody = json.loads(request.body)
        if WX_CODE_HEADER in jsonBody.keys(): # 处理code
            code = jsonBody[WX_CODE_HEADER]
            r = requests.post(WX_HTTP_API,data={"appid":WX_APPID, "secret":WX_SECRET, "js_code":code, "grant_type":"authorization_code"})
            res = json.loads(r.text)
            print(res)
            if ("errcode" not in res.keys()) or (res["errcode"] == 0):
                request.session[OPENID_CONST]=res["openid"]
                request.session[LOGGED_IN_CONST] = True
                THUID = None
                try:
                    THUID = WX_OPENID_TO_THUID.objects.select_for_update().get(OPENID = res["openid"]).THUID
                except:
                    THUID = None
                print(THUID)
                # 检查有没有绑定
                if THUID is not None:
                    volunteer = VOLUNTEER.objects.select_for_update().get(THUID=THUID)
                    jsonData = {
                        "THUID":volunteer.THUID,
                        "NAME": volunteer.NAME,
                        "DEPARTMENT": volunteer.DEPARTMENT,
                        "NICKNAME": volunteer.NICKNAME,
                        "SIGNATURE": volunteer.SIGNATURE,
                        "PHONE": volunteer.PHONE,
                        "VOLUNTEER_TIME": volunteer.VOLUNTEER_TIME,
                        "EMAIL": volunteer.EMAIL,
                        "BINDED": True
                    }
                    print(jsonData)
                    return JsonResponse(jsonData)
                else:
                    return JsonResponse({"BINDED":False})
            else:
                return HttpResponse(status=404)
        else:
            return HttpResponse("not found WX_CODE_HEADER",status=404)
    else: # Case2: PC端，GET请求
        ip = get_client_ip(request).replace('.','_')
        r = requests.get(TICKET_AUTHENTICATION+request.GET.get("ticket")+'/'+ip)
        r = parseUserInfoFromTHUAuthentication(r.text)
        request.session[LOGGED_IN_CONST] = True
        THUID = r["zjh"]
        request.session[THUID_CONST] = THUID
        # 更新VOLUNTEER表
        try:
            VOLUNTEER.objects.select_for_update().get(THUID=THUID)
        except:
            volunteer = VOLUNTEER(THUID = THUID, NAME = r["xm"], DEPARTMENT=r["dw"], EMAIL=r["email"], NICKNAME = r["xm"])
            volunteer.save()
        return JsonResponse(json.dumps(r), safe=False)

def managerLoginApi(request):
    '''
    志愿中心老师/公益团体的登录接口，网页端。
    '''
    jsonBody = json.loads(request.body)
    username = jsonBody["username"]
    passwd = jsonBody["password"]
    try:
        print(passwd)
        print(username)
        user = authenticate(username=username, password=passwd)
        print("xixi")
        if user is not None:
            login(request, user)
        else:
            return HttpResponse("LOGIN FAILED", status=404)
        return HttpResponse("LOGIN SUCCESS")
    except:
        traceback.print_exc()
        return HttpResponse("LOGIN FAILED", status=404)


def bindApi(request):
    '''
    绑定微信的openid与学号
    '''
    if not checkSessionValid(request)[0]:
        return HttpResponse("You need to login!", status=401)
    client_type = request.META['HTTP_USER_AGENT']
    if "MicroMessenger" in client_type: # Case 1: 微信端，POST请求
        sessionid = request.META["HTTP_SET_COOKIE"].split("=")[1]
        s = SessionStore(session_key=sessionid)
        OPENID = s.get('OPENID')
        alreadyBinded = True # 若已经绑定，可以重新绑定
        try:
            wxuser = WX_OPENID_TO_THUID.objects.select_for_update().get(OPENID=OPENID)
        except:
            alreadyBinded = False
        TOKEN = json.loads(request.body)[WX_TOKEN_HEADER]
        url = "https://alumni-test.iterator-traits.com/fake-id-tsinghua-proxy/api/user/session/token"
        data = {"token": TOKEN}
        r = requests.post(url, json=data)
        r = json.loads(r.text)
        if not "error" in r.keys() or r["error"]["code"]!=0:
            return HttpResponse("Unable to bind", status=401)
        thuuser = r["user"]
        THUID = thuuser["card"]
        if alreadyBinded:
            print("rebind!")
            wxuser.THUID = THUID
            wxuser.save()
        else:
            print("bind!")
            wxuser = WX_OPENID_TO_THUID(OPENID=OPENID, THUID = THUID)
            wxuser.save()
        # 更新VOLUNTEER表
        try:
            volunteer = VOLUNTEER.objects.select_for_update().get(THUID=THUID)
        except:
            volunteer = VOLUNTEER(THUID = THUID, NAME = thuuser["name"], DEPARTMENT=thuuser["department"], EMAIL=thuuser["mail"], NICKNAME = thuuser["name"])
            volunteer.save()
        jsonData = {
            "THUID":volunteer.THUID,
            "NAME": volunteer.NAME,
            "DEPARTMENT": volunteer.DEPARTMENT,
            "NICKNAME": volunteer.NICKNAME,
            "SIGNATURE": volunteer.SIGNATURE,
            "PHONE": volunteer.PHONE,
            "VOLUNTEER_TIME": volunteer.VOLUNTEER_TIME,
            "EMAIL": volunteer.EMAIL
        }

        return JsonResponse(jsonData)
    else:
        return HttpResponse("Unable to bind for PC client", status=401)

def volunteerChangeInfo(request):
    '''
    志愿者修改个人信息
    '''
    sessionValidInfo = checkSessionValid(request)
    print(sessionValidInfo)
    if not sessionValidInfo[0]:
        return HttpResponse("You need to login!", status=401)
    THUID = sessionValidInfo[1]
    if THUID is None:
        return HttpResponse("Failed to get THUID!", status=404)
    MODIFIABLE_PROPS = ["NICKNAME","SIGNATURE","PHONE","EMAIL"]
    try:
        print("xixixi")
        info = VOLUNTEER.objects.select_for_update().get(THUID=THUID)
        body = json.loads(request.body)
        print("hhh")
        print(body)
        client_type = request.META['HTTP_USER_AGENT']
        if "MicroMessenger" in client_type:
            key = body["key"]
            if key.upper() in MODIFIABLE_PROPS:
                setattr(info, key.upper(), body["value"])
            info.save()
        else:
            for key in body.keys():
                if key.upper() in MODIFIABLE_PROPS:
                    setattr(info, key.upper(), body[key])
            info.save()
        return HttpResponse("OPERATION SUCCESS", status=200)
    except:
        return HttpResponse("OPERATION FAILED", status=404)

# 注册团体账号
def createUser(request):
    # setuptime = json.loads(request.body)["setuptime"]
    login_name = json.loads(request.body)["username"]
    pwd = json.loads(request.body)["password"]
    code = json.loads(request.body)["code"]
    # pwd = get_hash(pwd)
    # identity = json.loads(request.body)["identity"] # identity = 0 or 1
    identity = 0
    try:
        VerificationCode.objects.select_for_update().get(VerificationCode=code)
        try:
            user = User.objects.create_user(username = login_name, password = pwd)
            user.save()
            UserIdentity(isTeacher = identity,user=user).save()
            #userIdentity = UserIdentity(isTeacher = 0,)
            login(request, user)
            return HttpResponse("CREATE USER SUCCESS",status = 200)
        except:
            traceback.print_exc()
            return HttpResponse("CREATE USER FAIL", status = 404)
    except:
        return HttpResponse("Unvalid code!", status = 404)

# 创建团队
def createGroup(request):
    # name = json.loads(request.body)["name"]              #账户名
    groupname = json.loads(request.body)["name"]    #团队名
    time = json.loads(request.body)["setuptime"]
    phonenumber = json.loads(request.body)["phone"]
    email = json.loads(request.body)["email"]
    about = json.loads(request.body)["about"]
    members = json.loads(request.body)["members"]
    
    #membersname = json.dumps(json.loads(request.body)["membersname"])
    #subjects = json.dumps(json.loads(request.body)["subjects"])

    try:
        #user = User.objects.select_for_update().get(username = name)
        user = request.user
        user_identity = UserIdentity.objects.select_for_update().get(user=user)
        user_identity.isTeacher = 2
        user_identity.setuptime = time
        user_identity.groupname = groupname
        user_identity.email = email
        user_identity.phone = phonenumber
        user_identity.about = about
        user_identity.members = json.dumps(members)
        user_identity.status = 1
        user_identity.save()
        return HttpResponse("Create group success",status = 200)
    except:
        traceback.print_exc()
        return HttpResponse("Create group fail", status = 404)

# 修改团队信息
def editGroup(request):
    if checkUserType(request) == PERMISSION_CONST['ORGANIZATION']:
        group = UserIdentity.objects.select_for_update().get(user = request.user)
        group.phone = json.loads(request.body)["phone"]
        group.email = json.loads(request.body)["email"]
        group.about = json.loads(request.body)["about"]
        group.status = 1
        group.save()
        return HttpResponse("Edit group success",status = 200)
    else:
        return HttpResponse("Edit group fail", status = 404)


def weblogin(request):
    login_name = json.loads(request.body)["username"]
    pwd = json.loads(request.body)["password"]
    pwd = get_hash(pwd)
    user = authenticate(request, username= login_name, password = pwd)
    try:
        login(request, user)
        request.session[LOGGED_IN_CONST] = True
        return HttpResponse("LOGIN SUCCESS", status = 200)
    except:
        request.session[LOGGED_IN_CONST] = False
        return HttpResponse("LOGIN FAILED", status = 404)

# 生成注册团体账号的邀请码
def generateVerificationCode(request):
    if checkUserType(request) in [PERMISSION_CONST['TEACHER']]:
        str_list = [random.choice(string.digits + string.ascii_letters) for i in range(20)]
        random_str = ''.join(str_list)
        code = VerificationCode(VerificationCode = random_str)
        print("code:",random_str)
        code.save()
        return JsonResponse({"code":random_str})
    else:
        print("type",checkUserType(request))
        return HttpResponse("You have no access", status = 401)

# 志愿中心账号获取团体账号列表
def selectfromGroup(request):
    if checkUserType(request) in [PERMISSION_CONST['TEACHER']]:
        rtn_list = []
        for group in UserIdentity.objects.select_for_update().filter(isTeacher=2, status = 1):
            rtn = {}
            # group = UserIdentity.objects.select_for_update().get(id = groupid)
            rtn["groupname"] = group.groupname              #团队名
            setuptime = group.setuptime
            if 'T' in setuptime:
                setuptime = setuptime.split('T')[0]
            else:
                setuptime = setuptime[:10]
            rtn["setuptime"] = setuptime
            rtn["phone"] = group.phone
            rtn["email"] = group.email
            rtn["about"] = group.about
            members = group.members
            if not members:
                members = '[]'
            rtn["members"] = json.loads(members)
            rtn_list.append(rtn)
        return JsonResponse({"groups":rtn_list})
    else:
        return HttpResponse("You have no access", status = 401)

# 网页端登出
def managerLogoutApi(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponse("LOGOUT SUCCESS")

#志愿中心选择待审核的志愿团体账号
def selectGroup(request):
    if checkUserType(request) in [PERMISSION_CONST['TEACHER']]:
        groupid = json.loads(request.body)["id"]

        rtn = {}
        group = UserIdentity.objects.select_for_update().get(id = groupid)
        rtn["groupname"] = group.groupname              #团队名
        rtn["setuptime"] = group.setuptime
        rtn["phone"] = group.phone
        rtn["email"] = group.email
        rtn["about"] = group.about
        rtn["membersname"] = group.membersname
        rtn["subjects"] = group.subjects

        return JsonResponse(rtn)
    else:
        return HttpResponse("You have no access", status = 401)

#志愿中心决定某个志愿团体的注册是否通过
def auditGroup(request):
    if checkUserType(request) in [PERMISSION_CONST['TEACHER']]:
        groupid = json.loads(request.body)["id"]
        result = json.loads(request.body)["result"] #审核结果,-1表示不通过,1表示通过
         
        group = UserIdentity.objects.select_for_update().get(id = groupid)
        group.update(status = result)
        group.save()
        return HttpResponse("Audit group successful", status = 200)
    else:
        return HttpResponse("You have no access", status = 401)

# 查看志愿工时（志愿者）
def check_volunteerhours(request):
    if checkUserType(request) != PERMISSION_CONST['VOLUNTEER']:
        return JsonResponse({"success": False, FAIL_INFO_KEY: "Only logged-in volunteer can check volunteer hours!"})
    THUID = checkSessionValid(request)[1]
    if THUID is None:
        return JsonResponse({"success": False, FAIL_INFO_KEY: "Fail to get THUID!"})
    user = VOLUNTEER.objects.select_for_update().get(pk = THUID)
    hours = user.VOLUNTEER_TIME

    return JsonResponse({"hours": hours})


def getGroupInfo(request):
    '''
    志愿团体获取团体账号信息
    '''
    usertype = checkUserType(request)
    if usertype != PERMISSION_CONST["ORGANIZATION"]:
        return HttpResponse("NOT ORGANIZATION", status=401)
    else:
        user = request.user
        info = UserIdentity.objects.select_for_update().get(user=user)
        res = {}
        setuptime = info.setuptime
        if 'T' in setuptime:
            setuptime = setuptime.split('T')[0]
        else:
            setuptime = setuptime[:10]
        res["setuptime"] = setuptime
        res["groupname"] = info.groupname
        res["email"] = info.email
        res["phone"] = info.phone
        res["about"] = info.about
        res["members"] = json.loads(info.members)
        return JsonResponse(res)