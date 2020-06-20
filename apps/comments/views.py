from django.db.models import F
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser, DjangoModelPermissions
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from django_filters import rest_framework as filters
from common.mixin import DeleteMultipleModelMixin
from .serializers import (
    CommentsSerializer,
    DeleteCommentsSerializer,
    CommentStatusSerializer)
from .models import CommentsModel
from .filters import CommentFilter


class CommentViewSet(viewsets.ModelViewSet, DeleteMultipleModelMixin):
    queryset = CommentsModel.objects.all()
    serializer_class = CommentsSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = CommentFilter
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAdminUser, DjangoModelPermissions]

    def get_serializer_class(self):
        if self.action == "delete_multiple":
            serializer_class = DeleteCommentsSerializer
        elif self.action == "status":
            serializer_class = CommentStatusSerializer
        else:
            serializer_class = CommentsSerializer
        return serializer_class

    @action(methods=['patch'], detail=False)
    def status(self, request):
        """设置评论状态"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        coid_list = serializer.validated_data['coid']
        co_status = serializer.validated_data['status']
        self.get_queryset().filter(pk__in=coid_list).update(status=co_status)
        return Response(serializer.data, status=status.HTTP_200_OK)
