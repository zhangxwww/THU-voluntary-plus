from django.db import models

# Create your models here.
class Message(models.Model):
    """
    活动消息
    """
    MessageId = models.AutoField(primary_key=True, verbose_name='消息ID')
    #ReadOrNot = models.ManyToManyField(WX_OPENID_TO_THUID)
    ActivityNumber = models.ForeignKey(Activity, to_field='ActivityNumber', verbose_name='活动编号')
    THUID = models.ForeignKey(User,to_field='THUID',verbose_name='用户学号')
    
class Activity(models.Model):
    """
    活动信息
    """
    ActivityNumber = models.CharField(max_length=50, primary_key=True, verbose_name='活动编号')
    ActivityName = models.CharField(max_length=255, unique=True, verbose_name='活动名称')
    ActivityTime = models.CharField(verbose_name='活动时间')
    ActivityOrganizer = models.CharField(max_length=255, null=True, blank=True, verbose_name='发起者')
    ActivityIntro = models.TextField(null=True, blank=True, verbose_name='活动介绍')
    ActivityRemain = models.IntegerField(default=0, verbose_name='剩余名额')
    IsFull = models.IntegerField(default=0, verbose_name='是否报满')
    IsOverDeadline = models.IntegerField(default=0, verbose_name='是否截止报名') # 1 for unable to sign up
    Intro_pic = models.ImageField(null=True, blank=True, verbose_name='介绍图片')
    Category = models.CharField(null=True, blank=True, max_length=20, verbose_name='分类')
    ReleaseDate = models.DateTimeField(null=True, verbose_name='发布日期')
    #ReadOrNot = models.ManyToManyField(WX_OPENID_TO_THUID)

    def __str__(self):
        return '{}({})'.format(self.ActivityName, self.ActivityNumber)

    class Meta:
        verbose_name = "活动信息"
        verbose_name_plural = verbose_name
#
class ActivityPic(models.Model):
    """活动所有的描述图片"""
    PicId = models.AutoField(primary_key=True, verbose_name='图片ID')
    ActivityNumber = models.ForeignKey(Activity, to_field='ActivityNumber', verbose_name='活动编号')
    ActivityPic = models.ImageField(verbose_name='文件名')

    def __str__(self):
        return '{}({})'.format(self.ActivityNumber.ActivityName, self.ActivityPic)

    class Meta:
        verbose_name = "活动图像"
        verbose_name_plural = verbose_name

class WX_OPENID_TO_THUID(models.Model) :
    """
    微信绑定学号
    """
    OPENID = models.TextField(primary_key=True)
    THUID = models.TextField(unique=True)

class User(models.Model):
    """
    用户
    """
    THUID = models.TextField(primary_key=True)