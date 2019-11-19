from django.db import models
from datetime import datetime, timedelta

class WX_OPENID_TO_THUID(models.Model):
    OPENID = models.TextField(primary_key=True)
    THUID = models.TextField(unique=True)
