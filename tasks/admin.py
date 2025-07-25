from django.contrib import admin
from tasks.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'work_space', 'status', 'priority', 'active', 'created_at']
    list_display_links = ['user', 'status']
    search_fields = ['title', 'work_space']
    list_filter = ['status', 'priority', 'active', 'created_at']
