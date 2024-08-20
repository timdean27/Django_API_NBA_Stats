from rest_framework import serializers
from .models import Player, Player_Season_stats_model, Player_LastFive_stats_model

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['id', 'name', 'team']

class PlayerSeasonStatsSerializer(serializers.ModelSerializer):
    player = PlayerSerializer()  # Nested serializer

    class Meta:
        model = Player_Season_stats_model
        fields = '__all__'

class PlayerLastFiveStatsSerializer(serializers.ModelSerializer):
    player = PlayerSerializer()  # Nested serializer

    class Meta:
        model = Player_LastFive_stats_model
        fields = '__all__'
