from django.urls import path
from .views import player_list, player_season_details, player_last_five_details, home

urlpatterns = [
    path('', home, name='home'),
    path('api/players/', player_list, name='player-list'),
    path('api/player/season/<int:pk>/', player_season_details, name='player-season-details'),
    path('api/player/last5/<int:pk>/', player_last_five_details, name='player-last-five-details'),
]
