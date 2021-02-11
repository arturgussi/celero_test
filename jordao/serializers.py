from rest_framework import serializers
from .models import Athlete, City, Season, Game

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

class GameSerializer(serializers.ModelSerializer):
    season = SeasonSerializer(source=seasons)
    city = CitySerializer(source=cities)

    class Meta:
        model = Game
        fields = ['id', 'season', 'city', 'game', 'year']


        