from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from common.mixin import DeleteMultipleModelMixin
from .serializers import *


class LinkViewSet(viewsets.ModelViewSet, DeleteMultipleModelMixin):
    serializer_class = LinksSerializer
    queryset = LinksModel.objects.all()
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminUser]

    def get_serializer_class(self):
        if self.action == "delete_multiple":
            serializer_class = DeleteLinksSerializer
        else:
            serializer_class = LinksSerializer
        return serializer_class
