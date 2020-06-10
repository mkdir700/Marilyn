from django.contrib import admin
from .models import ContentsModel


@admin.register(ContentsModel)
class ContentsAdmin(admin.ModelAdmin):
    list_display = ['title', 'created', 'author', 'view', 'commentsNum']
    prepopulated_fields = {"slug": ("title",)}
