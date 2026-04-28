from django.contrib import admin
from apps.leads.models import Lead


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display  = ['name', 'phone', 'email', 'status', 'created_at']
    list_filter   = ['status', 'created_at']
    search_fields = ['name', 'phone', 'email']
    list_editable = ['status']
