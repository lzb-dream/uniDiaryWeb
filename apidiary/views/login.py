from rest_framework.views import Response,APIView
from ..serializersAll import Us,User
import requests
import os
import time


class UserManagement(APIView):
    # 用户登录或新增用户
    def get(self,request):
        get_data = request.query_params
        try:
            js_code = get_data['js_code']
            add_time = time.localtime(int(get_data['addTime']) / 1000)
            addTime = time.strftime('%Y-%m-%d %H:%M:%S', add_time)
            nickName = get_data['nickName']
            headPortrait = get_data['headPortrait']
            code = requests.get(url=f'https://api.weixin.qq.com/sns/jscode2session?appid=wx08afdb587195d891&secret=f618055699c8fc45c3a6d32a10dfa7e8&js_code={js_code}&grant_type=authorization_code').json()
            openId = code['openid']
            oldUser = User.objects.filter(openId=openId)
            print(oldUser)
            if not oldUser:
                print('这是一个新用户')
                data = {'openId':openId,'addTime':addTime,'nickName':nickName,'headPortrait':headPortrait}
                u = Us(data=data)
                if u.is_valid(raise_exception=True):
                    u.save()
                user = User.objects.filter(openId=openId)[0].__dict__
                user.pop('_state')
            else:
                print('用户已经存在')
                user = oldUser[0].__dict__
                user.pop('_state')
            return Response(user)
        except Exception:
            return Response({'errormsg':'请求失败'},status=500)

    def post(self, request):
        post_data = request.data
        openId = post_data.get('openId')
        nickName = post_data.get('nickName')
        updateTime = post_data.get('addTime')
        identify = post_data.get('identify')
        print(identify)
        print(openId, nickName, updateTime)
        user = User.objects.filter(openId=openId).first()
        print(user)
        if not user:
            return Response({'msg': '用户不存在'},status=500)
        if identify == 'image':
            judge = os.path.exists(f'static/user/{openId}/headPortrait')
            if not judge:
                os.makedirs(f'static/user/{openId}/headPortrait')
            file = post_data.get(openId+updateTime)
            image_houzhui = str(file).split('.')[1]
            fileName = openId+updateTime+'.'+image_houzhui
            fileName = f'static/user/{openId}/headPortrait/{fileName}'
            print(fileName)
            with open(fileName,mode='wb') as f:
                for i in file:
                    f.write(i)
            updateTime = time.localtime(int(updateTime) / 1000)
            updateTime = time.strftime('%Y-%m-%d %H:%M:%S', updateTime)
            userS = Us(instance=user,data={'headPortrait':f'http://127.0.0.1:8000/{fileName}', 'updateTime':updateTime}, partial=True)
            if userS.is_valid(raise_exception=True):
                userS.save()
        elif identify == 'nickName':
            updateTime = time.localtime(int(updateTime) / 1000)
            updateTime = time.strftime('%Y-%m-%d %H:%M:%S', updateTime)
            print(updateTime)
            userS = Us(instance=user,data={'nickName':nickName,'updateTime':updateTime},partial=True)
            if userS.is_valid(raise_exception=True):
                userS.save()
        return Response({'msg': 'ok'})

