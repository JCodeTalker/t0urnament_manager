from rest_framework import serializers
from .models import Tournament, Cards, Deck, Tournament_players, User


class TournamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournament
        fields = ('id', 'name', 'description', 'address', 'date')


class CardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cards
        fields = ('deck', 'name', 'desc', 'api_id')


class DeckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deck
        fields = ('owner', 'name', 'desc')


class TourPlayersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournament_players
        fields = ('tournament', 'player')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'email', 'password', 'cpf', 'address', 'tel')
