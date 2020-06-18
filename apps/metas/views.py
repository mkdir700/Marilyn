from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .serializers import *


class MetaViewSet(viewsets.ModelViewSet):
    queryset = MetasModel.objects.all()
    serializer_class = MetaSerializer

    def get_serializer_class(self):
        if self.action == "delete_multiple":
            serializer_class = MetaDeleteMultiple
        else:
            serializer_class = MetaSerializer
        return serializer_class

    @action(methods=['delete'], detail=False)
    def delete_multiple(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        delete_list = serializer.validated_data['delete_list']
        self.get_queryset().filter(mid__in=delete_list).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
