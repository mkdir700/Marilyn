from django_filters import rest_framework as filters
from .models import CommentsModel

STATUS_CHOICES = (
    ('approved', '已通过'),
    ('waiting', '待审核'),
    ('spam', '垃圾评论'),
)


class CommentFilter(filters.FilterSet):

    status = filters.ChoiceFilter(choices=STATUS_CHOICES, label="状态")

    class Meta:
        model = CommentsModel
        fields = ['status']
