from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('artists/', views.ArtistList.as_view(), name='artist_list'),
    path('artists/<int:pk>', views.ArtistDetail.as_view(), name='artist_detail'),
    path('songs/', views.SongList.as_view(), name='song_list'),
    path('songs/<int:pk>', views.SongDetail.as_view(), name='song_detail'),

]

