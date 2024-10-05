from django.contrib import admin
from urls.infrastructure.models import VideoURL

@admin.register(VideoURL)
class VideoURLAdmin(admin.ModelAdmin):
    list_display = ('url', 'added_at')
    search_fields = ('url',)
