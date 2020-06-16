import json
from json.decoder import JSONDecodeError
from rest_framework import serializers
from .models import ContentsModel
from metas.models import MetasModel


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


class DeleteContentSerializer(serializers.Serializer):
    """删除一篇或多篇文章"""

    content_list = serializers.CharField(required=True, label="待删除文章ID")

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    def validate(self, attrs):
        content_list = attrs['content_list']
        try:
            attrs['content_list'] = json.loads(content_list)
        except JSONDecodeError:
            raise serializers.ValidationError('格式不正确')
        return attrs
