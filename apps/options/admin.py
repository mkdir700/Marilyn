from django.contrib import admin
from .models import OptionsModel


@admin.register(OptionsModel)
class OptionsAdmin(admin.ModelAdmin):
    list_display = ['title']