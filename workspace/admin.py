from django.contrib import admin
from workspace.models import WorkSpace


@admin.register(WorkSpace)
class WorkSpaceAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'active', 'created_at']
    list_display_links = ['user']
    search_fields = ['title']
    list_filter = ['title', 'active', 'created_at']
