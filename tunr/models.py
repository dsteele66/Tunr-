from django.db import models
from django.db.models.fields import related

# Create your models here.

class Artist(models.Model):
    name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    photo_url = models.TextField()
    print("At Artist Model")

    def __str__(self):
        return self.name
        
# class Song(models.Model):
#     artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='songs')
#     title = models.CharField(max_length=100, default='no song title')
#     album = models.CharField(max_length=100, default='no album title')
#     preview_url = models.CharField(max_length=100, null=True)
    
#     def __self__(self):
#         return self.title

class Song(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='songs')
    title = models.CharField(max_length=100, default='no song title')
    album = models.CharField(max_length=100, default='no album title')
    preview_url = models.CharField(max_length=200, null=True)
    print('At Song Model ')

    def __str__(self):
        return self.title

        