from rest_framework import serializers

from .models import Album

class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    """serializer for album"""
    class Meta:
        model = Album
        fields = ('title', 'rating', 'track_list', 'link_to_download', 'link_to_album')
