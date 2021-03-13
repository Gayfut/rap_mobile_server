from django.contrib import admin
from .forms import AlbumForm
from .models import Album


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    """register albums in admin panel"""
    list_display = ('title', 'rating', 'track_list', 'link_to_download', 'link_to_album')
    form = AlbumForm
