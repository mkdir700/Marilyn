from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from .serializers import *
from common.mixin import DeleteMultipleModelMixin


class MetaViewSet(viewsets.ModelViewSet, DeleteMultipleModelMixin):
    queryset = MetasModel.objects.all()
    serializer_class = MetaSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminUser]

    def get_serializer_class(self):
        if self.action == "delete_multiple":
            serializer_class = DeleteMetasSerializer
        else:
            serializer_class = MetaSerializer
        return serializer_class

