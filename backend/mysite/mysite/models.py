from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from datetime import datetime, timedelta

class WX_OPENID_TO_THUID(models.Model):
    OPENID = models.CharField(max_length=100, primary_key=True)
    THUID = models.IntegerField()

class VOLUNTEER(models.Model):
    THUID = models.IntegerField(primary_key=True)
    NAME = models.CharField(max_length=100)
    DEPARTMENT = models.TextField()
    NICKNAME = models.CharField(max_length=100)
    SIGNATURE = models.TextField()
    PHONE = models.TextField()
    VOLUNTEER_TIME = models.FloatField(default=0)
    EMAIL = models.TextField()
    #AVATAR = 

class UserManager(BaseUserManager):
    def _create_user(self , Identity, username, password, **kwargs):
        if not Identity:
            raise  ValueError("必须要确认用户身份！")
        if not password:
            raise  ValueError("必须输入密码！")
        user = self.model( Identity = Tdentity, username= username , **kwargs)
        user.set_password( password )
        user.save()
        return user

    def create_user(self,  telephone, username, password, **kwargs):
        kwargs['is_superuser'] = False
        return self._create_user( telephone = telephone, username=username, password = password, **kwargs )

    def create_superuser(self, telephone, username, password, **kwargs):
        kwargs['is_superuser'] = True
        return  self._create_user( telephone = telephone, username=username, password = password, **kwargs )

class User(AbstractUser):  # 老师或志愿团体
    Identity = models.IntegerField(verbose_name='身份', blank=True, null=True)  # 0 表示老师， 1表示志愿团体

    #USERNAME_FIELD = "Identity"

    objects = UserManager()
