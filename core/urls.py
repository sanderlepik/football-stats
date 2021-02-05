from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('countries', views.CountryViewSet)
router.register('seasons', views.SeasonViewSet)
router.register('competitions', views.CompetitionViewSet)
router.register('teams', views.TeamViewSet)
router.register('players', views.PlayerViewSet)
router.register('contracts', views.ContractViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
