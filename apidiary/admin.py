from django.contrib import admin

# Register your models here.
from .models import User,Diary
# 将表配置在admin里面
admin.site.register(User)
admin.site.register(Diary)
