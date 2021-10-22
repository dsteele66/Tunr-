from django.shortcuts import render, redirect
from django.http import JsonResponse
from rest_framework import generics, serializers

# Create your views here.

from .models import Artist, Song
from .forms import ArtistForm
from .serializers import ArtistSerializers, SongSerializers

# import json 


class ArtistList(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializers

class ArtistDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializers

class SongList(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializers

class SongDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializers