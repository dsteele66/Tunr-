from django import forms
from .models import Artist, Song


class ArtistForm(forms.ModelForm):

    class Meta:
        model = Artist 
        #whats in fields is a tuple 
        fields = ('name', 'photo_url', 'nationality')