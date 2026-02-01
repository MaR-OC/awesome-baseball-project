"""
League management module for organizing multiple teams.
"""
import json
import os
from baseball_stats.team import Team
from baseball_stats.player import Player


class League:
    """Represents a baseball league with multiple teams."""
    
    def __init__(self, name):
        """
        Initialize a league.
        
        Args:
            name (str): League name
        """
        self.name = name
        self.teams = {}
    
    def add_team(self, team):
        """
        Add a team to the league.
        
        Args:
            team (Team): Team object to add
        """
        self.teams[team.name] = team
    
    def remove_team(self, team_name):
        """
        Remove a team from the league.
        
        Args:
            team_name (str): Name of team to remove
        """
        if team_name in self.teams:
            del self.teams[team_name]
    
    def get_team(self, team_name):
        """
        Get a team by name.
        
        Args:
            team_name (str): Name of team
            
        Returns:
            Team: Team object or None if not found
        """
        return self.teams.get(team_name)
    
    def get_standings(self):
        """
        Get league standings sorted by win percentage.
        
        Returns:
            list: List of Team objects sorted by win percentage
        """
        return sorted(self.teams.values(), key=lambda t: t.win_percentage(), reverse=True)
    
    def get_all_teams(self):
        """Get list of all teams."""
        return list(self.teams.values())
    
    def save_to_file(self, filename):
        """
        Save league data to JSON file.
        
        Args:
            filename (str): Path to save file
        """
        data = {
            'name': self.name,
            'teams': {name: team.to_dict() for name, team in self.teams.items()}
        }
        
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
    
    @classmethod
    def load_from_file(cls, filename):
        """
        Load league data from JSON file.
        
        Args:
            filename (str): Path to load file
            
        Returns:
            League: League object
        """
        if not os.path.exists(filename):
            raise FileNotFoundError(f"File {filename} not found")
        
        with open(filename, 'r') as f:
            data = json.load(f)
        
        league = cls(data['name'])
        league.teams = {name: Team.from_dict(team_data) 
                       for name, team_data in data['teams'].items()}
        return league
    
    def __str__(self):
        """String representation of league."""
        output = [f"=== {self.name} ===\n"]
        output.append("Standings:")
        
        for i, team in enumerate(self.get_standings(), 1):
            output.append(f"{i}. {team.name}: {team.wins}-{team.losses} ({team.win_percentage():.3f})")
        
        return "\n".join(output)
