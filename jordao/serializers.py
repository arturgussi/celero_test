from rest_framework import serializers
from .models import Athlete, City, Season, Game, Sport, Event, Team, GameeventRl, AthletegameeventRl

class AthleteSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Athlete
        fields = ['id', 'name', 'sex']

    def create(self, validated_data):
        athlete, created = Athlete.objects.get_or_create(**validated_data)
        return athlete

class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = ['id', 'season']
        
    def create(self, validated_data):
        season, created = Season.objects.get_or_create(**validated_data)
        return season

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'city']

    def create(self, validated_data):
        city, created = City.objects.get_or_create(**validated_data)
        return city

class SportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sport
        fields = ['id', 'sport']

    def create(self, validated_data):
        sport, created = Sport.objects.get_or_create(**validated_data)
        return sport
    
class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'team', 'noc']
    
    def create(self, validated_data):
        team, created = Team.objects.get_or_create(**validated_data)
        return team

class EventSerializer(serializers.ModelSerializer):
    sports = SportSerializer(many=False, write_only=True)
    
    class Meta:
        model = Event
        fields = ['id', 'event', 'sports', 'idsport']
        read_only = ['idsport']

    def create(self, validated_data):
        sport_data = validated_data.pop('sports')
        sport_serializer = SportSerializer(data=sport_data)
        sport_serializer.is_valid()
        sport = sport_serializer.save()
        event, created = Event.objects.get_or_create(idsport=sport, **validated_data)
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
        season_data = validated_data.pop('seasons')
        city_serializer = CitySerializer(data=city_data)
        city_serializer.is_valid()
        city = city_serializer.save()
        season_serializer = SeasonSerializer(data=season_data)
        season_serializer.is_valid()
        season = season_serializer.save()
        game, created = Game.objects.get_or_create(idcity=city, idseason=season, **validated_data)
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
        event_serializer = EventSerializer(data=event_data)
        event_serializer.is_valid()
        event = event_serializer.save()
        game_serializer = GameSerializer(data=game_data)
        game_serializer.is_valid()
        game = game_serializer.save()
        gameeventrl, created = GameeventRl.objects.get_or_create(idgame=game, idevent=event)
        return gameeventrl

class AthletegameeventRlSerializer(serializers.ModelSerializer):
    gameevents = GameeventRlSerializer(many=False, write_only=True)
    athletes = AthleteSerializer(many=False, write_only=True)
    teams = TeamSerializer(many=False, write_only=True)

    class Meta:
        model = AthletegameeventRl
        fields = ['id', 'medal', 'height', 'age', 'weight', 'gameevents', 'athletes', 'teams', 'idgameevent', 'idathlete', 'idteam']
        read_only_fields = ['idgameevent', 'idathlete', 'idteam']
        
    def create(self, validated_data):
        gameevent_data = validated_data.pop('gameevents')
        athlete_data = validated_data.pop('athletes')
        team_data = validated_data.pop('teams')
        gameevent_serializer = GameeventRlSerializer(data=gameevent_data)
        gameevent_serializer.is_valid()
        gameevent = gameevent_serializer.save()
        athlete_serializer = AthleteSerializer(data=athlete_data)
        athlete_serializer.is_valid()
        athlete = athlete_serializer.save()
        team_serializer = TeamSerializer(data=team_data)
        team_serializer.is_valid()
        team = team_serializer.save()
        athletegameeventrl, created = AthletegameeventRl.objects.get_or_create(idgameevent=gameevent, idathlete=athlete, idteam=team, **validated_data)
        return athletegameeventrl
