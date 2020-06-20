from rest_framework import viewsets
from rest_framework import mixins
from django.contrib.auth.models import Permission
from .serializer import GroupSerializer
# from .paginations import PermissionPagination


class PermissionViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Permission.objects.all()
    serializer_class = GroupSerializer
    # pagination_class = PermissionPagination
