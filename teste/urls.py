"""teste URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from jordao.views import *

router = routers.DefaultRouter()
router.register('athletes', AthleteView, basename='Athlete')
router.register('seasons', SeasonView, basename='Season')
router.register('cities', CityView, basename='City')
router.register('games', GameView, basename='Game')
router.register('sports', SportView, basename='Sport')
router.register('teams', TeamView, basename='Team')
router.register('events', EventView, basename='Event')
router.register('teste', Teste, basename='Teste')
router.register('main', AthletegameeventRlViews, basename='Master')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
