from django.db import models


class Album(models.Model):
    title = models.TextField(verbose_name="Title")
    rating = models.TextField(verbose_name="Rating")
    track_list = models.TextField(verbose_name="List of tracks")
    link_to_download = models.URLField(verbose_name="Link for download")
    link_to_album = models.URLField(verbose_name="Link to album on site", unique=True)

    class Meta:
        verbose_name = 'Album'
        verbose_name_plural = 'Albums'

