from rest_framework import serializers
from .models import Artist, Song


class ArtistSerializers(serializers.HyperlinkedModelSerializer):
    songs = serializers.HyperlinkedRelatedField(
        view_name='song_detail',
        many=True,
        read_only=True
    )
    class Meta:
        model = Artist 
        fields = ('id', 'photo_url', 'nationality', 'name', 'songs',)

class SongSerializers(serializers.HyperlinkedModelSerializer):
    artist = serializers.HyperlinkedRelatedField(
        view_name='artist_detail',
        read_only=True
    )
    class Meta:
        model = Song 
        fields = ('id', 'artist', 'title', 'album', 'preview_url',)