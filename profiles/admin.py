from django.contrib import admin

from profiles.models import ContactDetails

@admin.register(ContactDetails)
class ContactDetailsAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone', 'city', 'state', 'active', 'created_at']
    list_display_links = ['user']
    search_fields = ['user']
    list_filter = ['city', 'state', 'active', 'created_at']
