import json
from rest_framework import serializers
from .models import MetasModel


class MetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetasModel
        fields = '__all__'
        extra_kwargs = {
            'count': {'read_only': True}
        }


class MetaDeleteMultiple(serializers.Serializer):
    delete_list = serializers.CharField(
        max_length=100, label='删除列表', required=True)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    def validate(self, attrs):
        delete_list = attrs['delete_list']
        from json.decoder import JSONDecodeError
        try:
            attrs['delete_list'] = json.loads(delete_list)
        except JSONDecodeError:
            raise serializers.ValidationError('格式不正确')
        return attrs
