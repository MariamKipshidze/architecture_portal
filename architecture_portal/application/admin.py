from django.contrib import admin
from application.models import Application


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('project_title', 'client_name', 'project_type', 'submission_date', 'viewed')
    list_filter = ('viewed', 'project_type', 'submission_date')
    search_fields = ('project_title', 'client_name', 'client_email')
    actions = ['mark_as_processed']

    def mark_as_processed(self, request, queryset):
        queryset.update(viewed=True)

    mark_as_processed.short_description = "Mark selected applications as processed"
