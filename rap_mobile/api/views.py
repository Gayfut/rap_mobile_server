from rest_framework import viewsets

from .serializers import AlbumSerializer
from .models import Album


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all().order_by('title')
    serializer_class = AlbumSerializer
