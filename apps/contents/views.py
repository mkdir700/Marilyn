from rest_framework import status
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import *
from .models import ContentsModel


class ContentsViewSet(viewsets.ModelViewSet):

    queryset = ContentsModel.objects.all()
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ContentSerializer

    def get_serializer_class(self):
        if self.action == "delete_multiple":
            serializer_class = DeleteContentSerializer
        else:
            serializer_class = ContentSerializer
        return serializer_class

    # def create(self, request, *args, **kwargs):
    #     """新建文章"""
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    #
    # def perform_create(self, serializer):
    #     serializer.save()

    @action(methods=['delete'], detail=False)
    def delete_multiple(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        content_list = serializer.validated_data['content_list']
        self.get_queryset().filter(cid__in=content_list).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

