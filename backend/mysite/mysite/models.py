from django.db import models
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