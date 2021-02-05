from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from core.models import Country, Season, Competition, Team, Player, Contract


class CountrySerializer(ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class SeasonSerializer(ModelSerializer):
    class Meta:
        model = Season
        fields = '__all__'


class CompetitionSerializer(ModelSerializer):
    class Meta:
        model = Competition
        fields = '__all__'


class TeamSerializer(ModelSerializer):
    contracts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Team
        fields = '__all__'


class PlayerSerializer(ModelSerializer):
    contracts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Player
        fields = '__all__'


class ContractSerializer(ModelSerializer):
    class Meta:
        model = Contract
        fields = '__all__'
