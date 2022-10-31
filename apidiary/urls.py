from django.urls import path
from .views.login import UserManagement
from .views.saveDiary import DiaryManagement,VideoManagement,ImageManagement
urlpatterns = [
    path('',UserManagement.as_view()),
    path('diary', DiaryManagement.as_view()),
    path('videoManagement',VideoManagement.as_view()),
    path('imageManagement',ImageManagement.as_view())
]
