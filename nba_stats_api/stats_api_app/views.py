from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import NBAPlayer, NBAPlayerSeasonStats, NBAPlayersLast5Games
from .serializers import NBAPlayerSerializer, NBAPlayerSeasonStatsSerializer, NBAPlayersLast5GamesSerializer

def home(request):
    return HttpResponse("Welcome to NBA Stats API")

@api_view(['GET', 'POST'])
def player_list(request):
    if request.method == 'GET':
        players = NBAPlayer.objects.all()
        serializer = NBAPlayerSerializer(players, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = NBAPlayerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def player_season_details(request, player_id):
    if request.method == 'GET':
        player_stats = NBAPlayerSeasonStats.objects.filter(player_id=player_id)
        serializer = NBAPlayerSeasonStatsSerializer(player_stats, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = NBAPlayerSeasonStatsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def player_last_five_details(request, player_id):
    if request.method == 'GET':
        player_stats = NBAPlayersLast5Games.objects.filter(player_id=player_id)
        serializer = NBAPlayersLast5GamesSerializer(player_stats, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = NBAPlayersLast5GamesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
