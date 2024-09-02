from rest_framework import serializers
from .models import NBAPlayer, NBAPlayerSeasonStats, NBAPlayersLast5Games

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = NBAPlayer
        fields = ['id', 'name', 'team']

class PlayerSeasonStatsSerializer(serializers.ModelSerializer):
    player = PlayerSerializer()  # Nested serializer

    class Meta:
        model = NBAPlayerSeasonStats
        fields = '__all__'

class PlayerLastFiveStatsSerializer(serializers.ModelSerializer):
    player = PlayerSerializer()  # Nested serializer

    class Meta:
        model = NBAPlayersLast5Games
        fields = '__all__'
