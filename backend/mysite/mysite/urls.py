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
    path(r'admin/', admin.site.urls),
    path(r'api/redirectToTHUAuthentication', views.redirectToTHUAuthentication, name="THUAuthentication"),
    path(r'api/login', views.loginApi, name="login"),
    path(r'api/manager/login', views.managerLoginApi, name="manegerLogin"),
    path(r'login.do', views.loginApi),

    path(r'api/weblogin',views.weblogin, name="weblogin"),
    path(r'api/users/create',views.createUser, name="createUser"),

    path(r'api/bind', views.bindApi),
    path(r'api/volunteer/changeInfo', views.volunteerChangeInfo),

    path(r'api/activities/postactivity', showactivity_views.post_activity),
    
    path(r'api/activities/list', showactivity_views.catalog_grid),

    
    path(r'api/activities/detail',showactivity_views.activity_detail),
    #path(r'api/activities/search', showactivity_views.search),
    path(r'api/activities/post', showactivity_views.post_activity),
    path(r'api/activities/edit',showactivity_views.edit_activity),
    path(r'api/activities/register', showactivity_views.register_activity),
    path(r'api/activities/cancelregistration', showactivity_views.cancel_registration),
    path(r'api/activities/checkin', showactivity_views.checkinApi),

    path(r'api/messages/list', showactivity_views.message_catalog_grid),
    path(r'api/messages/edit', showactivity_views.edit_message),
    #path(r'api/messages/detail',showactivity_views.read_message),
    path(r'api/messages/read',showactivity_views.mark_read),
    path(r'api/messages/delete',showactivity_views.delete_message),
    path(r'api/messages/post', showactivity_views.post_message),

    path(r'api/code/generate', views.generateVerificationCode),
    path(r'api/group/create', views.createGroup),
    path(r'api/group/edit', views.editGroup),
    path(r'api/group/selectfrom',views.selectfromGroup),
    path(r'api/group/select', views.selectGroup),
    path(r'api/group/audit', views.auditGroup),

    path(r'api/volunteerhours/allocate', showactivity_views.allocate_volunteerhours),
    path(r'api/volunteerhpurs/check',views.check_volunteerhours)
]
