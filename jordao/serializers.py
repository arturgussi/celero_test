from rest_framework import serializers
from .models import Athlete, City, Season, Game

class AthleteSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Athlete
        fields = ['id', 'name', 'sex']

class SeasonSerializer(serializers.ModelSerializer):
    #games = GameSerializer(read_only=True,many=True)

    class Meta:
        model = Season
        fields = '__all__'
        read_only_field = ['id']

class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = ['id', 'city']


class GameSerializer(serializers.ModelSerializer):
    citys = CitySerializer(many=False)
    #seasons = SeasonSerializer(read_only=True, many=True)

    class Meta:
        model = Game
        fields = ['id', 'game', 'year', 'citys']
        
    def create(self, validated_data):
        city_data = validated_data.pop('citys')
        game = Game.objects.create(idcity=City.objects.get(id=citys["city"]), **validated_data))
        game.save()
        serializer = GameSerializer(game)

        return Response(serializer.data)
    
