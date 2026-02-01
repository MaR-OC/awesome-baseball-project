"""
Player statistics module for tracking individual player performance.
"""


class Player:
    """Represents a baseball player with their statistics."""
    
    def __init__(self, name, team="", position=""):
        """
        Initialize a player.
        
        Args:
            name (str): Player's name
            team (str): Team name
            position (str): Player's position
        """
        self.name = name
        self.team = team
        self.position = position
        
        # Batting statistics
        self.at_bats = 0
        self.hits = 0
        self.doubles = 0
        self.triples = 0
        self.home_runs = 0
        self.rbis = 0
        self.walks = 0
        self.strikeouts = 0
        self.stolen_bases = 0
        
        # Pitching statistics
        self.innings_pitched = 0.0
        self.earned_runs = 0
        self.strikeouts_pitched = 0
        self.walks_allowed = 0
        self.wins = 0
        self.losses = 0
        self.saves = 0
    
    def add_at_bat(self, result, rbis=0):
        """
        Record an at-bat result.
        
        Args:
            result (str): 'hit', 'double', 'triple', 'home_run', 'out', 'walk', 'strikeout'
            rbis (int): Runs batted in on this at-bat
        """
        if result != 'walk':
            self.at_bats += 1
        
        if result == 'hit':
            self.hits += 1
        elif result == 'double':
            self.hits += 1
            self.doubles += 1
        elif result == 'triple':
            self.hits += 1
            self.triples += 1
        elif result == 'home_run':
            self.hits += 1
            self.home_runs += 1
        elif result == 'walk':
            self.walks += 1
        elif result == 'strikeout':
            self.strikeouts += 1
        
        self.rbis += rbis
    
    def add_stolen_base(self):
        """Record a stolen base."""
        self.stolen_bases += 1
    
    def batting_average(self):
        """Calculate batting average."""
        if self.at_bats == 0:
            return 0.0
        return round(self.hits / self.at_bats, 3)
    
    def slugging_percentage(self):
        """Calculate slugging percentage."""
        if self.at_bats == 0:
            return 0.0
        
        total_bases = (
            (self.hits - self.doubles - self.triples - self.home_runs) +
            (self.doubles * 2) +
            (self.triples * 3) +
            (self.home_runs * 4)
        )
        return round(total_bases / self.at_bats, 3)
    
    def on_base_percentage(self):
        """Calculate on-base percentage."""
        plate_appearances = self.at_bats + self.walks
        if plate_appearances == 0:
            return 0.0
        
        return round((self.hits + self.walks) / plate_appearances, 3)
    
    def add_pitching_stats(self, innings, earned_runs, strikeouts, walks):
        """
        Add pitching statistics.
        
        Args:
            innings (float): Innings pitched
            earned_runs (int): Earned runs allowed
            strikeouts (int): Strikeouts
            walks (int): Walks allowed
        """
        self.innings_pitched += innings
        self.earned_runs += earned_runs
        self.strikeouts_pitched += strikeouts
        self.walks_allowed += walks
    
    def era(self):
        """Calculate earned run average."""
        if self.innings_pitched == 0:
            return 0.0
        return round((self.earned_runs * 9) / self.innings_pitched, 2)
    
    def record_win(self):
        """Record a win for a pitcher."""
        self.wins += 1
    
    def record_loss(self):
        """Record a loss for a pitcher."""
        self.losses += 1
    
    def record_save(self):
        """Record a save for a pitcher."""
        self.saves += 1
    
    def to_dict(self):
        """Convert player to dictionary for serialization."""
        return {
            'name': self.name,
            'team': self.team,
            'position': self.position,
            'at_bats': self.at_bats,
            'hits': self.hits,
            'doubles': self.doubles,
            'triples': self.triples,
            'home_runs': self.home_runs,
            'rbis': self.rbis,
            'walks': self.walks,
            'strikeouts': self.strikeouts,
            'stolen_bases': self.stolen_bases,
            'innings_pitched': self.innings_pitched,
            'earned_runs': self.earned_runs,
            'strikeouts_pitched': self.strikeouts_pitched,
            'walks_allowed': self.walks_allowed,
            'wins': self.wins,
            'losses': self.losses,
            'saves': self.saves
        }
    
    @classmethod
    def from_dict(cls, data):
        """Create player from dictionary."""
        player = cls(data['name'], data['team'], data['position'])
        player.at_bats = data['at_bats']
        player.hits = data['hits']
        player.doubles = data['doubles']
        player.triples = data['triples']
        player.home_runs = data['home_runs']
        player.rbis = data['rbis']
        player.walks = data['walks']
        player.strikeouts = data['strikeouts']
        player.stolen_bases = data['stolen_bases']
        player.innings_pitched = data['innings_pitched']
        player.earned_runs = data['earned_runs']
        player.strikeouts_pitched = data['strikeouts_pitched']
        player.walks_allowed = data['walks_allowed']
        player.wins = data['wins']
        player.losses = data['losses']
        player.saves = data['saves']
        return player
    
    def __str__(self):
        """String representation of player."""
        return (
            f"{self.name} ({self.position}) - {self.team}\n"
            f"  BA: {self.batting_average():.3f} | "
            f"HR: {self.home_runs} | "
            f"RBI: {self.rbis} | "
            f"SB: {self.stolen_bases}"
        )
