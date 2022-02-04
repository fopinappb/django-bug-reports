from django.contrib import admin
from . import models


@admin.register(models.Finding)
class FindingAdmin(admin.ModelAdmin):
    search_fields = ['id', 'title']
    autocomplete_fields = ['related_to']
    list_display = ['id', 'title', 'extra']
