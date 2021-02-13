from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework_csv import renderers

from .serializers    import *
from .models         import *

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

class TeamView(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class EventView(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class Teste(viewsets.ModelViewSet):
    queryset = GameeventRl.objects.all()
    serializer_class = GameeventRlSerializer

class AthletegameeventRlViews(viewsets.ModelViewSet):
    queryset = AthletegameeventRl.objects.all()
    serializer_class = AthletegameeventRlSerializer
    