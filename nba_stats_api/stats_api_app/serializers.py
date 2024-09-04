from rest_framework import serializers
from .models import NBAPlayer, NBAPlayerSeasonStats, NBAPlayersLast5Games

class NBAPlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = NBAPlayer
        fields = '__all__'  # Or list all fields explicitly if you prefer

class NBAPlayerSeasonStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NBAPlayerSeasonStats
        fields = '__all__'  # Or list all fields explicitly if you prefer

class NBAPlayersLast5GamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = NBAPlayersLast5Games
        fields = '__all__'  # Or list all fields explicitly if you prefer
