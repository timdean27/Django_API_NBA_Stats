
from django.urls import path
from .views import player_list, player_detail, home

urlpatterns = [
    path('', home, name='home'),
    path('api/players/', player_list, name='player-list'),  # For /api/players/
    path('api/player/<int:pk>/', player_detail, name='player-detail'),  # For /api/player/<pk>/
]
