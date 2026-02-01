# ⚾ Awesome Baseball Project

A comprehensive Python-based baseball statistics tracker for managing players, teams, and league standings. Track batting averages, home runs, RBIs, pitching statistics, and much more!

## Features

- **Player Statistics Tracking**
  - Batting statistics: Average, hits, home runs, RBIs, stolen bases
  - Advanced metrics: Slugging percentage, on-base percentage
  - Pitching statistics: ERA, wins, losses, saves, strikeouts
  
- **Team Management**
  - Organize players into teams
  - Track team wins, losses, and win percentage
  - Calculate team batting averages and aggregate stats
  - View top performers on each team

- **League Organization**
  - Manage multiple teams in a league
  - View league standings
  - Save and load league data to/from JSON files

- **Interactive CLI**
  - Demo mode with example data
  - Load and save league data
  - Display comprehensive statistics and standings

## Installation

1. Clone the repository:
```bash
git clone https://github.com/MaR-OC/awesome-baseball-project.git
cd awesome-baseball-project
```

2. No external dependencies needed! The project uses only Python standard library.

3. Make sure you have Python 3.6+ installed:
```bash
python3 --version
```

## Usage

### Quick Demo

Run the demo to see the baseball statistics tracker in action:

```bash
python3 baseball_stats.py --demo
```

This will create a sample league with teams and players, displaying:
- League standings
- Team statistics
- Individual player performance
- Top hitters and pitchers

### Save and Load Data

Save demo data to a file:
```bash
python3 baseball_stats.py --demo --save league_data.json
```

Load previously saved data:
```bash
python3 baseball_stats.py --load league_data.json
```

### Programmatic Usage

You can also use the baseball statistics modules in your own Python code:

```python
from baseball_stats.player import Player
from baseball_stats.team import Team
from baseball_stats.league import League

# Create a player
player = Player("Babe Ruth", "Yankees", "RF")
player.add_at_bat("home_run", rbis=1)
player.add_at_bat("hit", rbis=0)

print(f"Batting Average: {player.batting_average()}")
print(f"Home Runs: {player.home_runs}")

# Create a team
team = Team("New York Yankees", "American League", "East")
team.add_player(player)
team.record_game("win")

print(f"Win Percentage: {team.win_percentage()}")

# Create a league
league = League("Major League Baseball")
league.add_team(team)
print(league)

# Save league data
league.save_to_file("my_league.json")
```

## Project Structure

```
awesome-baseball-project/
├── baseball_stats/
│   ├── __init__.py      # Package initialization
│   ├── player.py        # Player class with batting/pitching stats
│   ├── team.py          # Team class with roster management
│   └── league.py        # League class with standings and data persistence
├── baseball_stats.py    # Main CLI application
├── requirements.txt     # Dependencies (none needed!)
├── README.md           # This file
└── LICENSE             # MIT License
```

## Statistics Tracked

### Batting Statistics
- At Bats (AB)
- Hits (H)
- Doubles (2B)
- Triples (3B)
- Home Runs (HR)
- Runs Batted In (RBI)
- Walks (BB)
- Strikeouts (K)
- Stolen Bases (SB)
- Batting Average (AVG)
- Slugging Percentage (SLG)
- On-Base Percentage (OBP)

### Pitching Statistics
- Innings Pitched (IP)
- Earned Runs (ER)
- Strikeouts (K)
- Walks (BB)
- Wins (W)
- Losses (L)
- Saves (SV)
- Earned Run Average (ERA)

### Team Statistics
- Wins
- Losses
- Ties
- Win Percentage
- Team Batting Average
- Total Home Runs
- Total RBIs

## Example Output

```
============================================================
=== Major League Baseball ===

Standings:
1. Los Angeles Dodgers: 3-0 (1.000)
2. New York Yankees: 2-1 (0.667)
3. Boston Red Sox: 1-2 (0.333)
============================================================

--- Team Statistics ---

Los Angeles Dodgers (National League - West)
  Record: 3-0-0 (1.000)
  Team BA: 1.000 | HR: 1 | RBI: 4

  Top Hitters:
    Mookie Betts (RF) - Los Angeles Dodgers
      BA: 1.000 | HR: 1 | RBI: 4 | SB: 2

  Pitchers:
    Clayton Kershaw: 1-0, ERA: 1.12, K: 12
```

## Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Future Enhancements

- Add defensive statistics (fielding percentage, errors)
- Implement game simulation
- Add database support (SQLite)
- Create a web interface
- Add statistical visualizations and charts
- Import real player data from APIs
- Advanced analytics (WAR, wOBA, FIP)

---

Made with ⚾ and ❤️ by the Awesome Baseball Project team
