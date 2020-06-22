import json
from rest_framework import serializers
from .models import ContentsModel
from metas.models import MetasModel
from common.utils import DeleteMultipleSerializer


class ContentSerializer(serializers.ModelSerializer):
    """内容"""

    metas = serializers.PrimaryKeyRelatedField(many=True, allow_null=False, allow_empty=False, label="分类",
                                               queryset=MetasModel.objects.all())

    class Meta:
        model = ContentsModel
        fields = '__all__'
        # extra_kwargs = {
        #     'text': {'write_only': True},
        #     'password': {'write_only': True},
        #     'allowComment': {'write_only': True},
        #     'slug': {'write_only': True},
        #     'template': {'write_only': True},
        #     'commentsNum': {'write_only': True},
        #     'created': {'write_only': True}
        # }


class ContentDetailSerializer(serializers.ModelSerializer):
    """详细文章内容"""

    class Meta:
        model = ContentsModel
        fields = '__all__'


class DeleteContentSerializer(DeleteMultipleSerializer):
    """删除一篇或多篇文章"""
    pass
