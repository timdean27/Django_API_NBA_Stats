from django.urls import path
from .views import player_list, player_season_details, player_last_five_details, home

urlpatterns = [
    path('', home, name='home'),
    path('api/players/', player_list, name='player-list'),
    path('api/player/season/<int:player_id>/', player_season_details, name='player-season-details'),
    path('api/player/season/<int:player_id>/<int:id>', player_season_details, name='player-season-details'),
    path('api/player/last5/<int:player_id>/', player_last_five_details, name='player-last-five-details'),
    path('api/player/last5/<int:player_id>/<int:id>', player_last_five_details, name='player-last-five-details'),
]
