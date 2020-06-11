from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from .serializers import *
from .models import Profile


class UserViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        if self.action == "list":
            queryset = User.objects.order_by('-id')
        else:
            queryset = User.objects.order_by('-id')
        return queryset

    def get_serializer_class(self):
        if self.action == "list":
            serializer_class = UserSerializer
        elif self.action == "retrieve":
            serializer_class = UserDetailSerializer
        elif self.action == "create":
            serializer_class = CreateUserSerializer
        elif self.action == "update":
            serializer_class = UpdateUserSerializer
        elif self.action == "change_password":
            serializer_class = ChangePasswordSerialize
        else:
            serializer_class = UserDetailSerializer
        return serializer_class

    def update(self, request, *args, **kwargs):
        """更新用户信息"""
        partial = kwargs.pop('partial', False)
        user = User.objects.filter(pk=kwargs['pk']).first()
        serializer = self.get_serializer(user, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        screenName = serializer.validated_data.get('screenName', '')  # 为空则保持不变
        if screenName:
            user.profile.screenName = screenName
            user.profile.save()
        self.perform_update(serializer)
        return Response({'status': 'ok'}, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        """新增用户"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        User.objects.create_user(username=username, password=password)
        return Response({'status': 'ok', 'msg': '用户新建成功'}, status=status.HTTP_201_CREATED)

    @action(methods=['PUT'], detail=False)
    def change_password(self, request):
        """修改用户密码
        id 用户主键;
        password 密码
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        uid = serializer.validated_data['id']
        password = serializer.validated_data['password']
        user = User.objects.filter(id=uid).first()
        user.set_password(password)
        user.save()
        return Response({'status': 'ok'}, status=status.HTTP_200_OK)
