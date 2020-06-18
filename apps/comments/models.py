from django.db import models
from django.contrib.auth.models import User
from contents.models import ContentsModel


class CommentsModel(models.Model):
    STATUS_CHOICES = [
        ('approved', "已通过"),
        ('waiting', "待审核"),
        ('spam', "垃圾评论")
    ]

    coid = models.AutoField(primary_key=True, unique=True, verbose_name="coid")
    cid = models.ForeignKey(ContentsModel, on_delete=models.CASCADE, verbose_name="所属文章")
    created = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    # 游客需要输入他的名字, 如果是登录用户,可以去数据库里面取出来
    author = models.CharField(max_length=20, verbose_name="姓名")
    # 允许为空, 空代表游客
    authorId = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    mail = models.EmailField(max_length=50, verbose_name="邮箱")
    url = models.CharField(max_length=50, verbose_name="主页")
    ip = models.GenericIPAddressField(max_length=20, verbose_name="ip地址")
    agent = models.CharField(max_length=200, verbose_name="用户代理")
    text = models.TextField(max_length=300, verbose_name="评论内容")
    type = models.CharField(default="comment", max_length=20, verbose_name="类型")
    status = models.CharField(choices=STATUS_CHOICES, max_length=10, verbose_name="状态")
    parent = models.ForeignKey('self', null=True, blank=True, verbose_name="上级", on_delete=models.CASCADE)
    stars = models.IntegerField(default=0, verbose_name="点赞数")

    class Meta:
        verbose_name = "留言/评论"
        verbose_name_plural = verbose_name
        ordering = ['coid']
        db_table = "marilyn_comments"

    def __str__(self):
        return f"{self.text[:20]}"
