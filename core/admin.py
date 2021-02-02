from django.contrib import admin
from core.models import Country, Team, Player, Season, Contract, League, Match, MatchPlayer, Goal, Assist, Stadium


class MatchAdmin(admin.ModelAdmin):
    list_display = ('kick_off', 'home_team', 'away_team', 'home_team_goals', 'away_team_goals')


class ContractAdmin(admin.ModelAdmin):
    list_display = ('player', 'team', 'season')


admin.site.register(Match, MatchAdmin)
admin.site.register(Team)
admin.site.register(Country)
admin.site.register(Player)
admin.site.register(Season)
admin.site.register(Contract, ContractAdmin)
admin.site.register(League)
admin.site.register(MatchPlayer)
admin.site.register(Goal)
admin.site.register(Assist)
admin.site.register(Stadium)
