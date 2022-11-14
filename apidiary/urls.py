from django.urls import path
from .views.login import UserManagement
from .views.saveDiary import DiaryManagement,VideoManagement,ImageManagement,videoPhotoManagement
urlpatterns = [
    path('userManagement',UserManagement.as_view()),
    path('diary', DiaryManagement.as_view()),
    path('videoManagement',VideoManagement.as_view()),
    path('imageManagement',ImageManagement.as_view()),
    path('videoPhotoManagement',videoPhotoManagement.as_view())
    # path('updateVideo',UpdateVideo.as_view()),
    # path('updateImage',UpdateImage.as_view())
]
