from rest_framework import serializers
from .models import LinksModel
from common.utils import DeleteMultipleSerializer


class LinksSerializer(serializers.ModelSerializer):

    class Meta:
        model = LinksModel
        fields = '__all__'


class DeleteLinksSerializer(DeleteMultipleSerializer):
    pass
