from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth import login
from .settings import TICKET_AUTHENTICATION, WX_TOKEN_HEADER, WX_OPENID_HEADER
import requests
import json

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

def loginApi(request):
    '''
    登陆接口
    '''
    if WX_OPENID_HEADER in request.META.keys(): # Case1: 微信端，POST请求，需要维护token和openid的对应关系、openid和学号的对应关系
        TOKEN = request.POST[WX_TOKEN_HEADER]
        OPENID = request.POST[WX_OPENID_HEADER]
        '''
        检查是否数据库中存了相应OPENID到学号的映射。

        若存了相应OPENID，说明已经绑定；

        若未存相应OPENID到学号的映射，说明未绑定，检查是否request header里有token：
        有的话就和助教服务器后端通讯，若确认token有效就保存openid和学号的关系；
        若token无效或者header里没token，返回错误信息提示用户重新绑定

        注意openid对同一用户使用同一小程序是不变的，不会过期
        '''
        raise NotImplementedError
    else: # Case1: PC端，GET请求
        if request.user.is_authenticated: # 防止同一客户端未注销后再次发出登录请求
            return HttpResponse("You've already logged in!")
        ip = get_client_ip(request).replace('.','_')
        r = requests.get(TICKET_AUTHENTICATION+request.GET.get("ticket")+'/'+ip)
        r = parseUserInfoFromTHUAuthentication(r.text)
        login(request, r["zjh"])
        return JsonResponse(json.dumps(r), safe=False)

    
    

    