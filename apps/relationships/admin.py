from django.contrib import admin
from .models import RelationshipsModel
from django_restful_admin import site


@admin.register(RelationshipsModel)
class RelationshipsAdmin(admin.ModelAdmin):
    list_display = ['__str__']


site.register(RelationshipsModel)
