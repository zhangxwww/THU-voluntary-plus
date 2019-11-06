from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth import login
from .settings import TICKET_AUTHENTICATION
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
    if request.user.is_authenticated: # 防止同一客户端未注销后再次发出登录请求
        return HttpResponse("You've already logged in!")
    ip = get_client_ip(request).replace('.','_')
    r = requests.get(TICKET_AUTHENTICATION+request.GET.get("ticket")+'/'+ip)
    r = parseUserInfoFromTHUAuthentication(r.text)
    login(request, r["zjh"])
    return JsonResponse(json.dumps(r), safe=False)

    
    

    