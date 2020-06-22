from django_filters import rest_framework as filters
from .models import User, Profile


class UserFilter(filters.FilterSet):
    query = filters.CharFilter(field_name="username", lookup_expr='icontains')

    class Meta:
        model = User
        fields = ['query']
