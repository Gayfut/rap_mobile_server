from django import forms
from .models import Album


class AlbumForm(forms.ModelForm):
    """form for showing album in admin panel"""
    class Meta:
        model = Album
        fields = ('title', 'rating', 'track_list', 'link_to_download', 'link_to_album')
        widgets = {'rating': forms.TextInput}
