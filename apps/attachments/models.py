import uuid
import datetime
from django.db import models
from contents.models import ContentsModel


def new_path(instance, filename):
    _, suffix = filename.split(".", 1)
    new_file_name = "{}.{}".format(uuid.uuid1(), suffix)
    now = datetime.datetime.now()
    month = '%02d' % now.month
    day = '%02d' % now.day
    return f'upload/{now.year}/{month}/{day}/{new_file_name}'


class AttachmentModel(models.Model):
    content = models.ForeignKey(ContentsModel, on_delete=models.CASCADE, verbose_name="所属文章")
    # file = models.FileField(upload_to='upload/%Y/%m/%d/')
    file = models.FileField(upload_to=new_path)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "附件"
        verbose_name_plural = verbose_name
        ordering = ['-created']
        db_table = "marilyn_attachments"
