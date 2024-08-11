from django.http import HttpResponse
from .models import Player
from .serializers import PlayerSerializer
from rest_framework.response import Response  # Import Response for handling API responses
from rest_framework.decorators import api_view, permission_classes # Import the api_view decorator for handling HTTP methods and permission classes for decorator 
from rest_framework import status  # Import status codes for API responses

def home(request):
    return HttpResponse("Welcome to NBA Stats API")

@api_view(['GET', 'POST'])
def player_list(request):
    if request.method == 'GET':
        players = Player.objects.all()
        serializer = PlayerSerializer(players, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PlayerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
def player_detail(request, pk):
    try:
        player = Player.objects.get(pk=pk)
    except Player.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = PlayerSerializer(player)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PlayerSerializer(player, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        player.delete()
        return Response(status=204)
