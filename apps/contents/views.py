from rest_framework import status
from rest_framework import viewsets
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

    @action(methods=['delete'], detail=False)
    def delete_multiple(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        delete_list = serializer.validated_data['delete_list']
        self.get_queryset().filter(cid__in=delete_list).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

