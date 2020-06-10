from django.contrib import admin
from .models import CommentsModel


@admin.register(CommentsModel)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ['cid', 'created', 'authorId']