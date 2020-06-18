from django.db import models


class MetasModel(models.Model):

    META_TYPE = [
        ('category', '文章分类'),
        ('tag', '标签分类')
    ]
    mid = models.AutoField(primary_key=True, unique=True, verbose_name="分类id")
    slug = models.SlugField(allow_unicode=True, verbose_name="缩写")
    name = models.CharField(max_length=10, verbose_name="分类名称")
    type = models.CharField(choices=META_TYPE, default=META_TYPE[0][0], max_length=20, verbose_name="分类类型")
    order = models.IntegerField(default=0, verbose_name="排序")
    count = models.IntegerField(default=0, verbose_name="文章数量")
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, verbose_name="上级分类")

    class Meta:
        verbose_name = "分类"
        verbose_name_plural = verbose_name
        db_table = "marilyn_metas"
        ordering = ['order']

    def __str__(self):
        return self.name
