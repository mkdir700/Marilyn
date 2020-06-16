from django.db.models.signals import pre_delete, m2m_changed
from django.dispatch import receiver
from contents.models import ContentsModel, RelationshipsModel
from metas.models import MetasModel


def add_count(metas):
    for meta in metas:
        meta.count += 1
        meta.save()


def sub_count(metas):
    for meta in metas:
        meta.count -= 1
        meta.save()


@receiver(m2m_changed, sender=RelationshipsModel, dispatch_uid="create_content")
def create_content(sender, instance, action, pk_set, **kwargs):
    print(action, pk_set, type(pk_set))
    # metas = MetasModel.objects.filter(meta_list__cid=instance.cid)
    metas = MetasModel.objects.filter(mid__in=pk_set)
    if action == "pre_remove":
        sub_count(metas)
    elif action == "post_remove":
        pass
    elif action == "pre_add":
        pass
    elif action == "post_add":
        add_count(metas)


@receiver(pre_delete, sender=ContentsModel, dispatch_uid="delete_content")
def delete_content(sender, instance, **kwargs):
    metas = MetasModel.objects.filter(meta_list__cid=instance.cid)
    sub_count(metas)
