from django.db import models


class Athlete(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    sex = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        #migrations nao afetarao a class
        managed = False
        db_table = 'athlete'

class AthletegameeventRl(models.Model):
    idgameevent = models.ForeignKey('GameeventRl', models.DO_NOTHING, db_column='idGameEvent', blank=True, null=True)  # Field name made lowercase.
    idathlete = models.ForeignKey(Athlete, models.DO_NOTHING, db_column='idAthlete', blank=True, null=True)  # Field name made lowercase.
    idteam = models.ForeignKey('Team', models.DO_NOTHING, db_column='idTeam', blank=True, null=True)  # Field name made lowercase.
    medal = models.CharField(max_length=1, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'athleteGameEvent_rl'


class City(models.Model):
    city = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'city'


class Event(models.Model):
    idsport = models.ForeignKey('Sport', models.DO_NOTHING, db_column='idSport', blank=True, null=True)  # Field name made lowercase.
    event = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'event'


class Game(models.Model):
    idseason = models.ForeignKey('Season', models.DO_NOTHING, db_column='idSeason', blank=True, null=True)  # Field name made lowercase.
    idcity = models.ForeignKey(City, models.DO_NOTHING, db_column='idCity', blank=True, null=True)  # Field name made lowercase.
    game = models.CharField(max_length=255, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'game'


class GameeventRl(models.Model):
    idgame = models.ForeignKey(Game, models.DO_NOTHING, db_column='idGame', blank=True, null=True)  # Field name made lowercase.
    idevent = models.ForeignKey(Event, models.DO_NOTHING, db_column='idEvent', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'gameEvent_rl'


class Season(models.Model):
    season = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'season'


class Sport(models.Model):
    sport = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sport'


class Team(models.Model):
    team = models.CharField(max_length=255, blank=True, null=True)
    noc = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'team'
