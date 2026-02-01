#!/usr/bin/env python3
"""
Example script demonstrating the Awesome Baseball Statistics Tracker.
This script shows how to create players, teams, and track statistics.
"""
from baseball_stats.player import Player
from baseball_stats.team import Team
from baseball_stats.league import League


def main():
    print("=" * 70)
    print("Welcome to the Awesome Baseball Statistics Tracker - Example Demo")
    print("=" * 70)
    
    # Example 1: Creating a player and tracking stats
    print("\n--- Example 1: Player Statistics ---")
    player = Player("Mike Trout", "Angels", "CF")
    
    # Simulate some at-bats
    player.add_at_bat("home_run", rbis=2)
    player.add_at_bat("double", rbis=1)
    player.add_at_bat("hit", rbis=0)
    player.add_at_bat("strikeout", rbis=0)
    player.add_at_bat("walk", rbis=0)
    player.add_stolen_base()
    
    print(f"\nPlayer: {player.name}")
    print(f"Position: {player.position}")
    print(f"At Bats: {player.at_bats}")
    print(f"Hits: {player.hits}")
    print(f"Home Runs: {player.home_runs}")
    print(f"RBIs: {player.rbis}")
    print(f"Stolen Bases: {player.stolen_bases}")
    print(f"Batting Average: {player.batting_average():.3f}")
    print(f"Slugging Percentage: {player.slugging_percentage():.3f}")
    print(f"On-Base Percentage: {player.on_base_percentage():.3f}")
    
    # Example 2: Creating a pitcher and tracking stats
    print("\n--- Example 2: Pitcher Statistics ---")
    pitcher = Player("Jacob deGrom", "Mets", "P")
    pitcher.add_pitching_stats(7.0, 1, 11, 1)
    pitcher.record_win()
    
    print(f"\nPitcher: {pitcher.name}")
    print(f"Innings Pitched: {pitcher.innings_pitched}")
    print(f"Earned Runs: {pitcher.earned_runs}")
    print(f"Strikeouts: {pitcher.strikeouts_pitched}")
    print(f"Walks Allowed: {pitcher.walks_allowed}")
    print(f"ERA: {pitcher.era():.2f}")
    print(f"Record: {pitcher.wins}-{pitcher.losses}")
    
    # Example 3: Creating a team and managing roster
    print("\n--- Example 3: Team Management ---")
    team = Team("San Francisco Giants", "National League", "West")
    
    # Add multiple players
    player1 = Player("Brandon Crawford", "Giants", "SS")
    player1.add_at_bat("double", rbis=2)
    player1.add_at_bat("hit", rbis=1)
    
    player2 = Player("Buster Posey", "Giants", "C")
    player2.add_at_bat("home_run", rbis=3)
    player2.add_at_bat("hit", rbis=0)
    
    team.add_player(player1)
    team.add_player(player2)
    
    # Record some games
    team.record_game("win")
    team.record_game("win")
    team.record_game("loss")
    
    print(f"\nTeam: {team.name}")
    print(f"Record: {team.wins}-{team.losses}")
    print(f"Win Percentage: {team.win_percentage():.3f}")
    print(f"Team Batting Average: {team.team_batting_average():.3f}")
    print(f"Total Home Runs: {team.total_home_runs()}")
    print(f"Total RBIs: {team.total_rbis()}")
    
    print(f"\nRoster ({len(team.get_roster())} players):")
    for p in team.get_roster():
        print(f"  - {p.name} ({p.position}): BA {p.batting_average():.3f}")
    
    # Example 4: League standings
    print("\n--- Example 4: League Management ---")
    league = League("Example League")
    
    # Create multiple teams
    team1 = Team("Team A", "Example League", "Division 1")
    team1.record_game("win")
    team1.record_game("win")
    team1.record_game("win")
    
    team2 = Team("Team B", "Example League", "Division 1")
    team2.record_game("win")
    team2.record_game("win")
    team2.record_game("loss")
    
    team3 = Team("Team C", "Example League", "Division 1")
    team3.record_game("win")
    team3.record_game("loss")
    team3.record_game("loss")
    
    league.add_team(team1)
    league.add_team(team2)
    league.add_team(team3)
    
    print(f"\n{league}")
    
    # Example 5: Save and load data
    print("\n--- Example 5: Data Persistence ---")
    filename = "/tmp/example_league.json"
    league.save_to_file(filename)
    print(f"League data saved to: {filename}")
    
    loaded_league = League.load_from_file(filename)
    print(f"League data loaded successfully!")
    print(f"Loaded league name: {loaded_league.name}")
    print(f"Number of teams: {len(loaded_league.get_all_teams())}")
    
    print("\n" + "=" * 70)
    print("Demo completed! Check out baseball_stats.py for more features.")
    print("=" * 70)


if __name__ == "__main__":
    main()
