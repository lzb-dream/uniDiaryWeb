from rest_framework import serializers
from .models import User,Diary


class Us(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nickName = serializers.CharField(max_length=20)
    openId = serializers.CharField(max_length=255)
    addTime = serializers.DateTimeField()
    updateTime = serializers.DateTimeField(required=False)
    headPortrait = serializers.CharField(max_length=255,required=False)
    state = serializers.BooleanField(required=False)
    flowers = serializers.IntegerField(required=False)
    money = serializers.DecimalField(required=False,decimal_places=2,max_digits=4)
    diaryNumber = serializers.IntegerField(required=False)

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        return user

    def update(self, instance, validated_data):
        print(validated_data)
        for key, value in validated_data.items():
            setattr(instance,key,value)
        instance.save()
        return instance

class Ds(serializers.Serializer):
    id = serializers.IntegerField(read_only=True,required=False)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    video = serializers.CharField(allow_blank=True, required=False)
    image = serializers.CharField(allow_blank=True, required=False)
    diary = serializers.CharField()
    writeTime = serializers.DateTimeField()
    updateTime = serializers.DateTimeField(allow_null=True,required=False)
    mood = serializers.CharField(max_length=10)
    weather = serializers.CharField(max_length=10)
    address = serializers.CharField(max_length=255,allow_blank=True)
    thumbUpNumber = serializers.IntegerField(default=0)
    flowerCount = serializers.IntegerField(default=0)
    squareSwitch = serializers.BooleanField(default=False)

    def validate(self, attrs):
        print('全局',attrs)
        return attrs

    def update(self, instance, validated_data):
        print('更新',validated_data)
        for key, value in validated_data.items():
            setattr(instance,key,value)
        instance.save()
        return instance

    def create(self, validated_data):
        diary = Diary.objects.create(**validated_data)
        return diary


# class Vs(serializers.Serializer):
#     diary = serializers.PrimaryKeyRelatedField(queryset=Diary.objects.all())
#     src = serializers.CharField()
#     addTime = serializers.DateTimeField()
#
#     def validate(self, attrs):
#         print('全局',attrs)
#         return attrs
#
#     def update(self, instance, validated_data):
#         print(validated_data)
#         for key, value in validated_data.items():
#             setattr(instance,key,value)
#         instance.save()
#         return instance
#
#     def create(self, validated_data):
#         video = Video.objects.create(**validated_data)
#         return video
#
#
# class Is(serializers.Serializer):
#     diary = serializers.PrimaryKeyRelatedField(queryset=Diary.objects.all())
#     src = serializers.CharField()
#     addTime = serializers.DateTimeField()
#
#     def validate(self, attrs):
#         print('全局', attrs)
#         return attrs
#
#     def update(self, instance, validated_data):
#         print(validated_data)
#         for key, value in validated_data.items():
#             setattr(instance, key, value)
#         instance.save()
#         return instance
#
#     def create(self, validated_data):
#         image = Image.objects.create(**validated_data)
#         return image