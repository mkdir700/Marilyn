import os
from django.db import models
from contents.models import ContentsModel


class AttachmentModel(models.Model):
    content = models.ForeignKey(ContentsModel, on_delete=models.CASCADE, verbose_name="所属文章")
    file = models.FileField(upload_to='upload/%Y/%m/%d/')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "附件"
        verbose_name_plural = verbose_name
        ordering = ['-created']
        db_table = "marilyn_attachments"
