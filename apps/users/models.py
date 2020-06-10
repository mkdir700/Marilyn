from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    url = models.CharField(max_length=30, null=True, blank=True, verbose_name="主页")
    screenName = models.CharField(max_length=20, verbose_name="显示的名称")

    class Meta:
        verbose_name = "用户管理"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.__str__()


# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)


# @receiver(post_save, sender=User)
# def update_user_profile(sender, instance, **kwargs):
#     instance.profile.save()