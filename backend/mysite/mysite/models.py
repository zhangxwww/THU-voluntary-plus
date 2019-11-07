from django.db import models
from datetime import datetime, timedelta
from .settings import WX_TOKEN_TO_OPENID_EXPIRE_TIMEDELTA

class WX_OPENID_TO_THUID(models.Model):
    OPENID = models.TextField(primary_key=True)
    THUID = models.TextField(unique=True)