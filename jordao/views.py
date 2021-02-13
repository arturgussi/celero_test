from rest_framework import viewsets

from .serializers    import AthleteSerializer, GameSerializer, SeasonSerializer, CitySerializer, SportSerializer, EventSerializer
from .models         import Athlete, Game, Season, City, Sport, Event

# Create your views here.
class AthleteView(viewsets.ModelViewSet):
    """Exibindo todos os atletas"""
    queryset = Athlete.objects.all()
    serializer_class = AthleteSerializer

class SeasonView(viewsets.ModelViewSet):
    """Exibindo todos os atletas"""
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer

class CityView(viewsets.ModelViewSet):
    """Exibindo todos os atletas"""
    queryset = City.objects.all()
    serializer_class = CitySerializer

class GameView(viewsets.ModelViewSet):
    """Exibindo todos os games"""
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class SportView(viewsets.ModelViewSet):
    queryset = Sport.objects.all()
    serializer_class = SportSerializer

class EventView(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer