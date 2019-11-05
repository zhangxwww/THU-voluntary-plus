from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .settings import REDIRECT_TO_LOGIN, REDIRECT_TO_TICKET_AUTHENTICATION
import requests

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def redirectToTHUAuthentication(request):
    if request.user.is_authenticated: # 防止同一客户端未注销后再次发出登录请求
        raise NotImplementedError
    return HttpResponseRedirect(REDIRECT_TO_LOGIN)

def loginApi(request, ticket:str):
    '''
    登陆接口
    '''
    if request.user.is_authenticated: # 防止同一客户端未注销后再次发出登录请求
        raise NotImplementedError
    ip = get_client_ip(request).replace('.','_')
    r = requests.get(REDIRECT_TO_TICKET_AUTHENTICATION+ticket+'/'+ip)
    print(r.text)
    

    
    

    