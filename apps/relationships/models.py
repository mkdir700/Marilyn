from django.db import models
from contents.models import ContentsModel
from metas.models import MetasModel


class RelationshipsModel(models.Model):
    content = models.ForeignKey(ContentsModel, on_delete=models.CASCADE)
    meta = models.ForeignKey(MetasModel, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "关系表"
        verbose_name_plural = verbose_name
        db_table = "marilyn_relationships"
