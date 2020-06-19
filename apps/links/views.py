from rest_framework import viewsets
from common.mixin import DeleteMultipleModelMixin
from .serializers import *


class LinkViewSet(viewsets.ModelViewSet, DeleteMultipleModelMixin):
    serializer_class = LinksSerializer
    queryset = LinksModel.objects.all()

    def get_serializer_class(self):
        if self.action == "delete_multiple":
            serializer_class = DeleteLinksSerializer
        else:
            serializer_class = LinksSerializer
        return serializer_class
