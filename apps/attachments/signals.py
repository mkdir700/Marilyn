import os
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from attachments.models import AttachmentModel


@receiver(pre_delete, sender=AttachmentModel, dispatch_uid="del_file")
def del_file(sender, instance, **kwargs):
    os.remove(instance.file.path)
