from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.permissions import IsAdminUser, DjangoModelPermissions
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializer import OptionSerializer
from .models import OptionsModel


class OptionViewSet(viewsets.ReadOnlyModelViewSet,
                    mixins.CreateModelMixin,
                    mixins.UpdateModelMixin,):
    queryset = OptionsModel.objects.all()
    serializer_class = OptionSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAdminUser, DjangoModelPermissions]

