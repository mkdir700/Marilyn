from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.permissions import DjangoModelPermissions, IsAdminUser
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth.models import Permission
from .serializer import GroupSerializer
# from .paginations import PermissionPagination


class PermissionViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Permission.objects.all()
    serializer_class = GroupSerializer
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    # pagination_class = PermissionPagination
