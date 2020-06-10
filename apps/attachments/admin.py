from django.contrib import admin
from .models import AttachmentModel


@admin.register(AttachmentModel)
class AttachmentAdmin(admin.ModelAdmin):
    list_display = ['id']