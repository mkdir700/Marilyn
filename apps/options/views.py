from rest_framework import viewsets
from rest_framework import mixins
from .serializer import OptionSerializer
from .models import OptionsModel


class OptionViewSet(viewsets.ReadOnlyModelViewSet,
                    mixins.CreateModelMixin,
                    mixins.UpdateModelMixin,):
    queryset = OptionsModel.objects.all()
    serializer_class = OptionSerializer

