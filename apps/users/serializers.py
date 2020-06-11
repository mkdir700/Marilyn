from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Profile as UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    """用户扩展"""

    class Meta:
        model = UserProfile
        fields = ['screenName']


class UserSerializer(serializers.ModelSerializer):
    """用户"""
    profile = UserProfileSerializer(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'is_active', 'is_staff', 'profile']


class UserDetailSerializer(serializers.ModelSerializer):
    """用户详细信息"""
    profile = UserProfileSerializer(read_only=True)
    password = serializers.CharField(required=False, write_only=True, label="密码")

    class Meta:
        model = User
        exclude = ['last_name', 'first_name']


class CreateUserSerializer(serializers.ModelSerializer):
    """新建用户"""
    password = serializers.CharField(required=True, label="密码", max_length=16)
    password2 = serializers.CharField(required=True, label="重复密码", max_length=16)

    class Meta:
        model = User
        fields = ['username', 'password', 'password2']

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError('两次密码不一致')
        return attrs


class UpdateUserSerializer(serializers.ModelSerializer):
    """修改用户信息"""
    screenName = serializers.CharField(max_length=20, label="昵称", allow_null=True, allow_blank=True, write_only=True)
    email = serializers.EmailField(max_length=50, label="邮箱")

    class Meta:
        model = User
        fields = ['screenName', 'is_active', 'is_staff', 'email', 'groups']


class ChangePasswordSerialize(serializers.ModelSerializer):
    """修改账号密码"""
    id = serializers.IntegerField(label="用户id", required=True)
    password = serializers.CharField(label="新密码", required=True)

    class Meta:
        model = User
        fields = ['id', 'password']
        read_only_fields = ['username']
