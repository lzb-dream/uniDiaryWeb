# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


# class Users(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     nickname = models.CharField(max_length=255)
#     head_portrait = models.CharField(db_column='Head_portrait', max_length=255)  # Field name made lowercase.
#     open_id = models.CharField(max_length=255)
#     add_time = models.CharField(max_length=255)
#     update_time = models.CharField(max_length=255)
#     diary_background = models.CharField(max_length=255)
#     personal_background = models.CharField(max_length=255)
#     read_diary_background = models.CharField(max_length=255)
#
#     class Meta:
#         managed = True
#         db_table = 'users'
#
#
# class Diarys(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     nickname = models.CharField(max_length=255)
#     head_portrait = models.CharField(db_column='Head_portrait', max_length=255)  # Field name made lowercase.
#     open_id = models.CharField(max_length=255)
#     diary = models.TextField()
#     mood = models.CharField(max_length=20)
#     weather = models.CharField(max_length=20)
#     praise = models.IntegerField()
#     no_praise = models.IntegerField()
#     flowers = models.IntegerField()
#     share_status = models.SmallIntegerField()
#     add_time = models.CharField(max_length=255)
#     update_time = models.CharField(max_length=255)
#     addressname = models.CharField(max_length=255)
#     detailaddress = models.CharField(max_length=255)
#     image = models.CharField(max_length=255)
#     video = models.CharField(max_length=255)
#
#     class Meta:
#         # 允许操作表
#         managed = True
#         db_table = 'diarys'

class User(models.Model):
    nickName = models.CharField(max_length=20)
    openId = models.CharField(max_length=255,unique=True)
    addTime = models.DateTimeField()
    updateTime = models.DateTimeField(blank=True,null=True)
    headPortrait = models.CharField(max_length=255,default='static/heard.png')
    diaryPassword = models.IntegerField(null=True)
    state = models.BooleanField(default=True)
    flowers = models.IntegerField(default=0)
    praise = models.IntegerField(default=0)
    money = models.DecimalField(default=0,decimal_places=2,max_digits=6)
    diaryNumber = models.IntegerField(default=0)

    def __str__(self):
        return self.nickName

    class Meta:
        managed = True
        db_table = 'user'
        verbose_name = '用户'
        verbose_name_plural = verbose_name


class Diary(models.Model):
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    diary = models.TextField()
    video = models.TextField(blank=True)
    videoPhoto = models.TextField(blank=True)
    image = models.TextField(blank=True)
    writeTime = models.DateTimeField()
    updateTime = models.DateTimeField(null=True,blank=True)
    mood = models.CharField(max_length=10)
    weather = models.CharField(max_length=10)
    address = models.CharField(max_length=255,blank=True)
    thumbUpNumber = models.IntegerField(default=0)
    flowerCount = models.IntegerField(default=0)
    squareSwitch = models.BooleanField(default=False)

    def __str__(self):
        return self.user.nickName

    class Meta:
        managed = True
        db_table = 'diary'
        verbose_name = '用户日记'
        verbose_name_plural = verbose_name


# class Image(models.Model):
#     diary = models.ForeignKey(Diary,on_delete=models.DO_NOTHING)
#     addTime = models.DateTimeField(null=True)
#     src = models.CharField(max_length=255)
#
#     class Meta:
#         managed = True
#         db_table = 'image'
#         verbose_name = '日记图片'
#         verbose_name_plural = verbose_name
#
#
# class Video(models.Model):
#     diary = models.ForeignKey(Diary,on_delete=models.DO_NOTHING)
#     addTime = models.DateTimeField(null=True)
#     src = models.CharField(max_length=255)
#
#     def __str__(self):
#         id = Diary.objects.filter(id=self.diary_id).first().user_id
#         return User.objects.filter(id = id).first().nickName
#
#     class Meta:
#         managed = True
#         db_table = 'video'
#         verbose_name = '用户视频'
#         verbose_name_plural = verbose_name