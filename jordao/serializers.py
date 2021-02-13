from rest_framework import serializers
from rest_framework.response import Response
from .models import Athlete, City, Season, Game, Sport, Event, Team, GameeventRl

class AthleteSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Athlete
        fields = ['id', 'name', 'sex']

class SeasonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Season
        fields = ['id', 'season']

class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = ['id', 'city']

class SportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sport
        fields = ['id', 'sport']
    
class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'team', 'noc']

class EventSerializer(serializers.ModelSerializer):
    sports = SportSerializer(many=False, write_only=True)
    
    class Meta:
        model = Event
        fields = ['id', 'event', 'sports', 'idsport']
        read_only = ['idsport']

    def create(self, validated_data):
        sport_data = validated_data.pop('sports')
        s, o = Sport.objects.get_or_create(**sport_data)
        event, u = Event.objects.get_or_create(idsport=s, **validated_data)
        return event

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
        game, o = Game.objects.get_or_create(idcity=c, idseason=s, **validated_data)
        return game

class GameeventRlSerializer(serializers.ModelSerializer):
    games = GameSerializer(many=False, write_only=True)
    events = EventSerializer(many=False, write_only=True)

    class Meta:
        model = GameeventRl
        fields = ['id', 'games', 'events', 'idgame', 'idevent']
        read_only_fields = ['idgame', 'idevent']

    def create(self, validated_data):
        game_data = validated_data.pop('games')
        event_data = validated_data.pop('events')
        game, o = Game.objects.create(**game_data)
        event, u = Event.objects.get_or_create(**event_data)
        gameeventrl, y = GameeventRl.objects.get_or_create(idgame=game, idevent=event)
        return gameeventrl
