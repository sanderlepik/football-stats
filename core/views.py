from rest_framework import viewsets

from core.models import Country, Season, Competition, Team, Player, Contract
from core.serializers import CountrySerializer, SeasonSerializer, CompetitionSerializer, TeamSerializer, \
    PlayerSerializer, ContractSerializer


class CountryViewSet(viewsets.ModelViewSet):
    """
    CRUD Country
    ---
    request_serializer: CountrySerializer
    """
    serializer_class = CountrySerializer
    queryset = Country.objects.all()


class SeasonViewSet(viewsets.ModelViewSet):
    """
    CRUD Season
    ---
    request_serializer: SeasonSerializer
    """
    serializer_class = SeasonSerializer
    queryset = Season.objects.all()


class CompetitionViewSet(viewsets.ModelViewSet):
    """
    CRUD Competition
    ---
    request_serializer: CompetitionSerializer
    """
    serializer_class = CompetitionSerializer
    queryset = Competition.objects.all()


class TeamViewSet(viewsets.ModelViewSet):
    """
    CRUD Team
    ---
    request_serializer: TeamSerializer
    """
    serializer_class = TeamSerializer
    queryset = Team.objects.all()


class PlayerViewSet(viewsets.ModelViewSet):
    """
    CRUD Player
    ---
    request_serializer: PlayerSerializer
    """
    serializer_class = PlayerSerializer
    queryset = Player.objects.all()


class ContractViewSet(viewsets.ModelViewSet):
    """
    CRUD Team
    ---
    request_serializer: TeamSerializer
    """
    serializer_class = ContractSerializer
    queryset = Contract.objects.all()
