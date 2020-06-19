from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action


class DeleteMultipleModelMixin:
    """
    提供批量删除方法
    """
    @action(methods=['delete'], detail=False)
    def delete_multiple(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        delete_list = serializer.validated_data['pending_deletion']
        self.get_queryset().filter(pk__in=delete_list).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
