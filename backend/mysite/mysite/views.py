from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth import login
from .settings import TICKET_AUTHENTICATION, WX_TOKEN_HEADER, WX_OPENID_HEADER, WX_CODE_HEADER, WX_HTTP_API, \
    WX_APPID, WX_SECRET, REDIRECT_TO_LOGIN
from .models import WX_OPENID_TO_THUID
import requests
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.sessions.backends.db import SessionStore


THUID_CONST="THUID"
TOKEN_CONST="TOKEN"
OPENID_CONST="OPENID"
SUCCESS_CONST="SUCCESS"

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

def checkSessionExpiry(request):
    print('Session expiry date: ')
    print(request.session.get_expiry_date())

def loginApi(request):
    '''
    登陆接口
    '''
    client_type = request.META['HTTP_USER_AGENT']
    
    if "MicroMessenger" in client_type: # Case 1: 微信端，POST请求
        print(request)
        print(request.META.keys())
        jsonBody = json.loads(request.body)
        if WX_CODE_HEADER in jsonBody.keys(): # 处理code
            code = jsonBody[WX_CODE_HEADER]
            r = requests.post(WX_HTTP_API,data={"appid":WX_APPID, "secret":WX_SECRET, "js_code":code, "grant_type":"authorization_code"})
            res = json.loads(r.text)
            print(res)
            if ("errcode" not in res.keys()) or (res["errcode"] == 0):
                request.session[OPENID_CONST]=res["openid"]
                # 检查有没有绑定
                try:
                    record = WX_OPENID_TO_THUID.objects.get(OPENID = res["openid"])
                    THUID = record.THUID
                    return JsonResponse({"THUID":THUID})
                except:
                    return JsonResponse({"THUID":"Not binded"})
            else:
                return HttpResponse(status=404)
        else:
            return HttpResponse("not found WX_CODE_HEADER",status=404)
    else: # Case2: PC端，GET请求
        if request.user.is_authenticated: # 防止同一客户端未注销后再次发出登录请求
            return HttpResponse("You've already logged in!")
        ip = get_client_ip(request).replace('.','_')
        r = requests.get(TICKET_AUTHENTICATION+request.GET.get("ticket")+'/'+ip)
        r = parseUserInfoFromTHUAuthentication(r.text)
        login(request, r["zjh"])
        return JsonResponse(json.dumps(r), safe=False)

def bindApi(request):
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
        print(request.body)
        TOKEN = json.loads(request.body)[WX_TOKEN_HEADER]
        url = "https://alumni-test.iterator-traits.com/fake-id-tsinghua-proxy/api/user/session/token"
        data = {"token": TOKEN}
        r = requests.post(url, data)
        r = json.loads(r.text)
        print(r)
        thuuser = r["user"]
        THUID = thuuser["card"]
        if alreadyBinded:
            wxuser = WX_OPENID_TO_THUID(OPENID=OPENID)
            wxuser.update(THUID = THUID)
            wxuser.save()
        else:
            wxuser = WX_OPENID_TO_THUID(OPENID=OPENID, THUID = THUID)
            wxuser.save()
        print(THUID)
        return HttpResponse('',status=200)
    else:
        return HttpResponse("Unable to bind", status=401)

