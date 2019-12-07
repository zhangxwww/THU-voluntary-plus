from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth import login
from django.contrib.auth import  authenticate
from django.contrib.auth.models import User
from .settings import TICKET_AUTHENTICATION, WX_TOKEN_HEADER, WX_OPENID_HEADER, WX_CODE_HEADER, WX_HTTP_API, \
    WX_APPID, WX_SECRET, REDIRECT_TO_LOGIN
from .models import WX_OPENID_TO_THUID, VOLUNTEER, UserIdentity
#User, UserManager
import requests
import json
from django.contrib.sessions.backends.db import SessionStore
import datetime 
from django.utils.timezone import utc
import hashlib
import traceback


THUID_CONST="THUID"
TOKEN_CONST="TOKEN"
OPENID_CONST="OPENID"
SUCCESS_CONST="SUCCESS"
LOGGED_IN_CONST="LOGGED_IN"

def get_hash(s):
    hash = hashlib.sha256()
    hash.update(s.encode('utf-8'))
    return hash.hexdigest()

def redirectToTHUAuthentication(request):
    #TODO: 防止同一客户端未注销后再次发出登录请求
    if False:
        raise NotImplementedError
    return HttpResponseRedirect(REDIRECT_TO_LOGIN)

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def parseUserInfoFromTHUAuthentication(text):
    parsed = {}
    for r in text.split(':'):
        prop = r.split('=')[0]
        value = r.split('=')[1]
        parsed[prop] = value
    return parsed

def getOpenID(request):
    raise NotImplementedError

def validateToken(token, openid):
    raise NotImplementedError
    return {SUCCESS_CONST:True, THUID_CONST:"2016110011"}   

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
                    record = WX_OPENID_TO_THUID.objects.get(OPENID = s[OPENID_CONST])
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


'''
def getStudentID(request):
    
    #获取学号，调用此函数前应调用checkSessionValid函数检查登录状态
    #若获取成功则返回学号，否则返回None
    
    client_type = request.META['HTTP_USER_AGENT']
    if "MicroMessenger" in client_type:
        try:
            sessionid = request.META["HTTP_SET_COOKIE"].split("=")[1]
            OPENID = SessionStore(session_key=sessionid)[OPENID_CONST]
            record = WX_OPENID_TO_THUID.objects.get(OPENID = OPENID)
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
                    THUID = WX_OPENID_TO_THUID.objects.get(OPENID = res["openid"]).THUID
                except:
                    THUID = None
                print(THUID)
                # 检查有没有绑定
                if THUID is not None:
                    volunteer = VOLUNTEER.objects.get(THUID=THUID)
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
            VOLUNTEER.objects.get(THUID=THUID)
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
    if not checkSessionValid(request)[0]:
        return HttpResponse("You need to login!", status=401)
    client_type = request.META['HTTP_USER_AGENT']
    if "MicroMessenger" in client_type: # Case 1: 微信端，POST请求
        sessionid = request.META["HTTP_SET_COOKIE"].split("=")[1]
        s = SessionStore(session_key=sessionid)
        OPENID = s.get('OPENID')
        alreadyBinded = True # 若已经绑定，可以重新绑定
        try:
            wxuser = WX_OPENID_TO_THUID.objects.get(OPENID=OPENID)
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
            volunteer = VOLUNTEER.objects.get(THUID=THUID)
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
        info = VOLUNTEER.objects.get(THUID=THUID)
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

def createUser(request):
    login_name = json.loads(request.body)["username"]
    pwd = json.loads(request.body)["password"]
    pwd = get_hash(pwd)
    # identity = json.loads(request.body)["identity"] # identity = 0 or 1
    identity = 1
    try:
        user = User.objects.create_user(Identity = identity, username = login_name, password = pwd)
        return HttpResponse("CREATE USER SUCCESS",status = 200)
    except:
        return HttpResponse("CREATE USER FAIL", status = 404)

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
