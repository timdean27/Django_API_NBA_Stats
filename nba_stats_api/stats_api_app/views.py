from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import NBAPlayer, NBAPlayerSeasonStats, NBAPlayersLast5Games
from .serializers import NBAPlayerSerializer, NBAPlayerSeasonStatsSerializer, NBAPlayersLast5GamesSerializer

from django.db.models import Max  # Import Max for aggregation

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

@api_view(['GET'])
def all_player_season_stats(request):
    """
    Retrieve the most recent season stats for all players for the 2023-2024 season.
    """
    try:
        # Get distinct players with the most recent season records for 2023-24
        players_with_season = NBAPlayerSeasonStats.objects.filter(season_year='2023-24').values('player_id').annotate(latest_date=Max('date_created'))
        print(f"Players with season data: {players_with_season}")  # Debug output

        # Fetch the most recent season for each player
        season_stats = [
            NBAPlayerSeasonStats.objects.filter(player_id=player['player_id'], date_created=player['latest_date']).first()
            for player in players_with_season
        ]
        print(f"Season Stats: {season_stats}")  # Debug output

        # Serialize the filtered records
        serializer = NBAPlayerSeasonStatsSerializer(season_stats, many=True)
        return Response(serializer.data)
    
    except Exception as e:
        print(f"Error: {e}")  # Capture error output
        return Response({"error": str(e)}, status=500)

@api_view(['GET'])
def all_player_last_five_games(request):
    """
    Retrieve the most recent last 5 games stats for all players.
    """
    # Get distinct players with the most recent game records
    players_with_games = NBAPlayersLast5Games.objects.values('player_id').annotate(latest_date=Max('date_created'))
    # Fetch the most recent last 5 games for each player
    last_five_games = [
        NBAPlayersLast5Games.objects.filter(player_id=player['player_id'], date_created=player['latest_date']).first()
        for player in players_with_games
    ]
    # Serialize the filtered records
    serializer = NBAPlayersLast5GamesSerializer(last_five_games, many=True)
    return Response(serializer.data)


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

@api_view(['GET', 'PUT', 'DELETE'])
def single_player_season_details(request, player_id, id):
    try:
        player_stats = NBAPlayerSeasonStats.objects.get(id=id, player_id=player_id)
    except NBAPlayerSeasonStats.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = NBAPlayerSeasonStatsSerializer(player_stats)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = NBAPlayerSeasonStatsSerializer(player_stats, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        player_stats.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

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

@api_view(['GET', 'PUT', 'DELETE'])
def single_player_last_five_details(request, player_id, id):
    try:
        player_stats = NBAPlayersLast5Games.objects.get(id=id, player_id=player_id)
    except NBAPlayersLast5Games.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = NBAPlayersLast5GamesSerializer(player_stats)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = NBAPlayersLast5GamesSerializer(player_stats, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        player_stats.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
