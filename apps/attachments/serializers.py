from rest_framework import serializers
from .models import AttachmentModel
from common.utils import DeleteMultipleSerializer


class AttachmentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = AttachmentModel
        fields = '__all__'


class DeleteAttachmentsSerializer(DeleteMultipleSerializer):
    pass
