from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import *
from .models import ContentsModel
from common.mixin import DeleteMultipleModelMixin


class ContentsViewSet(viewsets.ModelViewSet, DeleteMultipleModelMixin):

    queryset = ContentsModel.objects.all()
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = ContentSerializer

    def get_serializer_class(self):
        if self.action == "delete_multiple":
            serializer_class = DeleteContentSerializer
        else:
            serializer_class = ContentSerializer
        return serializer_class

