from django.contrib import admin
from .models import MetasModel


@admin.register(MetasModel)
class MetasAdmin(admin.ModelAdmin):
    list_display = ["mid", "name", "type", "order", "count", "parent"]

