from rest_framework.views import APIView,Response
from ..models import Diary,User
import time
from ..serializersAll import Ds
import os
import json


class DiaryManagement(APIView):
    def post(self,request):
        post_data = request.data
        openId = post_data.get('openId')
        user = User.objects.filter(openId=openId).first()
        if not user:
            return Response({'msg':'用户不存在'})
        post_data.pop('openId')
        add_time = time.localtime(int(post_data['writeTime']) / 1000)
        writeTime = time.strftime('%Y-%m-%d %H:%M:%S', add_time)
        post_data['writeTime'] = writeTime
        post_data['user'] = int(user.id)
        diary = Ds(data=post_data)
        if diary.is_valid():
            diary.save()
            print('通过')
        else:
            print('不通过')
        diaryId = Diary.objects.filter(user_id=user.id,writeTime=writeTime).first().id
        return Response({'diaryId': diaryId})


class VideoManagement(APIView):
    def post(self,request):
        post_data = request.data
        print(post_data)
        openId = post_data.get('openId')
        videoName = post_data.get('name')
        video = post_data.get(videoName)
        videoHouZhui = str(video).split('.')[1]
        judge = os.path.exists(f'static/user/{openId}/video')
        if not judge:
            os.makedirs(f'static/user/{openId}/video')
        src = f'static/user/{openId}/video/{videoName}'+'.'+videoHouZhui
        diaryId = int(post_data.get('diaryId'))
        diary = Diary.objects.filter(id=diaryId).first()
        oldVideo = Ds(instance=diary).data.get('video')
        if oldVideo:
            srcList = json.loads(oldVideo)
            srcList.append(src)
            srcList = json.dumps(srcList)
        else:
            srclist = []
            srclist.append(src)
            srcList = json.dumps(srclist)
            print(srcList)
        diary = Ds(instance=diary,data={'video':srcList},partial=True)
        if diary.is_valid(raise_exception=True):
            diary.save()
        with open(src,mode='wb') as f:
            for i in video:
                f.write(i)
        return Response({'msg':'成功'})


class ImageManagement(APIView):
    def post(self,request):
        post_data = request.data
        print(post_data)
        openId = post_data.get('openId')
        imageName = post_data.get('name')
        video = post_data.get(imageName)
        imageHouZhui = str(video).split('.')[1]
        judge = os.path.exists(f'static/user/{openId}/image')
        if not judge:
            os.makedirs(f'static/user/{openId}/image')
        src = f'static/user/{openId}/image/{imageName}'+'.'+imageHouZhui
        diaryId = int(post_data.get('diaryId'))
        diary = Diary.objects.filter(id=diaryId).first()
        oldImage = Ds(instance=diary).data.get('image')
        if oldImage:
            srcList = json.loads(oldImage)
            srcList.append(src)
            srcList = json.dumps(srcList)
        else:
            srclist = []
            srclist.append(src)
            srcList = json.dumps(srclist)
            print(srcList)
        diary = Ds(instance=diary,data={'image':srcList},partial=True)
        if diary.is_valid(raise_exception=True):
            diary.save()
        with open(src,mode='wb') as f:
            for i in video:
                f.write(i)
        return Response({'msg':'成功'})