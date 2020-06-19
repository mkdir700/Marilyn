from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import *


class AttachmentViewSet(viewsets.ModelViewSet):
    queryset = AttachmentModel.objects.all()
    serializer_class = AttachmentsSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAdminUser]

    def get_serializer_class(self):
        if self.action == "delete_multiple":
            serializer_class = DeleteAttachmentsSerializer
        else:
            serializer_class = AttachmentsSerializer
        return serializer_class

    @action(methods=['delete'], detail=False)
    def delete_multiple(self, request, *args, **kwargs):
        """批量删除或删除单个"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        delete_list = serializer.validated_data['pending_deletion']
        self.get_queryset().filter(id__in=delete_list).delete()
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
