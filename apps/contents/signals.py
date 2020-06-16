from django.db.models.signals import pre_delete, m2m_changed
from django.dispatch import receiver
from contents.models import ContentsModel, RelationshipsModel
from metas.models import MetasModel


@receiver(m2m_changed, sender=RelationshipsModel, dispatch_uid="create_content")
def create_content(sender, instance, action, pk_set, **kwargs):
    if action == "post_add":
        metas = MetasModel.objects.filter(meta_list__cid=instance.cid)
        for meta in metas:
            meta.count += 1
            meta.save()


@receiver(pre_delete, sender=ContentsModel, dispatch_uid="delete_content")
def delete_content(sender, instance, **kwargs):
    metas = MetasModel.objects.filter(meta_list__cid=instance.cid)
    for meta in metas:
        meta.count -= 1
        meta.save()
