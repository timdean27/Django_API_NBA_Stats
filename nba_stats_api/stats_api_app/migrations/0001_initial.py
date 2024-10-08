# Generated by Django 5.0.7 on 2024-09-02 14:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NBAPlayer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('href', models.URLField(max_length=255, unique=True)),
                ('img_src', models.URLField(max_length=255)),
                ('player_id', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='NBAPlayerSeasonStats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season_year', models.CharField(max_length=50)),
                ('team', models.CharField(max_length=50)),
                ('games_played', models.FloatField()),
                ('minutes_per_game', models.FloatField()),
                ('points_per_game', models.FloatField()),
                ('field_goals_made', models.FloatField()),
                ('field_goals_attempted', models.FloatField()),
                ('field_goal_percentage', models.FloatField()),
                ('three_points_made', models.FloatField()),
                ('three_points_attempted', models.FloatField()),
                ('three_point_percentage', models.FloatField()),
                ('free_throws_made', models.FloatField()),
                ('free_throws_attempted', models.FloatField()),
                ('free_throw_percentage', models.FloatField()),
                ('offensive_rebounds', models.FloatField()),
                ('defensive_rebounds', models.FloatField()),
                ('total_rebounds', models.FloatField()),
                ('assists', models.FloatField()),
                ('turnovers', models.FloatField()),
                ('steals', models.FloatField()),
                ('blocks', models.FloatField()),
                ('personal_fouls', models.FloatField()),
                ('fantasy_points', models.FloatField()),
                ('double_doubles', models.FloatField()),
                ('triple_doubles', models.FloatField()),
                ('plus_minus', models.FloatField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stats_api_app.nbaplayer', to_field='player_id')),
            ],
        ),
        migrations.CreateModel(
            name='NBAPlayersLast5Games',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_date', models.DateField()),
                ('matchup', models.CharField(max_length=100)),
                ('win_loss', models.CharField(max_length=1)),
                ('minutes', models.FloatField()),
                ('points', models.FloatField()),
                ('field_goals_made', models.FloatField()),
                ('field_goals_attempted', models.FloatField()),
                ('field_goal_percentage', models.FloatField()),
                ('three_points_made', models.FloatField()),
                ('three_points_attempted', models.FloatField()),
                ('three_point_percentage', models.FloatField()),
                ('free_throws_made', models.FloatField()),
                ('free_throws_attempted', models.FloatField()),
                ('free_throw_percentage', models.FloatField()),
                ('offensive_rebounds', models.FloatField()),
                ('defensive_rebounds', models.FloatField()),
                ('total_rebounds', models.FloatField()),
                ('assists', models.FloatField()),
                ('steals', models.FloatField()),
                ('blocks', models.FloatField()),
                ('turnovers', models.FloatField()),
                ('personal_fouls', models.FloatField()),
                ('plus_minus', models.FloatField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stats_api_app.nbaplayer', to_field='player_id')),
            ],
            options={
                'unique_together': {('player', 'game_date')},
            },
        ),
    ]
