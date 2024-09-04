from django.db import models

class NBAPlayer(models.Model):
    full_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    href = models.URLField(max_length=255, unique=True)
    img_src = models.URLField(max_length=255)
    player_id = models.CharField(max_length=255, unique=True)

    class Meta:
        db_table = 'nba_players'  # This must match the existing table name

    def __str__(self):
        return self.full_name


class NBAPlayerSeasonStats(models.Model):
    player = models.ForeignKey(NBAPlayer, to_field='player_id', on_delete=models.CASCADE)
    season_year = models.CharField(max_length=50)
    team = models.CharField(max_length=50)
    games_played = models.FloatField()
    minutes_per_game = models.FloatField()
    points_per_game = models.FloatField()
    field_goals_made = models.FloatField()
    field_goals_attempted = models.FloatField()
    field_goal_percentage = models.FloatField()
    three_points_made = models.FloatField()
    three_points_attempted = models.FloatField()
    three_point_percentage = models.FloatField()
    free_throws_made = models.FloatField()
    free_throws_attempted = models.FloatField()
    free_throw_percentage = models.FloatField()
    offensive_rebounds = models.FloatField()
    defensive_rebounds = models.FloatField()
    total_rebounds = models.FloatField()
    assists = models.FloatField()
    turnovers = models.FloatField()
    steals = models.FloatField()
    blocks = models.FloatField()
    personal_fouls = models.FloatField()
    fantasy_points = models.FloatField()
    double_doubles = models.FloatField()
    triple_doubles = models.FloatField()
    plus_minus = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'nba_player_season_stats'  # This must match the existing table name

    def __str__(self):
        return f"{self.player.full_name} - {self.season_year}"


class NBAPlayersLast5Games(models.Model):
    player = models.ForeignKey(NBAPlayer, to_field='player_id', on_delete=models.CASCADE)
    game_date = models.DateField()
    matchup = models.CharField(max_length=100)
    win_loss = models.CharField(max_length=1)
    minutes = models.FloatField()
    points = models.FloatField()
    field_goals_made = models.FloatField()
    field_goals_attempted = models.FloatField()
    field_goal_percentage = models.FloatField()
    three_points_made = models.FloatField()
    three_points_attempted = models.FloatField()
    three_point_percentage = models.FloatField()
    free_throws_made = models.FloatField()
    free_throws_attempted = models.FloatField()
    free_throw_percentage = models.FloatField()
    offensive_rebounds = models.FloatField()
    defensive_rebounds = models.FloatField()
    total_rebounds = models.FloatField()
    assists = models.FloatField()
    steals = models.FloatField()
    blocks = models.FloatField()
    turnovers = models.FloatField()
    personal_fouls = models.FloatField()
    plus_minus = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'nba_players_last_5_games'  # This must match the existing table name
        unique_together = ('player', 'game_date')

    def __str__(self):
        return f"{self.player.full_name} - {self.game_date} ({self.matchup})"
