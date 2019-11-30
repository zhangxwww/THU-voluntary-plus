from django.db import models
from django.contrib.auth.models import AbstractUser
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
    PHONE = models.IntegerField(blank=True, null=True)
    TIME = models.FloatField(default=0)
    EMAIL = models.TextField()
    #AVATAR = 

class Managers(AbstractUser):
    Identity = models.IntegerField(verbose_name='身份', blank=True, null=True)  # 0 表示老师， 1表示志愿团体

    def __str__(self):
        return self.username