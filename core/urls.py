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
router.register('matches', views.MatchViewSet)
router.register('match-players', views.MatchPlayerViewSet)
router.register('goals', views.GoalViewSet)
router.register('assists', views.AssistViewSet)
router.register('bookings', views.BookingViewSet)
router.register('substitutions', views.SubstitutionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
