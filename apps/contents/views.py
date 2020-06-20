from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import DjangoModelPermissions, IsAdminUser
from .serializers import *
from .models import ContentsModel
from common.mixin import DeleteMultipleModelMixin


class ContentsViewSet(viewsets.ModelViewSet, DeleteMultipleModelMixin):

    queryset = ContentsModel.objects.all()
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    serializer_class = ContentSerializer

    def get_serializer_class(self):
        if self.action == "delete_multiple":
            serializer_class = DeleteContentSerializer
        else:
            serializer_class = ContentSerializer
        return serializer_class

