from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('api/players/', views.player_list, name='player_list'),
    path('api/players/season/', views.all_player_season_stats, name='all_player_season_stats'),  # New route
    path('api/players/last5/', views.all_player_last_five_games, name='all_player_last_five_games'),  # New route
    path('api/players/season/<int:player_id>', views.player_season_details, name='player_season_details'),
    path('api/players/season/<int:player_id>/<int:id>/', views.single_player_season_details, name='single_player_season_details'),
    path('api/players/last5/<int:player_id>', views.player_last_five_details, name='player_last_five_details'),
    path('api/players/last5/<int:player_id>/<int:id>/', views.single_player_last_five_details, name='single_player_last_five_details'),
]
