from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "countries"

    def __str__(self):
        return self.name


class Season(models.Model):
    year = models.IntegerField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.year)


class Competition(models.Model):
    name = models.CharField(max_length=75, null=False, blank=False)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='competitions')
    season = models.ForeignKey(Season, on_delete=models.CASCADE, related_name='competitions')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} | {self.season.year}"


class Team(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False)
    competitions = models.ManyToManyField(Competition)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    date_of_birth = models.DateField(null=False, blank=False)
    nationality = models.ForeignKey(Country, null=True, blank=True, on_delete=models.CASCADE, related_name='players')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name


class Contract(models.Model):
    player = models.ForeignKey(Player, null=False, blank=False, on_delete=models.DO_NOTHING, related_name='contracts')
    team = models.ForeignKey(Team, null=False, blank=False, on_delete=models.DO_NOTHING, related_name='contracts')
    season = models.ForeignKey(Season, null=False, blank=False, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.team.name} | {self.player.name} | {self.season.year}"


class Stadium(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    country = models.ForeignKey(Country, blank=False, null=False, on_delete=models.CASCADE, related_name='stadiums')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.name)


class Match(models.Model):
    competition = models.ForeignKey(Competition, null=False, blank=False, on_delete=models.DO_NOTHING)
    home_team = models.ForeignKey(Team, null=False, blank=False, on_delete=models.DO_NOTHING,
                                  related_name="home_matches")
    away_team = models.ForeignKey(Team, null=False, blank=False, on_delete=models.DO_NOTHING,
                                  related_name="away_matches")
    home_team_goals = models.IntegerField(blank=True, null=True)
    away_team_goals = models.IntegerField(blank=True, null=True)
    kick_off = models.DateTimeField(null=True, blank=True)
    stadium = models.ForeignKey(Stadium, null=True, blank=True, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "matches"

    def __str__(self):
        return f"{self.kick_off} | {self.home_team.name}  " \
               f"{self.home_team_goals} : {self.away_team_goals}   {self.away_team.name}"


class MatchPlayer(models.Model):
    match = models.ForeignKey(Match, null=False, blank=False, on_delete=models.DO_NOTHING)
    player = models.ForeignKey(Player, null=False, blank=False, on_delete=models.DO_NOTHING, related_name='matches')
    is_substitute = models.BooleanField(null=False, blank=False)
    minutes_played = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.player.name} | {self.match.home_team.name} - {self.match.away_team.name} | {self.match.kick_off}"


class Goal(models.Model):
    match = models.ForeignKey(Match, null=False, blank=False, on_delete=models.DO_NOTHING, related_name='goals')
    player = models.ForeignKey(Player, null=False, blank=False, on_delete=models.DO_NOTHING, related_name='goals')
    team = models.ForeignKey(Team, null=False, blank=False, on_delete=models.DO_NOTHING)
    is_own_goal = models.BooleanField(null=True, blank=True)
    minute = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return f"{self.minute}' - {self.player.name} | {self.team.name}"


class Assist(models.Model):
    match = models.ForeignKey(Match, null=False, blank=False, on_delete=models.DO_NOTHING, related_name='assists')
    player = models.ForeignKey(Player, null=False, blank=False, on_delete=models.DO_NOTHING,
                               related_name='assists')
    team = models.ForeignKey(Team, null=False, blank=False, on_delete=models.DO_NOTHING)
    minute = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return f"{self.minute}' - {self.player.name} | {self.team.name}"


class Booking(models.Model):
    match = models.ForeignKey(Match, null=False, blank=False, on_delete=models.DO_NOTHING, related_name='bookings')
    player = models.ForeignKey(Player, null=False, blank=False, on_delete=models.DO_NOTHING,
                               related_name='bookings')
    team = models.ForeignKey(Team, null=False, blank=False, on_delete=models.DO_NOTHING)
    minute = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return f"{self.minute}' - {self.player.name} | {self.team.name}"


class Substitution(models.Model):
    match = models.ForeignKey(Match, null=False, blank=False, on_delete=models.DO_NOTHING, related_name='substitutions')
    player = models.ForeignKey(Player, null=False, blank=False, on_delete=models.DO_NOTHING,
                               related_name='substitutions')
    team = models.ForeignKey(Team, null=False, blank=False, on_delete=models.DO_NOTHING)
    minute = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return f"{self.minute}' - {self.player.name} | {self.team.name}"
