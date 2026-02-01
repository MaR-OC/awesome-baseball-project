#!/usr/bin/env python3
"""
Main CLI application for the Awesome Baseball Statistics Tracker.
"""
import argparse
import sys
from baseball_stats.player import Player
from baseball_stats.team import Team
from baseball_stats.league import League


def create_example_league():
    """Create an example league with sample data."""
    # Create league
    league = League("Major League Baseball")
    
    # Create teams
    yankees = Team("New York Yankees", "American League", "East")
    red_sox = Team("Boston Red Sox", "American League", "East")
    dodgers = Team("Los Angeles Dodgers", "National League", "West")
    
    # Add Yankees players
    judge = Player("Aaron Judge", "New York Yankees", "RF")
    judge.add_at_bat("home_run", rbis=1)
    judge.add_at_bat("hit", rbis=0)
    judge.add_at_bat("home_run", rbis=2)
    judge.add_at_bat("double", rbis=1)
    judge.add_at_bat("out", rbis=0)
    yankees.add_player(judge)
    
    cole = Player("Gerrit Cole", "New York Yankees", "P")
    cole.add_pitching_stats(7.0, 2, 10, 2)
    cole.record_win()
    yankees.add_player(cole)
    
    yankees.record_game("win")
    yankees.record_game("win")
    yankees.record_game("loss")
    
    # Add Red Sox players
    devers = Player("Rafael Devers", "Boston Red Sox", "3B")
    devers.add_at_bat("hit", rbis=0)
    devers.add_at_bat("double", rbis=2)
    devers.add_at_bat("home_run", rbis=3)
    devers.add_at_bat("out", rbis=0)
    devers.add_stolen_base()
    red_sox.add_player(devers)
    
    sale = Player("Chris Sale", "Boston Red Sox", "P")
    sale.add_pitching_stats(6.0, 3, 8, 3)
    sale.record_loss()
    red_sox.add_player(sale)
    
    red_sox.record_game("win")
    red_sox.record_game("loss")
    red_sox.record_game("loss")
    
    # Add Dodgers players
    betts = Player("Mookie Betts", "Los Angeles Dodgers", "RF")
    betts.add_at_bat("triple", rbis=1)
    betts.add_at_bat("hit", rbis=0)
    betts.add_at_bat("hit", rbis=1)
    betts.add_at_bat("home_run", rbis=2)
    betts.add_stolen_base()
    betts.add_stolen_base()
    dodgers.add_player(betts)
    
    kershaw = Player("Clayton Kershaw", "Los Angeles Dodgers", "P")
    kershaw.add_pitching_stats(8.0, 1, 12, 1)
    kershaw.record_win()
    dodgers.add_player(kershaw)
    
    dodgers.record_game("win")
    dodgers.record_game("win")
    dodgers.record_game("win")
    
    # Add teams to league
    league.add_team(yankees)
    league.add_team(red_sox)
    league.add_team(dodgers)
    
    return league


def display_league_info(league):
    """Display league standings and statistics."""
    print("\n" + "="*60)
    print(league)
    print("="*60)
    
    print("\n--- Team Statistics ---")
    for team in league.get_standings():
        print(f"\n{team}")
        
        print("\n  Top Hitters:")
        for player in team.get_top_hitters(3):
            print(f"    {player}")
        
        # Show pitchers
        pitchers = [p for p in team.get_roster() if p.innings_pitched > 0]
        if pitchers:
            print("\n  Pitchers:")
            for pitcher in pitchers:
                print(f"    {pitcher.name}: {pitcher.wins}-{pitcher.losses}, "
                      f"ERA: {pitcher.era():.2f}, K: {pitcher.strikeouts_pitched}")


def main():
    """Main CLI application."""
    parser = argparse.ArgumentParser(
        description="Awesome Baseball Statistics Tracker"
    )
    parser.add_argument(
        '--demo',
        action='store_true',
        help='Run demo with example data'
    )
    parser.add_argument(
        '--load',
        type=str,
        help='Load league data from file'
    )
    parser.add_argument(
        '--save',
        type=str,
        help='Save league data to file'
    )
    
    args = parser.parse_args()
    
    if args.load:
        try:
            league = League.load_from_file(args.load)
            print(f"Loaded league data from {args.load}")
            display_league_info(league)
        except FileNotFoundError as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)
    elif args.demo:
        print("Running demo with example data...")
        league = create_example_league()
        display_league_info(league)
        
        if args.save:
            league.save_to_file(args.save)
            print(f"\nSaved league data to {args.save}")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
