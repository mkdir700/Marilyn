import os
import datetime
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from ..models import AttachmentModel


def new_name(created: datetime, id: int) -> str:
    """重命名文件,保证文件名唯一
    :param created 创建时间
    :param id 主键
    """
    return str(hash(datetime.datetime.timestamp(created) + id))


@receiver(post_save, sender=AttachmentModel, dispatch_uid="re_file_name")
def re_file_name(sender, instance, created, **kwargs):
    instance = sender.objects.first()
    if created:
        abs_file_path = instance.file.path
        rel_folder_path, old_file_name = abs_file_path.rsplit("/", 1)
        _, suffix = old_file_name.split(".", 1)
        # new_file_name = f"123.{suffix}"
        new_file_name = "{}.{}".format(new_name(instance.created, instance.id), suffix)
        os.rename(abs_file_path, abs_file_path.rsplit("/", 1)[0] + "/" + new_file_name)
        instance.file = f"{rel_folder_path}/{new_file_name}"
        instance.save()


@receiver(pre_delete, sender=AttachmentModel, dispatch_uid="del_file")
def del_file(sender, instance, **kwargs):
    os.remove(instance.file.path)