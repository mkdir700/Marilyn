from django.db import models
from django.contrib.auth.models import User
from metas.models import MetasModel


class ContentsModel(models.Model):
    STATUS = [
        ('public', '公开'),
        ('private', '私有'),
        ('protect', '密码保护')
    ]

    cid = models.AutoField(primary_key=True, unique=True, verbose_name="id")
    title = models.CharField(max_length=30, verbose_name="标题")
    metas = models.ManyToManyField(MetasModel, through='RelationshipsModel',
                                   through_fields=['content', 'meta'],
                                   related_name="meta_list")
    # slug用户可以自定义, 默认和主键cid同值
    slug = models.SlugField(allow_unicode=True, verbose_name="缩写")
    created = models.DateTimeField(auto_created=True, verbose_name="创建时间")
    modified = models.DateTimeField(auto_now=True, verbose_name="修改时间")
    text = models.TextField(null=True, blank=True, verbose_name="内容")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="作者")
    # 文章模板,专题模板,项目模板,相册模板
    template = models.CharField(max_length=20, default=None, null=True, blank=True, verbose_name="模板")
    # 公开public, 私有private, 保护protect(输入密码后查看)
    status = models.CharField(choices=STATUS, max_length=10, default=0, verbose_name="状态")
    password = models.CharField(null=True, blank=True, max_length=20, verbose_name="密码")
    commentsNum = models.IntegerField(default=0, verbose_name="评论数")
    allowComment = models.BooleanField(default=True, verbose_name="评论开关")
    view = models.IntegerField(default=0, verbose_name="阅读数")

    class Meta:
        verbose_name = "文章"
        verbose_name_plural = verbose_name
        db_table = "marilyn_contents"
        ordering = ['cid']

    def __str__(self):
        return self.title


class RelationshipsModel(models.Model):
    content = models.ForeignKey(ContentsModel, on_delete=models.CASCADE)
    meta = models.ForeignKey(MetasModel, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "关系表"
        verbose_name_plural = verbose_name
        db_table = "marilyn_relationships"
