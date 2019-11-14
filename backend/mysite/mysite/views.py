from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth import login
from .settings import TICKET_AUTHENTICATION, WX_TOKEN_HEADER, WX_OPENID_HEADER, WX_CODE_HEADER, WX_HTTP_API, \
    WX_APPID, WX_SECRET, SESSION_ID_COL
from mysite.models import WX_OPENID_TO_THUID
import requests
import json

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

def loginApi(request):
    '''
    登陆接口
    '''
    client_type = request.session.get('MicroMessenger')
    if client_type == '': # Case 1: 微信端，POST请求
        if WX_CODE_HEADER in request.META.keys(): # 处理code
            code = request.POST[WX_CODE_HEADER]
            r = requests.post(WX_HTTP_API,data={"appid":WX_APPID, "secret":WX_SECRET, "js_code":code, "grant_type":"authorization_code"})
            res = json.loads(r.text)
            if res["errcode"] == 0:
                request.session[SESSION_ID_COL]=res["openid"]
                # 检查有没有绑定
                try:
                    record = WX_OPENID_TO_THUID.objects.get(OPENID = res["openid"])
                    THUID = record.THUID
                    return JsonResponse({"THUID":THUID})
                except:
                    return JsonResponse({"THUID":"Not binded"})
            else:
                return HttpResponse(status=404)
    else: # Case2: PC端，GET请求
        if request.user.is_authenticated: # 防止同一客户端未注销后再次发出登录请求
            return HttpResponse("You've already logged in!")
        ip = get_client_ip(request).replace('.','_')
        r = requests.get(TICKET_AUTHENTICATION+request.GET.get("ticket")+'/'+ip)
        r = parseUserInfoFromTHUAuthentication(r.text)
        login(request, r["zjh"])
        return JsonResponse(json.dumps(r), safe=False)

def bindApi(request):
    #id = request.session.get('sessionid')
    client_type = request.session.get('MicroMessenger')
    if client_type != '':
        OPENID = request.session.get('OPENID')
        wxuser = WX_OPENID_TO_THUID.objects.get(OPENID=OPENID)
        TOKEN = request.POST[WX_TOKEN_HEADER]
        url = "https://alumni-test.iterator-traits.com/fake-id-tsinghuaproxy/api/user/session/token"
        data = {"token": TOKEN}
        r = requests.POST(url, data)
        js = json.loads(r.text)
        thuuser = js["user"]
        THUID = thuuser["card"]
        wxuser.update(THUID = THUID)
        wxuser.save()
        return HttpResponse('',status=200)
    else:
        return HttpResponse("Unable to bind", status=401)

