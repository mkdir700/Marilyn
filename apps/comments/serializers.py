from rest_framework import serializers
from .models import CommentsModel
from common.utils import DeleteMultipleSerializer

STATUS_CHOICES = [
    ('approved', "已通过"),
    ('waiting', "待审核"),
    ('spam', "垃圾评论")
]


class CommentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = CommentsModel
        fields = '__all__'


class CommentStatusSerializer(serializers.ModelSerializer):
    coid = serializers.ListField(child=serializers.IntegerField())

    class Meta:
        model = CommentsModel
        fields = ['coid', 'status']


class DeleteCommentsSerializer(DeleteMultipleSerializer):
    pass
