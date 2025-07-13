from django.contrib import admin
from project.models import Project, ProjectImage


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1  # Number of empty forms displayed
    fields = ('image', 'caption')  # Fields to show inline
    readonly_fields = ()
    can_delete = True


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'client', 'location', 'start_date', 'end_date', 'is_published')
    list_filter = ('is_published', 'start_date', 'end_date')
    search_fields = ('title', 'client', 'location')
    inlines = [ProjectImageInline]
