from django.db import models


class OptionsModel(models.Model):
    title = models.CharField(default="Marilyn", max_length=30, verbose_name="站点名称")
    keywords = models.CharField(null=True, blank=True, max_length=50, verbose_name="关键字")
    description = models.TextField(null=True, blank=True, max_length=200, verbose_name="描述")
    siteUrl = models.CharField(null=True, blank=True, max_length=50, verbose_name="站点网址")
    allowRegister = models.BooleanField(default=False, verbose_name="是否允许注册")
    defaultAllowComment = models.BooleanField(default=True, verbose_name="是否允许评论")

    class Meta:
        verbose_name = "站点信息"
        verbose_name_plural = verbose_name
        db_table = "marilyn_options"
