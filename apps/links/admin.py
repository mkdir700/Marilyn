from django.contrib import admin
from .models import LinksModel


@admin.register(LinksModel)
class LinksAdmin(admin.ModelAdmin):
    list_display = ['name', 'url', 'order']
