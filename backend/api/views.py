from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TournamentSerializer, CardsSerializer, TourPlayersSerializer, DeckSerializer, UserSerializer
from .models import Tournament, Cards, Deck, Tournament_players
# from .models import Tournament, User, Cards, Deck, Tournament_players
from django.contrib.auth.models import User

# Create your views here.


class TournamentView(viewsets.ModelViewSet):
    serializer_class = TournamentSerializer
    queryset = Tournament.objects.all()


class CardsView(viewsets.ModelViewSet):
    serializer_class = CardsSerializer
    queryset = Cards.objects.all()


class UserView(viewsets.ModelViewSet):
    pass
    user = User.objects.create_user()
    # serializer_class = UserSerializer
    # queryset = User.objects.all()



class DeckView(viewsets.ModelViewSet):
    serializer_class = DeckSerializer
    queryset = Deck.objects.all()


class TourPlayerView(viewsets.ModelViewSet):
    serializer_class = TourPlayersSerializer
    queryset = Tournament_players.objects.all()
