from rest_framework import serializers
from drf_compound_fields.fields import ListOrItemField
from .models import AttachmentModel


class AttachmentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = AttachmentModel
        fields = '__all__'


class DeleteAttachmentsSerializer(serializers.Serializer):
    # delete_list = ListOrItemField(serializers.CharField(max_length=10))
    pending_deletion = serializers.ListField(child=serializers.IntegerField())

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

