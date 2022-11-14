from rest_framework.views import APIView,Response
from ..models import Diary,User
import time
from ..serializersAll import Ds
import os
import json
from .components import conversionTime

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
        print('diaryId标识符',diaryId)
        return Response({'diaryId': diaryId})

    def get(self,request):
        get_data = request.query_params
        userId = get_data.get('userId')
        print('id标识',userId)
        diarys = Diary.objects.filter(user_id=userId).order_by('-id')
        diarys_data = Ds(instance=diarys,many=True)
        return Response({'DiaryManagementMsg':'成功','diarys':diarys_data.data})

    def put(self,request):
        put_data = request.data
        updateTime = put_data.get('updateTime')
        updateTime = conversionTime(updateTime)
        data = put_data.get('data')
        data['updateTime'] = updateTime
        print(data)
        diary = Diary.objects.filter(id=put_data.get('id')).first()

        ds = Ds(instance=diary,data=data,partial=True)
        if ds.is_valid(raise_exception=True):
            ds.save()
        return Response({'msg':'成功'})



class VideoManagement(APIView):
    def post(self,request):
        try:
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
            return Response({'VideoManagementMsg':'成功'})
        except:
            return Response({'VideoManagementMsg':'失败'}, status=500)

class ImageManagement(APIView):
    def post(self,request):
        try:
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
            return Response({'ImageManagementMsg':'成功'})
        except:
            return Response({'ImageManagementMsg':'失败'},status=500)

class videoPhotoManagement(APIView):
    def post(self,request):
        # try:
        post_data = request.data
        print('videoPhotoManagement',post_data)
        openId = post_data.get('openId')
        videoPhotoHouZhuiName = post_data.get('name')

        videoPhoto = post_data.get(videoPhotoHouZhuiName)

        videoPhotoHouZhui = str(videoPhoto).split('.')[1]
        judge = os.path.exists(f'static/user/{openId}/videoPhoto')
        if not judge:
            os.makedirs(f'static/user/{openId}/videoPhoto')
        src = f'static/user/{openId}/videoPhoto/{videoPhotoHouZhuiName}'+'.'+videoPhotoHouZhui
        diaryId = int(post_data.get('diaryId'))
        diary = Diary.objects.filter(id=diaryId).first()
        oldVideoPhoto = Ds(instance=diary).data.get('videoPhoto')
        if oldVideoPhoto:
            srcList = json.loads(oldVideoPhoto)
            srcList.append(src)
            srcList = json.dumps(srcList)
        else:
            srclist = []
            srclist.append(src)
            srcList = json.dumps(srclist)
            print(srcList)
        diary = Ds(instance=diary,data={'videoPhoto':srcList},partial=True)
        if diary.is_valid(raise_exception=True):
            diary.save()
        with open(src,mode='wb') as f:
            for i in videoPhoto:
                f.write(i)
        return Response({'videoPhotoManagementMsg':'成功'})
        # except:
        #     return Response({'videoPhotoManagementMsg':'失败'},status=500)

# class UpdateVideo(APIView):
#     def post(self,request):
#         post_data = request.data
#         id = post_data.get('id')
#         videoList = post_data.get('videoList')
#         videoPhotoList = post_data.get('videoPhotoList')
#         newVideoPhoto = post_data.get('newVideoPhoto')
#         newVideo = post_data.get('newVideo')
#         name = post_data.get('name')
#         print(id,videoList,videoPhotoList,newVideo,newVideoPhoto,name)
#         return Response({'msg': '成功'})
# class UpdateImage(APIView):
#     def post(self,request):
#         print(request.data)
#         return Response({'msg':'成功'})