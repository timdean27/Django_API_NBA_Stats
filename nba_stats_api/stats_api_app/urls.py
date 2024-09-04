from django.urls import path
from .views import home, player_list, player_season_details, single_player_season_details, player_last_five_details, single_player_last_five_details

urlpatterns = [
    path('', home, name='home'),
    path('api/players/', player_list, name='player-list'),
    path('api/player/season/<int:player_id>/', player_season_details, name='player-season-list'),
    path('api/player/season/<int:player_id>/<int:id>/', single_player_season_details, name='single_player_season_details'),
    path('api/player/last5/<int:player_id>/', player_last_five_details, name='player-last-five-list'),
    path('api/player/last5/<int:player_id>/<int:id>/', single_player_last_five_details, name='single_player_last_five_details'),
]
