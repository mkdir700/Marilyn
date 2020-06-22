from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, DjangoModelPermissions
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import *
from common.mixin import DeleteMultipleModelMixin


class AttachmentViewSet(viewsets.ModelViewSet, DeleteMultipleModelMixin):
    queryset = AttachmentModel.objects.all()
    serializer_class = AttachmentsSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAdminUser, DjangoModelPermissions]

    def get_serializer_class(self):
        if self.action == "delete_multiple":
            serializer_class = DeleteAttachmentsSerializer
        else:
            serializer_class = AttachmentsSerializer
        return serializer_class
