from django.contrib import admin
from .models import RelationshipsModel


@admin.register(RelationshipsModel)
class RelationshipsAdmin(admin.ModelAdmin):
    list_display = ['__str__']