from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from core.models import Country, Season, Competition, Team, Player, Contract, Match, MatchPlayer, Goal, Assist, Booking, \
    Substitution


class CompetitionSerializer(ModelSerializer):
    class Meta:
        model = Competition
        fields = '__all__'


class SeasonSerializer(ModelSerializer):
    competitions = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Season
        fields = '__all__'


class TeamSerializer(ModelSerializer):
    contracts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Team
        fields = '__all__'


class ContractSerializer(ModelSerializer):
    season = SeasonSerializer(many=False)
    team = TeamSerializer(many=False)

    class Meta:
        model = Contract
        fields = '__all__'


class GoalSerializer(ModelSerializer):
    class Meta:
        model = Goal
        fields = '__all__'


class AssistSerializer(ModelSerializer):
    class Meta:
        model = Assist
        fields = '__all__'


class BookingSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'


class SubstitutionSerializer(ModelSerializer):
    class Meta:
        model = Substitution
        fields = '__all__'


class MatchSerializer(ModelSerializer):
    home_team = TeamSerializer(many=False)
    away_team = TeamSerializer(many=False)
    competition = CompetitionSerializer(many=False)
    goals = GoalSerializer(many=True, read_only=True)
    assists = AssistSerializer(many=True, read_only=True)
    bookings = BookingSerializer(many=True, read_only=True)
    substitutions = SubstitutionSerializer(many=True, read_only=True)

    class Meta:
        model = Match
        fields = '__all__'


class MatchPlayerSerializer(ModelSerializer):
    class Meta:
        model = MatchPlayer
        fields = '__all__'


class PlayerSerializer(ModelSerializer):
    contracts = ContractSerializer(many=True, read_only=True)
    matches = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    goals = GoalSerializer(many=True, read_only=True)
    assists = AssistSerializer(many=True, read_only=True)
    bookings = BookingSerializer(many=True, read_only=True)
    substitutions = SubstitutionSerializer(many=True, read_only=True)

    class Meta:
        model = Player
        fields = '__all__'


class CountrySerializer(ModelSerializer):
    players = PlayerSerializer(many=True, read_only=True)
    competitions = CompetitionSerializer(many=True, read_only=True)

    class Meta:
        model = Country
        fields = '__all__'
