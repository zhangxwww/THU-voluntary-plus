"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.views.generic.base import RedirectView
from django.urls import path, re_path
from . import views
import showactivity.views as showactivity_views

favicon_view = RedirectView.as_view(url='static/favicon.ico', permanent=True)

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'api/redirectToTHUAuthentication', views.redirectToTHUAuthentication, name="THUAuthentication"),
    path(r'api/login', views.loginApi, name="login"),
    path(r'login.do', views.loginApi),

    path(r'api/weblogin',views.weblogin, name="weblogin")

    path(r'api/bind', views.bindApi),
    path(r'api/volunteer/changeInfo', views.volunteerChangeInfo),

    path(r'api/activities/postactivity', showactivity_views.post_activity),
    
    path(r'api/activities/list', showactivity_views.catalog_grid),

    
    path(r'api/acrivities/detail',showactivity_views.activity_detail),
    #path(r'api/activities/search', showactivity_views.search),
    path(r'api/activities/post', showactivity_views.post_activity),
    #path(r'api/activities/register', showactivity_views.register_activity),
    #path(r'api/activities/cancelregistration', showactivity_views.cancel_registration),

    #path(r'api/messages/list', showactivity_views.message_catalog_grid),
    #path(r'api/messages/detail',showactivity_views.read_message),
    #path(r'api/messages/mark',showactivity_views.mark_read),
    #path(r'api/messages/delete',showactivity_views.delete_message),
]
