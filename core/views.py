from rest_framework import viewsets

from core.models import Country, Season, Competition, Team, Player, Contract, Match, MatchPlayer, Goal, Substitution, \
    Booking, Assist
from core.serializers import CountrySerializer, SeasonSerializer, CompetitionSerializer, TeamSerializer, \
    PlayerSerializer, ContractSerializer, MatchSerializer, MatchPlayerSerializer, GoalSerializer, AssistSerializer, \
    BookingSerializer, SubstitutionSerializer


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
    CRUD Contract
    ---
    request_serializer: ContractSerializer
    """
    serializer_class = ContractSerializer
    queryset = Contract.objects.all()


class MatchViewSet(viewsets.ModelViewSet):
    """
    CRUD Team
    ---
    request_serializer: MatchSerializer
    """
    serializer_class = MatchSerializer
    queryset = Match.objects.all()


class MatchPlayerViewSet(viewsets.ModelViewSet):
    """
    CRUD Team
    ---
    request_serializer: MatchPlayerSerializer
    """
    serializer_class = MatchPlayerSerializer
    queryset = MatchPlayer.objects.all()


class GoalViewSet(viewsets.ModelViewSet):
    """
    CRUD Goal
    ---
    request_serializer: GoalSerializer
    """
    serializer_class = GoalSerializer
    queryset = Goal.objects.all()


class AssistViewSet(viewsets.ModelViewSet):
    """
    CRUD Assist
    ---
    request_serializer: AssistSerializer
    """
    serializer_class = AssistSerializer
    queryset = Assist.objects.all()


class BookingViewSet(viewsets.ModelViewSet):
    """
    CRUD Booking
    ---
    request_serializer: BookingSerializer
    """
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()


class SubstitutionViewSet(viewsets.ModelViewSet):
    """
    CRUD Substitution
    ---
    request_serializer: SubstitutionSerializer
    """
    serializer_class = SubstitutionSerializer
    queryset = Substitution.objects.all()
