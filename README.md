
# NBA Player Data API

This project is a **Django-powered REST API** that aggregates and delivers comprehensive NBA player performance data. Designed with scalability and reliability in mind, the API is hosted on **AWS EC2**, allowing easy access to real-time player data through various endpoints. The system collects, processes, and stores player statistics, offering a range of insights that can be highly valuable for individuals or businesses focused on **fantasy sports**, sports analytics, or any application that involves tracking player performance.

## How It Works

The NBA Player Data API is connected to a web-scraping system that periodically collects player performance data, such as points, rebounds, assists, and game-by-game statistics. This data is stored in a **PostgreSQL database**, which is hosted using **Amazon RDS** for enhanced security, availability, and scalability.

Once the data is collected and stored, the Django API provides a range of endpoints that users can interact with. Each endpoint returns detailed player information or performance metrics, offering flexibility to request data by player, season, or even specific games. The API is structured to allow quick access to performance overviews or drill-down insights on individual games.

### Key Data Points

- **Player Profiles**: Basic information about players, such as name, team, and position.
- **Season Averages**: Stats like points per game (PPG), rebounds per game (RPG), assists per game (APG), and more.
- **Last 5 Games**: Specific data on the player's performance over their most recent five games.

This data is highly valuable for users who need to track player performance trends, whether for analysis, sports reporting, or more interactive use cases like **fantasy sports**.

## Use Case: Fantasy Sports Optimization

A significant use case for the NBA Player Data API is optimizing strategies in **fantasy basketball leagues**. The API allows users to evaluate player performance in real-time, particularly in identifying **players who are performing above or below their seasonal averages**.

For example, if a player typically averages 20 points per game but has been underperforming in the last few games, this insight could be used to adjust lineups, predict future performance, or make informed trades in fantasy leagues. Conversely, if a player is exceeding their average in key metrics like rebounds or assists, fantasy managers could gain a competitive edge by capitalizing on this hot streak before it ends.

Here’s how it could be applied:

- **Above-Average Performers**: The API can be queried to find players who are scoring more points or grabbing more rebounds in recent games than their season averages. This helps users make decisions about which players to start in fantasy matchups.
- **Below-Average Performers**: Users can also identify underperforming players and adjust their lineups accordingly. This insight helps avoid missed opportunities or losses due to poor player performance.

This data-driven approach to fantasy sports could provide a **competitive advantage**, making your API an essential tool for enthusiasts looking to maximize their chances of winning.


## API Endpoints

Here is a list of available endpoints for the NBA Player Data API:

```
path('', views.home, name='home')
path('api/players/', views.player_list, name='player_list')
path('api/players/season/', views.all_player_season_stats, name='all_player_season_stats')
path('api/players/last5/', views.all_player_last_five_games, name='all_player_last_five_games')
path('api/players/season/<int:player_id>', views.player_season_details, name='player_season_details')
path('api/players/season/<int:player_id>/<int:id>/', views.single_player_season_details, name='single_player_season_details')
path('api/players/last5/<int:player_id>', views.player_last_five_details, name='player_last_five_details')
path('api/players/last5/<int:player_id>/<int:id>/', views.single_player_last_five_details, name='single_player_last_five_details')
```

### Requirements

The API can be deployed by installing the required packages:
```bash
pip install -r requirements.txt
```
