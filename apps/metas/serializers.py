from rest_framework import serializers
from .models import MetasModel
from common.utils import DeleteMultipleSerializer


class MetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetasModel
        fields = '__all__'
        extra_kwargs = {
            'count': {'read_only': True}
        }


class DeleteMetasSerializer(DeleteMultipleSerializer):
    """批量删除文章"""
    pass
