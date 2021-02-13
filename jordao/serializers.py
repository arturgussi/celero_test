from rest_framework import serializers
from rest_framework.response import Response
from .models import Athlete, City, Season, Game, Sport, Event

class AthleteSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Athlete
        fields = ['id', 'name', 'sex']

class SeasonSerializer(serializers.ModelSerializer):
    #games = GameSerializer(read_only=True,many=True)

    class Meta:
        model = Season
        fields = '__all__'

class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = ['id', 'city']


class GameSerializer(serializers.ModelSerializer):
    cities = CitySerializer(many=False, write_only=True)
    seasons = SeasonSerializer(many=False, write_only=True)

    class Meta:
        model = Game
        fields = ['id', 'game', 'year', 'cities', 'seasons', 'idseason', 'idcity']
        read_only = ['idcity', 'idseason']
        
    def create(self, validated_data):
        city_data = validated_data.pop('cities')
        c, o = City.objects.get_or_create(**city_data)
        season_data = validated_data.pop('seasons')
        s, o = Season.objects.get_or_create(**season_data)
        game = Game.objects.create(idcity=c, idseason=s, **validated_data)
        return game

class SportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sport
        fields = ['id', 'sport']

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'event', 'idsport']