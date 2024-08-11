from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    season_average_games_played = models.IntegerField() 
    season_average_minutes_per_game = models.FloatField()  
    season_average_points_per_game = models.FloatField()  
    season_average_field_goals_made = models.FloatField()  
    season_average_field_goals_attempted = models.FloatField()  
    season_average_field_goal_percentage = models.FloatField() 
    season_average_three_points_made = models.FloatField()  
    season_average_three_points_attempted = models.FloatField()  
    season_average_three_point_percentage = models.FloatField() 
    season_average_free_throws_made = models.FloatField()  
    season_average_free_throws_attempted = models.FloatField()  
    season_average_free_throw_percentage = models.FloatField() 
    season_average_offensive_rebounds = models.FloatField()  
    season_average_defensive_rebounds = models.FloatField()  
    season_average_total_rebounds = models.FloatField()  
    season_average_assists = models.FloatField()  
    season_average_turnovers = models.FloatField()  
    season_average_steals = models.FloatField()  
    season_average_blocks = models.FloatField()  
    season_average_personal_fouls = models.FloatField() 
    season_average_fantasy_points = models.FloatField() 
    season_average_double_doubles = models.FloatField()  
    season_average_triple_doubles = models.FloatField()  
    season_average_plus_minus = models.FloatField()  

    def __str__(self):
        return f"{self.name} ({self.team})"
