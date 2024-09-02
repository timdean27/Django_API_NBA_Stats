from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import NBAPlayer, NBAPlayerSeasonStats, NBAPlayersLast5Games
from .serializers import PlayerSerializer, PlayerSeasonStatsSerializer, PlayerLastFiveStatsSerializer

def home(request):
    return HttpResponse("Welcome to NBA Stats API")

@api_view(['GET', 'POST'])
def player_list(request):
    if request.method == 'GET':
        players = NBAPlayer.objects.all()
        serializer = PlayerSerializer(players, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PlayerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def player_season_details(request, pk):
    try:
        player_stats = NBAPlayerSeasonStats.objects.get(player_id=pk)
    except NBAPlayerSeasonStats.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PlayerSeasonStatsSerializer(player_stats)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PlayerSeasonStatsSerializer(player_stats, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        player_stats.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def player_last_five_details(request, pk):
    try:
        player_stats = NBAPlayersLast5Games.objects.get(player_id=pk)
    except NBAPlayersLast5Games.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PlayerLastFiveStatsSerializer(player_stats)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PlayerLastFiveStatsSerializer(player_stats, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        player_stats.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
