from django_filters import rest_framework as filters
from .models import ContentsModel


class ContentFilter(filters.FilterSet):
    query = filters.CharFilter(field_name="title", lookup_expr='icontains')

    class Meta:
        model = ContentsModel
        fields = ['query']
