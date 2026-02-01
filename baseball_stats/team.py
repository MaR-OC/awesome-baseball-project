"""
Team statistics module for tracking team performance.
"""
from baseball_stats.player import Player


class Team:
    """Represents a baseball team with its roster and statistics."""
    
    def __init__(self, name, league="", division=""):
        """
        Initialize a team.
        
        Args:
            name (str): Team name
            league (str): League name (e.g., "American League", "National League")
            division (str): Division name (e.g., "East", "West", "Central")
        """
        self.name = name
        self.league = league
        self.division = division
        self.players = {}
        self.wins = 0
        self.losses = 0
        self.ties = 0
    
    def add_player(self, player):
        """
        Add a player to the team.
        
        Args:
            player (Player): Player object to add
        """
        player.team = self.name
        self.players[player.name] = player
    
    def remove_player(self, player_name):
        """
        Remove a player from the team.
        
        Args:
            player_name (str): Name of player to remove
        """
        if player_name in self.players:
            del self.players[player_name]
    
    def get_player(self, player_name):
        """
        Get a player by name.
        
        Args:
            player_name (str): Name of player
            
        Returns:
            Player: Player object or None if not found
        """
        return self.players.get(player_name)
    
    def record_game(self, result):
        """
        Record a game result.
        
        Args:
            result (str): 'win', 'loss', or 'tie'
        """
        if result == 'win':
            self.wins += 1
        elif result == 'loss':
            self.losses += 1
        elif result == 'tie':
            self.ties += 1
    
    def win_percentage(self):
        """Calculate team win percentage."""
        total_games = self.wins + self.losses
        if total_games == 0:
            return 0.0
        return round(self.wins / total_games, 3)
    
    def team_batting_average(self):
        """Calculate team batting average."""
        total_hits = sum(p.hits for p in self.players.values())
        total_at_bats = sum(p.at_bats for p in self.players.values())
        
        if total_at_bats == 0:
            return 0.0
        return round(total_hits / total_at_bats, 3)
    
    def total_home_runs(self):
        """Calculate total team home runs."""
        return sum(p.home_runs for p in self.players.values())
    
    def total_rbis(self):
        """Calculate total team RBIs."""
        return sum(p.rbis for p in self.players.values())
    
    def get_roster(self):
        """Get list of all players."""
        return list(self.players.values())
    
    def get_top_hitters(self, limit=5):
        """
        Get top hitters by batting average.
        
        Args:
            limit (int): Number of players to return
            
        Returns:
            list: List of Player objects sorted by batting average
        """
        hitters = [p for p in self.players.values() if p.at_bats > 0]
        return sorted(hitters, key=lambda p: p.batting_average(), reverse=True)[:limit]
    
    def get_top_home_run_hitters(self, limit=5):
        """
        Get top home run hitters.
        
        Args:
            limit (int): Number of players to return
            
        Returns:
            list: List of Player objects sorted by home runs
        """
        return sorted(self.players.values(), key=lambda p: p.home_runs, reverse=True)[:limit]
    
    def to_dict(self):
        """Convert team to dictionary for serialization."""
        return {
            'name': self.name,
            'league': self.league,
            'division': self.division,
            'wins': self.wins,
            'losses': self.losses,
            'ties': self.ties,
            'players': {name: player.to_dict() for name, player in self.players.items()}
        }
    
    @classmethod
    def from_dict(cls, data):
        """Create team from dictionary."""
        team = cls(data['name'], data['league'], data['division'])
        team.wins = data['wins']
        team.losses = data['losses']
        team.ties = data['ties']
        team.players = {name: Player.from_dict(player_data) 
                       for name, player_data in data['players'].items()}
        return team
    
    def __str__(self):
        """String representation of team."""
        return (
            f"{self.name} ({self.league} - {self.division})\n"
            f"  Record: {self.wins}-{self.losses}-{self.ties} "
            f"({self.win_percentage():.3f})\n"
            f"  Team BA: {self.team_batting_average():.3f} | "
            f"HR: {self.total_home_runs()} | "
            f"RBI: {self.total_rbis()}"
        )
