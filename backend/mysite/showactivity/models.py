from django.db import models
from mysite.models import VOLUNTEER, User
# Create your models here.

ENROLL_STATE_CONST = {
    'UNCENSORED': 2323,
    'ACCEPTED': 3434,
    'REJECTED': 4545
}

class Activity(models.Model):
    """
    活动信息
    """
    ActivityName = models.CharField(max_length=255, verbose_name='活动名称')
    ActivityCity = models.CharField(max_length=255,verbose_name='活动城市')
    ActivityLocation = models.CharField(max_length=255,verbose_name='活动地点')
    ActivityStartDate = models.CharField(max_length=255,verbose_name='活动开始日期')
    ActivityEndDate = models.CharField(max_length=255,verbose_name='活动结束日期')
    #ActivityTime = models.CharField(max_length=255,verbose_name='活动时间')
    ActivityOrganizer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='发起者')
    ActivityIntro = models.TextField(null=True, blank=True, verbose_name='活动介绍')
    ActivityTotalAmount = models.IntegerField(default=0, verbose_name='总名额')
    ActivityRemain = models.IntegerField(default=0, verbose_name='剩余名额')
    IsFull = models.IntegerField(default=0, verbose_name='是否报满')
    IsOverDeadline = models.IntegerField(default=0, verbose_name='是否截止报名') # 1 for unable to sign up
    Intro_pic = models.ImageField(null=True, blank=True, verbose_name='介绍图片')
    Tag = models.CharField(null=True, blank=True, max_length=100, verbose_name='标签')
    ReleaseDate = models.DateTimeField(null=True, verbose_name='发布日期')
    ActivityStatus = models.IntegerField(default=0, verbose_name='状态')  # 0 for success, 1 for warning, 2 for danger
    #ReadOrNot = models.ManyToManyField(WX_OPENID_TO_THUID)
    members = models.ManyToManyField(VOLUNTEER, through='Membership', verbose_name='参与者')

    def __str__(self):
        return '{}({})'.format(self.ActivityName, self.ActivityNumber)

    class Meta:
        verbose_name = "活动信息"
        verbose_name_plural = verbose_name

class Membership(models.Model):
    volunteer = models.ForeignKey(VOLUNTEER, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    state = models.IntegerField(default=ENROLL_STATE_CONST["UNCENSORED"])
    alreadyAssignedVolunteerHour = models.BooleanField(default=False)
    comment = models.TextField()

class checkin(models.Model):
    membership = models.ForeignKey(Membership, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longtitude = models.FloatField()
    address = models.TextField()
    checkinTime = models.CharField(max_length=255, verbose_name="签到时间")


class Message(models.Model):
    """
    活动消息
    """
    #MessageId = models.AutoField(primary_key=True, verbose_name='消息ID')
    MessageTitle = models.TextField(null = True, blank = True, verbose_name="消息标题")
    #MessageBriefContent = models.TextField(null = True, blank = True, verbose_name="消息简略内容")
    MessageDetailContent = models.TextField(null = True, blank = True, verbose_name="消息详细内容")
    PostTime = models.TextField(verbose_name="发布时间")
    #ReadOrNot = models.ManyToManyField(WX_OPENID_TO_THUID)
    ActivityNumber = models.ForeignKey(Activity, verbose_name='活动编号', on_delete=models.CASCADE)
    volunteers = models.ManyToManyField(VOLUNTEER, through='MessageReadOrNot', verbose_name='消息接受者')
    #THUID = models.ForeignKey(User,to_field='THUID',verbose_name='用户学号')
    
class MessageReadOrNot(models.Model):
    """
    消息是否被某个用户阅读
    """
    MessageID = models.ForeignKey(Message,verbose_name='消息编号', on_delete=models.CASCADE)
    VolunteerID = models.ForeignKey(VOLUNTEER, verbose_name='用户学号', on_delete=models.CASCADE)
    ReadOrNot = models.BooleanField(default=False, verbose_name='某用户是否阅读该条消息')
   

class ActivityPic(models.Model):
    """活动所有的描述图片"""
    PicId = models.AutoField(primary_key=True, verbose_name='图片ID')
    ActivityId = models.ForeignKey(Activity, verbose_name='活动编号', on_delete=models.CASCADE)
    ActivityPic = models.ImageField(verbose_name='文件名')

    def __str__(self):
        return '{}({})'.format(self.ActivityNumber.ActivityName, self.ActivityPic)

    class Meta:
        verbose_name = "活动图像"
        verbose_name_plural = verbose_name

"""
class User(models.Model):
 
#    用
    THUID = models.TextField(primary_key=True)
    UserName = models.CharField(max_length=255, unique=True, verbose_name='用户姓名')
    Activities = models.ManyToManyField(Activity, blank = True, verbose_name = '参与的活动')
"""



    