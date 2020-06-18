from django.db import models


class LinksModel(models.Model):
    name = models.CharField(max_length=30, verbose_name='站名')
    url = models.CharField(max_length=30, verbose_name="链接")
    description = models.CharField(max_length=50, verbose_name="简介")
    order = models.IntegerField(default=0, verbose_name="排序")
    image = models.CharField(max_length=50, null=True, blank=True, verbose_name="图标链接")

    class Meta:
        verbose_name = "友情"
        verbose_name_plural = verbose_name
        db_table = "marilyn_links"
        ordering = ['order']

    def __str__(self):
        return f"{self.name}"
