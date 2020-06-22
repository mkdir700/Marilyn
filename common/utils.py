from rest_framework import serializers


class DeleteMultipleSerializer(serializers.Serializer):
    """批量删除序列化类"""
    pending_deletion = serializers.ListField(child=serializers.IntegerField())

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass
