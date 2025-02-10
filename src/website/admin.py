from django.contrib import admin
from .models import Project, GalleryMedia, GalleryUpload, ProjectMedia
from ..core.admin import admin_site


class ProjectImageInline(admin.TabularInline):
    model = ProjectMedia
    extra = 1

class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImageInline]

class GalleryUploadAdmin(admin.ModelAdmin):
    list_display = ('zip_file', 'images', 'uploaded_at')

admin_site.register(Project)
admin_site.register(ProjectMedia)
admin_site.register(GalleryMedia)
admin_site.register(GalleryUpload)