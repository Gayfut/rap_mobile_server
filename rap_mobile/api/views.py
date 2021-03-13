from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .serializers import AlbumSerializer
from .models import Album


class AlbumViewSet(viewsets.ModelViewSet):
    """view for album in api"""
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Album.objects.all().order_by('title')
    serializer_class = AlbumSerializer
